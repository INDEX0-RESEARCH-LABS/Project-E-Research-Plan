# Project E — Pre-Execution Research Plan

**Status:** proposal for owner approval; not implemented  
**Date:** 2026-10-23  
**Repository audited:** `e75be96` (unchanged)  
**Companion files:** `REPOSITORY_AUDIT.md`, `SOURCE_VERIFICATION.md`, `HYPOTHESIS_REGISTER.csv`

---

## 1. Executive verdict

**No — the current repository is not aligned with the original energy-core vision.**

It is a credible, reproducible **benchmark and negative result** for one invented portable mission. It does not investigate a new mechanism, a new primary source, or a step-change architecture. Its own conclusion is that the portable-hybrid branch is "a cost and integration problem between A1, C2 and C1 — not a search for new physics."

The repository should be preserved as **Track A — Baseline and model credibility**. It should not be the program mission, and its 35 kg / 60 L / $5,000 / $0.40 per kWh target should not be a universal constraint on discovery.

The immediate deliverable is a research plan, not a build. No architecture is selected here.

---

## 2. What the repository actually achieves

**Verified work:**

- Eight conventional architectures (A1–A2 storage, B1–B4 generation/conversion, C1–C2 hybrids) with a common energy boundary.
- Closed energy accounting; dispatch at 1 s with convergence at 0.5/1/2 s; unmet-load closure ≤ 1e-6 kWh.
- Reduced-order storage, thermal, conversion, sizing, packaging, and LCOE models.
- 57 passing tests; CI success (`39845121841`); current code reproduces the published table exactly.
- Baseline result: no candidate meets all targets; best score 3/5; A1 cannot reach 35 kg for the 8 h mission under the 300 W/kg continuous rating (~40 kg at 0.5 h); C2 floor 44.8 kg.
- Sensitivity and 2,000-draw cost Monte Carlo; red-team review; 12 Crossref-verified source records (abstracts only).
- A safe, falsifiable hybrid-buffer experiment plan.

**Assumptions and aspirations:**

- The 35 kg / 60 L / $5,000 / $0.40 / 10-year mission is invented; there is no customer or use case.
- Most component masses, efficiencies, and all prices are E0/E1 estimates. Several E2 labels lack traceable sources.
- B2 and B3 are converters with external heat, not self-contained generators. B3 excludes the heat plant and thermal-store standby loss.
- No nuclear, solar, fusion, flywheel, CAES, pumped hydro, thermionic/AMTEC, metal-air, Li-S, SOFC, or SMR model exists.
- No measurement exists (E4–E6). No prototype, no field data, no independent replication.

**Bottom line:** the repository proves a useful negative result about a conventional portable unit. It does not prove anything about a new energy core.

---

## 3. Critical alignment gaps

### Must change

1. **Mission scope.** Separate the benchmark mission from the discovery mission. Version the requirements. Stop treating 35 kg as the definition of success.
2. **Category discipline.** Storage, conversion, and generation must be separate registers. A converter with an external heat source is not a generator.
3. **Evidence traceability.** Every E2 value needs a DOI/datasheet and a page/figure locator; otherwise downgrade to E1. The current 17 E2 entries have only one registry ID.
4. **Run provenance.** The committed baseline artifact was edited after creation and still records an older commit. Rebuild an immutable, content-addressed run store; never edit a run.
5. **Stale numbers.** Requirements still quote `$0.85/L`, `$0.44/kWh`, `$0.070/kWh`, and 3/5 / 4/5 scores that the model contradicts. Correct in a new branch after approval.
6. **Literature map.** Expand beyond the 12 benchmark sources; include nuclear, solar system performance, fusion, flywheel, CAES, pumped hydro, thermionics/AMTEC, advanced batteries, and negative results.
7. **Discovery process.** Add hypothesis and kill-criteria registers, physics screening, benchmark missions, and Gates 0–6.

### Must remain

- The no-net-generation rule and closed energy balance.
- The evidence ladder and the distinction between model, measurement, and qualification.
- The eight-architecture benchmark, baseline results, cost model, and red-team review.
- The test suite, analytical checks, and immutable-run principle (once repaired).
- The hybrid-buffer experiment plan as a benchmark test, not the main mission.
- The negative result: at 1 kW scale, no conventional compact source beats incumbents on all axes.

