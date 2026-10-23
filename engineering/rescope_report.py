"""Generate the E-Micro re-scope decision report from the Gate 2 model.

Run:
    cd /home/darion-dev/project-e_research_plan
    ../project-e/.venv/bin/python -m engineering.rescope_report

The report is deliberately short: it turns the negative Gate 2 result into
explicit product options. It does not select an architecture. It writes a run
manifest so the numbers can be reproduced.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from . import physics, rescope
from .feasibility import screen, screen_all
from .mechanisms import MECHANISMS, get
from .report import _git_commit, _sha256

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
POWER_KW = 3.0
TARGET_L = 2.16
HOURS = 1.0


def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def _duration(value_h: float) -> str:
    if value_h == 0.0:
        return "0 (fixed volume already exceeds)"
    if value_h == float("inf"):
        return "unbounded (constant volume)"
    if value_h < 1.0:
        return f"{value_h * 60.0:.1f} min"
    return f"{value_h:,.2f} h"


def _power(value_kw: float) -> str:
    if value_kw == 0.0:
        return "0"
    if value_kw == float("inf"):
        return "unbounded"
    if value_kw < 0.0001:
        return "<0.0001"
    if value_kw < 0.01:
        return f"{value_kw:.4f}"
    return f"{value_kw:.2f}"


def _limits_table() -> str:
    rows: list[list[str]] = []
    for m in sorted(MECHANISMS, key=lambda x: rescope.max_power_kw(x, HOURS, TARGET_L), reverse=True):
        max_h = rescope.max_duration_h(m, POWER_KW, TARGET_L)
        max_p = rescope.max_power_kw(m, HOURS, TARGET_L)
        one_h = screen(m, POWER_KW, HOURS, TARGET_L)
        rows.append(
            [
                m.name,
                m.maturity,
                _duration(max_h),
                _power(max_p),
                f"{one_h.best_volume_l:.2f}",
            ]
        )
    return _md_table(
        [
            "Mechanism",
            "Maturity",
            "Max duration at 3 kW in 2.16 L",
            "Max power for 1 h in 2.16 L (kW)",
            "3 kW/1 h volume (L)",
        ],
        rows,
    )


def main() -> int:
    one_h = screen_all(POWER_KW, HOURS, TARGET_L)
    best_current = min((r for r in one_h if r.maturity == "current"), key=lambda r: r.best_volume_l)
    best_generator = min(
        (r for r in one_h if r.maturity == "current" and r.category == "generation"),
        key=lambda r: r.best_volume_l,
    )
    li_duration = rescope.max_duration_h("li_ion", POWER_KW, TARGET_L)
    li_power = rescope.max_power_kw("li_ion", HOURS, TARGET_L)
    cell_125 = rescope.required_cell_wh_l(POWER_KW, HOURS, TARGET_L, 1.25, 0.2)
    cell_110 = rescope.required_cell_wh_l(POWER_KW, HOURS, TARGET_L, 1.10, 0.1)
    cell_zero = rescope.required_cell_wh_l(POWER_KW, HOURS, TARGET_L, 1.0, 0.0)
    pem_stack = rescope.required_stack_kw_per_l(POWER_KW, HOURS, TARGET_L, 0.60, 1.25, 1.5)
    stirling_engine = rescope.required_engine_l_per_kw(POWER_KW, HOURS, TARGET_L, 0.40)

    # A fuel-cell "core" with the fuel tank outside the envelope. This is a
    # concept boundary, not a complete system; quantify the stack density needed.
    core_stack_needed = POWER_KW / (TARGET_L / 1.25 - 1.5) if TARGET_L / 1.25 - 1.5 > 0 else float("inf")

    limits = _limits_table()
    options = _md_table(
        ["Option", "Target", "Best current result", "Status"],
        [
            [
                "A. As stated",
                "3 kWe for 1 h in 2.16 L",
                f"Li-ion {best_current.best_volume_l:.2f} L ({best_current.best_ratio:.2f}×, storage); {best_generator.name} {best_generator.best_volume_l:.2f} L (generator)",
                "FAIL",
            ],
            [
                "B. Buffer module",
                "3 kWe for ≤~21 min in 2.16 L",
                f"Li-ion {li_duration * 60:.1f} min best; no continuous generation",
                "PASS (volume only; cell power limit not modeled)",
            ],
            [
                "C. Lower-power core",
                "≤~1.07 kWe for 1 h in 2.16 L",
                f"Li-ion {li_power:.2f} kW max; not 3 kWe",
                "CONDITIONAL (volume only; 3 kWe relaxed)",
            ],
            [
                "D. Larger storage envelope",
                "3 kWe for 1 h in ≥5.61 L",
                f"Li-ion {best_current.best_volume_l:.2f} L; still storage, not generation",
                "CONDITIONAL (volume only)",
            ],
            [
                "E. Larger generator envelope",
                "3 kWe for 1 h in ≥7.81 L",
                f"{best_generator.name} {best_generator.best_volume_l:.2f} L",
                "CONDITIONAL (volume only)",
            ],
            [
                "F. New mechanism",
                "3 kWe for 1 h in 2.16 L",
                f"Requires ≥{cell_125:,.0f} Wh/L cell at 1.25 packaging; no current chemistry",
                "INSUFFICIENT EVIDENCE",
            ],
            [
                "G. Core + external fuel cartridge",
                "2.16 L power core, fuel outside",
                f"Needs ~{core_stack_needed:.1f} kW/L stack with 1.5 L BOP; current PEM is 1–3 kW/L",
                "CONCEPT, not a complete system",
            ],
        ],
    )

    thresholds = _md_table(
        ["Threshold", "Value", "Interpretation"],
        [
            [
                "Cell density at 1.25 packaging, 0.2 L BOP",
                f"{cell_125:,.0f} Wh/L",
                "≈2.8× a 700 Wh/L cell; Li-air territory",
            ],
            [
                "Cell density at 1.10 packaging, 0.1 L BOP",
                f"{cell_110:,.0f} Wh/L",
                "≈2.3× a 700 Wh/L cell",
            ],
            [
                "Cell density with zero packaging/BOP",
                f"{cell_zero:,.0f} Wh/L",
                "≈2.0× a 700 Wh/L cell; not a system",
            ],
            [
                "PEM stack density with 700 bar H2",
                "infeasible" if pem_stack == float("inf") else f"{pem_stack:.2f} kW/L",
                "H2 tank alone is 3.75 L for 3 kW/1 h",
            ],
            [
                "Stirling engine specific volume",
                "infeasible" if stirling_engine == float("inf") else f"{stirling_engine:.2f} L/kW",
                "Fuel + radiator + BOP already exceed 2.16 L at 3 kW/1 h",
            ],
        ],
    )

    report = f"""# E-Micro re-scope after Gate 2

