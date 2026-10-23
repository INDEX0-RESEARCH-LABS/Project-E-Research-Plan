# E-Micro re-scope after Gate 2

**Date:** 2026-10-23  
**Input:** `reports/E_MICRO_FEASIBILITY.md` (revision 0.2); `engineering/tests` stdlib tests  
**Question:** if 3 kWe / 1 h / 2.16 L fails, what are the honest product options?

---

## 1. The inverse limits

The Gate 2 screen asks whether a mechanism fits. This table asks the inverse: at 3 kW, how long does the envelope last; at 1 h, how much power can it deliver?

| Mechanism | Maturity | Max duration at 3 kW in 2.16 L | Max power for 1 h in 2.16 L (kW) | 3 kW/1 h volume (L) |
|---|---|---|---|---|
| Li-air battery (theoretical) | theoretical | 33.8 min | 1.69 | 3.25 |
| Li-ion battery | current | 15.8 min | 0.79 | 6.11 |
| Supercapacitor bank | current | 0.2 min | 0.01 | 375.75 |
| Diesel genset | current | 0 (fixed volume already exceeds) | 0 | 42.69 |
| Stirling engine + alternator | advanced | 0 (fixed volume already exceeds) | 0 | 23.47 |
| Microturbine + high-speed alternator | advanced | 0 (fixed volume already exceeds) | 0 | 35.19 |
| PEM fuel cell + 700 bar H2 | current | 0 (fixed volume already exceeds) | 0 | 8.94 |
| Thermophotovoltaic converter | advanced | 0 (fixed volume already exceeds) | 0 | 23.94 |
| Thermoelectric generator | advanced | 0 (fixed volume already exceeds) | 0 | 36.62 |
| Solar PV + storage | current | 0 (fixed volume already exceeds) | 0 | 307.73 |
| Radioisotope thermoelectric generator | restricted | 0 (fixed volume already exceeds) | 0 | 302.38 |
| Ambient harvesting | theoretical | 0 (fixed volume already exceeds) | 0 | 18752.38 |

A zero duration means the fixed subsystem volume alone (engine, stack, BOP, converter) already exceeds 2.16 L before fuel or storage. The same fixed-volume artifact produces the zero **max power** entries: at any power, 1.5 L BOP + 0.4 L converter × 1.25 packaging = 2.375 L, so the model returns 0. This does **not** prove that a micro-power heat engine or fuel cell is impossible; it proves that this BOP allowance cannot close at 3 kWe. `Unbounded` means the screening volume is independent of duration, not that the system is practical. The 0.4 L converter is an estimate; it is included because a 3 kWe product needs one.

---

## 2. Product options

| Option | Target | Best current result | Status |
|---|---|---|---|
| A. As stated | 3 kWe for 1 h in 2.16 L | Li-ion 6.11 L (2.83×, storage); PEM fuel cell + 700 bar H2 8.94 L (generator) | FAIL |
| B. Buffer module | 3 kWe for ≤~16 min in 2.16 L | Li-ion 15.8 min best (100% DoD); ~12 min at 80% DoD/95% converter; no generation | PASS (volume only; cell power limit not modeled) |
| C. Lower-power core | ≤~0.79 kWe for 1 h in 2.16 L | Li-ion 0.79 kW max; not 3 kWe | CONDITIONAL (volume only; 3 kWe relaxed) |
| D. Larger storage envelope | 3 kWe for 1 h in ≥6.11 L | Li-ion 6.11 L; still storage, not generation | CONDITIONAL (volume only) |
| E. Larger generator envelope | 3 kWe for 1 h in ≥8.94 L | PEM fuel cell + 700 bar H2 8.94 L | CONDITIONAL (volume only) |
| F. New mechanism | 3 kWe for 1 h in 2.16 L | Requires ≥2,660 Wh/L cell at 1.25 packaging, 0.2 L BOP, 0.4 L converter; no current chemistry | INSUFFICIENT EVIDENCE |
| G. Core + external fuel cartridge | 2.16 L power core, fuel outside | No positive stack volume with 1.5 L BOP + 0.4 L converter (fixed 1.9 L × 1.25 = 2.375 L); even with zero converter, ~13.2 kW/L vs 1–3 kW/L current PEM | CONCEPT, not a complete system |

**Option A is the only one that preserves all four stated constraints, and it fails.** Options B and C change the product; D and E change the envelope; F requires a new mechanism; G changes the system boundary.

---

## 3. What would have to be true