### Must not happen

- Do not delete the repository or rewrite its history.
- Do not continue the portable-hybrid roadmap as the main mission by default.
- Do not select a final architecture before Gate 3.
- Do not buy hardware, start experiments, or claim a prototype.
- Do not treat the Arc Reactor as a specification or proof.

---

## 4. Proposed research architecture

Six tracks; they connect through gates, not through a single fixed mission.

| Track | Purpose | Outputs | Gate |
|---|---|---|---|
| **A — Baseline and model credibility** | Preserve and audit the eight-architecture benchmark; repair provenance; define which results are decision-grade | Benchmark v2, evidence traceability, uncertainty report | 0, 1 |
| **B — Scientific mechanism landscape** | Map known sources, converters, storage, and limits; find underexplored combinations | Verified landscape; mechanism register; negative results | 1 |
| **C — Architecture hypotheses** | Build a diverse shortlist with declared source, conversion path, losses, heat, mass, and constraints | Hypothesis register; 3–5 provisional candidates | 2, 3 |
| **D — Computational research** | Use analytical and numerical models only where the physics requires them; verify and validate | Verified models; sensitivity; Pareto fronts; uncertainty | 4 |
| **E — Experimental validation** | Run the smallest safe, affordable test that can falsify a leading hypothesis | Measured component/system data; E4/E5 evidence | 5 |
| **F — Engineering and commercialization** | Packaging, materials, manufacturing, life, safety, IP, cost — only after evidence supports progression | Costed BOM; safety case; deployment concept | 6 |

**Why these boundaries:** they prevent the benchmark from dictating discovery (A vs C), prevent a converter from being mistaken for a source (B vs C), and prevent simulation from being mistaken for validation (D vs E). Track F is deliberately last; commercial assumptions must not choose the physics.

**Cross-track rule:** a candidate can enter Track D only after a closed-form energy/mass/heat budget in Track C. It can enter Track E only after Gate 4 verification. It can enter Track F only after Gate 5 evidence.

---

## 5. Scientific landscape — initial findings

This is a first map, not the completed Gate 1 review. Ranges are screening estimates; page-level verification is pending. Source IDs refer to `SOURCE_VERIFICATION.md`.

| Family | Best credible position | Fundamental/system penalty | Evidence | Discovery relevance |
|---|---|---|---|---|
| Li-ion / advanced Li | ~200–300 Wh/kg cell; pack lower; high round-trip; mature | Pack mass, pulse power, thermal management, cost, cycle life | S03, S04, N01, N02 | Incremental; can improve M1 but not create a new source |
| Li–S / Li–air / solid-state | Higher theoretical cell energy; solid-state promises safety; Li–S/Li–air cycle and efficiency problems | Practical pack energy, cycle life, interfaces, manufacturing | N01, N02; detailed reviews pending | Possible storage step-change; must be measured, not assumed |
| Diesel / fuel-based generators | ~25–35% small genset; high fuel energy density; mature | Part-load efficiency, fuel logistics, emissions, noise, converter mass | S11, N03 | Benchmark incumbent; not a new core |
| PEM / SOFC fuel cells | ~45–60% LHV for PEM systems; SOFC higher with heat | H2 storage (350–700 bar or hydride), stack cost/mass, degradation | S11, N03, N04, N11 | Viable only with cheap H2 and light tanks |
| Nuclear fission / RTG | Kilopower 1 kWe fission–Stirling ground test; 10 kWe design concept; RTG W-scale | Reactor + shielding + radiator + regulatory system; not 35 kg | N08, N13, N14 | Strong for long-duration remote M2; not portable M1 |
| Fusion | Pilot-plant roadmap; net electricity not demonstrated | Tritium breeding, neutron damage, containment, facility scale | N09 | Not a near-term compact core; monitor, do not fund |
| Solar PV | Commercial Si modules just under 25% (2026); 1 kW/m² standard irradiance | Area, diurnal/seasonal storage, system derating | S05, N10 | External source; system mass dominated by storage |
| Thermal/mechanical storage | Pumped hydro and CAES are grid-scale; flywheel high power; PCM low conductivity | Site/scale, containment, self-discharge, low energy density | S06, S08, S09, S10, N05–N07 | Not portable at 10 kWh; possible pulse buffer |
| Heat engines / TEG / TPV | TEG ~5–8% at ZT≈1; TPV 40% cell efficiency with a 1900–2400 °C emitter; ORC low-grade | Carnot, heat rejection, high-temperature materials, external heat source | S01, S02, S07, S12 | TPV is a stationary converter, not a portable source |
| Thermionic / AMTEC | Lab-scale high-temperature conversion; ~10–20% class | Cathode/electrode life, high T, waste heat, low power density | Detailed review pending | Possible niche for M4; not yet a shortlist candidate |
| Supercapacitors / flywheels | High power, long cycle life; low energy | 6 Wh/kg class supercaps; flywheel containment/self-discharge | S03, N05 | Pulse buffer only; no energy win |
| LENR / over-unity / zero-point | No reproducible peer-reviewed demonstration | Conservation violation if net output; calibration/background errors | N12 (negative review) | Screen out; no compute until a pre-registered, replicated claim exists |

