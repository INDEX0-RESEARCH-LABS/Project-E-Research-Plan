# Project E — Repository Audit

**Audit date:** 2026-10-23  
**Repository:** `INDEX0-RESEARCH-LABS/Project-E`  
**Commit audited:** `e75be9688085f72dc28514c039c1e7d1ae042b10` (`main`)  
**Working tree:** clean before audit; no files edited  
**CI:** GitHub Actions run `39845121841`, conclusion `success`  
**Tests:** 57 passed (`tests/test_core.py`: 37; `tests/test_systems.py`: 20)  
**Fresh run:** current code at `e75be96` reproduces the published eight-architecture table exactly (run executed outside the repository at `/tmp/opencode/pe_audit_run`).

This audit is read-only. It does not modify the repository, commit, push, purchase hardware, or start experiments.

---

## 1. Executive finding

The repository is a **well-executed conventional portable-power feasibility study**, not an energy-core discovery program.

It asks whether eight pre-selected storage, generator, and hybrid architectures can meet an invented 35 kg / 60 L / $5,000 / $0.40 per kWh mission. It answers that question with a closed energy balance, reproducible reduced-order model, tests, uncertainty analysis, and a red-team review. It also concludes, correctly, that no candidate meets all targets and that the portable-hybrid branch is "not a search for new physics."

That is a useful **negative result and Track A benchmark**. It is not the original mission: it does not search for a new mechanism, does not model nuclear, solar, fusion, advanced electrochemical, thermionic, AMTEC, flywheel, CAES, or pumped-hydro options, and does not test any hypothesis that could produce a step-change energy core.

**Verdict: not aligned with the original vision; preserve as benchmark, redirect the program.**

---

## 2. What the software actually models

| Area | Implementation | What it supports | What it does not support |
|---|---|---|---|
| Mission and dispatch | `src/project_e/simulation/dispatch.py`; 1 s timestep, convergence checked at 2 s and 0.5 s | 1 kW continuous, 6 kW / 30 s pulses, 8 h; energy closure | Electrical dynamics, start transients, converter control, fault ride-through |
| Storage | `src/project_e/models/storage.py` | LiFePO4 pack SOC, power limits, round trip, fade; supercapacitor energy/ESR | Cell-level electrochemistry, thermal runaway, BMS, second-life, real C-rate curves |
| Conversion | `src/project_e/models/conversion.py` | Carnot, TEG, heat engine, TPV parameterisation, PV temperature derating, fuel flow | Nuclear, solar system, fusion, thermionic, AMTEC, metal-air, Li-S, SOFC, part-load maps |
| Thermal | `src/project_e/models/thermal.py` | Lumped mass, conduction, convection, radiation, ε-NTU, pump parasitic | Transient thermal, CFD, hot-spot/spatial gradients, two-phase cooling |
| Architectures | `src/project_e/simulation/architectures.py` | Eight fixed candidates A1–A2, B1–B4, C1–C2; sizing, packaging, radiator, converter | Any architecture outside the fixed eight; nuclear/solar/grid systems |
| Economics | `src/project_e/economics.py` | Discounted LCOE, replacement timing, capex/O&M/fuel | Real quotations, taxes, financing, grid connection, decommissioning |
| Sensitivity | `src/project_e/simulation/sensitivity.py` | One-at-a-time sweeps; 2,000-draw cost Monte Carlo | Correlated inputs, physics uncertainty propagation, global sensitivity |
| Reproducibility | `src/project_e/simulation/runner.py`; run artifacts | Config checksum, git commit, environment, provenance CSV, summary/report | Content-addressed immutability; the committed baseline artifact was edited after creation (see D5) |

The eight candidates are:

- A1 LiFePO4 battery; A2 battery + supercapacitor.
- B1 diesel genset; B2 TEG on a burner; B3 TPV + high-temperature thermal store; B4 PEM fuel cell.
- C1 fuel cell + battery buffer; C2 diesel + battery buffer.

All eight use the same mission and a common system boundary. That is appropriate for the benchmark. It is not a mechanism landscape.

---

## 3. Analytical, simulated, estimated, measured

| Category | Examples | Evidence |
|---|---|---|
| Analytical / closed-form | Carnot limit, TEG optimum-efficiency formula, Stefan–Boltzmann radiation, LCOE annuity, fuel flow | E3 within the model; hand-checked in tests |
| Numerical simulation | Dispatch at 1 s, SOC integration, lumped thermal, sizing grid, mission scaling | E3 within the model; convergence checked at 0.5/1/2 s |
| Engineering estimates | Component masses, packaging factor, converter mass, most efficiencies, costs | E0/E1; ranges only |
| Literature parameters | TPV 40% cell result, TEG ZT, Li-ion context, hydrogen/fuel-cell context | E2 in name; only one entry names a registry ID; most lack traceable citations (D3) |
| Measurements by this project | None | No E4–E6 |