**Date:** 2026-10-23  
**Input:** `reports/E_MICRO_FEASIBILITY.md`; 30 stdlib tests  
**Question:** if 3 kWe / 1 h / 2.16 L fails, what are the honest product options?

---

## 1. The inverse limits

The Gate 2 screen asks whether a mechanism fits. This table asks the inverse: at 3 kW, how long does the envelope last; at 1 h, how much power can it deliver?

{limits}

A zero duration means the fixed subsystem volume alone (engine, stack, BOP) already exceeds 2.16 L, before fuel or storage. `Unbounded` means the screening volume is independent of duration, not that the system is practical.

---

## 2. Product options

{options}

**Option A is the only one that preserves all four stated constraints, and it fails.** Options B and C change the product; D and E change the envelope; F requires a new mechanism; G changes the system boundary.

---

## 3. What would have to be true

{thresholds}

The 2.16 L envelope is not a small-storage problem. It is a **1.4–2.0 kWh/L cell** problem for a 1 h battery, or a **~13 kW/L PEM stack** problem for a core with external fuel. Neither is a current product.

---

## 4. Inventor's architecture: separate the energy store from the power core

The only physically coherent way to keep a 2.16 L module and still deliver 3 kWe is to stop treating 2.16 L as the complete energy system:

- **2.16 L power core:** fuel-cell stack, air blower, cooling, DC/DC, controls, protection, short buffer.
- **External cartridge:** fuel or H2, with its own volume, mass, containment and cost. It is part of the complete system and must be counted in any product claim.