**Initial conclusion:** no known mechanism in this map supports a 35 kg, 6 kW, 8 h self-contained core with current evidence. The strongest physics-valid options are mission-specific: advanced storage for M1, nuclear/thermal for M2, high-power storage/flywheel for M3, and TPV/ORC for stationary M4. That is a hypothesis to test, not a selection.

**Pending Gate 1 work:** full-text/page-level verification; SMR/regulatory review; thermionic/AMTEC; metal-air; Li–S; SOFC; solar system mass; nuclear shielding; cost quotes; negative-results register.

---

## 6. Candidate hypothesis shortlist (provisional)

No candidate is selected. IDs are stable for the register.

| ID | Hypothesis | Source / mechanism | Predicted system position | Cheapest decisive test | Kill criterion |
|---|---|---|---|---|---|
| H1 | Advanced Li-metal/solid-state pack meets M1 | Electrochemical storage; Li-metal anode / solid electrolyte | 300–400 Wh/kg cell; 200–260 Wh/kg pack; 10 kWh pack ~40–50 kg; still ~50–65 kg system | Literature + cell datasheet; then 1–2 cells | <250 Wh/kg pack at C/2, or <500 cycles, or >$400/kWh |
| H2 | Li–S or Li–air gives a storage step-change | Conversion/alloying or metal–air chemistry | 300–500 Wh/kg cell claim; practical pack lower; cycle life uncertain | Literature + sample cell | <200 Wh/kg pack, <100 cycles, or round-trip <60% |
| H3 | Micro-fission Stirling serves long-duration remote M2 | U-235 fission → heat → Stirling | 1 kWe ground test; 10 kWe design concept; system 10²–10³ kg; fuel mass negligible; shielding/regulatory dominate | Paper study + NTRS data; no nuclear experiment | System >500 kg per kWe, no regulatory path, or cost >M2 budget |
| H4 | TPV + thermal store serves stationary M4 | External heat → emitter → TPV cells | 25–32% system; 10 kWh electric needs ~39 kWh thermal; graphite store ~140 kg + vessel | Paper study + vendor data | System <20%, or store <1 kWh/kg, or heat source not co-located |
| H5 | H2 fuel cell + advanced tank meets M1/M2 | H2 oxidation → PEM; 350–700 bar or hydride storage | 45–55% LHV; 10 kWh needs ~0.6 kg H2; 5 wt% tank ~12.6 kg; C1 average-sized 1.4 kW stack ~11.6 kg; system ~56 kg | BOM/literature; then lab test | System >35 kg for M1, or H2 >$4/kg, or tank <5 wt% |
| H6 | Thermionic/AMTEC/Stirling converter enables M4 | Heat → electrons/electrochemical/mechanical | 10–40% depending on T and maturity; high-T materials and waste heat | Literature + vendor/lab data | <15% system, or >5 kg/kW, or life <5,000 h |
| H7 | Flywheel/supercap buffer solves M3 pulse | Electromechanical/electrostatic storage | High power; 0.05–0.3 kWh at 6–100 Wh/kg; containment/safety | Paper + cell/module data | Buffer >5 kg for 0.05 kWh, or round-trip <90%, or containment mass prohibitive |
| H8 | A genuinely new mechanism (LENR/over-unity/zero-point) | Unknown | No credible prediction | Pre-registered calorimetry with full energy balance, independently replicated | Any net-output claim without accounted source; calibration/background not excluded |

