# Project E — Research Roadmap

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** proposed; no gate beyond 0 is passed; no spend authorised  
**Rule:** a gate is complete only when its deliverables exist, its evidence is reviewed, and its decision is recorded

---

## 1. Gate overview

| Gate | Question | Status | Budget tier | Indicative duration |
|---|---|---|---|---|
| **0** | What is true about the baseline, scope, and resources? | conditionally accepted | ₹0–25k | 1–2 weeks |
| **1** | What is established, frontier, and unverified? | partial | ₹0–50k | 2–4 weeks |
| **2** | Which mechanisms survive a first physical screen? | **provisional; not passed** | ₹0–0.25 lakh | 3–4 weeks |
| **3** | Do the survivors close mathematically? | not opened | ₹0–0.5 lakh | 6–10 weeks |
| **4** | Do validated models agree with known data? | not started | ₹25–70 lakh (T1) | 3–6 months |
| **5** | Is the effect real in a controlled experiment? | not started | ₹55–130 lakh (T2) | 6–12 months |
| **6** | Does an independent lab replicate it? | not started | ₹1.06–2.56 crore (T3) | 6–12 months |
| **7** | Does the integrated system meet a mission? | not started | quote-dependent | 12–24 months |
| **8** | Is there a lawful, fundable, manufacturable path? | not started | quote-dependent | 3–6 months (parallel) |

Budgets are ranges from `RESOURCE_AND_BUDGET_PLAN.md`; they are not commitments. Currency is INR primary, USD comparison at ₹94.593871/USD (2026-10-22, market API).

---

## 2. Gate 0 — Truth and scope

**Entry:** repository access; owner authorisation for read-only inspection.

**Deliverables:**

- `REPOSITORY_AUDIT.md`: default branch, commit, file map, test count, reproduced results, defects D1–D15.
- `PROJECT_E_VISION.md`: ambition, non-claims, category separation.
- evidence rules and metrics (`MISSION_MATRIX.md`).
- resource inventory: people, software, lab access, budget.

**Decision criteria:** baseline commit and tests verified; benchmark preserved; storage/conversion/generation separated; negative result accepted as a possible outcome.

**Stop condition:** repository state cannot be verified, or the owner requires a positive result as a condition of the program.

**Current:** conditionally accepted. Owner sign-off is pending.

---

## 3. Gate 1 — Scientific landscape

**Entry:** Gate 0 accepted.

**Deliverables:**

- `SCIENTIFIC_LANDSCAPE.md`: mechanisms, demonstrated performance, limits, open problems.
- `SOURCE_VERIFICATION.md`: DOI/URL, date, claim, limitation, replication status.
- `MECHANISM_REGISTER.md`: 20 mechanisms plus combinations and closed entries.
- `NEGATIVE_RESULTS.md`: negative results and corrections.

**Decision criteria:** every major claim has a source or is labelled E0; the landscape is broad enough to include at least one non-conventional route; no fabricated citation.

**Stop condition:** the landscape reduces to a single known technology and no testable opportunity remains.

**Current:** partial. DOI/title verification is done; page/figure locators, full-text review of nuclear/SMR, thermionic/AMTEC, Li–S/Li–air, SOFC, and supplier data remain.

---

## 4. Gate 2 — Candidate mechanisms

**Entry:** Gate 1 sufficient to name mechanisms and limits.

**Deliverables:**

- `MECHANISM_REGISTER.md` (updated).
- `HYPOTHESIS_REGISTER.md` + CSV (H1–H11, evidence class, stop criteria).
- `SYSTEM_LIMITS.md` (mass, volume, heat, cost, thermodynamic bounds).
- `BOTTLENECK_MAP.md` (ranked constraints and interactions).
- `MISSION_MATRIX.md` (M1–M5, metrics, boundary).
- `GATE2_SCREENING.md` + `screening.py` + `limits.py` (reproducible calculations).

**Decision criteria:** every candidate declares a source and closes its energy balance; at least one candidate has a plausible path to a mission; all rejected candidates have a written reason.

**Stop condition:** every candidate fails a hard physical check, or the mission set is internally inconsistent and cannot be repaired.

**Current:** **provisional; not passed.** Volume, heat, cost, lifetime, E2 locators, external review, and supplier data are incomplete. The mission matrix has two arithmetic inconsistencies (M2 capex/LCOE, M5 charging/LCOE) that must be resolved or explicitly accepted.

---

## 5. Gate 3 — Mathematical screening

**Entry:** Gate 2 accepted; owner authorises paper work.

**Deliverables:**