No claim in the repository is an experimental measurement. The validation register states this correctly: ceiling E3 for models, E2 for a few parameters, E0 for most prices.

---

## 4. Verified achievements

These are real and should be preserved:

1. **Closed energy accounting.** Every architecture declares a source; dispatch asserts unmet load ≤ 1e-6 kWh; converter and storage losses are charged to the input.
2. **Reproducible model.** Current code reproduces the published table exactly; 57 tests pass; CI is green.
3. **Useful benchmark result.** No candidate meets all five targets; the best baseline score is 3/5; Under the 300 W/kg continuous pack rating, A1 cannot reach 35 kg for the 8 h mission (~40 kg at 0.5 h); C2's floor is 44.8 kg. The rating is an assumption, not a universal limit.
4. **Sensitivity and uncertainty.** The report identifies utilization, fuel price, TEG cost/ZT, lifetime, and fuel-cell cost as dominant unknowns; the Monte Carlo spread is wider than the difference between leading candidates.
5. **Red-team discipline.** `reports/RED_TEAM_REVIEW.md` correctly attacks the invented mission, E0 prices, omitted thermal-store loss, external TPV heat, radiator optimism, and missing safety/emissions.
6. **Literature registry, limited but verified.** All 12 registry DOIs resolve through Crossref and match title/year/venue. The records are abstracts only.
7. **Experiment plan for one benchmark claim.** `experiments/EXPERIMENT_PLAN.md` defines a safe, falsifiable hybrid-buffer test with pass/fail criteria.

---

## 5. Material defects and alignment gaps

### D1 — The mission is a fixed product target, not a discovery question

`docs/PROJECT_E_REQUIREMENTS.md` lines 7–9 lock the mission and state that every architecture is scored against it and nothing else. Lines 25–40 fix 1 kW / 6 kW / 8 h; the targets are 35 kg, 60 L, $5,000, $0.40/kWh, 10 years. `docs/PLAN.md` lines 17–20 repeat them.

Consequence: the repository can only answer "which of eight conventional candidates is closest to this invented portable target?" It cannot answer "what energy core is physically possible?" The requirements exclude long-duration remote, high-power compact, stationary heat-to-power, nuclear, solar, and grid-connected use cases before any physics is examined.

The red team already records this: "The mission is invented" (`reports/RED_TEAM_REVIEW.md`, item 1).

### D2 — Storage, conversion, and generation are mixed in one ranking

The comparison labels B2 (TEG on a burner) and B3 (TPV + thermal store) as generation architectures, but both are **converters** whose primary heat is supplied externally. B3 prices ≥1500 °C heat at $0.04/kWh and excludes the heat plant, delivery, and storage hardware. The red team records this (`RED_TEAM_REVIEW.md`, item 4).

Consequence: B3's low LCOE is not comparable to a self-contained energy core. The ranking does not maintain the three-category distinction the original vision requires.

### D3 — E2 labels are not traceable to sources

`validation/MODEL_VALIDATION_REGISTER.md` defines E2 as "published/datasheet value, not independently reproduced" and "parameter input with citation." In `configs/baseline.yaml` there are 17 `evidence: E2` entries. Only the TPV entry names a registry ID (`S01`). The others use generic phrases such as "typical LiFePO4 charger," "pack-level ESTIMATE," "small diesel genset, rated-load ESTIMATE," "PEM system efficiency on H2 LHV, mid-range," and "700 bar system H2 mass fraction ESTIMATE."

Consequence: the provenance chain is incomplete. A reader cannot reproduce an E2 value from the repository. Several are estimates promoted to E2 by label, not by evidence.

### D4 — Published numbers are stale or contradictory

`docs/PROJECT_E_REQUIREMENTS.md` still says:

- line 102: diesel break-even is `$0.85/L`; `docs/ARCHITECTURE_COMPARISON.md` and `economics/COST_MODEL.md` give `$0.732/L`.
- line 104: free H2 leaves the fuel-cell hybrid at `$0.44/kWh`; the model gives `$0.492/kWh`.
- line 105: TPV stays under $0.40/kWh up to `$0.070/kWh` heat; the model gives `$0.0656/kWh`.
- lines 125–126: B1 is listed at 3/5 (actual 2/5); optimistic C2 is listed at 4/5 (actual 3/5).

Consequence: a "locked" requirements document contains numbers that no current code path reproduces. This is exactly the failure the red team warned about in item 16.

