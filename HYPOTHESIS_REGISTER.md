# Project E — Hypothesis Register

**Version:** 0.2 (Gate 2)  
**Date:** 2026-10-23  
**Status:** provisional; no hypothesis selected; no experiment authorised  
**Machine-readable annex:** `HYPOTHESIS_REGISTER.csv` (same IDs; CSV kept for tabular filtering)  
**Evidence classes:** E0 speculative · E1 theoretical/preliminary · E2 related established evidence · E3 numerical validation · E4 controlled experiment · E5 independent replication · E6 system demonstration

> Evidence class describes maturity, **not** probability of success. A simulation output never promotes a hypothesis.

---

## 1. Summary

| ID | Hypothesis | Category | Missions | Evidence | Gate 2 verdict | Next |
|---|---|---|---|---|---|---|
| H1 | Advanced Li-metal / solid-state pack | Storage | M1, M3, M5 | E1 | open / paper | datasheet + cell test |
| H2 | Li–S or Li–air step-change | Storage | M1, M3, M5 | E1 | open / paper | literature + sample cell |
| H3 | Micro-fission Stirling | Generation | M2 | E1 | parked / unresolved | paper + regulatory study |
| H4 | TPV + thermal store | Conversion | M4 | E1 | **killed for now** (store <1 kWh/kg) | reopen only with a denser store |
| H5 | PEM fuel cell + advanced tank | Generation | M1, M2 | E1 | **parked at $6/kg H₂** | revisit if H₂ ≤$4/kg |
| H6 | Thermionic / AMTEC / Stirling | Conversion | M4, M2 | E1 | open / paper | vendor/lab data |
| H7 | Flywheel / supercapacitor buffer | Power | M3 | E1 | **killed as stated** (8.3 kg) | reopen at ≥13 Wh/kg |
| H8 | LENR / over-unity / zero-point | Negative control | — | E1 | negative control | no spend until a specific claim |
| H9 | SOFC + reformer | Generation | M4, M2 | E1 (source pending) | open / paper | vendor data |
| H10 | Free-piston / microturbine | Generation | M1, M3 | E0/E1 | open / paper | literature + bench data |
| H11 | Phase-change thermal store | Storage/conversion | M4 | E1 (S09) | open / paper | material data |

**No hypothesis is above E1.** No hypothesis has a measured system-level result. The register is deliberately diverse; it is not a shortlist.

---

## 2. Detailed cards

### H1 — Advanced Li-metal / solid-state pack

| Field | Entry |
|---|---|
| ID / name | H1 — Advanced Li-metal solid-state pack |
| Category / missions | Storage; M1, M3, M5 |
| Physical mechanism | Li-metal anode and/or solid electrolyte; electrochemical storage charged from an external source |
| Supporting evidence | S04 (Li-ion materials limits), N01 (materials/cost), N02 (solid-state promise and interfaces); all E1 until page locators |
| What is new | Higher cell energy and safety than LFP; **not a new source** |
| Model | \(e_\text{pack}=e_\text{cell}/(1+f)\); \(m=(1+f)E_\text{name}/e_\text{cell}+p_cP(1+f)+m_\text{BOP}\) |
| Predicted effect | 300–400 Wh/kg cell. At 200–260 Wh/kg pack, M1 is ~70–87 kg; at 300–400 Wh/kg pack, ~50–65 kg. **No M1 pass without 510–691 Wh/kg pack.** |
| System benefit | M1 mass falls from ~118 kg to ~70–87 kg (200–260 pack) or ~50–65 kg (300–400 pack); M3 near-feasible; M5 feasible |
| Best / realistic | 400 Wh/kg cell / 260 pack; 300 cell / 210 pack |
| Assumptions / uncertainty | packaging 1.25; 92% round-trip; 95% converter; 90% DoD; interface life and cost high uncertainty |
| Physics conflict | None; the constraint is materials/interfaces, not thermodynamics |
| Alternative explanation | Gains may be cell-level only and vanish in pack packaging, thermal management, and cycle life |
| Computational model | Ragone + pack build-up; no DFT required at Gate 3 |
| Smallest falsifying experiment | One commercial/lab cell at C/2: energy density, 500 cycles, thermal runaway behaviour |
| Instruments | Calibrated cycler, calorimeter, arc/flame test, uncertainty ±2% |
| Cost / time | ₹3–6 lakh; 4–8 weeks (T1) |
| Safety / regulatory | Li-metal reactivity, UN38.3 transport, fire containment; certified lab |
| Stop criteria | Component milestone: <250 Wh/kg pack; <500 cycles; >$400/kWh; unsafe failure mode. **M1 additionally fails unless the pack reaches 510–691 Wh/kg.** |
| Independent review | Cell data checked by a second lab; no vendor-only claim |
| Evidence class | E1 |
| Gate 2 verdict | Open; paper/datasheet. **Not a solution to M1** unless a pack in the 510–691 Wh/kg range is demonstrated |