**Why this shortlist is diverse:** H1/H2 are storage; H3/H5 are generation; H4/H6 are conversion; H7 is power; H8 is a negative-control screen. It does not assume the answer is a battery, a reactor, or a new physics mechanism.

**Not shortlisted:** TEG at kW scale (physics/radiator), supercapacitor-only (energy), CAES/pumped hydro (scale), betavoltaics (µW–mW), magnetic motors/perpetual motion (no evidence). These remain in the negative-results register.

---

## 7. Quantitative screening plan

Before any complex simulation, every candidate must pass a one-page budget with units and uncertainty.

### 7.1 Required quantities

- Primary source and origin; source energy per mission.
- Input power, output power, delivered energy over the mission.
- Every conversion stage efficiency; overall efficiency; Carnot check for thermal stages.
- Stored energy, usable depth of discharge, round-trip efficiency.
- Component and system mass; component and system volume.
- Waste heat at average and peak; radiator area and mass; coolant/pump power.
- Startup, standby, control, and auxiliary power.
- Degradation, replacement, and lifetime.
- Capex, fuel/O&M, LCOE; uncertainty and evidence label.
- Safety, regulatory, environmental constraints.

### 7.2 Screening calculations (examples)

**M1 storage floor.** 10 kWh delivered; 95% converter; 92% round trip; 90% usable window → 12.7 kWh nameplate. At 175 Wh/kg pack → 72.6 kg cells; with 1.25 packaging → 90.8 kg, before converter/radiator. At 300 Wh/kg → 42.4 kg cells / 53 kg packaged; at 500 Wh/kg → 25.4 kg / 31.8 kg packaged. A 35 kg system therefore needs roughly >500 Wh/kg pack plus a converter substantially lighter than 11.25 kg, or a relaxed mission. This is a first-principles screen, not a product prediction.

**M1 diesel floor.** 10 kWh delivered at ~25% system efficiency needs ~40 kWh fuel LHV; diesel at 9.94 kWh/L → ~4 L per mission. Fuel mass is small; the 1.4 kW genset, 6 kW converter, buffer, and radiator dominate. C2's 50.3 kg is a converter/pulse-power floor, not a fuel floor. Relaxing 6 kW to 2 kW moves C2 to ~36.8 kg; relaxing mass alone does not.

**M4 TPV floor.** 10 kWh electric at 32% cell × 0.85 spectral × 0.95 output = 25.8% → 38.7 kWh thermal. Graphite at 0.28 kWh/kg → 138 kg; 25% vessel → 173 kg; plus emitter, cells, radiator → ~257 kg. To reach 35 kg, storage must exceed ~1.1 kWh/kg thermal or system efficiency must exceed ~70%; neither is credible with current materials.

**M2 nuclear scale.** Fuel energy density is not the constraint. A 1 kWe fission–Stirling ground test (with a 10 kWe design concept) is a reactor + reflector + shielding + heat rejection + control + regulatory system. The fuel mass is grams-to-kilograms; the system mass is 10²–10³ kg. This can be excellent for a 30-day remote mission and is disqualified for a 35 kg portable one.

**M1 solar scale.** At 1 kW/m² and 25% module efficiency, 1 kW average needs ~4 m² of modules in full sun; 24 h operation needs ~10 kWh storage (~60 kg at 175 Wh/kg pack). Solar is an external source with area and diurnal storage, not a compact core.

### 7.3 Metrics and scorecard

Hard pass/fail before scoring:

- Closed energy balance with a named source.
- No conservation violation; no omitted source.
- Safety/regulatory path plausible for the proposed experiment.
- All subsystems inside the declared boundary (source, converter, storage, cooling, shielding, fuel, BOP).

Score (100), used only for triage:

