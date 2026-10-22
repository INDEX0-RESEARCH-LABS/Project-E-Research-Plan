# Project E — Decision Memo

**Date:** 2026-10-23  
**Prepared by:** research program (outside the tracked Project-E repository)  
**Repository state:** Project-E frozen at `e75be96`; no edits, commits, or pushes  
**Hardware state:** none purchased; no experiment started  
**Gate status:** Gate 0 conditionally accepted; Gate 1 partial; **Gate 2 provisional and not passed**; Gates 3–8 not opened  
**Currency:** INR primary; USD comparison at ₹94.593871/USD (2026-10-22, `open.er-api.com`; market API, not an RBI rate and not a quotation)

---

## 1. Decision requested

1. Preserve the existing eight-architecture benchmark and negative result as **Track A**.
2. Accept the redirection from “build the 35 kg portable hybrid” to a mission-driven, evidence-gated search across storage, conversion, and generation.
3. Accept that **no architecture is selected** and that Gate 2 is not passed.
4. Authorise **Gate 3 paper work only** (₹0–0.5 lakh) plus the external desk review (₹0.70–1.25 lakh), total T0 ≤₹2.0 lakh; first target **M3** (converter/storage) or **M2** (source).
5. Authorise the external desk review (₹70,000–1,25,000), included in the T0 ceiling.
6. Confirm that **no hardware, purchase, experiment, repository edit, commit, or push** is authorised by this memo.

---

## 2. What was established

| Finding | Evidence | Confidence |
|---|---|---|
| The repository is a credible benchmark and negative result | Audit at `e75be96`; 57 tests; reproduced eight-architecture table | High |
| No benchmark architecture meets all M1 targets | Repository results; best score 3/5 | High |
| A1 cannot reach 35 kg at 175 Wh/kg | 118.3 kg screen; 83.5 kg cells + 11.25 kg converter + packaging | High (arithmetic) |
| M1 at 35 kg needs **510–691 Wh/kg pack** (638–864 cell) depending on converter mass | `limits.py`; 1.5 vs 0.5 kg/kW; 10 kWh basis | High (conditional on assumptions) |
| If the repo’s 1 kW × 8 h = 8 kWh config is authoritative, M1 needs 408–553 Wh/kg pack | Audit D16; 20% lower energy | High (arithmetic); verdict unchanged |
| No demonstrated pack is at 500–700 Wh/kg | Best credible 150–250 Wh/kg pack (E1; no datasheet) | Medium-high |
| M1’s 690 Wh/kg headline is **conditional**, not a physical law | Converter 1.5 kg/kW is an assumption | High |
| M2 is source-bound: battery needs 1,112–1,127 Wh/kg pack; diesel is ~165 kg | `limits.py`; diesel 3.6 kWh/kg fuel at 30% | High (screening) |
| M2’s $50k capex / $0.50 per kWh targets are mutually inconsistent | $50k over 122 missions × 360 kWh = $1.14/kWh capital | High (arithmetic) |
| M3 is the closest to conventional feasibility | 186 Wh/kg pack at 0.5 kg/kW vs 355 at 1.5 kg/kW | Medium (assumption-sensitive) |
| M4 is heat-bound, not storage-bound | 30 kW waste at 25% → 30 m², ~150 kg radiator | High (conservation + heat transfer) |
| B3 TPV is a converter, not a source; store is 484–806 kg | External ≥1500 °C heat; 0.06–0.10 kWh/kg usable | High (screening) |
| C1 PEM is ~56 kg and fails H5 at $6/kg H₂ | Fuel alone $0.36/kWh; capex needs 12,500 missions | High |
| C2 diesel is ~49 kg and fuel-limited at $0.54/kWh | $1.40/L, 26.3% overall | High |
| Nuclear is mass-plausible for M2 but regulation-bound | 100–1,000 kg/kWe concept range; no lawful path yet | Medium-low |
| The full Arc-Reactoresque vision is not supported by known physics | Source hierarchy: only nuclear/chemical exceed 1 kWh/kg system | High |

---

## 3. The twelve questions

### Q1. What is the most ambitious version of the vision that remains scientifically defensible?

**A 10 kWh / 6 kW / 8 h unit at 35 kg is not defensible with known storage.** It requires 510–691 Wh/kg pack (638–864 Wh/kg cell), roughly 2–4× the best credible pack, before margin, cooling, or 10-year degradation. If the repository’s 1 kW × 8 h = 8 kWh config is authoritative, the requirement falls to 408–553 Wh/kg pack; the verdict is still “not with known storage,” but the gap is 1.6–3.7× rather than 2.0–4.6×.

