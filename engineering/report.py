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

from . import physics
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


def _heat_table() -> str:
    rows: list[list[str]] = []
    for eta in (0.15, 0.25, 0.35, 0.40):
        q_w = physics.heat_engine_waste_heat_w(POWER_KW, eta)
        a_nat = physics.heat_rejection_area_m2(q_w, 100.0, 30.0)
        a_forced = physics.heat_rejection_area_m2(q_w, 500.0, 50.0)
        a_coldplate = physics.heat_rejection_area_m2(q_w, 1000.0, 80.0)
        rows.append(
            [
                f"{eta:.0%}",
                f"{q_w:,.0f}",
                f"{a_nat:.3f}",
                f"{a_forced:.3f}",
                f"{a_coldplate:.3f}",
                f"{a_coldplate / 0.1008:.2f}×",
            ]
        )
    return _md_table(
        [
            "Heat-engine efficiency",
            "Waste heat (W)",
            "Area h=100, ΔT=30 (m²)",
            "Area h=500, ΔT=50 (m²)",
            "Area h=1,000, ΔT=80 (m²)",
            "Cold-plate area / envelope surface",
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
            "Largest component (best case)",
        ],
        rows,
    )


def _relaxation_table() -> str:
    li = get("li_ion")
    best = screen(li, POWER_KW, 1.0, TARGET_L)

    def max_duration(cell_wh_l: float, packaging: float, bop_l: float) -> float:
        allowed_kwh = (TARGET_L / packaging - bop_l) * cell_wh_l / physics.W_PER_KW
        return physics.max_duration_h(allowed_kwh, POWER_KW)

    def max_power(cell_wh_l: float, packaging: float, bop_l: float, hours: float = 1.0) -> float:
        allowed_kwh = (TARGET_L / packaging - bop_l) * cell_wh_l / physics.W_PER_KW
        return allowed_kwh / hours

    def cell_needed(packaging: float, bop_l: float) -> float:
        allowed_cell_l = TARGET_L / packaging - bop_l
        return POWER_KW * physics.W_PER_KW * 1.0 / allowed_cell_l

    rows = [
        [
            "Best current 1 h system (Li-ion)",
            f"{best.best_volume_l:.2f} L",
            f"{best.best_ratio:.2f}× the envelope",
            "Current",
        ],
        [
            "Max duration at 2.16 L, 3 kW, best case",
            f"{max_duration(700.0, 1.25, 0.2) * 60:.1f} min",
            "Short buffer only",
            "Current",
        ],
        [
            "Max duration at 2.16 L, 3 kW, worst case",
            f"{max_duration(400.0, 1.35, 0.3) * 60:.1f} min",
            "Short buffer only",
            "Current",
        ],
        [
            "Max power for 1 h at 2.16 L, best case",
            f"{max_power(700.0, 1.25, 0.2):.2f} kW",
            f"{POWER_KW / max_power(700.0, 1.25, 0.2):.1f}× lower than 3 kW",
            "Current",
        ],
        [
            "Max power for 1 h at 2.16 L, worst case",
            f"{max_power(400.0, 1.35, 0.3):.2f} kW",
            f"{POWER_KW / max_power(400.0, 1.35, 0.3):.1f}× lower than 3 kW",
            "Current",
        ],
        [
            "Cell energy density needed for 3 kW/1 h at 1.25 packaging, 0.2 L BOP",
            f"{cell_needed(1.25, 0.2):,.0f} Wh/L",
            "≈2.8× a 700 Wh/L cell",
            "Advanced/theoretical",
        ],
        [
            "Cell energy density needed at 1.10 packaging, 0.1 L BOP",
            f"{cell_needed(1.10, 0.1):,.0f} Wh/L",
            "≈2.3× a 700 Wh/L cell",
            "Advanced/theoretical",
        ],
        [
            "Cell energy density needed with zero packaging/BOP",
            f"{cell_needed(1.0, 0.0):,.0f} Wh/L",
            "≈2.0× a 700 Wh/L cell",
            "Theoretical",
        ],
    ]
    return _md_table(["Relaxation path", "Value", "Interpretation", "Class"], rows)