| Threshold | Value | Interpretation |
|---|---|---|
| Cell density at 1.25 packaging, 0.2 L BOP, 0.4 L converter | 2,660 Wh/L | ≈3.8× a 700 Wh/L cell; Li-air territory |
| Cell density at 1.10 packaging, 0.1 L BOP, 0.4 L converter | 2,050 Wh/L | ≈2.9× a 700 Wh/L cell |
| Cell density with zero packaging/BOP/converter | 1,389 Wh/L | ≈2.0× a 700 Wh/L cell; not a system |
| PEM stack density with 700 bar H2 | infeasible | H2 gas alone is 3.75 L for 3 kW/1 h; a Type IV vessel is larger; BOP+converter already exceed 1.728 L |
| Stirling engine specific volume | infeasible | Fuel + radiator + BOP + converter already exceed 2.16 L at 3 kW/1 h |

The 2.16 L envelope is not a small-storage problem. It is a **1.4–2.7 kWh/L cell** problem for a 1 h battery with the converter counted, or a **no-positive-volume PEM core** problem once 1.5 L BOP and 0.4 L converter are inside 2.16 L. Even with zero converter, the core needs ~13.2 kW/L. Neither is a current product.

---

## 4. Inventor's architecture: separate the energy store from the power core

The architectural route that keeps a 2.16 L module is to stop treating 2.16 L as the complete energy system:

- **2.16 L power core:** fuel-cell stack, air blower, cooling, DC/DC, controls, protection, short buffer.
- **External cartridge:** fuel or H2, with its own volume, mass, containment and cost. It is part of the complete system and must be counted in any product claim.

This is a legitimate modular architecture. It is **not** a self-contained 2.16 L generator, and it does not satisfy the current directive's boundary unless the cartridge is explicitly included. With 1.5 L BOP and 0.4 L converter, the fixed volume is **1.9 L × 1.25 = 2.375 L**, already larger than 2.16 L, so there is **no positive stack volume**. Even with zero converter, the core needs about **13.2 kW/L** stack density, above current 1–3 kW/L PEM systems. It is a research concept, not a design.

A second option is a **2.16 L buffer module**: 3 kW for ~16 min at 100% DoD (~12 min at 80% DoD/95% converter), charged externally. That is a physically credible product option, but it is not continuous generation.

---

## 5. Recommendation

1. **Do not build CAD for a 2.16 L continuous 3 kWe generator.** The gate has failed; packaging would be optimizing an infeasible target.
2. **Ask the owner to choose one boundary:** (a) 2.16 L buffer module; (b) 3 kWe/1 h at 6–9 L (storage, not generation); (c) 3 kWe/1 h with an external fuel cartridge; or (d) a new mechanism with a complete-system closure.
3. **The liquid-fuel review is complete and does not rescue the envelope.** The best documented reformed-methanol module is 81 L for 5 kW; a 3 kW/1 h complete system is ≈86 L (≈40×). H2 at 700 bar is also 3.75 L of gas before the vessel and stack. Only a market scan for a sub-81 L 3 kW liquid-fuel product could reopen this.
4. **Keep the negative result.** N-39 records the gap; it should not be relabelled as a pass because a subsystem fits. N-41 records the revision-0.2 corrections.

---

## 6. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** the 2.16 L envelope can host a 3 kW **buffer** for about 16 min at 100% DoD (12 min at 80% DoD/95% converter) with current Li-ion, but not a 3 kWe **continuous generator** for 1 h.

**Evidence:** the Gate 2 volume screen (revision 0.2), inverse limits, cell/stack/engine thresholds, and the air-side heat-rejection check. The envelope skin is 0.1008 m² but is not itself a radiator.

**Method:** forward complete-system volume model with a 0.4 L converter, then monotonic bisection for inverse limits; no new fitted parameters.

**Assumptions:** 700 Wh/L cell, 1.25 packaging, 0.2 L battery BOP, 0.4 L converter, 3 kW/L PEM stack, 1.5 L PEM BOP, 0.040 kg/L H2 gas, 40% Stirling, and a 4 kW/L fin-stack equivalent for the best radiator. The 105 °C skin at ΔT=80 K is not claimed as touch-safe.

**Uncertainty:** best-case volumes are lower bounds; real systems are larger. The converter is a 0.4 L estimate; cell C-rate, cycle life, BMS details, vessel external volume and detailed inverter design are not modeled. The buffer duration is a volume upper bound, not a pack design; the generator thresholds are more assumption-sensitive.

**Counterargument:** a new chemistry or a liquid-fuel reformer could shrink the generator. That is why option F is “insufficient evidence,” not “impossible.” The liquid-fuel review found no sub-81 L 3 kW product; it weakens, rather than supports, the liquid-fuel rescue.

**Verdict:** **FAIL for the self-contained 2.16 L continuous generator.** The only volume-only pass is a short buffer (~8–16 min); a lower-power core or a larger/external-source system is a conditional re-scope, not a 3 kWe/1 h generator.

---

## 7. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.rescope_report
```
