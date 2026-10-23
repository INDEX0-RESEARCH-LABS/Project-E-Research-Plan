"""Generate the E-Micro Gate 2 feasibility report, figures and run manifest.

Run from the repository root with the project virtual environment:

    ../project-e/.venv/bin/python -m engineering.report

The model and the Markdown report need only the standard library. Matplotlib is
optional; if it is unavailable the report is still written and the figure step
is skipped with a warning.
"""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import physics, rescope
from .feasibility import screen, screen_all
from .mechanisms import MECHANISMS, get

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
TARGET_L = 2.16
POWER_KW = 3.0
DURATIONS_H = (1.0, 8.0, 100.0, 1_000.0, 10_000.0)
PLOT_MECHANISMS = (
    "li_ion",
    "li_air",
    "pem_fuel_cell",
    "diesel",
    "stirling",
    "microturbine",
    "rtg",
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def _model_dirty() -> bool:
    """True if tracked model files differ from HEAD; generated reports are excluded."""
    try:
        output = subprocess.check_output(
            ["git", "-C", str(ROOT), "status", "--porcelain", "--", "engineering"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return True
    return bool(output.strip())


def _model_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def _fmt_litres(value: float) -> str:
    if value >= 1_000:
        return f"{value:,.0f}"
    if value >= 10:
        return f"{value:,.1f}"
    return f"{value:.2f}"


def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def _load_requirements() -> dict:
    path = ROOT / "engineering" / "data" / "requirements.json"
    return json.loads(path.read_text())


def _heat_table(surface_m2: float) -> str:
    """Air-side rejection area and fin-stack volume, not a cold-plate fantasy.

    ``h=100 W/m2K`` is optimistic forced air over fins; ``h=50`` is a more
    realistic small forced-air unit. The envelope skin is a boundary, not a
    radiator: a sealed box cannot reject this heat through its own surface.
    """
    rows: list[list[str]] = []
    for eta in (0.15, 0.25, 0.35, 0.40, 0.60):
        q_w = physics.heat_engine_waste_heat_w(POWER_KW, eta)
        a_forced = physics.heat_rejection_area_m2(q_w, 100.0, 30.0)
        a_real = physics.heat_rejection_area_m2(q_w, 50.0, 30.0)
        fin_l = q_w / physics.W_PER_KW / 4.0
        rows.append(
            [
                f"{eta:.0%}",
                f"{q_w:,.0f}",
                f"{a_forced:.3f}",
                f"{a_real:.3f}",
                f"{fin_l:.2f}",
                f"{a_forced / surface_m2:.1f}×",
            ]
        )
    return _md_table(
        [
            "Efficiency",
            "Waste heat (W)",
            "Air-side area, h=100, ΔT=30 (m²)",
            "Air-side area, h=50, ΔT=30 (m²)",
            "Fin-stack volume at 4 kW/L (L)",
            "Fin area / skin area",
        ],
        rows,
    )


def _volume_table() -> tuple[str, list]:
    screens_by_duration = {h: {r.mechanism_id: r for r in screen_all(POWER_KW, h, TARGET_L)} for h in DURATIONS_H}
    one_hour = screens_by_duration[1.0]
    order = sorted(MECHANISMS, key=lambda m: one_hour[m.id].best_volume_l)
    rows: list[list[str]] = []
    for mechanism in order:
        marker = ""
        if mechanism.maturity == "theoretical":
            marker = " †"
        elif mechanism.maturity == "restricted":
            marker = " ‡"
        rows.append(
            [mechanism.name + marker, mechanism.maturity]
            + [_fmt_litres(screens_by_duration[h][mechanism.id].best_volume_l) for h in DURATIONS_H]
        )
    table = _md_table(
        ["Mechanism", "Maturity", "1 h", "8 h", "100 h", "1,000 h", "10,000 h"],
        rows,
    )
    return table, screens_by_duration


def _one_hour_table(screens_by_duration: dict) -> str:
    results = sorted(screens_by_duration[1.0].values(), key=lambda r: r.best_volume_l)
    rows: list[list[str]] = []
    for result in results:
        rows.append(
            [
                result.name,
                result.maturity,
                _fmt_litres(result.best_volume_l),
                _fmt_litres(result.worst_volume_l),
                f"{result.best_ratio:.2f}×",
                result.verdict,
                result.best_limiting,
            ]
        )
    return _md_table(
        [
            "Mechanism",
            "Maturity",
            "Best case (L)",
            "Worst case (L)",
            "Best / 2.16 L",
            "Verdict",
            "Largest component (best case; share of unpackaged sum)",
        ],
        rows,
    )


def _relaxation_table() -> str:
    best = screen(get("li_ion"), POWER_KW, 1.0, TARGET_L)
    hours = rescope.max_duration_h("li_ion", POWER_KW, TARGET_L)
    power = rescope.max_power_kw("li_ion", 1.0, TARGET_L)
    cell_125 = rescope.required_cell_wh_l(POWER_KW, 1.0, TARGET_L, 1.25, 0.2)
    cell_110 = rescope.required_cell_wh_l(POWER_KW, 1.0, TARGET_L, 1.10, 0.1)
    cell_zero = rescope.required_cell_wh_l(POWER_KW, 1.0, TARGET_L, 1.0, 0.0, 0.0)
    derated_h = hours * 0.80 * 0.95
    derated_cell = cell_125 / (0.80 * 0.95)

    rows = [
        [
            "Best current 1 h system (Li-ion, converter included)",
            f"{best.best_volume_l:.2f} L",
            f"{best.best_ratio:.2f}× the envelope",
            "Current",
        ],
        [
            "Max duration at 2.16 L, 3 kW, 100% DoD, no conversion loss",
            f"{hours * 60:.1f} min",
            "Volume-only upper bound",
            "Current",
        ],
        [
            "Max duration at 2.16 L, 3 kW, 80% DoD, 95% converter",
            f"{derated_h * 60:.1f} min",
            "Honest small-pack estimate",
            "Current",
        ],
        [
            "Max power for 1 h at 2.16 L",
            f"{power:.2f} kW",
            f"{POWER_KW / power:.1f}× lower than 3 kW",
            "Current",
        ],
        [
            "Cell energy density needed at 1.25 packaging, 0.2 L BOP, 0.4 L converter",
            f"{cell_125:,.0f} Wh/L",
            f"≈{cell_125 / 700.0:.1f}× a 700 Wh/L cell",
            "Advanced/theoretical",
        ],
        [
            "Cell energy density needed at 1.10 packaging, 0.1 L BOP, 0.4 L converter",
            f"{cell_110:,.0f} Wh/L",
            f"≈{cell_110 / 700.0:.1f}× a 700 Wh/L cell",
            "Advanced/theoretical",
        ],
        [
            "Cell energy density needed with zero packaging/BOP/converter",
            f"{cell_zero:,.0f} Wh/L",
            f"≈{cell_zero / 700.0:.1f}× a 700 Wh/L cell",
            "Theoretical",
        ],
        [
            "Cell energy density with 80% DoD and 95% converter",
            f"{derated_cell:,.0f} Wh/L",
            f"≈{derated_cell / 700.0:.1f}× a 700 Wh/L cell",
            "Theoretical",
        ],
    ]
    return _md_table(["Relaxation path", "Value", "Interpretation", "Class"], rows)


def _plots(screens_by_duration: dict, surface_m2: float) -> list[Path]:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover - optional dependency
        print(f"plot step skipped: {exc}", file=sys.stderr)
        return []

    FIGURES.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    # Figure 1: volume vs duration, best case.
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    for mechanism_id in PLOT_MECHANISMS:
        mechanism = get(mechanism_id)
        xs = list(DURATIONS_H)
        ys = [screens_by_duration[h][mechanism_id].best_volume_l for h in xs]
        ax.plot(xs, ys, marker="o", linewidth=1.6, label=mechanism.name)
    ax.axhline(TARGET_L, color="black", linestyle="--", linewidth=1.2, label="2.16 L envelope")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Continuous output duration (h)")
    ax.set_ylabel("Best-case complete-system volume (L)")
    ax.set_title("Project E — E-Micro 3 kWe volume screen (best case)")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=7, ncol=2, loc="upper left")
    fig.tight_layout()
    path = FIGURES / "e_micro_volume_vs_duration.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    outputs.append(path)

    # Figure 2: heat rejection area vs efficiency.
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    etas = [0.05 + i * 0.005 for i in range(91)]
    for h, dt, label in (
        (100.0, 30.0, "optimistic forced air: h=100, dT=30 K"),
        (50.0, 30.0, "small forced-air unit: h=50, dT=30 K"),
        (10.0, 30.0, "natural convection + radiation: h=10, dT=30 K"),
    ):
        areas = [
            physics.heat_rejection_area_m2(physics.heat_engine_waste_heat_w(POWER_KW, e), h, dt)
            for e in etas
        ]
        ax.plot(etas, areas, linewidth=1.6, label=label)
    ax.axhline(surface_m2, color="black", linestyle="--", linewidth=1.2, label=f"envelope skin {surface_m2:.4f} m²")
    ax.set_yscale("log")
    ax.set_xlabel("Heat-engine efficiency")
    ax.set_ylabel("Required air-side heat-rejection area (m²)")
    ax.set_title("Project E - 3 kWe air-side heat rejection (skin is not a radiator)")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=7)
    fig.tight_layout()
    path = FIGURES / "e_micro_heat_rejection.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    outputs.append(path)

    # Figure 3: one-hour best-case bar chart.
    results = sorted(screens_by_duration[1.0].values(), key=lambda r: r.best_volume_l)
    fig, ax = plt.subplots(figsize=(9.6, 5.8))
    labels = [r.name for r in results]
    values = [r.best_volume_l for r in results]
    colors = ["#1f77b4" if r.maturity == "current" else "#ff7f0e" for r in results]
    ax.barh(labels, values, color=colors)
    ax.axvline(TARGET_L, color="black", linestyle="--", linewidth=1.2, label="2.16 L envelope (dashed)")
    ax.set_xscale("log")
    ax.set_xlabel("Best-case complete-system volume (L), 3 kWe for 1 h")
    ax.set_title("Project E — E-Micro 1 h best-case volume\n(blue=current, orange=advanced/theoretical/restricted)")
    ax.grid(True, axis="x", which="both", alpha=0.20)
    ax.legend(fontsize=8, loc="lower right")
    fig.subplots_adjust(left=0.36, right=0.98, top=0.84, bottom=0.14)
    path = FIGURES / "e_micro_volume_at_1h.png"
    fig.savefig(path, dpi=140)
    plt.close(fig)
    outputs.append(path)

    return outputs


def main() -> int:
    requirements = _load_requirements()
    micro = next(p for p in requirements["products"] if p["id"] == "E-MICRO")
    if abs(micro["continuous_kw"] - POWER_KW) > 1e-9 or abs(micro["envelope_l"] - TARGET_L) > 1e-9:
        raise SystemExit("requirements.json no longer matches the 3 kW / 2.16 L screen")
    if not micro.get("envelope_mm"):
        raise SystemExit("requirements.json has no envelope_mm")
    envelope_m = [v / 1000.0 for v in micro["envelope_mm"]]
    volume_check = physics.box_volume_l(*envelope_m)
    surface_m2 = physics.box_surface_area_m2(*envelope_m)
    if abs(volume_check - TARGET_L) > 1e-9:
        raise SystemExit(f"envelope_mm gives {volume_check:.6f} L, not {TARGET_L} L")

    table, screens_by_duration = _volume_table()
    one_hour = _one_hour_table(screens_by_duration)
    heat = _heat_table(surface_m2)
    relaxation = _relaxation_table()

    one_h = screens_by_duration[1.0]
    current = [r for r in one_h.values() if r.maturity == "current"]
    current_generation = [r for r in current if r.category == "generation"]
    best_current = min(current, key=lambda r: r.best_volume_l)
    best_current_generation = min(current_generation, key=lambda r: r.best_volume_l)
    generation_ratio_max = max(r.best_ratio for r in current_generation)
    best_any = min(one_h.values(), key=lambda r: r.best_volume_l)

    outputs = _plots(screens_by_duration, surface_m2)
    REPORTS.mkdir(parents=True, exist_ok=True)

    report = f"""# E-Micro Gate 2 feasibility — 3 kWe in 2.16 L

**Version:** 0.2  
**Date:** 2026-10-23  
**Status:** analytical screen; no component quote, no CAD, no measurement. Revision 0.2 corrects the heat-rejection narrative, adds a 0.4 L converter and fuel-cell radiator, and qualifies the maturity labels; the fail is unchanged and larger.  
**Target:** E-Micro, 3 kWe continuous, external envelope 120 × 150 × 120 mm (2.16 L)  
**Model:** `engineering/`; `engineering/tests` stdlib `unittest` cases

---

## 1. Answer

**No mechanism among the twelve screened in this report — including all current commercial families represented — fits 3 kWe for 1 hour in 2.16 L once source, conversion, heat rejection and packaging are counted.**

- The best current **storage** mechanism is **{best_current.name}** at **{best_current.best_volume_l:.2f} L** for 1 h — **{best_current.best_ratio:.2f}×** the envelope.
- The best current **generator** is **{best_current_generation.name}** at **{best_current_generation.best_volume_l:.2f} L** — **{best_current_generation.best_ratio:.2f}×** the envelope.
- The best case of any mechanism is **{best_any.name}** at **{best_any.best_volume_l:.2f} L** — {best_any.maturity}, **{best_any.best_ratio:.2f}×** the envelope.
- A current Li-ion buffer fits the envelope for only about **{rescope.max_duration_h("li_ion", POWER_KW, TARGET_L) * 60:.0f} min** at 3 kW with 100% DoD and no conversion loss; at 80% DoD and 95% converter it is about **{rescope.max_duration_h("li_ion", POWER_KW, TARGET_L) * 0.80 * 0.95 * 60:.0f} min**. A continuous generator is a different problem.

The target is not a small margin. It is a **{best_current.best_ratio:.1f}× volume gap for the best current storage** and a **{best_current_generation.best_ratio:.1f}–{generation_ratio_max:.0f}× gap for current generation**, before any real packaging, controls, cooling loop, or safety hardware.

The failure is independent of packaging: **3 kWh ÷ 700 Wh/L = 4.29 L of cells alone**, already **1.98×** the envelope; a 1 L stack plus 3.75 L of H₂ gas is **4.75 L**, **2.20×**. No packaging or BOP assumption can rescue either. The theoretical Li-air entry would need **≥{rescope.required_cell_wh_l(POWER_KW, 1.0, TARGET_L, 1.25, 0.2):,.0f} Wh/L cell** with this packaging, BOP and converter; the 1,500 Wh/L case used here does not fit. That threshold is not a commercial product.

---

## 2. Volumetric power density

| Quantity | Value |
|---|---:|
| Electrical power | 3.0 kW |
| External envelope | 2.16 L |
| Volumetric power density | **{physics.volumetric_power_density_mw_m3(POWER_KW, TARGET_L):.3f} MW/m³** |
| Envelope surface area | **{surface_m2:.4f} m²** |

A **0.4 L converter** allowance is included in every row (0.3–0.6 L is the estimate for a 3 kW isolated DC-DC at 5–10 kW/L; it is not a datasheet). High-performance electric motors reach several kW/L and power electronics reach tens of kW/L, so the converter is a small term, not the problem. The **source** is.

---

## 3. Best-case complete-system volume (L)

The table is the **best case** of each mechanism: optimistic efficiency, volume, heat-transfer coefficient, packaging and BOP. A real system is larger. `†` = theoretical; `‡` = restricted nuclear.

{table}

`Li-air` is theoretical and does not have a commercial pack. `RTG` is a space/nuclear source and is not a 3 kW product. The `ambient` row is not a contender; it is included as a lower bound.

**Label caveat:** the `current` column labels the **mechanism family**, not every best-case parameter. Two best cases are optimistic extrapolations: PEM **3 kW/L** is an automotive large-stack metric (0.3–1.5 kW/L is closer at 3 kW), and diesel **10 L/kW** is a stripped bare engine (commercial 3 kW packages are 50–150 L/kW). They are retained because they favour the mechanism; the failure is therefore robust.

**Reading the table:** even the best current 1 h system is 6.1 L; the envelope is 2.16 L. At 8 h, the best current system is already tens of litres; at 10,000 h, no chemical system is close.

---

## 4. One-hour detail

{one_hour}

A `conditional` verdict means the optimistic case fits but the pessimistic case does not. No mechanism in the register is a clean `pass` at 3 kWe/1 h. The `insufficient evidence` verdict is reserved for mechanisms outside the register; every screened mechanism gets pass, conditional or fail.

---

## 5. Heat rejection

At 3 kWe, a heat engine rejects 3(1/η - 1) kW. The envelope skin is only **{surface_m2:.4f} m²**, and a sealed box cannot reject this heat through its own skin: the skin is a boundary, not a radiator. The table uses an air-side coefficient, which is the relevant basis:

{heat}

At 25% the waste heat is 9 kW; even at an optimistic forced-air **h=100 W/m²K, ΔT=30 K**, the required fin area is **3.00 m², 30× the skin**, and a 4 kW/L fin stack is **2.25 L** — already larger than the envelope before the engine, fuel or BOP. At 35% the fin area is 1.86 m² (18×) and the fin stack is 1.39 L; at 40%, 1.50 m² (15×) and 1.13 L. At 60% (the PEM best case) the 2 kW waste heat still needs 0.67 m² (6.6×) and a 0.5 L fin stack, plus a coolant loop. **Heat rejection rules out a sealed 2.16 L heat engine independent of engine volume, and it adds a real radiator to the fuel-cell case.**

---

## 6. Minimum relaxation

{relaxation}

The target needs one of:

1. **~2.0–3.8× better cell volumetric energy density** (1,389–2,660 Wh/L cell) for a 1 h battery, depending on packaging and converter allowance; with 80% DoD and 95% converter it is **~3,500 Wh/L (5.0×)**. Current high-energy Li-ion cells are ~700 Wh/L; Li-air is the only chemistry near the upper end, and it is not commercial.
2. **~3.8× lower power** for a 1 h system in the same envelope (0.79 kW max).
3. **~2.8× larger volume** for the best current 1 h storage system (6.1 L); the best current generator is ~4.1× (8.9 L).
4. **A short-duration buffer**, not a continuous generator: ~8–16 min at 3 kW with current Li-ion (about 12 min at 80% DoD and 95% converter).

---

## 7. What this does not prove

- It does not prove that a **new mechanism** is impossible. It bounds the current and near-current mechanisms in the register.
- It does not model transient performance, converter control, fault behaviour, vibration, crash, or lifetime.
- It uses **external** envelope volume. Internal volume is smaller after walls, insulation, clearances, connectors and mounting.
- The best case is deliberately optimistic. A real system is larger, so the failure is robust in the direction that matters.
- It does not price the system. A 6.1 L battery may meet ₹50,000 at some scale; that is a separate Gate 3/6 question.
- It does not select a mechanism. It rejects the **stated E-Micro envelope** as a continuous 3 kW generator with current technology.
- **Hardware not counted:** BMS/contactors/fuses/EMI filter beyond the 0.4 L converter allowance; fuel-cell air blower, humidifier, water separator/drain and H₂ leak detection/ventilation; diesel DPF/SCR, muffler and intake filtration (plausibly 1–3 L); Li-ion thermal-runaway venting/containment; structural walls, hardpoints, connectors and vibration isolation. These omissions make the best-case volumes lower bounds.
- **H₂ vessel:** the 3.75 L figure is **gas volume** at 700 bar, not vessel volume. A Type IV vessel is roughly 1.4–1.7× larger externally (≈5.3–6.4 L), so the PEM row is optimistic even before the radiator.
- **Touch safety:** the radiator-core best case uses an effective 4 kW/L fin stack; it does not mean the 105 °C skin at ΔT=80 K is acceptable. IEC 62368-1 touch limits for metal are far lower; a real product needs a ducted/forced-air path and a touch-safe enclosure, which breaks the sealed-box premise.

---

## 8. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** E-Micro’s 3 kWe / 2.16 L target is not achievable with any of the twelve screened mechanisms—including every current commercial family represented—for 1 hour of continuous output.

**Evidence:** component-level energy densities, fuel LHV, heat-transfer relations and the mechanisms register. No measured system is used; the best-case parameters are optimistic estimates.

**Method:** complete-system volume = source/fuel + converter + heat rejection + BOP, multiplied by a packaging factor; compare with 2.16 L; repeat for 1–10,000 h. The fuel-cell branch now includes a radiator; the heat table uses an **air-side** coefficient, not a cold-plate coefficient applied to the envelope skin.

**Assumptions:** 1.25 packaging (1.35 worst), 1.5 L BOP (2.0 worst), 0.4 L converter (0.3–0.6 L estimate, not separately varied), 700 Wh/L cell (400 worst), 3 kW/L PEM stack (1 worst; large-stack extrapolation), 10 L/kW diesel engine (20 worst; stripped, not a commercial package), and a 4 kW/L fin-stack equivalent for the best radiator (worst h=100 W/m²K, ΔT=30 K). The 105 °C skin implied by ΔT=80 K is **not** claimed as touch-safe.

**Uncertainty:** the best-case volume is a lower bound; the worst case is 1.5–3× larger. The sign of the conclusion does not change for current mechanisms at 1 h.

**Counterargument:** a new cell chemistry, a fuel cell with a liquid fuel, or a completely different mechanism could be smaller. That is why the report labels Li-air theoretical and lists the thresholds; it does not declare the whole vision impossible. The liquid-fuel evidence review is worse than H₂ on volume: the best documented reformed-methanol module is 81 L for 5 kW (≈40× the envelope after fuel, tank and buffer), and no 3 kW/2.16 L product was found.

**Verdict:** **FAIL for E-Micro as stated, among the twelve screened mechanisms, at 1 h.** **INSUFFICIENT EVIDENCE** for mechanisms outside the register; **CONDITIONAL** only for a short buffer (~8–16 min) or a lower power (~0.79 kW for 1 h). The earlier 1.1 kW figure ignored the converter volume and is superseded.

---

## 9. Implications for the programme

1. **Do not build CAD for a 2.16 L continuous generator yet.** The first design should be a **buffer/converter** or a **re-scoped generator** at 6–9 L.
2. **The service interval is a missing requirement.** At 1 h the best current storage gap is 2.8×; at 10,000 h it is orders of magnitude. The owner must state the interval before any architecture selection.
3. **E-Micro is the hardest target, not the easiest.** A 3 kW two-wheeler core in 2.16 L is beyond current storage and generation. E-Mobility (20 kW) and E-Heavy have no envelope or duty cycle yet; they cannot be screened.
4. **The liquid-fuel route is not a shortcut.** The best documented reformed-methanol module is 81 L for 5 kW; even a 3 kW/1 h complete system is ≈86 L (≈40×). 700 bar H₂ is also not a shortcut: 3.75 L is gas volume, and a Type IV vessel is ≥5.3 L before the stack. The only credible 2.16 L object is a short buffer.
5. **Preserve the negative result.** It prevents a year of packaging work around a target that cannot close.

---

## 10. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.report
```

The report and figures are generated from `engineering/data/requirements.json` and `engineering/mechanisms.py`; the run manifest records the commit, inputs, output hashes, `model_dirty` and `model_sha256`.
"""

    report_path = REPORTS / "E_MICRO_FEASIBILITY.md"
    report_path.write_text(report)

    # Manifest after outputs exist.
    inputs = [
        ROOT / "engineering" / "data" / "requirements.json",
        ROOT / "engineering" / "mechanisms.py",
        ROOT / "engineering" / "physics.py",
        ROOT / "engineering" / "feasibility.py",
        ROOT / "engineering" / "rescope.py",
        ROOT / "engineering" / "report.py",
    ]
    output_paths = [report_path, *outputs]
    manifest = {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "date": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit(),
        "git_commit_note": "HEAD at run time; model_dirty is true if engineering/ differs from HEAD; generated outputs are committed afterward",
        "model_dirty": _model_dirty(),
        "model_sha256": _model_sha256(inputs),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "target": {"product": "E-MICRO", "power_kw": POWER_KW, "volume_l": TARGET_L},
        "durations_h": list(DURATIONS_H),
        "mechanisms": [m.id for m in MECHANISMS],
        "inputs": {str(p.relative_to(ROOT)): _sha256(p) for p in inputs},
        "outputs": {str(p.relative_to(ROOT)): _sha256(p) for p in output_paths},
        "notes": [
            "Best-case volumes are lower bounds; real systems are larger.",
            "A 0.4 L converter allowance is included in every row; it is an estimate, not a datasheet.",
            "The fuel-cell branch includes a radiator; the envelope skin is not used as a radiator.",
            "No component quote or measurement is included.",
            "Project-E benchmark remains frozen at e75be96.",
        ],
    }
    (REPORTS / "e_micro_run.json").write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"wrote {report_path.relative_to(ROOT)}")
    for path in outputs:
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"wrote reports/e_micro_run.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