### H2 — Li–S or Li–air step-change

| Field | Entry |
|---|---|
| ID / name | H2 — Li–S or Li–air step-change storage |
| Category / missions | Storage; M1, M3, M5 |
| Physical mechanism | Li–S conversion chemistry, or Li–air with O₂ intake; charged from an external source |
| Supporting evidence | N01, N02 as context; **no verified Li–S/Li–air source yet**; E1 |
| What is new | Theoretical cell energy far above Li-ion; practical barriers are the question |
| Model | Same Ragone build-up; round-trip and cycle life enter as derating factors |
| Predicted effect | 300–500 Wh/kg cell claim; practical pack 200–300 Wh/kg; 100–500 cycles; Li–air round-trip poor |
| System benefit | M1 mass potentially ~60–80 kg; M5 strong; M2 still fails (needs >1,100 Wh/kg pack) |
| Best / realistic | 500 cell / 300 pack; 300 cell / 200 pack |
| Assumptions / uncertainty | Very high; chemistry, self-discharge, electrolyte/air handling |
| Physics conflict | None; Li–air is an open system and must account for O₂, CO₂, and H₂O management |
| Alternative explanation | Laboratory cells may use excess Li/electrolyte; pack-level gain may disappear |
| Computational model | Ragone + degradation curve; no new solver |
| Smallest falsifying experiment | Sample cell: ≥200 Wh/kg pack-equivalent, ≥100 cycles, ≥60% round-trip |
| Instruments | Cycler, coulombic efficiency, GC/MS for polysulfide/air side products |
| Cost / time | ₹2–5 lakh; 6–12 weeks |
| Safety / regulatory | Sulfur/air handling, fire, transport; fume hood |
| Stop criteria | <200 Wh/kg pack; <100 cycles; <60% round-trip; unsafe |
| Independent review | Cell results replicated before any system claim |
| Evidence class | E1 |
| Gate 2 verdict | Open; paper only. Do not model a system until a cell passes |

### H3 — Micro-fission Stirling

| Field | Entry |
|---|---|
| ID / name | H3 — Micro-fission Stirling for long-duration remote |
| Category / missions | Generation; M2 |
| Physical mechanism | U-235 fission → heat → Stirling/linear engine → electricity |
| Supporting evidence | N08 (KRUSTY 1 kWe ground test), N13/N14 (NASA reports); E1 |
| What is new | High energy density and 24/7 operation for M2; **not portable** |
| Model | \(m_\text{sys}=m_\text{reactor}+m_\text{shield}+m_\text{engine}+m_\text{radiator}+m_\text{control}\); \(Q_\text{rej}=P(1-\eta)/\eta\) |
| Predicted effect | 1 kWe ground test; 10 kWe design concept; 100–1,000 kg/kWe concept range; fuel mass negligible |
| System benefit | M2 mass and duration; no diurnal/seasonal limit |
| Best / realistic | 100–200 kg/kWe with a thin shield; 500–1,000 kg/kWe with full shielding/regulation |
| Assumptions / uncertainty | Shield, radiator, security, licensing, decommissioning; all site-specific |
| Physics conflict | None; the barriers are engineering, safety, and law |
| Alternative explanation | “Compact” claims often omit shielding, exclusion zone, and emergency planning |
| Computational model | Point-kinetics + thermal lumped model; **no criticality experiment** |
| Smallest falsifying experiment | None by this project; paper study + licensed partner data only |
| Instruments | n/a (no nuclear experiment authorised) |
| Cost / time | ₹0–2 lakh paper/regulatory study; 3–6 months |
| Safety / regulatory | Nuclear licensing, radiation, export control, security; no home experiment |
| Stop criteria | >500 kg/kWe for 1 kWe at M2; no lawful path; cost >M2 budget |
| Independent review | Nuclear engineer and regulatory specialist required |
| Evidence class | E1 |
| Gate 2 verdict | Parked; unresolved. Keep as an M2 note, not an M1 option |

### H4 — TPV + thermal store