The defensible ambitious target is:

- **M1 at ~60–75 kg** with a 250–350 Wh/kg pack, a measured ≤0.5 kg/kW converter, and a full thermal/volume closure. That is a **1.6–2× system improvement** over the 118 kg benchmark, not a 3.4× improvement.
- **M3 at 186–355 Wh/kg pack**, depending on converter mass. This is the mission where a conventional system may already be close; it is the most defensible near-term target.
- **M2 at ~150–250 kg** with diesel (mass-feasible) or **100–1,000 kg/kWe** with nuclear (mass-plausible, regulation-bound). Battery-only M2 is not defensible (1,100+ Wh/kg pack).
- **A >1 kWh/kg system is only defensible with nuclear or chemical fuel**, not with batteries, capacitors, flywheels, or thermal stores.

No architecture in this memo is claimed to achieve even the 60–75 kg target. It is a target, not a result.

### Q2. What does established physics permit today?

| System | Established performance | Mission consequence |
|---|---|---|
| Li-ion pack | 150–250 Wh/kg; 250–400 Wh/L (E1) | M1 35 kg fails; M5 near-feasible; M3 conditional |
| Li-ion cell | 250–300 Wh/kg commercial; 400 lab (E1) | cell gains do not automatically survive packaging |
| Diesel genset | 25–35% at rated load; ~26% screened overall | M1 ~49 kg, $0.54/kWh fuel; M2 mass-feasible |
| PEM + 5 wt% H₂ | 45–55% LHV; tank 12.6 kg for 0.63 kg H₂ | M1 ~56 kg; M2 tank-mass-limited |
| TPV | 40% cell at 1900–2400 °C (S01) | converter only; store 484–806 kg; M4 |
| Solar PV | ~25% commercial module (N10); 33.7% detailed-balance limit (S05) | M2/M4 with storage; not a compact core |
| Fission–Stirling | 1 kWe ground test (N08/N13); 10 kWe design | 100–1,000 kg/kWe; M2 paper only |
| Thermal store | ~0.10 kWh/kg usable graphite; 0.10–0.20 kWh/kg PCM | M4 store is hundreds of kg |
| Supercapacitor | ~6 Wh/kg | 0.05 kWh buffer = 8.3 kg; H7 fails |

### Q3. Which limits are fundamental, and which might be overcome?

**Fundamental:** conservation of energy; Carnot; fuel LHV; fission binding energy; Gibbs energy of electrochemical reactions; Stefan–Boltzmann radiation; graphite heat capacity; the source hierarchy (>1 kWh/kg only nuclear/chemical).

**Engineering:** pack packaging (1.15–1.40); converter kg/kW; heat-transfer coefficient and fin design; cycle life; manufacturing yield; BOP mass; cost at volume.

**Assumption, not limit:** 1.5 kg/kW converter; 1.25 packaging; $1.40/L diesel; $6/kg H₂; 50% fuel-cell efficiency; 26.3% diesel overall. The M1 “690 Wh/kg” number moves to 510 Wh/kg at 0.5 kg/kW. **Do not present an assumption as a physical law.**

### Q4. What are the strongest candidate research directions?

Ranked by expected information value and system leverage, not by excitement:

| Rank | Direction | Why | Main risk |
|---:|---|---|---|
| **1** | **M3: converter + pack closure** | Closest to conventional feasibility; a datasheet can flip 355 → 186 Wh/kg; 10 kWh/30 kW is a real market | Converter mass and heat are unmeasured |
| **2** | **M2: source comparison (diesel / H₂ / nuclear)** | Largest system-level gap; source choice dominates by ~23× | Cost/regulatory; nuclear path unresolved |
| **3** | **M4: heat rejection + SOFC/TPV/Stirling** | Stationary value; heat is the binding term; tests conversion physics | External heat source; radiator mass |
| **4** | **M1: advanced storage (H1/H2)** | Highest ambition; closes or kills the benchmark | 2–4× gap; low probability |
| **5** | **H8: negative control** | Protects the program from self-deception | Zero spend until a specific claim |

**The strongest scientific opportunity is not a new battery chemistry.** It is the **source–conversion pair** for M2 and the **thermal closure** for M4. Storage is the most familiar bottleneck, not necessarily the most tractable one.

### Q5. Which hypotheses have the highest expected information value per unit cost?