| Dimension | Points | Rule |
|---|---:|---|
| System-level improvement vs incumbent at a declared mission | 35 | Measured > modeled > paper; must be ≥1.5× on at least one axis and not worse than 0.8× on the others |
| Evidence quality (E0–E6) | 25 | E2 without citation = 0; E3 model = partial; E4/E5 = full |
| Mass and volume at the declared mission | 15 | Full boundary; penalties for omitted items |
| Efficiency and heat rejection | 10 | Includes Carnot check and radiator/pump power |
| Cost and LCOE | 10 | Quotations > estimates; E0 cost cannot win a ranking |
| Lifetime/manufacturability | 5 | Cycle life, replacement, materials availability |

Penalties: −20 for an omitted subsystem; −10 for an unsupported headline number; −10 for no independent check. A candidate cannot be declared superior on a headline number alone.

### 7.4 Benchmark missions (provisional)

| ID | Mission | Targets | Why it matters |
|---|---|---|---|
| **M1 Portable pulse** | 1 kW cont, 6 kW / 30 s every 10 min, 8 h | ≤35 kg, ≤60 L, ≤$5,000, ≤$0.40/kWh, 10 years | Existing benchmark; known infeasible; tests storage/pulse hybrids |
| **M2 Long-duration remote** | 0.5 kW cont, 5 kW peak, 30 days; −20 to +40 °C; no grid | ≤500 kg, ≤1,000 L, ≤$50,000, ≤$0.50/kWh | Tests nuclear/thermal/fuel systems where fuel logistics dominate |
| **M3 High-power compact** | 10 kW cont, 30 kW / 10 s, 1 h | ≤100 kg, ≤150 L, ≤$20,000, ≤$1.00/kWh, 5 years | Tests flywheel/supercap/high-power packs; power vs energy |
| **M4 Stationary heat-to-power** | 10 kW electric from 100 kW industrial heat; 8,000 h/year | ≤$1/W, 20 years; heat source cost excluded but declared | Separates conversion from generation; TPV/ORC/TEG |

M1–M3 are required; M4 is recommended because it prevents TPV/ORC from being misclassified as a portable source.

---

## 8. Roadmap and gates

### Gate definitions

| Gate | Question | Required evidence | Time | Stop if |
|---|---|---|---|---|
| **0 — Mission alignment** | Does the plan preserve the benchmark and address discovery? | Vision/non-claims, track map, benchmark charter, owner approval | 3–5 days | The plan is only a rebranded portable-hybrid roadmap |
| **1 — Evidence review** | What is known, what is demonstrated, what is impossible? | 40+ sources, 10 mechanisms × 7 fields, DOI/page locators, negative-results register | 3–5 weeks | <20 verified sources or no negative results |
| **2 — Physics screening** | Which concepts survive conservation, thermodynamics, and mass/heat budgets? | One-page budget per candidate; unit checks; Carnot; source accounting; reject >10× material gap | 2–3 weeks | All candidates require >10× unsupported properties |
| **2S — Safety/regulatory** | Can the proposed test be done safely and legally? | Hazard register; lab/regulatory route; no nuclear/H2/high-T without partner | 3–5 days | No safe path |
| **3 — Candidate selection** | Which 3–5 diverse candidates deserve models? | Quantitative comparison at M1–M3; uncertainty; scorecard; independent review | 1–2 weeks | Only one family survives, or ranking is cost-only |
| **4 — Model design** | What equations, parameters, tools, and tests are required? | Model spec; parameter provenance; verification plan; compute estimate | 3–4 weeks | Model complexity exceeds decision value |
| **4V — Independent review** | Are the critical equations and code correct? | Reviewer report; independent re-derivation; regression tests | 3–5 days | Unresolved critical defect |
| **5 — Falsifiable experiments** | What is the smallest test that can kill the hypothesis? | Protocol; instrumentation; calibration; safety; cost; pass/fail | 4–8 weeks | No measurable falsifier |
| **6 — Evidence-based continuation** | Continue, revise, pause, or abandon? | Measured result vs pre-registered threshold; updated uncertainty; decision memo | ongoing | Threshold missed or evidence quality insufficient |

A gate is complete only with the stated evidence. A document or a simulation alone does not complete a gate.

### Phases

