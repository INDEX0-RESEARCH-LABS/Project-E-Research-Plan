# Project E — Negative Results Register

**Version:** 0.1  
**Date:** 2026-10-23  
**Rule:** negative results are retained with their scope and the evidence that would reopen them. A negative result is not a failure of the program; it is a map of where not to spend.

---

## 1. Benchmark negative results (Track A, commit `e75be96`)

| ID | Result | Scope | Evidence | What would reopen it |
|---|---|---|---|---|
| N-01 | No benchmark architecture meets all five M1 targets | Eight fixed architectures; M1 boundary | Repository simulation; 57 tests; fresh run reproduced table | A new architecture or a verified component that changes the binding term |
| N-02 | A1 cannot reach 35 kg for the 8 h M1 mission under the 300 W/kg continuous pack rating | Li-ion pack behind a 6 kW converter | 6 kW / 300 W/kg = 21.1 kg cells; 26.3 kg packaged; 11.25 kg converter before energy; energy dominates at 8 h | A pulse-rated pack (600–1,000 W/kg) plus a shorter mission; this is an assumption, not a universal limit |
| N-03 | A1 needs ~870 Wh/kg cell-level (~696 Wh/kg pack-level) even at zero margin | M1; 6 kW pulse | Gate 2: 16.8 kg cells at 870 Wh/kg, 21.0 kg packaged, 34.9 kg total; 14.62/21.0 = 696 Wh/kg pack-level | A demonstrated ~690–700 Wh/kg pack (or ~865–870 Wh/kg cell) with cooling and cycle life |
| N-04 | C2 diesel hybrid floor is ~44.8 kg at 0.5 h | M1; converter + minimum genset | Repository peak-load sweep | Smaller converter/genset or relaxed peak |
| N-05 | C1 PEM hybrid is ~56.0–56.5 kg | M1; 5 wt% H2 tank; 1.1× source | Repository C1 56.5 kg; Gate 2 one-pass screen 56.0 kg with a different BOP split | 10 wt% system tank, lighter stack, or lower peak |
| N-06 | B2 TEG-on-burner fails on radiator and efficiency | M1; 6.2% conversion | 38 m² radiator; 300 kg class | ZT/device efficiency >2× with a compact heat exchanger |
| N-07 | B3 TPV thermal store is not self-contained and fails H4 | M4 converter; external ≥1500 °C heat | 484–806 kg usable graphite store alone (0.06–0.10 kWh/kg); repo 0.28 kWh/kg is full-swing, not TPV-usable | A usable store ≥1 kWh/kg, a co-located heat source, and emitter/cells/radiator inside the boundary |
| N-08 | Best baseline score is 3/5, not a pass | Scorecard | A1, B3, C2 at 3/5; no candidate at 5/5 | A candidate that passes hard gates and scores higher on evidence |

---

## 2. Gate 2 screening negatives

| ID | Result | Scope | Evidence | What would reopen it |
|---|---|---|---|---|
| N-09 | 175 Wh/kg basis cannot meet M1 mass | Screen; A1 basis (175 treated as pre-packaging) | 118.3 kg | ~690–700 Wh/kg pack or ~865–870 Wh/kg cell, with packaging and cooling |
| N-10 | 300 Wh/kg basis cannot meet M1 mass | Screen | 74.8 kg | ~690–700 Wh/kg pack or a different mission |
| N-11 | 500 Wh/kg basis cannot meet M1 mass with margin | Screen | 50.4 kg | ~690–700 Wh/kg pack and a lighter converter |
| N-12 | Diesel hybrid is ~49.3 kg (repo 50.3 kg) | Screen; 1.447 kW source | 49.3 kg one-pass; repo double-packages fuel by ~1 kg | Smaller source/converter or a relaxed peak |
| N-13 | PEM hybrid is ~56 kg | Screen; 5 wt% H2 | 56.0 kg | 10 wt% tank and lighter stack |
| N-14 | Solar + 14.62 kWh nameplate storage is 135.7 kg before mounting/MPPT | M2/M4; external sunlight; not M1-comparable | 4 m² panel + 104.4 kg pack + 11.25 kg converter; 10 kWh delivered | A much lighter storage system; solar is an M2/M4 option, not a compact core |
| N-15 | Fission–Stirling is 100–1,000 kg class; H3 unresolved | 1 kWe M2 concept range | Literature range; midpoint 550 kg; shielding not modeled | A verified <500 kg/kWe shielded unit and a lawful path; not expected soon |
| N-16 | Supercapacitor is a buffer, not an energy store | 0.05 kWh pulse | 8.3 kg at 6 Wh/kg | >100 Wh/kg supercap with safe packaging |

---

## 3. Landscape negatives

| ID | Result | Scope | Evidence | What would reopen it |
|---|---|---|---|---|
| N-17 | LENR / cold fusion is not a funded track | Literature; 2004 DOE review | Review found evidence not conclusive; no accepted replication | Pre-registered, independent, full-energy-balance replication |
| N-18 | Over-unity / perpetual motion is screened out | Physics | Conservation of energy; no reproducible evidence | A replicated net-output experiment with accounted source |
| N-19 | Betavoltaics are not kW-scale | Physics/landscape | µW–mW class | A verified kW-scale device with shielding |
| N-20 | Fusion is not near-term | Landscape | No net-electric pilot; facility scale | A net-electric pilot and a credible compact path |
| N-21 | Patents are not proof | Method | Prior art only | Independent performance and safety data |
| N-22 | C1 fails H5 at the baseline H2 price | M1; $6/kg H2 | H5 kill: H2 > $4/kg; repo C1 uses $6/kg | H2 ≤ $4/kg delivered, or a tank/stack improvement that offsets cost |
| N-23 | A2 and the supercapacitor buffer fail H7 | M1 pulse buffer | Supercap 0.05 kWh at 6 Wh/kg = 8.3 kg; H7 kill is >5 kg | A >100 Wh/kg supercap or a smaller pulse energy, with safe packaging |
| N-24 | B3 fails H4 on store density | M4; external heat | Usable 0.06–0.10 kWh/kg vs H4 ≥1 kWh/kg | A usable store ≥1 kWh/kg at ≥1500 °C emitter temperature |


---

## 4. Corrections and retractions

| ID | Item | Correction | Status |
|---|---|---|---|
| C-01 | First `screening.py` fuel-cell result 48.4 kg | Omitted packaging on stack/tank/BOP, used 1.4 kW instead of 1.447 kW, omitted radiator; corrected to ~56.0 kg and reconciled to repo 56.5 kg | Corrected in v0.2 |
| C-02 | “1.5 kg/kW gives 11.25 kg at 6 kW” | 11.25 kg includes the 1.25 packaging factor: 1.5 × 6 × 1.25 | Documented as audit note D12; code is consistent |
| C-03 | Converter mass first screen 9.0 kg | Used 1.5 × 6 without packaging; corrected to 11.25 kg | Corrected in v0.2 |
| C-04 | Diesel 2.0 kW row 51.4 kg | 2.0 kW was a source size, not a 2 kW peak mission; row removed to avoid a category error | Corrected in v0.2 |

---

## 5. What is not a negative result

- A model that has not been validated is **unvalidated**, not negative.
- A supplier who has not quoted is **unknown**, not negative.
- A test that was not run is **pending**, not negative.
- A paper that was not read is **pending**, not negative.
- A failure of the benchmark mission is **not** a failure of Project E.

---

## 6. Retention rule

Every negative result stays in this register. It may be superseded, but not deleted. Each entry must state its scope, evidence, and reopening condition.
