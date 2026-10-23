# E-Micro re-scope after Gate 2

**Date:** 2026-10-23  
**Input:** `reports/E_MICRO_FEASIBILITY.md`; 30 stdlib tests  
**Question:** if 3 kWe / 1 h / 2.16 L fails, what are the honest product options?

---

## 1. The inverse limits

The Gate 2 screen asks whether a mechanism fits. This table asks the inverse: at 3 kW, how long does the envelope last; at 1 h, how much power can it deliver?

| Mechanism | Maturity | Max duration at 3 kW in 2.16 L | Max power for 1 h in 2.16 L (kW) | 3 kW/1 h volume (L) |
|---|---|---|---|---|
| Li-air battery (theoretical) | theoretical | 45.8 min | 2.29 | 2.75 |
| Li-ion battery | current | 21.4 min | 1.07 | 5.61 |
| PEM fuel cell + 700 bar H2 | current | 0 (fixed volume already exceeds) | 0.14 | 7.81 |
| Stirling engine + alternator | advanced | 0 (fixed volume already exceeds) | 0.04 | 22.97 |
| Thermophotovoltaic converter | advanced | 0 (fixed volume already exceeds) | 0.04 | 23.44 |
| Microturbine + high-speed alternator | advanced | 0 (fixed volume already exceeds) | 0.03 | 34.69 |
| Thermoelectric generator | current | 0 (fixed volume already exceeds) | 0.02 | 36.12 |
| Diesel genset | current | 0 (fixed volume already exceeds) | 0.02 | 42.19 |
| Supercapacitor bank | current | 0.3 min | 0.02 | 375.25 |
| Radioisotope thermoelectric generator | restricted | 0 (fixed volume already exceeds) | 0.0029 | 301.88 |
| Solar PV + storage | current | 0 (fixed volume already exceeds) | 0.0028 | 307.23 |
| Ambient harvesting | theoretical | 0 (fixed volume already exceeds) | <0.0001 | 18751.88 |

A zero duration means the fixed subsystem volume alone (engine, stack, BOP) already exceeds 2.16 L, before fuel or storage. `Unbounded` means the screening volume is independent of duration, not that the system is practical.

---

## 2. Product options

| Option | Target | Best current result | Status |
|---|---|---|---|
| A. As stated | 3 kWe for 1 h in 2.16 L | Li-ion 5.61 L (2.60×, storage); PEM fuel cell + 700 bar H2 7.81 L (generator) | FAIL |
| B. Buffer module | 3 kWe for ≤~21 min in 2.16 L | Li-ion 21.4 min best; no continuous generation | PASS (volume only; cell power limit not modeled) |
| C. Lower-power core | ≤~1.07 kWe for 1 h in 2.16 L | Li-ion 1.07 kW max; not 3 kWe | CONDITIONAL (volume only; 3 kWe relaxed) |
| D. Larger storage envelope | 3 kWe for 1 h in ≥5.61 L | Li-ion 5.61 L; still storage, not generation | CONDITIONAL (volume only) |
| E. Larger generator envelope | 3 kWe for 1 h in ≥7.81 L | PEM fuel cell + 700 bar H2 7.81 L | CONDITIONAL (volume only) |
| F. New mechanism | 3 kWe for 1 h in 2.16 L | Requires ≥1,963 Wh/L cell at 1.25 packaging; no current chemistry | INSUFFICIENT EVIDENCE |
| G. Core + external fuel cartridge | 2.16 L power core, fuel outside | Needs ~13.2 kW/L stack with 1.5 L BOP; current PEM is 1–3 kW/L | CONCEPT, not a complete system |

**Option A is the only one that preserves all four stated constraints, and it fails.** Options B and C change the product; D and E change the envelope; F requires a new mechanism; G changes the system boundary.

---

## 3. What would have to be true

| Threshold | Value | Interpretation |
|---|---|---|
| Cell density at 1.25 packaging, 0.2 L BOP | 1,963 Wh/L | ≈2.8× a 700 Wh/L cell; Li-air territory |
| Cell density at 1.10 packaging, 0.1 L BOP | 1,610 Wh/L | ≈2.3× a 700 Wh/L cell |
| Cell density with zero packaging/BOP | 1,389 Wh/L | ≈2.0× a 700 Wh/L cell; not a system |
| PEM stack density with 700 bar H2 | infeasible | H2 tank alone is 3.75 L for 3 kW/1 h |
| Stirling engine specific volume | infeasible | Fuel + radiator + BOP already exceed 2.16 L at 3 kW/1 h |

The 2.16 L envelope is not a small-storage problem. It is a **1.4–2.0 kWh/L cell** problem for a 1 h battery, or a **~13 kW/L PEM stack** problem for a core with external fuel. Neither is a current product.

---

## 4. Inventor's architecture: separate the energy store from the power core

The only physically coherent way to keep a 2.16 L module and still deliver 3 kWe is to stop treating 2.16 L as the complete energy system:

- **2.16 L power core:** fuel-cell stack, air blower, cooling, DC/DC, controls, protection, short buffer.
- **External cartridge:** fuel or H2, with its own volume, mass, containment and cost. It is part of the complete system and must be counted in any product claim.

This is a legitimate modular architecture. It is **not** a self-contained 2.16 L generator, and it does not satisfy the current directive's boundary unless the cartridge is explicitly included. The core still needs about **13.2 kW/L** stack density with 1.5 L BOP, no fuel tank, and no separate buffer or DC/DC allowance beyond that 1.5 L. That is above current 1–3 kW/L PEM systems. It is a research concept, not a design.

A second option is a **2.16 L buffer module**: 3 kW for ~21 min, charged externally. That is a physically credible product option, but it is not continuous generation.

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