| Field | Entry |
|---|---|
| ID / name | H4 — TPV plus thermal store for stationary heat-to-power |
| Category / missions | Conversion; M4 |
| Physical mechanism | External heat → emitter (≥1500 °C) → TPV cells → electricity; thermal store decouples heat and power |
| Supporting evidence | S01 (40% cell at 1900–2400 °C), S08/S09 (thermal storage reviews); E1 |
| What is new | High-temperature TPV cell efficiency; thermal storage decouples heat and power |
| Model | \(E_\text{th}=E_e/(\eta_\text{cell}\eta_\text{spec}\eta_\text{conv})\); \(m_\text{store}=E_\text{th}/e_\text{store}\) |
| Predicted effect | Usable store 0.06–0.10 kWh/kg; 10 kWh electric needs ~39 kWh thermal; graphite 387–645 kg; store 484–806 kg before emitter/cells/radiator |
| System benefit | M4 only, with a co-located heat source; not a portable source |
| Best / realistic | 0.10 kWh/kg usable / 0.06 kWh/kg usable |
| Assumptions / uncertainty | Emitter ≥1500 °C; 32% cell × 0.85 spectral × 0.95 converter = 25.8%; insulation and standby loss |
| Physics conflict | None; the 0.28 kWh/kg repository figure is full-swing sensible heat, not usable at the emitter temperature |
| Alternative explanation | A smaller store with a continuous heat source may beat a large store; the heat source is then the system |
| Computational model | Thermal network + TPV detailed-balance; no CFD until justified |
| Smallest falsifying experiment | Material coupon + small TPV cell at temperature; measure usable kWh/kg and system efficiency |
| Instruments | Guarded hot plate, thermocouples, calibrated light/heat source, IV curve |
| Cost / time | ₹2–6 lakh; 6–10 weeks |
| Safety / regulatory | High temperature, burns, III-V materials; fume hood and shielding |
| Stop criteria | System <20%; usable store <1 kWh/kg; no co-located heat; >$1/W |
| Independent review | Thermal and photonics reviewer; replicate store measurement |
| Evidence class | E1 |
| Gate 2 verdict | **Killed for now** (store 484–806 kg). Reopen only with a store ≥1 kWh/kg usable |

### H5 — PEM fuel cell + advanced tank

| Field | Entry |
|---|---|
| ID / name | H5 — H₂ PEM fuel cell with advanced tank |
| Category / missions | Generation; M1, M2 |
| Physical mechanism | H₂ oxidation in a PEM stack → electricity + heat; H₂ stored in a tank |
| Supporting evidence | S11, N03, N04, N11; E1 |
| What is new | Lightweight tank + high-efficiency stack for M1/M2 |
| Model | \(m_{\mathrm{H_2}}=E/(\eta_\text{fc}\text{LHV})\); \(m_\text{tank}=m_{\mathrm{H_2}}/w\); system sum |
| Predicted effect | 45–55% LHV; 0.632 kg H₂ for 10 kWh; 5 wt% tank 12.63 kg; C1 ~56 kg; 6.3 kW stack variant >60 kg |
| System benefit | M2 if H₂ ≤$4/kg; M1 fails mass |
| Best / realistic | 55% LHV / 45%; 10 wt% tank / 5 wt% |
| Assumptions / uncertainty | 5 wt% system tank; 8 kg/kW stack; 95% converter; H₂ price $6/kg |
| Physics conflict | None; fuel-cell ΔG/ΔH ceiling is 83% at 25 °C |
| Alternative explanation | A “light tank” may be a lab vessel, not a certified system with valves, relief, and leak detection |
| Computational model | Stack polarization + tank mass + heat balance |
| Smallest falsifying experiment | Integrated 1 kW stack + 5 wt% tank: system mass, efficiency, leak rate |
| Instruments | Mass balance, H₂ detector, load bank, thermal sensors |
| Cost / time | ₹5–12 lakh; 8–12 weeks |
| Safety / regulatory | High-pressure H₂, fire, embrittlement; certified lab and ventilation |
| Stop criteria | C1 >35 kg for M1; H₂ >$4/kg; tank <5 wt%; leak/embrittlement unsafe |
| Independent review | H₂ safety reviewer; supplier datasheets, not brochure claims |
| Evidence class | E1 |
| Gate 2 verdict | **Parked at $6/kg H₂**; fuel alone is $0.36/kWh and capex needs 12,500 missions |

### H6 — Thermionic / AMTEC / Stirling