| Phase | Weeks | Work | Deliverable | Exit |
|---|---:|---|---|---|
| P0 | 1 | Freeze repo; audit; vision; benchmark charter | Vision, audit, Gate 0 memo | Gate 0 |
| P1 | 2–5 | Landscape; mechanism register; source verification | Landscape v1, mechanism register | Gate 1 |
| P2 | 6–8 | Physics screening; missions; scorecard | Screening sheets, mission set | Gate 2/2S |
| P3 | 9–10 | Shortlist; independent review | Hypothesis register v1, decision memo | Gate 3 |
| P4 | 11–14 | Model design; verification | Computational plan, verified models | Gate 4/4V |
| P5 | 15–20 | Experiment design; lab partner | Experiment strategy, costed protocol | Gate 5 |
| P6 | ongoing | Evidence review; go/revise/pause/abandon | Decision memo v2 | Gate 6 |

**Effort:** 60–80 person-days for P0–P3 (Stage A); 30–50 additional person-days for P4–P5, plus lab time. These are planning estimates, not commitments.

---

## 9. Computational plan

### Principles

- Analytical first; simulation only where the physics requires it.
- Keep units and provenance in the data model, not in comments.
- Every run immutable and content-addressed; old runs never edited.
- A model is not evidence of a device; verification ≠ validation ≠ qualification.

### Software milestones

| ID | Milestone | Inputs | Outputs | Acceptance test | Effort | Depends |
|---|---|---|---|---|---|---|
| S0 | Provenance repair | Existing run artifacts | Immutable manifest: commit, config hash, input hashes, environment | Re-run reproduces table; old run preserved, new run new ID | 2–3 days | Gate 0 |
| S1 | Parameter/source registry | Config, sources | Schema: value, unit, range, evidence, DOI/page | 100% of E2 values resolve to a source; unverified downgraded | 5 days | Gate 1 |
| S2 | Analytical screening tool | Candidate sheets | Closed-form mass/energy/heat/cost budgets | 6 hand-checked cases; unit/dimensional tests | 5 days | Gate 2 |
| S3 | Uncertainty/sweep | Parameter ranges | OAT, Latin hypercube/QMC, scenario sampling | Convergence; correlated scenarios; no unsupported distribution claims | 4 days | S1/S2 |
| S4 | Multi-objective comparison | Candidate models | Pareto front with constraints; no scalar “winner” | Constraints enforced; infeasible points excluded | 4–5 days | S2/S3 |
| S5 | Candidate model + verification | Shortlist | Model spec, equations, numerical checks | Grid/timestep convergence; energy closure; independent re-derivation | 10–15 days per candidate | Gate 4 |
| S6 | Experiment data pipeline | Bench data | Calibrated CSV/JSON, uncertainty, predicted-vs-measured | Round-trip test; calibration record; no hand-edited results | 3 days | Gate 5 |

### Tools

- Existing Python 3.12, NumPy, SciPy, pytest, matplotlib. Reuse the current repository for Track A.
- No GPU, FEA, CFD, electromagnetic solver, or agent orchestration before Gate 4. Add a tool only when a documented equation cannot be solved analytically or with the existing stack.
- If FEA/CFD is required later: open-source solver (e.g., FEniCS/scikit-fem/OpenFOAM) on a workstation/cluster; verification with manufactured solutions and grid convergence. Cost/compute estimate is an open question.
- Nuclear, high-pressure H2, and >1000 °C work require external lab facilities; not a laptop task.

### Verification and validation

- Verification: dimensional analysis, hand calculations, energy closure, convergence, regression tests, independent implementation of critical equations.
- Validation: comparison with published component data; E4 bench measurement; E5 integrated test; E6 independent replication.
- Uncertainty: report ranges and evidence labels; do not present a single number as a forecast.

---

## 10. Experiment strategy

### Principles

- The smallest experiment that can falsify the leading hypothesis.
- No experiment without a written protocol, calibration, controls, stop conditions, and safety review.
- A model check is not a performance record.
- No nuclear, high-pressure H2, or >1000 °C experiment without a qualified lab and regulatory route.

### Candidate experiments

