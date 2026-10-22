# Project E — Computational Research Plan

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** plan only; no new simulation has been run  
**Rule:** analytical bound first, then the smallest model that can change a decision.

---

## 1. What computation is for

Computation is used to:

1. close mass, volume, energy, and heat balances;
2. compare candidates at the same mission and boundary;
3. identify the binding term;
4. propagate uncertainty;
5. design the cheapest decisive experiment.

Computation is **not** used to claim a device works, to replace a measurement, or to produce a headline number.

---

## 2. Model hierarchy

| Level | Model | Purpose | Acceptance |
|---|---|---|---|
| L0 | Closed-form energy/mass/heat bounds | Kill impossible candidates before coding | Units checked; Carnot/thermodynamic limits enforced |
| L1 | Spreadsheet/Python system build-up | Compare M1–M5 at one boundary | Reproduces L0; every input has evidence level |
| L2 | Time-series dispatch | Pulse load, buffer SOC, fuel use, part-load efficiency | Energy closure ≤1e-6; timestep convergence |
| L3 | Thermal/radiator model | Coolant, heat rejection, radiator area/mass | Lumped model vs analytical; sensitivity to h, emissivity |
| L4 | Cost/LCOE model | Capex, fuel, replacement, discount rate | Separate estimate/quote/unknown; sensitivity |
| L5 | CFD/FEA/transient | Only if L3/L4 shows a design question that a lumped model cannot answer | Mesh/grid convergence; independent check |

No L5 model before L0–L3 are accepted.

---

## 3. Verification and validation

### Verification (is the model solved correctly?)

- Unit tests for every equation.
- Analytical limits: zero loss, zero mass, Carnot bound, energy closure.
- Timestep convergence: 1 s vs 2 s vs 0.5 s.
- Independent implementation of at least three calculations in a different language or by hand.
- Regression against the frozen repository at `e75be96`.
- Deterministic seeds and recorded environment.

### Validation (does the model match reality?)

- Component data from datasheets or the project's own bench test.
- Comparison at the component level before system level.
- Calibration only on a training dataset; held-out test data for validation.
- Report bias, scatter, and worst-case error, not only R².

A model that matches the repository is **verified against the repository**, not validated against reality.

---

## 4. Data and provenance

Every input record carries:

- parameter name and units;
- value and range;
- evidence level E0–E6;
- source DOI/URL and page/figure/table;
- date accessed;
- whether it is measured, modeled, or assumed;
- sensitivity result.

Rules:

- No E2 value without a locator.
- No silent unit conversion.
- No overwriting a run artifact; new run, new directory.
- Configuration and code version recorded with every result.
- Negative and failed runs retained.

---

## 5. Software

- Use the existing repository stack for Track A; do not fork it into the discovery program without a reason.
- New analysis scripts live outside the tracked repository until Gate 3.
- Prefer the standard library and existing dependencies; add a dependency only if it removes more code than it adds.
- No machine learning until there is a measured dataset large enough to justify it. A physical model with 10 points does not need a neural network.
- Plots are generated from the same data file as the tables; no hand-edited numbers.

---

## 6. Computational sequence

1. **L0 bounds** for M1–M5: storage, converter, source, heat, cost.
2. **L1 build-up** for H1–H11; reproduce the Gate 2 screen.
3. **L2 dispatch** only for candidates that pass L0/L1.
4. **L3 thermal** for the best two; radiator and pump power included.
5. **L4 cost** with scenario ranges, not point estimates.
6. **Sensitivity/uncertainty**: one-at-a-time, then a small factorial or Monte Carlo where distributions are defensible.
7. **Independent review** before any ranking is used for a gate.

---

## 7. Uncertainty

- Report a range for every headline.
- Distinguish aleatory (irreducible) from epistemic (knowledge) uncertainty.
- Do not average away a fatal worst case.
- A candidate that wins only in the optimistic corner is not a winner.
- Use scenario tables: pessimistic / base / optimistic, with the assumptions named.

---

## 8. Deliverables

| Deliverable | Gate | Status |
|---|---|---|
| L0 screening table | 2 | v0.2 done (`GATE2_SCREENING.md`, `limits.py`) |
| L1 build-up workbook | 2–3 | pending |
| L2 dispatch model | 3–4 | pending |
| L3 thermal model | 4 | pending |
| L4 cost/LCOE model | 4 | pending |
| Uncertainty report | 4 | pending |
| Independent review | 2 and 4 | pending |

---

## 9. Acceptance

- [ ] L0 reproduces by hand and by script.
- [ ] Every L1 input has an evidence level.
- [ ] L2 closes energy within tolerance.
- [ ] L3 includes radiator and pump power.
- [ ] L4 separates estimates, quotes, and unknowns.
- [ ] Sensitivity does not reverse the ranking silently.
- [ ] An independent reviewer can rerun the result from the record.