| Field | Entry |
|---|---|
| ID / name | H6 — Thermionic, AMTEC, or Stirling converter |
| Category / missions | Conversion; M4, M2 |
| Physical mechanism | Heat → electrons (thermionic), electrochemical cell (AMTEC), or mechanical piston (Stirling) → electricity |
| Supporting evidence | S12 (ORC/Stirling context); detailed thermionic/AMTEC review pending; E1 |
| What is new | High-temperature compact conversion for M4/M2 |
| Model | \(\eta\le\eta_\text{Carnot}\); practical fraction depends on temperature, electrode life, recuperation |
| Predicted effect | 10–40% depending on temperature and maturity; high-T materials; life uncertain |
| System benefit | M4 bottoming/standalone; M2 niche |
| Best / realistic | 30% at 1,200 K / 15% at 900 K |
| Assumptions / uncertainty | Hot side 800–1,500 K; cold 300–400 K; recuperation; radiator |
| Physics conflict | None; the limits are materials, seals, and electrode life |
| Alternative explanation | A laboratory efficiency at small area may not survive scale-up and thermal cycling |
| Computational model | Lumped thermal + empirical efficiency curve; no new solver |
| Smallest falsifying experiment | Bench converter at representative ΔT: efficiency, 1,000 h life, mass |
| Instruments | Calorimeter, load bank, thermocouples, vacuum chamber |
| Cost / time | ₹2–6 lakh; 8–12 weeks |
| Safety / regulatory | High temperature, seals, materials; qualified lab |
| Stop criteria | <15%; <5,000 h; >5 kg/kW; no supplier |
| Independent review | Converter specialist; replicate efficiency |
| Evidence class | E1 |
| Gate 2 verdict | Open; paper. Not an M1 option |

### H7 — Flywheel / supercapacitor buffer

| Field | Entry |
|---|---|
| ID / name | H7 — Flywheel or supercapacitor pulse buffer |
| Category / missions | Power; M3 (and M1 pulse) |
| Physical mechanism | Electromechanical or electrostatic storage; high power, low energy |
| Supporting evidence | S03 (supercapacitors), N05 (flywheels); E1 |
| What is new | High power and cycle life for pulses; **not mission energy** |
| Model | \(E=\tfrac12CV^2\) (supercap) or \(E=\tfrac12I\omega^2\) (flywheel); \(m=E/e\) + containment |
| Predicted effect | Supercap 6 Wh/kg; 0.05 kWh ~8.3 kg; flywheel 20–100 Wh/kg → 0.5–2.5 kg + containment |
| System benefit | Decouples pulse from converter rating; net saving only ~0.6 kg at current components |
| Best / realistic | 10 Wh/kg supercap / 6 Wh/kg; 100 Wh/kg flywheel / 30 Wh/kg |
| Assumptions / uncertainty | 90% round-trip; containment mass; self-discharge |
| Physics conflict | None; energy density is the limit |
| Alternative explanation | The converter saving may be smaller than assumed; the buffer may add thermal and safety mass |
| Computational model | Ragone + pulse duty + containment mass |
| Smallest falsifying experiment | Module test: 0.05 kWh, 6 kW pulse, round-trip, mass with containment |
| Instruments | Load bank, cycler, strain/containment test |
| Cost / time | ₹1–3 lakh; 4–6 weeks |
| Safety / regulatory | Flywheel burst, high voltage, PPE; containment cell |
| Stop criteria | Buffer >5 kg for 0.05 kWh; round-trip <90%; containment prohibitive |
| Independent review | Energy-storage reviewer; burst test witness |
| Evidence class | E1 |
| Gate 2 verdict | **Killed as stated**: 8.3 kg buffer vs 8.9 kg converter saving = 0.6 kg net. Reopen at ≥13 Wh/kg |

### H8 — LENR / over-unity / zero-point (negative control)