### D5 — The committed baseline run is not immutable and its recorded commit is stale

`results/runs/20261022T195415Z_920ce114/summary.json` records `"git_commit": "bbfe9d3a442e91a1f7b143ef060438631762eb07"`. `git log --follow` shows the same run's `summary.json` and `architectures.csv` were modified in commit `e3f603c` ("Apply the common packaging factor to supercapacitor mass"). The README says "Runs are never overwritten"; validation rule 5 says "the old run kept, not overwritten."

Consequence: the artifact's recorded commit does not match the code that produced its final numbers. The model itself is reproducible (a fresh run at `e75be96` matches), but the provenance record is not trustworthy as an immutable artifact.

### D6 — Validation register says converter efficiency is untested

`validation/MODEL_VALIDATION_REGISTER.md` section 3 lists "converter efficiency" as not covered. `tests/test_systems.py:104` and `tests/test_systems.py:167` test converter loss and config rejection. The register is stale.

### D7 — The literature map is a benchmark support set, not a landscape

`research/source_registry.csv` contains 12 records covering TPV, TEG, supercapacitors, Li-ion, Shockley–Queillier, grid storage, PCM, hydrogen/fuel cells, and ORC. It contains no nuclear/RTG/micro-fission, solar system performance, fusion, flywheel, CAES, pumped hydro, thermionic/AMTEC, metal-air/Li-S, or SMR/regulatory sources. `reports/PROJECT_E_STATUS.md` says "12 DOI-verified records; abstracts only."

Consequence: the repository cannot support a claim about the best available energy core. It only supports the eight chosen candidates.

### D8 — Model scope is deliberately reduced-order and omits decision-critical physics for discovery

The model has no electrical dynamics, no transient thermal, no spatial FEA/CFD, no part-load maps, no BMS/fault behavior, no 230 V output, no emissions/noise, no hydrogen boil-off, and no nuclear shielding/regulatory model. `validation/MODEL_VALIDATION_REGISTER.md` claims 26–27 list these as not modelled; `reports/RED_TEAM_REVIEW.md` items 5, 8, 9, 14 confirm.

This is acceptable for a screening benchmark. It is not sufficient to rule a new mechanism in or out without a first-principles screen.

### D9 — B3 thermal-store standby loss is omitted

`src/project_e/models/conversion.py` defines `SensibleHeatStore` with `insulation_ua_w_k: float = 0.0`; the B3 architecture does not supply a real loss term. `reports/RED_TEAM_REVIEW.md` item 3 records this as an open high-severity defect.

Consequence: B3's $0.301/kWh and 256.9 kg are optimistic; an 8 h hold at 1500 °C with real insulation loses a significant fraction of the stored heat.

### D10 — E0 cost inputs decide the ranking

`reports/SENSITIVITY_ANALYSIS.md` ranks `assumptions.missions_per_year` first (max ΔLCOE $2.824/kWh), then TEG cost, ZT, diesel fuel price, lifetime, and fuel-cell cost. The Monte Carlo P10–P90 spread (e.g., C2 $0.590–$1.008/kWh) is wider than the difference between leading candidates. `reports/RED_TEAM_REVIEW.md` item 2 records this.

Consequence: "B3 is cheapest in 83% of draws" is a statement about assumed uniform ranges, not about the world. No cost conclusion is decision-grade.

### D11 — No real use case

`reports/NEXT_ACTIONS.md` gate G1 is "unanswered — no external use case yet." `reports/RED_TEAM_REVIEW.md` item 15 says the project may be answering a question nobody is asking.

### D12 — Converter-mass statement omits the packaging factor

`docs/ARCHITECTURE_COMPARISON.md:27` says "converter mass 1.5 kg/kW at peak throughput (11.25 kg at 6 kW)". The code at `architectures.py:569–571` computes `6 kW × 1.5 kg/kW × 1.25 packaging = 11.25 kg`. The number is correct; the sentence is ambiguous because it omits the 1.25 factor. A reader cannot reproduce 11.25 from "1.5 kg/kW at 6 kW" alone. This is a documentation defect, not a model defect.

### D13 — C1 fuel-cell mass breakdown is not documented

`docs/ARCHITECTURE_COMPARISON.md` reports C1 at 56.5 kg but does not show the stack, tank, buffer, BOP, converter, and radiator terms. A first-principles rebuild gives ~56.0 kg with a different radiator/BOP split. The result is plausible, but the table is not independently reproducible from the document alone. Gate 2 resolves it at screening level; the repository should publish the build-up if it is ever revised.

### D14 — Battery specific energy is labelled pack-level but packaged again