| ID | Hypothesis | Measurement | Pass/fail | Cost (INR, planning) | Evidence |
|---|---|---|---|---|---|
| E0 | Paper/calorimetry screen for any new mechanism | Energy balance, calibration, background | No net output without accounted source; independent replication | ₹0 (time only) | — |
| E1 | Hybrid buffer meets M1 pulses | Input/output energy, SOC, temperatures, efficiency | Unmet ≤1%; efficiency within ±15% of model; thermal limits | ₹2.84–7.33 lakh (existing $3,000–7,750 estimate) | E4 |
| E2 | Advanced cell/pack at pulse C-rate and temperature | Capacity, round-trip, power, fade, temperature | ≥250 Wh/kg pack; ≥500 cycles; thermal limit | ₹1–3 lakh | E4 |
| E3 | H2 tank/stack integration | H2 mass, leak, stack efficiency, start/stop | 5 wt% system; leak <limit; efficiency within 10% of datasheet | ₹5–15 lakh; lab | E4/E5 |
| E4 | TPV/thermal store at high temperature | Emitter/cell temperature, electric output, heat loss | System ≥20%; store ≥1 kWh/kg; insulation loss declared | ₹10–30 lakh; lab | E4/E5 |
| E5 | Nuclear/RTG | — | Not proposed in this program; regulatory/facility barrier | Unknown; ₹crore+ | — |
| E6 | Independent replication of a positive result | Same protocol, different lab | Result within pre-registered uncertainty | ₹1–3 lakh | E6 |

**Recommended first experiment:** none in the discovery track until Gate 3. The existing hybrid test (E1) is a benchmark confirmation, not a discovery test; run it only if Track A needs the data and the owner approves the cost.

### Safety constraints

- Electrical: lockout/tagout, fusing, insulation, earth leakage, two-person rule for >60 V DC.
- Thermal: no >1000 °C outside a qualified furnace/lab; thermal-runaway containment for Li-ion; CO monitoring for combustion.
- Hydrogen: no >350 bar outside a certified facility; leak detection; grounding; venting.
- Nuclear: no handling, no reactor experiment, no radioactive source in this program.
- Data: record calibration, raw data, and uncertainty; no hand-edited results.

---

## 11. Budget scenarios

**Currency basis:** ₹94.593871 per USD on 2026-10-22, from `open.er-api.com/v6/latest/USD` (exchangerate-api). This is a market API rate, **not** an RBI reference rate and not a quotation. Planning rounds to ₹95/USD.

**All figures are estimates or ranges, not quotations.** Facility fees, regulatory costs, and nuclear work are unknown.

| Stage | Scope | INR (planning) | USD equivalent | Assumptions / unknowns |
|---|---|---:|---:|---|
| **A — Near-zero-cost** | Literature, audit, analytical screening, existing compute, owner time | ₹0–75,000 | $0–790 | Public papers, open-source tools, existing laptop; no lab; 60–80 person-days |
| **B — University/lab collaboration** | 3–6 month collaboration; cell/pack characterization; independent review | ₹2–8 lakh | $2,100–8,500 | Lab access in-kind; consumables, samples, characterization; facility overhead unknown; may be higher |
| **B+ — High-temp/H2/nuclear lab** | TPV/thermal store or H2 testing | ₹10–50 lakh+ | $10,600–52,900+ | Qualified lab, safety, certification; nuclear not included; may be unavailable |
| **C — Funded validation** | Bench hybrid test; calibration; prototype BOM; independent review | ₹19–60 lakh | $20,100–63,400 | E1 ₹2.84–7.33 lakh; E2 ₹1–3 lakh; prototype ₹15–50 lakh; review ₹0.5–1.5 lakh; all E0 |
| **C+ — Nuclear/regulatory** | Not estimated | ₹crore+ and years | — | Out of scope; requires licensee, shielding, site, regulator |

**Cheapest next action:** Stage A only, ₹0–75,000, focused on Gate 0/1/2. Do not spend on hardware before Gate 3.

---

## 12. Risks and stop conditions