| Field | Entry |
|---|---|
| ID / name | H8 — LENR, over-unity, zero-point |
| Category / missions | Negative control; none |
| Physical mechanism | No accepted reproducible mechanism; net output would violate conservation |
| Supporting evidence | N12 (2004 DOE review: occurrence not conclusively demonstrated); no positive peer-reviewed replication |
| What is new | Nothing established; a genuinely new source would be revolutionary if real |
| Model | Full energy balance: \(E_\text{out}-E_\text{in}\) with calorimetry and all inputs metered |
| Predicted effect | No credible quantitative prediction |
| System benefit | None until a reproducible claim exists |
| Best / realistic | Not assessable |
| Assumptions / uncertainty | Unknown; calibration, background, and stored energy are the usual explanations |
| Physics conflict | A net-output claim without an accounted source conflicts with conservation; a true anomaly would require extraordinary evidence |
| Alternative explanation | Calorimetry error, unmeasured input, stored energy, isotopic contamination, selective reporting |
| Computational model | None; only a pre-registered calorimetry protocol |
| Smallest falsifying experiment | Pre-registered closed-cell calorimetry with full input/output accounting and independent replication |
| Instruments | Calibrated calorimeter, mass flow, electrical power, blanks, uncertainty budget |
| Cost / time | ₹0 until a specific claim passes a paper screen; then ₹5–15 lakh |
| Safety / regulatory | Unknown; could be hazardous; no home experiment |
| Stop criteria | Any net claim without source; calibration/background not excluded; no replication |
| Independent review | Two independent labs; protocol and raw data published |
| Evidence class | E1 (negative) |
| Gate 2 verdict | Negative control. Do not spend on it until a specific, reproducible claim is identified |

### H9 — SOFC + reformer

| Field | Entry |
|---|---|
| ID / name | H9 — Solid-oxide fuel cell with reformer |
| Category / missions | Generation; M4, M2 |
| Physical mechanism | Fuel (natural gas, methanol, ammonia, or H₂) → reforming → electrochemical oxidation at 700–1,000 °C → electricity + high-grade heat |
| Supporting evidence | No verified SOFC source in the current registry; E1/E0. S11/N03 give fuel-cell context only |
| What is new | High electrical efficiency with fuel flexibility for stationary M4 |
| Model | \(\eta=V_\text{cell}nF/\Delta H\); system adds reformer, insulation, heat exchanger, blower |
| Predicted effect | 50–60% electrical LHV at kW–100 kW scale; 5–10 year stack life claim; 10–30 kg/kW |
| System benefit | M4 high efficiency reduces waste heat and radiator; M2 if fuel logistics fit |
| Best / realistic | 60% / 50%; 5 years / 3 years |
| Assumptions / uncertainty | Fuel composition, reformer mass, stack degradation, startup time |
| Physics conflict | None; high temperature and seals are engineering |
| Alternative explanation | Laboratory stack efficiency may exclude reformer and BOP; field degradation may be faster |
| Computational model | Electrochemical + thermal lumped model; vendor curve first |
| Smallest falsifying experiment | 1–5 kW module on declared fuel: electrical efficiency, 1,000 h degradation, system mass |
| Instruments | Gas analyser, load bank, thermocouples, mass flow |
| Cost / time | ₹5–12 lakh; 8–12 weeks |
| Safety / regulatory | High temperature, CO/H₂, fuel storage; ventilation and CO detection |
| Stop criteria | <50% electrical; <5 years stack life; >$1/W; reformer mass >10 kg/kW |
| Independent review | Fuel-cell engineer; third-party stack test |
| Evidence class | E1 (source pending) |
| Gate 2 verdict | Open; paper. Strongest stationary-conversion candidate after H6 |

### H10 — Free-piston linear generator / microturbine

| Field | Entry |
|---|---|
| ID / name | H10 — Free-piston linear generator or microturbine |
| Category / missions | Generation; M1, M3 |
| Physical mechanism | Fuel combustion drives a free piston coupled to a linear alternator, or a microturbine coupled to a high-speed generator |
| Supporting evidence | No verified source yet; E0/E1. Diesel genset context from the repository only |
| What is new | High power density, multi-fuel, fewer mechanical parts; potential for compact M1/M3 |
| Model | \(\eta=W_\text{out}/Q_\text{fuel}\); \(m_\text{sys}=m_\text{engine}+m_\text{alt}+m_\text{fuel}+m_\text{radiator}\) |
| Predicted effect | 25–35% at 1–10 kW; 1–3 kg/kW engine; 2–5 kg/kW with alternator and controls |
| System benefit | M1 mass could fall below diesel if engine is light; M3 high power |
| Best / realistic | 35% / 25%; 2 kg/kW / 5 kg/kW |
| Assumptions / uncertainty | Combustion stability, piston seals, linear alternator mass, emissions, noise |
| Physics conflict | None; the limits are combustion, heat, and mechanical life |
| Alternative explanation | “Free-piston” demonstrations are often single-cylinder lab units with poor lifetime and emissions |
| Computational model | Thermodynamic cycle + linear alternator; no CFD at Gate 3 |
| Smallest falsifying experiment | Bench unit: brake/electrical efficiency, kg/kW, 100 h endurance, emissions |
| Instruments | Dynamometer, power analyser, emissions analyser, thermocouples |
| Cost / time | ₹3–8 lakh; 8–16 weeks |
| Safety / regulatory | Combustion, high pressure, noise, emissions; test cell |
| Stop criteria | <20% efficiency; >5 kg/kW; emissions/noise unacceptable; <100 h life |
| Independent review | Engine specialist; replicate efficiency and emissions |
| Evidence class | E0/E1 |
| Gate 2 verdict | Open; paper. The most plausible non-battery M1 mass path after diesel |