def _plots(screens_by_duration: dict) -> list[Path]:
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
        (100.0, 30.0, "natural/forced air: h=100, dT=30 K"),
        (500.0, 50.0, "forced liquid: h=500, dT=50 K"),
        (1000.0, 80.0, "cold plate: h=1,000, dT=80 K"),
    ):
        areas = [
            physics.heat_rejection_area_m2(physics.heat_engine_waste_heat_w(POWER_KW, e), h, dt)
            for e in etas
        ]
        ax.plot(etas, areas, linewidth=1.6, label=label)
    ax.axhline(0.1008, color="black", linestyle="--", linewidth=1.2, label="envelope surface 0.1008 m²")
    ax.set_yscale("log")
    ax.set_xlabel("Heat-engine efficiency")
    ax.set_ylabel("Required heat-rejection area (m²)")
    ax.set_title("Project E - 3 kWe waste-heat rejection area")
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

    table, screens_by_duration = _volume_table()
    one_hour = _one_hour_table(screens_by_duration)
    heat = _heat_table()
    relaxation = _relaxation_table()

    one_h = screens_by_duration[1.0]
    current = [r for r in one_h.values() if r.maturity == "current"]
    current_generation = [r for r in current if r.category == "generation"]
    best_current = min(current, key=lambda r: r.best_volume_l)
    best_current_generation = min(current_generation, key=lambda r: r.best_volume_l)
    generation_ratio_max = max(r.best_ratio for r in current_generation)
    best_any = min(one_h.values(), key=lambda r: r.best_volume_l)

    outputs = _plots(screens_by_duration)
    REPORTS.mkdir(parents=True, exist_ok=True)

    report = f"""# E-Micro Gate 2 feasibility — 3 kWe in 2.16 L

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** analytical screen; no component quote, no CAD, no measurement  
**Target:** E-Micro, 3 kWe continuous, external envelope 120 × 150 × 120 mm (2.16 L)  
**Model:** `engineering/`; tests: 18 stdlib `unittest` cases

---

## 1. Answer

**No current commercial mechanism fits 3 kWe for 1 hour in 2.16 L once source, conversion, heat rejection and packaging are counted.**

- The best current **storage** mechanism is **{best_current.name}** at **{best_current.best_volume_l:.2f} L** for 1 h — **{best_current.best_ratio:.2f}×** the envelope.
- The best current **generator** is **{best_current_generation.name}** at **{best_current_generation.best_volume_l:.2f} L** — **{best_current_generation.best_ratio:.2f}×** the envelope.
- The best case of any mechanism is **{best_any.name}** at **{best_any.best_volume_l:.2f} L** — {best_any.maturity}, **{best_any.best_ratio:.2f}×** the envelope.
- A current Li-ion buffer fits the envelope for only about **{((TARGET_L / 1.25 - 0.2) * 700 / physics.W_PER_KW / POWER_KW) * 60:.0f} min** at 3 kW. A continuous generator is a different problem.

The target is not a small margin. It is a **{best_current.best_ratio:.1f}× volume gap for the best current storage** and a **{best_current_generation.best_ratio:.1f}–{generation_ratio_max:.0f}× gap for current generation**, before any real packaging, controls, cooling loop, or safety hardware.\n\nThe theoretical Li-air entry would fit only at **≥1,963 Wh/L cell** with this packaging and BOP; the 1,500 Wh/L case used here does not. That threshold is not a commercial product.

---

## 2. Volumetric power density

| Quantity | Value |
|---|---:|
| Electrical power | 3.0 kW |
| External envelope | 2.16 L |
| Volumetric power density | **{physics.volumetric_power_density_mw_m3(POWER_KW, TARGET_L):.3f} MW/m³** |
| Envelope surface area | **{physics.box_surface_area_m2(0.120, 0.150, 0.120):.4f} m²** |

For comparison, high-performance electric motors reach several kW/L; power electronics reach tens of kW/L. The 3 kW **converter** is not the problem. The **source** is.

---

## 3. Best-case complete-system volume (L)

The table is the **best case** of each mechanism: optimistic efficiency, volume, heat-transfer coefficient, packaging and BOP. A real system is larger. `†` = theoretical; `‡` = restricted nuclear.

{table}

`Li-air` is theoretical and does not have a commercial pack. `RTG` is a space/nuclear source and is not a 3 kW product. The `ambient` row is not a contender; it is included as a lower bound.

**Reading the table:** even the best current 1 h system is 5.6 L; the envelope is 2.16 L. At 8 h, the best current system is already tens of litres; at 10,000 h, no chemical system is close.

---

## 4. One-hour detail

{one_hour}

A `conditional` verdict means the optimistic case fits but the pessimistic case does not. No current mechanism is a clean `pass`.

---

## 5. Heat rejection

At 3 kWe, a heat engine rejects 3(1/η - 1) kW. The envelope surface is only **0.1008 m²**. Required area:

{heat}

At 25% efficiency and a very aggressive cold plate (h=1,000 W/m²K, ΔT=80 K), the required area is **0.1125 m²**, already larger than the envelope surface. At 35% it is 0.0696 m², below the surface — but the engine itself is 15–30 L, so heat rejection is not the only failure. The heat-rejection result rules out low-efficiency converters; it does not rescue high-efficiency ones.

---

## 6. Minimum relaxation

{relaxation}

The target needs one of:

1. **~2.0–2.8× better cell volumetric energy density** (1,389–1,963 Wh/L cell) for a 1 h battery, depending on packaging. Current high-energy Li-ion cells are ~700 Wh/L; Li-air is the only chemistry near the upper end, and it is not commercial.
2. **~2.8–5.8× lower power** for a 1 h system in the same envelope.
3. **~2.6× larger volume** for the best current 1 h storage system (5.6 L).
4. **A short-duration buffer**, not a continuous generator: ~10–21 min at 3 kW with current Li-ion.

---

## 7. What this does not prove

- It does not prove that a **new mechanism** is impossible. It bounds the current and near-current mechanisms in the register.
- It does not model transient performance, converter control, fault behaviour, vibration, crash, or lifetime.
- It uses **external** envelope volume. Internal volume is smaller after walls, insulation, clearances, connectors and mounting.
- The best case is deliberately optimistic. A real system is larger, so the failure is robust in the direction that matters.
- It does not price the system. A 5.6 L battery may meet ₹50,000 at some scale; that is a separate Gate 3/6 question.
- It does not select a mechanism. It rejects the **stated E-Micro envelope** as a continuous 3 kW generator with current technology.

---

## 8. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** E-Micro’s 3 kWe / 2.16 L target is not achievable with a current commercial mechanism for 1 hour of continuous output.

**Evidence:** component-level energy densities, fuel LHV, heat-transfer relations and the mechanisms register. No measured system is used; the best-case parameters are optimistic estimates.

**Method:** complete-system volume = source/fuel + converter + heat rejection + BOP, multiplied by a packaging factor; compare with 2.16 L; repeat for 1–10,000 h.

**Assumptions:** 1.25 packaging (1.35 worst), 1.5 L BOP (2.0 worst), 700 Wh/L cell (400 worst), 3 kW/L PEM stack (1 worst), 10 L/kW diesel genset (20 worst), h=1,000 W/m²K and ΔT=80 K best heat rejection (100 and 30 worst).

**Uncertainty:** the best-case volume is a lower bound; the worst case is 1.5–3× larger. The sign of the conclusion does not change for current mechanisms at 1 h.

**Counterargument:** a new cell chemistry, a fuel cell with a liquid fuel, or a completely different mechanism could be smaller. That is why the report labels Li-air theoretical and lists the thresholds; it does not declare the whole vision impossible.

**Verdict:** **FAIL for E-Micro as stated, with current commercial mechanisms, at 1 h.** **INSUFFICIENT EVIDENCE** for a new mechanism; **CONDITIONAL** only for a short buffer (~10–21 min) or a lower power (~1.1 kW for 1 h).

---

## 9. Implications for the programme

1. **Do not build CAD for a 2.16 L continuous generator yet.** The first design should be a **buffer/converter** or a **re-scoped generator** at 5–10 L.
2. **The service interval is a missing requirement.** At 1 h the gap is 2.6×; at 10,000 h it is orders of magnitude. The owner must state the interval before any architecture selection.
3. **E-Micro is the hardest target, not the easiest.** A 3 kW two-wheeler core in 2.16 L is beyond current storage and generation. E-Mobility (20 kW) and E-Heavy have no envelope or duty cycle yet; they cannot be screened.
4. **The next mechanism to examine is a liquid-fuel fuel cell or a reformed-methanol system**, because 700 bar H2 alone is 3.75 L for 1 h — larger than the envelope before the stack. This is a concrete Gate 3 question, not a CAD question.
5. **Preserve the negative result.** It prevents a year of packaging work around a target that cannot close.

---

## 10. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.report
```

The report and figures are generated from `engineering/data/requirements.json` and `engineering/mechanisms.py`; the run manifest records the commit, inputs and output hashes.
"""

    report_path = REPORTS / "E_MICRO_FEASIBILITY.md"
    report_path.write_text(report)

    # Manifest after outputs exist.
    inputs = [
        ROOT / "engineering" / "data" / "requirements.json",
        ROOT / "engineering" / "mechanisms.py",
        ROOT / "engineering" / "physics.py",
        ROOT / "engineering" / "feasibility.py",
    ]
    output_paths = [report_path, *outputs]
    manifest = {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "date": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit(),
        "git_commit_note": "commit at run time; generated outputs are committed afterward",
        "python": platform.python_version(),
        "platform": platform.platform(),
        "target": {"product": "E-MICRO", "power_kw": POWER_KW, "volume_l": TARGET_L},
        "durations_h": list(DURATIONS_H),
        "mechanisms": [m.id for m in MECHANISMS],
        "inputs": {str(p.relative_to(ROOT)): _sha256(p) for p in inputs},
        "outputs": {str(p.relative_to(ROOT)): _sha256(p) for p in output_paths},
        "notes": [
            "Best-case volumes are lower bounds; real systems are larger.",
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