1. **H1 pack datasheet + one cell test** (₹50k–2L): converts the 150–250 Wh/kg range from E1 to E2 and tests the M1/M5 storage question. A failure closes a generation of M1 claims.
2. **Converter datasheet + one measured inverter** (₹0–50k): resolves the 1.5 vs 0.5 kg/kW assumption that flips M3.
3. **H10 free-piston/microturbine paper + bench data** (₹3–8L): the most plausible non-battery M1 mass path after diesel.
4. **H9 SOFC vendor data** (₹5–12L): stationary efficiency; may be enough for M4 without a new lab.
5. **H6 thermionic/AMTEC/Stirling** (₹2–6L): converter efficiency and life.
6. **H11 PCM store** (₹2–5L): only if M4 is prioritised.
7. **H3 nuclear** (₹0–2L paper): high system leverage, long regulatory path; paper only.
8. **H8 LENR** (₹0): no spend until a specific, reproducible claim.

### Q6. What evidence supports each candidate?

| Candidate | Evidence | Class | What is missing |
|---|---|---|---|
| H1 solid-state | S04, N01, N02 (reviews) | E1 | pack datasheet, cycle data, cost |
| H2 Li–S/Li–air | N01/N02 context only | E1 | any verified cell result |
| H3 fission | N08, N13, N14 | E1 | shielding/regulatory mass, cost |
| H4 TPV | S01, S08, S09 | E1 | system efficiency, store measurement |
| H5 PEM | S11, N03, N04, N11 | E1 | tank/stack datasheet, H₂ price |
| H6 thermionic/AMTEC | S12 context; review pending | E1 | device efficiency and life |
| H7 buffer | S03, N05 | E1 | module mass with containment |
| H8 LENR | N12 (negative review) | E1 (negative) | a reproducible claim |
| H9 SOFC | S11/N03 context only | E1 | vendor stack data |
| H10 free-piston | repository diesel context | E0/E1 | any measured kg/kW |
| H11 PCM | S09 | E1 | usable kWh/kg with heat exchanger |

No candidate is above E1. No system-level result exists.

### Q7. What is the single most decisive next experiment or analysis?

**A supplier-grade mass/volume/heat closure for one 10 kWh pack and one 6 kW and one 30 kW converter, at the M3 boundary.**

Why this and not a new experiment:

- It resolves the **1.5 vs 0.5 kg/kW** assumption that flips M3 from 355 to 186 Wh/kg pack.
- It tests whether M3 — the closest mission — passes with conventional components.
- It costs <₹2 lakh and takes weeks, not months.
- If M3 passes, the program has a near-term system and a credible commercial path.
- If M3 fails, M1 is even less likely, and the program should shift to M2/M4 rather than buy cells.

This is an **analysis + datasheet** task, not a laboratory experiment. The first true experiment (H1 cell test) comes only after the closure says it can change a decision.

### Q8. What can be accomplished with minimal resources?

Within **₹0–2.0 lakh total** (Gate 2 close-out ₹0–0.25 lakh + Gate 3 ₹0–0.5 lakh + external review ₹0.70–1.25 lakh) and 6–10 weeks:

- close Gate 2’s missing volume/heat/cost/lifetime items at screening level;
- complete Gate 3 equations for M1, M2, M3, M4, M5;
- obtain three datasheets and add page/figure locators;
- run an independent desk review (₹0.70–1.25L, within T0);
- produce a go/no-go on M3 and a ranked Gate 3 shortlist;
- preserve the negative result and the benchmark.

This does **not** produce a device, a measured pack, or a validated system. It produces a defensible decision.

### Q9. What expertise, facilities, funding, and time would the next stages require?

| Stage | Expertise | Facilities | Funding (INR) | Time |
|---|---|---|---|---|
| Gate 3 | thermodynamics, electrochemistry, power electronics, nuclear/regulatory | desk + datasheets | ₹0–0.5 lakh (+ review) | 6–10 weeks |
| Gate 4 | modelling, V&V, uncertainty | compute + one bench | ₹25–70 lakh (T1) | 3–6 months |
| Gate 5 | experimental physics, metrology, safety | certified battery/H₂ lab, thermal bench | ₹55–130 lakh (T2) | 6–12 months |
| Gate 6 | independent lab | second-site replication | ₹1.06–2.56 crore (T3) | 6–12 months |
| Gate 7 | systems, safety, manufacturing | integration/test facility | quote-dependent | 12–24 months |
| Gate 8 | IP, economics, regulation | legal/patent | quote-dependent | 3–6 months |

Nuclear work needs a licensed partner; this program must not attempt it. H₂ work needs a certified facility. Li-metal work needs fire containment. None of these is currently confirmed.