| Risk | Why it matters | Mitigation | Stop/pause condition |
|---|---|---|---|
| No mechanism beats incumbents | The program becomes a benchmark with extra steps | Gate 2 quantitative screen; publish negative result | All candidates <1.5× on every axis, or require >10× unsupported material property |
| Physics invalid | Compute and experiments wasted | Conservation/thermodynamics screen before models | Net-output claim without source; Carnot/energy violation |
| Evidence unavailable | E2 labels become fiction | Source registry; downgrade to E1; quotes | <20 verified sources at Gate 1, or no source for a critical parameter |
| Cost runaway | Small budget consumed by models/hardware | Stage A cap; Gate 3 before spend | >₹10 lakh before Gate 3 |
| Safety/regulatory | Nuclear/H2/high-T harm; legal barrier | Gate 2S; qualified lab; no home experiments | No safe/legal path |
| No use case | Optimizes an invented mission | Define M1–M4; seek a real requirement | No owner/use case by Gate 3; stop at benchmark |
| Claims drift | Repository loses credibility | Immutable runs; regenerate from pinned run; independent review | Any hand-edited result table; stale commit |
| Team dependency | Single-person blind spots | Independent reviewer; re-derive critical equations | No reviewer for Gate 4V |
| Timeline slip | Gate 1 >8 weeks | Timebox; reduce scope, not evidence | Gate 1 >8 weeks; reassess |
| Negative result treated as failure | Loses the value of the work | Publish negative results; keep register | Pressure to claim breakthrough without evidence |

**Program-level stop:** if Gate 2 shows no candidate with a credible path to ≥1.5× system improvement on at least one axis, stop the discovery track and publish the benchmark plus negative results. That is a successful scientific outcome, not a failure.

---

## 13. First 7 days

| Day | Work | Output | Cost |
|---|---|---|---|
| 1 | Freeze repo; verify commit/tests/CI; archive the audit; write vision and non-claims | Vision v0.1; audit record | ₹0 |
| 2 | Reconcile stale claims and run provenance; do not edit repo; write correction list | Correction list; provenance memo | ₹0 |
| 3 | Verify sources; expand registry; label E2 gaps | Source table v0.1; 20+ verified sources | ₹0 |
| 4 | Build mechanism register v0.1 (10 families; source, conversion, limit, evidence) | Mechanism register | ₹0 |
| 5 | Physics screen six candidates at M1/M2/M4; one-page budgets | Screening sheets; reject list | ₹0 |
| 6 | Define M1–M4 and scorecard; draft hypothesis register | Mission set; scorecard; H-register | ₹0 |
| 7 | Independent review; decision memo; approval checklist | Gate 0 memo | ₹0 |

No purchases, no experiments, no repository edits, no architecture selection.

---

## 14. Approval checklist

The owner must approve:

- [ ] Re-scope the repository as **Track A benchmark**, not the whole Project E mission.
- [ ] Preserve the eight-architecture benchmark, tests, and negative result.
- [ ] Replace the single 35 kg target with provisional M1–M4; M1 remains the benchmark case.
- [ ] Adopt Tracks A–F and Gates 0–6; a gate requires evidence, not a document.
- [ ] Adopt the evidence rule: E2 requires a DOI/datasheet/page locator; otherwise E1.
- [ ] Approve a provenance repair branch (no history rewrite) to fix stale numbers, run artifacts, and validation register.
- [ ] Approve Stage A budget ₹0–75,000; Stage B only after Gate 3.
- [ ] Approve no nuclear, high-pressure H2, or >1000 °C experiment before Gate 5 and a qualified lab.
- [ ] Appoint an independent reviewer for Gate 4V.
- [ ] Approve the stop conditions, including publishing a negative result.
- [ ] Approve that no final architecture is selected before Gate 3.

---

## Conclusion

**Preserve:** the energy accounting, evidence ladder, tests, eight-architecture benchmark, cost model, red-team review, and the negative result. The repository is a credible Track A.

**Redirect:** the program from “optimize a 35 kg portable hybrid” to “map mechanisms, screen physics, and test a diverse shortlist across M1–M4.” The portable mission becomes one benchmark, not the definition of Project E.

**Do not build yet:** no hardware, no prototype, no reactor, no electrolyzer, no TPV/TEG purchase, no final architecture. No claim of a working energy core.

**Single best next action:** approve and run the 7-day Gate 0/1 sprint (audit, vision, source map, mechanism register, physics screen, missions, scorecard) at near-zero cost. It produces the evidence needed to decide whether any discovery track is worth funding.

**Implementation has not begun.**
