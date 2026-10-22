# Project E — Decision Memo (Gate 0/1/2)

**Date:** 2026-10-23  
**Prepared by:** research program (outside the tracked repository)  
**Repository state:** frozen at `e75be96`; no edits, commits, or pushes  
**Hardware state:** none purchased; no experiment started

---

## 1. Decision requested

Whether to:

1. preserve the existing eight-architecture benchmark as Track A;
2. redirect Project E from “build the portable hybrid” to a mission-driven discovery program;
3. authorize the next paper/analysis stage (Gate 2 completion and Gate 3 planning), but **not** hardware.

---

## 2. What was established

| Finding | Evidence | Status |
|---|---|---|
| The repository is a credible benchmark and negative result | Audit at `e75be96`; 57 tests; fresh reproduction of the eight-architecture table | Verified |
| No benchmark architecture meets all M1 targets | Repository results; best score 3/5 | Verified |
| A1 cannot reach 35 kg for the 8 h M1 mission under the 300 W/kg continuous rating | 21.1 kg cells before energy; 11.25 kg converter; Gate 2 screen 118.3 kg; ~40 kg at 0.5 h | Reproduced at screening level; not validated |
| A1 would need ~690–700 Wh/kg pack-level (~865–870 Wh/kg cell) even with no margin | Gate 2: 34.9 kg at 870 cell-level; effective pack 696 Wh/kg | Screening estimate; not a demonstrated pack |
| C2 diesel hybrid is ~49–50 kg; C1 PEM hybrid ~56.0–56.5 kg | Repository + Gate 2 screen | Reproduced at screening level; not validated |
| B3 TPV is a converter, not a self-contained generator, and fails H4 | External ≥1500 °C heat; 484–806 kg usable store alone; 0.06–0.10 kWh/kg | Reproduced at screening level; H4 kill applied |
| The 35 kg mission is one provisional case, not Project E | Vision and mission set | Decided |
| Converter mass 11.25 kg is correct: 1.5 kg/kW × 6 kW × 1.25 packaging | Code at `architectures.py:569–571` | Reconciled (D12) |
| Fuel-cell screen 48.4 kg was an error; corrected to ~56.0 kg vs repo 56.5 kg | Packaging/source/radiator omission | Corrected (v0.2) |

---

## 3. Decisions

### D1 — Preserve Track A
The repository, tests, evidence ladder, cost model, red-team review, and negative result are retained as the conventional benchmark. They are not deleted or rewritten.

### D2 — Redirect the mission
Project E is not defined by the 35 kg / 6 kW / 8 h mission. M1 remains the benchmark; M2 (long-duration remote), M3 (high-power compact), and M4 (stationary heat-to-power) are added as provisional missions.

### D3 — No architecture selection
No candidate is selected. H1–H8 remain provisional. Gate 3 is not opened.

### D4 — Storage, conversion, generation remain separate
No converter may be counted as a generator. No battery may be counted as a source. Every architecture declares its source and closes its energy balance.

### D5 — Paper and analysis only
Authorize completion of Gate 2 documentation, independent review, source verification, and Gate 3 planning. Do **not** authorize purchases, lab work, or hardware.

### D6 — Cost language
All costs are planning ranges unless a vendor quotation exists. The exchange rate is ₹94.593871/USD (2026-10-22, market API), not an RBI rate and not a quotation.

---

## 4. Gate status

| Gate | Status | Reason |
|---|---|---|
| 0 — Vision and guardrails | Conditionally accepted | Vision, non-claims, and three-category separation drafted; owner sign-off pending |
| 1 — Landscape and hypotheses | Partially complete | Register, landscape, source verification, and negative results drafted; full-text/page-level review pending |
| 2 — Physics screen | **Not passed; provisional** | Screen passes self-checks and an internal red-team review, but volume, heat, cost, lifetime, E2 locators, external independent review, and supplier data are incomplete |
| 3 — Candidate selection | Not opened | No architecture selected |
| 4 — Model V&V | Not started | Depends on Gate 3 |
| 5 — Experiment | Not started | Depends on Gate 4 and safety review |
| 6 — Translation | Not started | Depends on Gate 5 |

---

## 5. Open issues

1. Full-text/page-level verification for nuclear/SMR, thermionic/AMTEC, Li–S/Li–air, SOFC, and supplier data.
2. No supplier quotations; all costs are estimates.
3. No external independent review of the Gate 2 calculations yet; the internal red-team pass is complete.
4. Nuclear regulatory path unresolved; paper study only.
5. Converter/pack pulse data unmeasured.
6. Repository documentation ambiguity on converter mass (audit note D12).
7. Track A’s stale requirements/validation claims remain in the frozen repository; they are audit findings, not to be edited now.
8. Gate 2's own acceptance checklist is incomplete; it must not be reported as passed.
9. C1 fails H5 at $6/kg H2; B3 fails H4 at 0.06–0.10 kWh/kg; the supercap buffer fails H7 at 8.3 kg. These are parked, not selected.
10. The battery basis is ambiguous: 175 Wh/kg is labelled pack-level but packaged again. The 870 figure is cell-level, not pack-level.

---

## 6. Next best action

**Close the red-team findings and the remaining Gate 2 items (volume, heat, cost, lifetime, E2 locators), then run the L1 build-up for M2 and M4.**

The internal red-team review is complete. It found real errors: the C1 total, the TPV store basis, the battery pack/cell labelling, the diesel fuel packaging, and the category mixing. Those findings have been incorporated into v0.2. The next step is to finish the missing Gate 2 items, not to start a prototype.

M1’s eight conventional architectures have been explored; that does **not** prove M1 is physically exhausted. M2/M4 change the binding constraints (fuel logistics, heat rejection, duration), so they are worth testing — not assumed to be more likely.

Do not start with a prototype. Do not buy cells or a genset. Do not open Gate 3 until Gate 2 is accepted and the L1 build-up is reviewed.

---

## 7. Approval

- [ ] Owner accepts Track A preservation.
- [ ] Owner accepts the mission redirection.
- [ ] Owner accepts “no architecture selection.”
- [ ] Owner authorizes paper/analysis only.
- [ ] Owner accepts the budget as a range, not a commitment.

---

## 8. Required statements

**Preserve:** the existing benchmark, tests, evidence ladder, cost model, red-team review, and negative result at `e75be96`.

**Redirect:** Project E from a single portable-hybrid build to a mission-driven, evidence-gated search across storage, conversion, and generation.

**No-build:** no hardware, purchase, experiment, repository edit, commit, or push is authorized by this memo.

**Best next action:** external independent review of the Gate 2 screen, then the M2/M4 L1 build-up.

**Implementation not started:** no new device, prototype, or experiment has been implemented.