### Q10. What results would justify continuing, changing direction, or stopping?

**Continue** if any of:

- a measured pack ≥500 Wh/kg with ≥1,000 cycles and safe failure;
- M3 closure passes at ≤100 kg and ≤$20,000 with a measured converter;
- a converter ≤0.5 kg/kW is confirmed and the thermal closure holds;
- a nuclear paper study finds a lawful ≤500 kg/kWe path at M2 cost.

**Change direction** if:

- M1 fails but M3 passes → shift to M3;
- M2 diesel is mass-feasible but cost/heat-limited → shift to M4 or nuclear paper;
- M4 heat rejection dominates → prioritise SOFC/ORC and external heat, not storage;
- all storage routes fail → make the program a source/conversion program.

**Stop** if:

- no hypothesis reaches E2 after Gate 3;
- every shortlisted candidate fails Gate 4;
- no effect replicates at Gate 6;
- the only mass-feasible source has no lawful path and the chemical path fails cost/heat;
- two consecutive gates change no decision.

### Q11. What would count as a genuine breakthrough rather than a better conventional system?

- **≥2× system specific energy** at equal power, safety, life, and cost, measured at E5 and replicated at E6, at the full mission boundary.
- **≥2× system specific power** with the same conditions.
- **≥30% lower LCOE** with quotations and the same duty cycle.
- **A new source** with a closed, independently replicated energy balance and no conventional explanation.

Not a breakthrough: a 10–30% cell gain; a simulation; a patent; a single lab anomaly; a headline that omits cooling, shielding, converter, or fuel; a “compact” claim that only counts the core.

### Q12. What should the project do during its first seven days?

1. Re-verify `e75be96` and the 57 tests; archive the output.
2. Resolve D16: the config’s **1 kW × 8 h = 8 kWh** vs the **10 kWh** sizing; record which is authoritative.
3. Repair or explicitly accept the M2 and M5 target inconsistencies.
4. Obtain three datasheets: 6 kW inverter, 30 kW inverter, 10 kWh LFP/NMC pack.
5. Add page/figure locators for S01, S04, N01, N02, N08.
6. Run `screening.py` and `limits.py`; archive the outputs.
7. Identify two independent reviewers (thermal; electrochemistry) and send the Gate 2 package.
8. Choose **M3** as the first Gate 3 target (recommended) or M2; do not start both.
9. Spend nothing; buy nothing; start no experiment; do not edit Project-E; do not commit or push.

---

## 4. Ranked candidates

| Rank | Candidate | Impact | Plausibility | Evidence | Cost to next decision | Main uncertainty |
|---:|---|---|---|---|---|---|
| 1 | M3 converter + pack closure | High | **Highest** | E1 | ₹0–2 lakh | converter kg/kW, heat |
| 2 | M2 source comparison | Very high | Medium | E1 | ₹0–2 lakh paper | fuel cost, nuclear law |
| 3 | M4 heat + SOFC/TPV | High | Medium | E1 | ₹0–1 lakh model | external heat, radiator |
| 4 | H1 advanced storage | Very high | Low–medium | E1 | ₹50k–2 lakh | 2–4× gap, cycle life |
| 5 | H10 free-piston | High (M1 mass) | Medium | E0/E1 | ₹3–8 lakh | efficiency, emissions, life |
| 6 | H3 nuclear | Very high (M2) | Low (regulation) | E1 | ₹0–2 lakh paper | lawful path, shield mass |
| 7 | H4 TPV | Medium (M4) | Low (store) | E1 | ₹2–6 lakh | 484–806 kg store |
| 8 | H5 PEM | Medium | Low (price) | E1 | ₹5–12 lakh | H₂ $6/kg |
| 9 | H7 buffer | Low | Negative | E1 | ₹1–3 lakh | 8.3 kg vs 8.9 kg |
| 10 | H8 LENR | Unknown | Negative control | E1 | ₹0 | no reproducible claim |

**No candidate is selected.** Rank 1 is a decision-analysis task, not a technology winner.

---

## 5. Confidence and uncertainty

| Claim | Confidence | Why |
|---|---|---|
| Conservation, Carnot, source hierarchy | **High** | Established physics |
| M1 118.3 kg at 175 Wh/kg | **High** | Arithmetic + reproduced table |
| M1 510–691 Wh/kg pack requirement | **High** (conditional) | Depends on converter and packaging assumptions |
| M2 battery impossibility | **High** | 1,100+ Wh/kg pack, 4–7× gap |
| M4 30 kW waste / 30 m² radiator | **High** (order of magnitude) | Conservation + \(h\) assumption |
| M3 near-feasibility | **Medium** | Converter mass unmeasured |
| Diesel/H₂/TPV system masses | **Medium** | Screening estimates, no datasheets |
| Costs and LCOE | **Low** | E0 prices, no quotes |
| Nuclear mass/regulatory path | **Low** | Concept range, no licence |
| Any “new mechanism” | **Very low** | No reproducible evidence |