`configs/baseline.yaml:113` calls 175 Wh/kg "pack-level LiFePO4", but `battery_only` divides by 175 and `screen_architecture` then applies a 1.25 packaging factor. That is only consistent if 175 is **pre-packaging/cell-level**. If 175 is truly pack-level, A1 is ~97 kg, not 118.4 kg, and the 1.25 factor is a double count. The same ambiguity makes the document's "870 Wh/kg pack-level" claim wrong: with the code's packaging, 870 is cell-level and the effective pack-level is ~696 Wh/kg; without double packaging, the required pack-level is ~690 Wh/kg. This is a decision-critical basis error, not a rounding issue.

### D15 — C2 diesel fuel mass is packaged twice

In `diesel_hybrid` (`architectures.py:509–514`), the fuel mass is multiplied by 1.25 inside `mass_kg`, and `_hybrid` (`:423`) applies the packaging factor again. The effect is ~1.0 kg on C2 (repo 50.3 kg versus one-pass 49.3 kg). Small, but it violates the "packaging applied once" rule the comparison claims.

---

## 6. Dominant assumptions

The results are most sensitive to:

1. `assumptions.missions_per_year` (utilization), range 100–350.
2. Cost inputs: TEG $/W, diesel $/L, fuel-cell $/kW, H2 $/kg, battery $/kWh, discount rate, lifetime.
3. Mass inputs: battery pack 175 Wh/kg, 300 W/kg; converter 1.5 kg/kW; packaging 1.25; TEG ZT/temperatures; B3 thermal-store 0.28 kWh/kg; H2 tank 5 wt%.
4. Mission: 6 kW peak, 8 h duration, 35 kg target. A1 cannot reach 35 kg for the 8 h mission under the 300 W/kg continuous rating (~40 kg at 0.5 h); C2's floor is 44.8 kg.

The model's mass conclusions are more robust than its cost conclusions because mass is dominated by physical pulse-power and energy limits; cost is dominated by unquoted E0 prices.

---

## 7. Reproducibility

**Verified:**

- Current code at `e75be96` runs and reproduces the published table exactly.
- 57 tests pass; CI run `39845121841` succeeded.
- Run artifacts include config checksum, git commit, Python/platform/library versions, and provenance CSV.
- The dispatch converges at 0.5, 1, and 2 s.

**Not verified / defective:**

- The committed baseline artifact was edited in `e3f603c`; its `git_commit` still points to `bbfe9d3`.
- No content-addressed store; no signature; no independent re-run archived in the repository.
- Literature records are abstracts only; no page-level extraction or full-text verification.
- No E4–E6 measurement exists.

---

## 8. Alignment verdict

| Question | Answer |
|---|---|
| Does the repository model a new energy mechanism? | No. It models eight conventional architectures. |
| Does it search for a step-change energy core? | No. It optimizes a portable hybrid within fixed components. |
| Does it preserve energy accounting? | Yes, well. |
| Does it have a credible benchmark? | Yes, within its assumptions. |
| Is it aligned with the original vision? | **No.** It is a benchmark/feasibility study, not a discovery program. |
| Should it be deleted? | No. Preserve it as Track A and as a negative result. |
| Should its mission remain the program mission? | No. The 35 kg portable target is one provisional case, not the program. |

The repository's own conclusion is the strongest evidence: "The portable-hybrid branch reduces to a cost and integration problem between A1, C2 and C1 — not a search for new physics" (`docs/ARCHITECTURE_COMPARISON.md`, section 9). That is a valid finding, but it is not the original mission.

---

## 9. What to preserve, redirect, and not build

**Preserve:**

- Energy accounting and the no-net-generation rule.
- Evidence ladder, tests, analytical checks, red-team review.
- Eight-architecture benchmark, baseline results, cost model, negative result.
- Hybrid-buffer experiment plan as a benchmark test, not the main mission.
- Run artifacts, with provenance repaired.

**Redirect:**

- Re-scope the repository as **Track A — Baseline and model credibility**.
- Version the requirements; separate the benchmark mission from the discovery missions.
- Add tracks B–F and Gates 0–6.
- Make every E2 value traceable to a DOI/datasheet; downgrade untraceable values to E1.
- Expand the literature map; add nuclear, solar, fusion, flywheel, CAES, pumped hydro, thermionics/AMTEC, advanced batteries, and negative results.
- Fix stale numbers and run provenance in a new branch after owner approval.

**Do not build yet:**

- Do not buy a genset, battery, TPV, TEG, electrolyzer, or nuclear material.
- Do not start the hybrid bench test as the discovery mission.
- Do not select a final architecture.
- Do not claim a prototype, a working reactor, net generation, or a breakthrough.
- Do not run expensive FEA/CFD or agent orchestration before Gate 2.