### H11 — Phase-change thermal store

| Field | Entry |
|---|---|
| ID / name | H11 — Phase-change / latent-heat thermal store |
| Category / missions | Storage/conversion; M4 |
| Physical mechanism | Latent heat of fusion/vaporisation in a salt, metal, or composite; heat delivered at near-constant temperature |
| Supporting evidence | S09 (PCM review); E1 |
| What is new | Higher usable density and stable delivery temperature than sensible graphite |
| Model | \(E=m[c_p\Delta T+L]\); \(m_\text{store}=E_\text{th}/e_\text{store}\) |
| Predicted effect | 0.10–0.20 kWh/kg usable; containment and heat exchanger add 20–40% |
| System benefit | Smaller TPV/ORC store for M4; does not fix M1 |
| Best / realistic | 0.20 kWh/kg / 0.12 kWh/kg |
| Assumptions / uncertainty | Phase separation, corrosion, thermal conductivity, encapsulation |
| Physics conflict | None; materials and heat transfer are the limits |
| Alternative explanation | A PCM with poor conductivity needs a large heat exchanger, erasing the density gain |
| Computational model | 1-D thermal network + enthalpy method; no CFD initially |
| Smallest falsifying experiment | Coupon: usable kWh/kg over 100 cycles with a representative heat exchanger |
| Instruments | DSC, guarded hot plate, thermocouples, cycling rig |
| Cost / time | ₹2–5 lakh; 6–10 weeks |
| Safety / regulatory | Corrosive/high-temperature materials; PPE and ventilation |
| Stop criteria | <0.10 kWh/kg usable; <20% system; heat exchanger mass >30% |
| Independent review | Thermal-storage specialist; replicate cycling |
| Evidence class | E1 |
| Gate 2 verdict | Open; paper. Only matters if M4 is prioritised |

---

## 3. Deliberately excluded claims

| Claim | Why excluded |
|---|---|
| Perpetual motion / magnetic motor | Conservation violation; no reproducible measurement |
| “Zero-point” or vacuum-energy extraction | No accepted mechanism or net-output replication; would require extraordinary evidence |
| Cold fusion / LENR | N12 review not conclusive; no accepted replication; retained only as H8 negative control |
| Patent as proof | A patent is prior art, not evidence of performance |
| “AI-discovered material” without synthesis | A prediction is not a material |
| A cell result presented as a pack | Pack mass, thermal, BMS, and cycle life are not optional |

---

## 4. Register rules

1. A hypothesis is not a source. Record the source separately.
2. A review is context, not a device performance quote.
3. A laboratory result is not a product.
4. A simulation is not a measurement.
5. Every hypothesis keeps its strongest counterargument and its stop criteria.
6. Negative results are retained; a killed hypothesis may be reopened only by new evidence.
7. No hypothesis is promoted above E1 without a page/figure locator or a measurement.
8. The CSV and this document must stay consistent; the CSV is regenerated from the same fields when either changes.

---

## 5. Current ranking by information value per rupee

This is **not** a ranking by probability of success.

1. **H1** — cheapest decisive storage test; a failure closes the solid-state/Li-metal branch for M1, not all storage.
2. **H10** — cheapest non-battery M1 mass path; a bench unit can test kg/kW and efficiency.
3. **H9** — stationary efficiency; vendor data may be enough for M4.
4. **H6** — converter efficiency and life; needs a lab.
5. **H11** — only if M4 is prioritised.
6. **H2** — high upside, high uncertainty; sample cell first.
7. **H3** — high cost, regulatory; paper only.
8. **H4** — killed until a denser store exists.
9. **H5** — parked until H₂ price falls.
10. **H7** — killed at current components.
11. **H8** — zero spend until a specific claim.

The ranking will change after the first datasheet and the first cell test. That is the point of a register.