A ±20–30% error on masses and a ±50% error on costs do not change the M1 and M2 verdicts. They can change the M3 verdict. That is why M3 is the first target.

---

## 6. What would change this memo

- A measured 500+ Wh/kg pack with 1,000 cycles → M1 moves from “fails” to “near-feasible.”
- A measured converter ≤0.5 kg/kW → M3 may pass; the program shifts to M3.
- A lawful nuclear path ≤500 kg/kWe → M2 becomes a systems/regulatory program.
- A replicated net-output anomaly → the source hierarchy is wrong; a new branch is required.
- A revised mission definition (M2 capex, M5 charging, M1 duty) → the cost verdicts change, not the physics.

Until one of these arrives, the memo stands.

---

## 7. Deliverables map

| # | Required document | File | Status |
|---:|---|---|---|
| 1 | Vision | `PROJECT_E_VISION.md` | draft; Gate 0 conditional |
| 2 | Repository audit | `REPOSITORY_AUDIT.md` | complete for `e75be96` |
| 3 | Scientific landscape | `SCIENTIFIC_LANDSCAPE.md` | partial; page locators pending |
| 4 | System limits | `SYSTEM_LIMITS.md` | new; screening |
| 5 | Bottleneck map | `BOTTLENECK_MAP.md` | new; screening |
| 6 | Mechanism register | `MECHANISM_REGISTER.md` | draft; 20 mechanisms |
| 7 | Hypothesis register | `HYPOTHESIS_REGISTER.md` + `.csv` | 11 hypotheses; E1 max |
| 8 | Mission matrix | `MISSION_MATRIX.md` | M1–M5; M2/M5 targets inconsistent |
| 9 | Computational research plan | `COMPUTATIONAL_RESEARCH_PLAN.md` | draft |
| 10 | Experiment strategy | `EXPERIMENT_STRATEGY.md` | draft; no experiment authorised |
| 11 | Safety and risk register | `SAFETY_AND_RISK_REGISTER.md` | draft |
| 12 | Research roadmap | `RESEARCH_ROADMAP.md` | new; Gates 0–8 |
| 13 | Resource and budget plan | `RESOURCE_AND_BUDGET_PLAN.md` | ranges only |
| 14 | Independent review plan | `INDEPENDENT_REVIEW_PLAN.md` | new; no reviewer engaged |
| 15 | Decision memo | `PROJECT_E_DECISION_MEMO.md` | this document |

**Annexes:** `GATE2_SCREENING.md`, `screening.py`, `limits.py`, `SOURCE_VERIFICATION.md`, `NEGATIVE_RESULTS.md`, `PROJECT_E_PRE_EXECUTION_PLAN.md`.

All 15 required files exist. None is approved. Gate 2 is not passed.

---

## 8. Approval

- [ ] Owner accepts Track A preservation.
- [ ] Owner accepts the mission-driven redirection and M1–M5.
- [ ] Owner accepts “no architecture selection.”
- [ ] Owner accepts that Gate 2 is not passed.
- [ ] Owner authorises Gate 3 paper work only (₹0–0.5 lakh) plus review, total T0 ≤₹2.0 lakh.
- [ ] Owner approves M3 (recommended) or M2 as the first target.
- [ ] Owner approves the external desk review (₹70,000–1,25,000), within the T0 ceiling.
- [ ] Owner confirms no hardware, purchase, experiment, repository edit, commit, or push.

---

## 9. Required statements

**Preserve:** the existing benchmark, tests, evidence ladder, cost model, red-team review, and negative result at `e75be96`.

**Redirect:** Project E from a single portable-hybrid build to a mission-driven, evidence-gated search across storage, conversion, and generation.

**No-build:** no hardware, purchase, experiment, repository edit, commit, or push is authorised by this memo.

**Best next action:** the M3 converter/pack/thermal closure with supplier datasheets, then external desk review.

**Implementation not started:** no new device, prototype, or experiment has been implemented.

**No winner manufactured:** the evidence does not support selecting a candidate. The program’s first job is to close the cheapest decisive unknowns, not to defend a favourite.