This is a legitimate modular architecture. It is **not** a self-contained 2.16 L generator, and it does not satisfy the current directive's boundary unless the cartridge is explicitly included. The core still needs about **{core_stack_needed:.1f} kW/L** stack density with 1.5 L BOP, no fuel tank, and no separate buffer or DC/DC allowance beyond that 1.5 L. That is above current 1–3 kW/L PEM systems. It is a research concept, not a design.

A second option is a **2.16 L buffer module**: 3 kW for ~{li_duration * 60:.0f} min, charged externally. That is a physically credible product option, but it is not continuous generation.

---

## 5. Recommendation

1. **Do not build CAD for a 2.16 L continuous 3 kWe generator.** The gate has failed; packaging would be optimizing an infeasible target.
2. **Ask the owner to choose one boundary:** (a) 2.16 L buffer module; (b) 3 kWe/1 h at 6–8 L; (c) 3 kWe/1 h with an external fuel cartridge; or (d) a new mechanism with a complete-system closure.
3. **Run the liquid-fuel fuel-cell evidence review before selecting (b) or (c).** H2 at 700 bar is 3.75 L for 1 h before the stack; a liquid fuel may be smaller, but the reformer, CO cleanup, heat rejection and fuel tank must be counted.
4. **Keep the negative result.** N-39 records the gap; it should not be relabelled as a pass because a subsystem fits.

---

## 6. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** the 2.16 L envelope can host a 3 kW **buffer** for about 20 min with current Li-ion, but not a 3 kWe **continuous generator** for 1 h.

**Evidence:** the Gate 2 volume screen, inverse limits, cell/stack/engine thresholds, and the 0.1008 m² heat-rejection surface.

**Method:** forward complete-system volume model, then monotonic bisection for inverse limits; no new fitted parameters.

**Assumptions:** 700 Wh/L cell, 1.25 packaging, 0.2 L battery BOP, 3 kW/L PEM stack, 1.5 L PEM BOP, 0.040 kg/L H2, 40% Stirling, 1,000 W/m²K and 80 K best heat rejection.

**Uncertainty:** best-case volumes are lower bounds; real systems are larger. Cell power capability, C-rate, cycle life, BMS limits and inverter volume are not modeled. The buffer duration is a volume upper bound, not a pack design; the generator thresholds are more assumption-sensitive.

**Counterargument:** a new chemistry or a liquid-fuel reformer could shrink the generator. That is exactly why option F is “insufficient evidence,” not “impossible,” and why the liquid-fuel review is the next action.

**Verdict:** **FAIL for the self-contained 2.16 L continuous generator.** **PASS only as a short buffer, a lower-power core, or a larger/external-source system.**

---

## 7. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.rescope_report
```
"""
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / "E_MICRO_RESCOPE.md"
    path.write_text(report)

    inputs = [
        ROOT / "engineering" / "data" / "requirements.json",
        ROOT / "engineering" / "mechanisms.py",
        ROOT / "engineering" / "physics.py",
        ROOT / "engineering" / "feasibility.py",
        ROOT / "engineering" / "rescope.py",
    ]
    manifest = {
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "date": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit(),
        "git_commit_note": "commit at run time; generated outputs are committed afterward",
        "target": {"product": "E-MICRO", "power_kw": POWER_KW, "volume_l": TARGET_L, "hours": HOURS},
        "inputs": {str(p.relative_to(ROOT)): _sha256(p) for p in inputs},
        "outputs": {str(path.relative_to(ROOT)): _sha256(path)},
        "notes": [
            "Inverse limits use monotonic bisection on the forward volume screen.",
            "A zero duration means fixed subsystem volume already exceeds the envelope.",
            "Inverse limits are volume-only; cell C-rate, cycle life, BMS and inverter limits are not modeled.",
            "No component quote or measurement is included.",
        ],
    }
    (REPORTS / "e_micro_rescope_run.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {path.relative_to(ROOT)}")
    print("wrote reports/e_micro_rescope_run.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
