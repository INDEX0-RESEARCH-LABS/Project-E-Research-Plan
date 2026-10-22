# Project E — Independent Review Plan

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** proposed; **no external reviewer has been engaged**  
**Purpose:** prevent the program from grading its own homework

---

## 1. Why this exists

The Gate 0–2 package was written by the same group that will benefit from a positive result. Internal review found and fixed real errors (C1 total, TPV store basis, battery pack/cell labelling, diesel double-packaging). That is necessary but not sufficient. An external reviewer must be able to reproduce the arithmetic, challenge the boundary, and say “this claim is not supported” without career or financial cost.

**Rule:** no gate above 2 is accepted on internal review alone.

---

## 2. Review levels

| Level | Name | What is checked | When | Independence |
|---|---|---|---|---|
| **R1** | Desk review | Documents, units, 3 calculations, evidence labels | Gate 2/3 | external, no financial interest |
| **R2** | Calculation reproduction | Re-run `screening.py` / `limits.py` from scratch; compare | Gate 3 | external, separate implementation |
| **R3** | Experimental witness | Protocol, calibration, controls, raw data | Gate 5 | external observer |
| **R4** | Independent replication | Full repeat at a second lab | Gate 6 | no shared authorship or funding |

R1 and R2 are required before Gate 3. R3 is required for any Gate 5 claim. R4 is required before any “breakthrough” language.

---

## 3. Required expertise

| # | Expertise | Reviews | Why |
|---|---|---|---|
| E1 | Thermodynamics and heat transfer | M4, TPV, TEG, radiator, Carnot | The most common omitted term is waste heat |
| E2 | Electrochemistry and battery packs | H1, H2, M1/M3/M5 | Cell vs pack, cycle life, thermal runaway |
| E3 | Power electronics and pulse systems | Converter kg/kW, M3 pulse, buffer | The 1.5 kg/kW assumption flips M3 |
| E4 | Nuclear engineering and regulation | H3, M2 | Shielding, criticality, licensing, security |
| E5 | Photonics / TPV | H4, S01 | Cell vs system, spectral efficiency, emitter life |
| E6 | Metrology and calorimetry | H8, any anomalous claim | Input/output accounting, blanks, calibration |
| E7 | Safety and regulatory | H2, H5, H3, H10 | Fire, H₂, high temperature, radiation |
| E8 | Technology economics | LCOE, capex, fuel, duty cycle | E0 costs cannot win a ranking |
| E9 | IP and freedom to operate | Gate 8 | Patent landscape is not proof, but it is a constraint |

A single reviewer may cover E1/E5 or E2/E7 if qualified. E4 and E6 must be separate people for any nuclear or anomalous claim.

---

## 4. Independence criteria

A reviewer is independent only if all are true:

- no co-authorship with the program team in the last 3 years;
- no employment, equity, or paid consultancy with a vendor whose product is evaluated;
- no financial interest in the outcome;
- not the author of a source they are asked to validate;
- willing to sign a conflict-of-interest declaration;
- willing to have their review memo archived (with personal data minimised).

A vendor engineer may be consulted for datasheet clarification, but cannot be the independent reviewer of that vendor’s claim.

---

## 5. Review package

Send the reviewer:

1. `PROJECT_E_VISION.md`
2. `REPOSITORY_AUDIT.md`
3. `SCIENTIFIC_LANDSCAPE.md`
4. `SYSTEM_LIMITS.md`
5. `BOTTLENECK_MAP.md`
6. `MISSION_MATRIX.md`
7. `MECHANISM_REGISTER.md`
8. `HYPOTHESIS_REGISTER.md` + CSV
9. `GATE2_SCREENING.md`
10. `screening.py`, `limits.py`
11. `SOURCE_VERIFICATION.md`
12. `NEGATIVE_RESULTS.md`
13. `SAFETY_AND_RISK_REGISTER.md`
14. `RESEARCH_ROADMAP.md`
15. `PROJECT_E_DECISION_MEMO.md`

Plus the frozen commit hash and the exact command to reproduce the scripts.

---

## 6. Specific checks (R1/R2)

The reviewer must independently check at least these, and may add more:

