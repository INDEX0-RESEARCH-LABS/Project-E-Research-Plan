# Project E — Experiment Strategy

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** plan only; **no experiment has started**  
**Rule:** the cheapest test that can kill the hypothesis, run safely, with a pre-registered decision rule.

---

## 1. What experiments are for

The repository model cannot settle:

- whether a pack can deliver 6 kW pulses at the assumed efficiency and temperature;
- whether the converter mass/power density is real;
- whether the thermal loop rejects heat in the stated envelope;
- whether a fuel-cell/tank system meets its mass and startup assumptions;
- whether a TPV/TEG converter survives at temperature.

Experiments exist to answer those questions, not to demonstrate a preferred architecture.

---

## 2. Gate 5 prerequisites

No experiment starts until:

- [ ] Gate 3 candidate selection (or a deliberately component-only question).
- [ ] Gate 4 model verification and uncertainty.
- [ ] Written test plan with hypothesis, measurement, success/failure, and stop rule.
- [ ] Safety review: fire, H2, high temperature, electrical, pressure.
- [ ] Facility agreement and responsible person.
- [ ] Calibrated instruments and data log.
- [ ] Waste/disposal plan.
- [ ] Budget approval for that test only.

---

## 3. Test sequence

| Stage | Question | Cheapest test | Decision |
|---|---|---|---|
| 1 | Is the pack/converter pulse claim real? | One representative pack + converter, 6 kW / 30 s pulses, thermal sensors | If voltage sag, temperature, or efficiency misses the model, revise or kill |
| 2 | Is the converter mass/efficiency real? | Bench converter at 10–120% load, 25–45 °C | If efficiency <90% or packaged mass >2.0 kg/kW (baseline 1.875), revise |
| 3 | Does the thermal loop reject the heat? | Cold plate + radiator + pump at design heat load | If radiator area/mass exceeds envelope, revise |
| 4 | Does the fuel cell/tank meet startup and mass? | Stack + representative tank, not a full system | If startup >10 min, or M1 system >35 kg (M2 >500 kg), park |
| 5 | Does the TPV/TEG survive? | Small-area module at temperature, 100 h | If degradation >5% or efficiency <15%, park |
| 6 | Does the integrated system close? | Full unit at M1 profile, instrumented | Only if Stages 1–5 pass |

Stage 1 is the highest-value first test **if** a representative pack and converter are already available; otherwise the datasheet and supplier quotation come first. The 6 kW pulse and converter are the binding terms in the benchmark.

---

## 4. Measurement plan

- Electrical: calibrated power analyzer, voltage/current at cell, pack, converter input/output.
- Thermal: thermocouples/RTDs at cells, coolant, radiator; ambient; infrared camera where safe.
- Mechanical: mass scale, dimensions, enclosure volume.
- Fuel: gravimetric or volumetric measurement; no nominal “full tank.”
- Time: synchronized timestamps; pulse timing verified.
- Uncertainty: instrument accuracy, calibration date, repeatability, and a worst-case error budget.

---

## 5. Repeats and decision statistics

- At least 3 repeats per condition; report mean, range, and worst case.
- Use the same protocol for every candidate.
- Pre-register the success threshold and the stop rule.
- Do not add repeats until the result is “significant”; that is p-hacking.
- For a go/no-go component test, a single decisive failure can kill; a single success cannot qualify a system.

---

## 6. Safety

- Li-metal/Li-ion abuse: fire-rated enclosure, remote monitoring, no unattended charging.
- H2: detection, ventilation, pressure relief, grounding, no ignition sources.
- Diesel: exhaust extraction, fuel containment, fire suppression.
- High temperature: guards, thermal cutoffs, remote shutdown.
- Electrical: lockout/tagout, fusing, insulation monitoring.
- Nuclear/RTG: **not in this program** without a licensed partner and regulator approval.

---

## 7. Data integrity

- Raw data retained; processed data reproducible.
- No deletion of failed runs.
- Every plot traceable to a data file and script version.
- Test log records date, operator, instrument IDs, calibration, ambient, and deviations.
- Results are reported with uncertainty and evidence level (E4/E5).

---

## 8. What would make the program stop

- A safety incident that cannot be contained.
- A component test that fails the pre-registered kill criterion and cannot be fixed without changing the mission.
- A result that is not distinguishable from artefact.
- A cost or regulatory barrier that makes the mission infeasible.
- A negative result that is more valuable than continuing.

Stopping is a valid outcome. The negative result is recorded in `NEGATIVE_RESULTS.md`.