- governing equations per candidate (mass, energy, momentum/heat where relevant);
- dimensional analysis and unit checks;
- physical-limit checks (Carnot, conservation, Gibbs, Stefan–Boltzmann);
- a rejection memo for every candidate that fails;
- a shortlist of **at most three** candidates with decisive unknowns;
- a revised hypothesis register.

**Decision criteria:** the shortlist is defensible on paper; each survivor has a measurable prediction and a falsification test; no survivor depends on an E0 parameter for its pass.

**Stop condition:** no candidate survives; or all survivors depend on an unsourced parameter that cannot be measured within T1.

**Duration:** 6–10 weeks. **Budget:** ₹0–0.5 lakh (T0); external review ₹0.70–1.25 lakh; total T0 ≤₹2.0 lakh.

**Priority inputs:** M3 load type (motor/DC vs 50 Hz AC), one 10 kWh pack datasheet at ≥166 Wh/kg, H₂ price, heat-transfer coefficient, nuclear regulatory path. Converter mass is now measured: 7.5 kg (PM100) vs 80 kg (Deye 30K).

---

## 6. Gate 4 — Computational validation

**Entry:** Gate 3 shortlist; models specified with validity domains.

**Deliverables:**

- reduced-order models and, only where justified, FEA/CFD;
- verification against analytical solutions;
- validation against at least one published experiment per model;
- uncertainty propagation and sensitivity;
- immutable run configurations and result artifacts;
- a model-comparison report.

**Decision criteria:** model error is quantified; conclusions are robust to input uncertainty; a model changes a decision, not just a plot.

**Stop condition:** a model cannot be validated against any known case; or the uncertainty band spans both pass and fail and cannot be narrowed within budget.

**Duration:** 3–6 months. **Budget:** ₹25–70 lakh (T1, including component data).

**Rule:** no large compute on a model whose inputs are guesses. Start with the lumped model that can be checked by hand.

---

## 7. Gate 5 — Experimental proof

**Entry:** Gate 4 passed; safety review; explicit owner authorisation; qualified supervision; containment.

**Deliverables:**

- pre-registered test protocol with controls and blanks;
- calibrated instruments and uncertainty budget;
- input/output energy accounting including heat and auxiliaries;
- repeated trials and raw data;
- a falsification report, positive or negative.

**Decision criteria:** the measured effect is outside the uncertainty band and survives the controls; or the hypothesis is falsified and recorded.

**Stop condition:** safety or regulatory approval is absent; the effect is within noise; the test cannot distinguish the hypothesis from a conventional explanation.

**Duration:** 6–12 months. **Budget:** ₹55–130 lakh (T2).

**Rule:** the smallest experiment that can falsify comes first. No integrated prototype before a component-level result.

---

## 8. Gate 6 — Independent confirmation

**Entry:** a Gate 5 result surprising enough to matter.

**Deliverables:**

- replication protocol and raw data package;
- an independent laboratory with no financial interest;
- a pre-registered analysis plan;
- a replication report, including failure to replicate.

**Decision criteria:** the effect replicates at the stated uncertainty; artefacts and conventional explanations are excluded.

**Stop condition:** no replication; or the effect is explained by calibration, stored energy, or unmeasured input.

**Duration:** 6–12 months. **Budget:** ₹1.06–2.56 crore (T3).

---

## 9. Gate 7 — System integration

**Entry:** Gate 6 replication of a component or effect worth integrating.

**Deliverables:**

- integrated design with full mass, volume, heat, cost, and safety accounting;
- interface and control design;
- failure modes and derating;
- a system test against a declared mission;
- an independent design review.

**Decision criteria:** the integrated system meets the mission at the full boundary, or the integration penalty is quantified and acceptable.

**Stop condition:** integration erases the component gain; or the system cannot meet safety, cost, or lifetime.

**Duration:** 12–24 months. **Budget:** quote-dependent; not authorised.

---

## 10. Gate 8 — Technology and IP

**Entry:** Gate 7 system result.

**Deliverables:**

- patent landscape and freedom-to-operate opinion;
- publication and data-release plan;
- partner and supply-chain assessment;
- manufacturing cost at volume;
- funding and commercialisation options;
- a stop/publish/license decision.

**Decision criteria:** a lawful path to manufacture and deploy exists; IP position is clear enough to proceed; the economics survive quotes.

**Stop condition:** no FTO; no manufacturable supply chain; or the only path is a regulated technology the programme cannot license.

**Duration:** 3–6 months, parallel with Gate 7. **Budget:** quote-dependent.

---

## 11. Dependencies and decision points