| # | Check | Expected | Why it matters |
|---|---|---|---|
| 1 | Converter mass at 6 kW | 11.25 kg | 1.5 kg/kW × 6 × 1.25 |
| 2 | A1 system mass at 175 Wh/kg | ~118.3 kg | Reproduces the repository |
| 3 | Required M1 pack at 1.5 kg/kW | ~691 Wh/kg | The headline gap |
| 4 | Required M1 pack at 0.5 kg/kW | ~510 Wh/kg | Shows the assumption sensitivity |
| 5 | C1 PEM system | ~56.0 kg vs repo 56.5 | Corrects the earlier 48.4 error |
| 6 | C2 diesel system | ~49.3 kg vs repo 50.3 | Checks the double-packaging correction |
| 7 | TPV usable store | 484–806 kg | The largest physics correction |
| 8 | Diesel fuel cost at $1.40/L, 26.3% | ~$0.536/kWh | Shows the M1 cost failure |
| 9 | H₂ fuel cost at $6/kg, 50% | ~$0.360/kWh | Shows why H5 is parked |
| 10 | M2 capital cost | ~$1.14/kWh | Shows the mission target is inconsistent |
| 11 | M4 radiator at 25%, 10 kWe | ~30 m², ~150 kg | Shows heat is not free |
| 12 | Graphite usable store | ~0.10 kWh/kg | Checks the 0.28 full-swing error |

A reviewer who cannot reproduce a number must say so in the issue log, not silently correct it.

---

## 7. Review questions

1. Is the system boundary complete for the mission being claimed?
2. Is any source, fuel, coolant, shield, converter, or auxiliary omitted?
3. Is energy counted twice anywhere?
4. Are units and dimensions consistent?
5. Is the evidence level honest (E0/E1 vs E2/E4)?
6. Is the calculation reproducible from the stated inputs?
7. Does the conclusion follow from the numbers, or is it asserted?
8. Is the strongest counterargument stated?
9. Is the falsification test actually capable of falsifying the hypothesis?
10. Is the safety/regulatory path addressed, or only mentioned?
11. Is the cost language honest (estimate vs quote, currency, date)?
12. What single measurement would change the verdict?

---

## 8. Issue severity and disposition

| Severity | Definition | Required response |
|---|---|---|
| **Critical** | Invalidates a gate conclusion or a safety claim | fix and re-review before the gate |
| **High** | Materially changes a ranking or a number | fix or explicitly accept with rationale |
| **Medium** | Ambiguity, missing locator, weak sensitivity | fix in the next revision |
| **Low** | Style, clarity, minor inconsistency | optional |

A gate cannot pass with an open critical or high issue. “Accepted with rationale” must be written, not implied.

---

## 9. Schedule and budget

| Activity | Duration | Cost (INR) | Notes |
|---|---|---:|---|
| R1 desk review, 2 reviewers | 2–3 weeks | ₹40,000–70,000 | 2–3 days each |
| R2 independent reproduction | 2–4 weeks | ₹25,000–45,000 | separate implementation |
| R3 experimental witness | per Gate 5 | ₹50,000–1,50,000 | travel/time |
| R4 replication | 6–12 months | T3, ₹1.06–2.56 crore | only after a real effect |
| Conflict/administration | — | ₹5,000–10,000 | declarations, archive |

These are planning ranges, not quotations. Total R1+R2+administration: **₹70,000–1,25,000**, within T0.

---

## 10. Reviewer deliverables

Each reviewer returns:

1. a signed independence/conflict declaration;
2. a review memo with a clear recommendation (accept / accept with changes / reject);
3. an issue log with severity and location;
4. a reproduction log for the calculations they checked;
5. a statement of what they did **not** review.

The program responds with a disposition matrix: every issue fixed, accepted with rationale, or disputed with evidence. No issue is deleted.

---

## 11. Acceptance criteria for the review itself

The review is complete when:

- [ ] at least two independent reviewers have signed;
- [ ] all critical and high issues are closed or explicitly accepted;
- [ ] at least three calculations have been reproduced independently;
- [ ] the reviewers’ conflicts are declared and archived;
- [ ] the review memo and issue log are stored with the gate package;
- [ ] the decision memo records the review outcome, including dissent.

**Current status:** internal red-team review complete; **external review not started**. Gate 2 remains not passed until R1/R2 are complete.

---

## 12. What this plan does not do

- It does not make a hypothesis true by peer approval.
- It does not replace an experimental replication.
- It does not transfer responsibility for safety or regulatory compliance.
- It does not authorise any purchase, experiment, or repository change.