| Decision point | After | Question | If yes | If no |
|---|---|---|---|---|
| **DP0** | Gate 0 | Is the baseline verified and the scope accepted? | proceed | stop and repair |
| **DP1** | Gate 1 | Is the landscape sufficient to generate testable hypotheses? | proceed | extend search |
| **DP2** | Gate 2 | Does any candidate close physically and fit a mission? | Gate 3 | stop or reframe mission |
| **DP3** | Gate 3 | Do ≤3 candidates survive the math? | Gate 4 | record negative result; stop |
| **DP4** | Gate 4 | Do validated models support a measurable effect? | Gate 5 | revise model or stop |
| **DP5** | Gate 5 | Is the effect real and outside noise? | Gate 6 | record falsification |
| **DP6** | Gate 6 | Does an independent lab replicate it? | Gate 7 | stop; publish negative |
| **DP7** | Gate 7 | Does the system meet the mission? | Gate 8 | redesign or stop |

**Dependency notes:**

- Gate 3 cannot be credible without a measured converter mass and pack datasheet.
- Gate 4 cannot start before the Gate 3 equations are reviewed.
- Gate 5 cannot start without a safety review and explicit authorization.
- Gate 6 is worthless without a Gate 5 result worth replicating; do not run it on a marginal effect.
- Gate 7 must not be used to rescue a failed component test.

---

## 12. Parallel tracks

| Track | Scope | Gates | Output |
|---|---|---|---|
| **A — Baseline** | preserve and audit the eight-architecture benchmark | 0–2 | negative result, benchmark |
| **B — Storage** | H1, H2, H11; M1/M3/M5 mass and volume | 3–6 | pack datasheet, cell test |
| **C — Source** | H3, H5, H9, H10; M2/M4 source and conversion | 3–6 | paper comparison, bench data |
| **D — Thermal** | H4, H6, H11; M4 heat rejection | 3–6 | thermal model, coupon test |

Tracks share the mission matrix, the source registry, and the review plan. A track may stop without stopping the program.

---

## 13. Program-level stop conditions

The program stops, or pauses for owner review, if any of these is true:

1. No hypothesis reaches E2 after Gate 3.
2. Every shortlisted candidate fails Gate 4 validation.
3. No effect replicates at Gate 6.
4. The only mass-feasible source (nuclear) has no lawful path and the chemical path fails cost/heat.
5. Two consecutive gates produce no change in a decision (the “zombie project” rule).
6. Spend exceeds the approved tier by >50% without new evidence.
7. The owner withdraws authorisation or the safety review fails.

A stop is a result, not a failure. The negative record is preserved.

---

## 14. First seven days (no spend)

1. Freeze and re-verify the Project-E commit and test count (already `e75be96`, 57 tests).
2. Close D16 as withdrawn: 10 kWh = 8 kWh base + 2 kWh pulses (`dispatch.py`). **Done.**
3. Repair or explicitly accept the M2 and M5 target inconsistencies. **Done:** M2’s capex cap was a ceiling (`M2_CLOSURE.md`); M5’s pack requirement was wrong and its LCOE is charging-price-bound (`M5_CLOSURE.md`).
4. Datasheets: 30 kW converter **done** (PM100 7.5 kg, Deye 80 kg). Still needed: a 6 kW inverter and a 10 kWh pack at ≥166 Wh/kg pack-level. Record in `SOURCE_VERIFICATION.md`.
5. Page/figure locators: S01 and S05 **abstract-verified**; S09, S04, N01, N02, N08 pending.
6. Run `screening.py` and `limits.py`; archive the outputs. **Done; both pass.**
7. Identify two independent reviewers (thermal; electrochemistry) and send the Gate 2 package for desk review. **Pending.**
8. **M3 is the provisional compactness target** (conditional on a DC/motor load); **M2 is the feasibility target** (212 kg, $0.441/kWh with diesel, engine-life-bound). M1 is not a Gate 3 target at 35 kg (`M1_CLOSURE.md`). Do not start both; choose the axis first.
9. **Project-E frozen at `e75be96`; commits and pushes to this plan are authorised.** No purchase, no experiment, no hardware spend.

---

## 15. Approval required

- [ ] Accept the gate structure and the stop conditions.
- [ ] Accept that Gate 2 is not passed.
- [ ] Authorise Gate 3 paper work only (₹0–0.5 lakh) plus review, total T0 ≤₹2.0 lakh.
- [ ] Approve the first target: M3 (converter/storage) or M2 (source).
- [ ] Approve the independent review plan and reviewer list.
- [ ] Confirm no hardware, purchase, or experiment is authorised.
