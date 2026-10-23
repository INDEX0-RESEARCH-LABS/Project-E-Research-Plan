# Project E — Engineering Audit and Staged Implementation Plan

**Version:** 0.1  
**Date:** 2026-10-23  
**Auditor:** Project E research agent  
**Scope:** `/home/darion-dev/project-e` (benchmark, frozen) and `/home/darion-dev/project-e_research_plan` (research plan, active)  
**Branch for this work:** `engineering-v0` in the research-plan repository

---

## 1. What exists today

### 1.1 Benchmark repository — `project-e`

| Item | State |
|---|---|
| Commit | `e75be96` (`main`), clean working tree |
| Tests | **57 passed** in the project virtual environment (Python 3.12) |
| CI | GitHub Actions green at the audited commit |
| Model | Reduced-order energy system, 1 s dispatch, eight fixed architectures A1–A2/B1–B4/C1–C2 |
| Physics | Carnot, TEG, TPV guard, PV derating, radiation/conduction/convection, lumped thermal, battery/supercapacitor, fuel flow, LCOE |
| Provenance | Config checksum, run manifests, committed baseline run; one baseline artifact was edited after creation (D5 in `REPOSITORY_AUDIT.md`) |
| Tests | Analytical reference values and invariants; no hardware measurements |
| Gaps | Fixed eight candidates; no mechanism search; no component database; no CAD; no multiphysics; no geometry; no compatibility engine |

The benchmark is a credible **negative result and Track A reference**, not the discovery mission. It is frozen and is not modified by this plan.

### 1.2 Research-plan repository — `project-e_research_plan`

| Item | State |
|---|---|
| Commit | `e4c02fe` (`main`), clean working tree; this work is on `engineering-v0` |
| Documents | 25 Markdown files, including M1–M5 closures, mission matrix, mechanism register, negative results, source ledger, safety register, independent-review plan |
| Quantitative scripts | `screening.py`, `limits.py`; both exit 0; self-checks pass |
| Registers | 38 negative results (N-01–N-38); 19 sources (S01–S19); 20 mechanisms (M01–M20) |
| Gaps | No packaged model, no automated tests for the scripts, no machine-readable requirements/mechanisms/components, no CAD, no multiphysics, no compatibility engine, no run manifest |

### 1.3 Toolchain available

| Capability | State |
|---|---|
| System Python | 3.14.8, **no numpy/scipy/matplotlib/pytest** |
| Project virtual environment | Python 3.12.14 with numpy, scipy, matplotlib, pandas, PyYAML, pytest |
| CAD | No `build123d`, `cadquery`, or `trimesh` installed |
| Solvers | No OpenModelica, ngspice, FEMM, Elmer, or CalculiX verified |
| Plotting | Matplotlib available only in the project virtual environment |

**Decision:** the first engineering package uses the **standard library only** for the model, so it runs on either interpreter. Plot generation uses the project virtual environment and degrades to a text-only report if matplotlib is absent. No software is installed in this milestone.

---

## 2. What has genuinely been tested

| Test | Evidence | Result |
|---|---|---|
| Benchmark test suite | `project-e/.venv/bin/python -m pytest -q` | 57 passed |
| Benchmark reproduction | Fresh run at `e75be96` outside the repository | Published eight-architecture table reproduced |
| Research-plan arithmetic | `python3 screening.py`, `python3 limits.py` | Exit 0; self-checks pass |
| M1 mass closure | Hand calculation + `limits.py` | 50.3 kg at 26.35%; 45.6 kg at 35%; 35 kg only with a ≤12 kg/kW genset |
| M2 engine sensitivity | `limits.py` §11 | Pass only at ≤$298 (26.35%) or ≤$797 (35%) replacement at 10,000 h |
| M3 pack/converters | `COMPONENT_EVIDENCE.md` + calculation | 166 Wh/kg at zero margin; AC branch fails |
| M4 converter/radiator | Stirling price range + Stefan–Boltzmann/convection | $14–18.5/W vs $1/W; radiator 26–30 m², 79–150 kg |
| M5 LCOE/pack | Annuity + pack sizing | $0.144/kWh vs $0.08; 170–189 Wh/kg; 5,475 cycles |

No result in either repository is an experimental measurement. All are analytical, reduced-order numerical, or literature/teardown-derived. Evidence grades remain E0–E3.

---

## 3. What the existing research has ruled out

1. **M1 at 35 kg with conventional parts.** A 1.5 kW genset at ≤12 kg/kW and ≤$1,000 is required; no verified product meets both. The 45.6 kg / 35% case is the conventional frontier.
2. **M2 as a comfortable pass.** The continuous 0.58 kW diesel path is a knife-edge on engine replacement and fuel price. Cycle-charging with a standard 3–5 kW genset fails at realistic $700–$1,000/kW genset capex.
3. **M3 with a 50 Hz AC load.** An 80 kg hybrid inverter leaves negative pack mass. The DC/motor branch is conditional at 166 Wh/kg and zero margin.
4. **M4 at ≤$1/W with a Stirling converter.** The converter alone is 14–18.5× the target; the radiator is not the binding term.
5. **M5 at $0.08/kWh with $0.10 charging.** Charging alone delivers $0.117/kWh; the target needs ≤$0.043/kWh and a 170–189 Wh/kg pack at 5,475 cycles.
6. **Perpetual motion, LENR, and over-unity claims.** Retained as a negative control; no reproducible net-output evidence with a closed source balance.

These are preserved. This plan does not reopen them without new evidence.

---

## 4. What remains scientifically unresolved

| Question | Why it matters | Current state |
|---|---|---|
| What is the **service interval** for E-Micro/E-Mobility/E-Heavy? | A 3 kW source in 2.16 L means very different things at 1 h and 10,000 h | Not specified in the directive beyond “without routine charging/refuelling” |
| What are the **load profiles**? | Continuous 3 kW, peaking, duty cycle, ambient | Not specified |
| Can any **current** mechanism fit 3 kW in 2.16 L? | The first hard gate for E-Micro | This milestone answers it |
| Is the **E-Micro 2.16 L** envelope an internal volume or external envelope? | Changes packaging allowance | Assumed external 120×150×120 mm |
| What **component** can meet the selected source? | Gate 3 | No quotes/datasheets for a 3 kW source |
| Is **M3** a DC/motor or 50 Hz AC load? | Changes M3 verdict | Owner decision pending |
| Is there a **lawful nuclear path**? | M2/M4 long-duration option | Paper study only |
| Can an **independent reviewer** reproduce the claims? | Gate 7 | No reviewer engaged |

The new directive adds three product targets that are **not** in the M1–M5 matrix. They require a new requirements baseline before any design work.

---

## 5. Capabilities missing for virtual component assembly and multiphysics

| Capability | Needed for | Current gap | First implementation |
|---|---|---|---|
| Machine-readable requirements | Traceability from target to model/test | Only prose | `engineering/data/requirements.json` |
| Machine-readable mechanism library | Reproducible screening | Prose table | `engineering/mechanisms.py` |
| Component catalogue | BOM, compatibility, mass/volume/cost | Four parts in Markdown | Deferred to Gate 3; schema defined then |
| Compatibility engine | Reject invalid voltage/current/thermal combinations | None | Deferred until a candidate BOM exists |
| Geometry/packaging | 2.16 L claim, collisions, clearances | None | First-pass analytical volume; 3D deferred until a candidate survives |
| Multiphysics | Thermal/electrical/mechanical coupling | Lumped thermal only | Reduced-order thermal/electrical model after the feasibility gate |
| Test harness | Reproducible pass/fail | No tests for research-plan scripts | `engineering/tests/` with stdlib `unittest` |
| Run provenance | Auditable outputs | Ad hoc | Run manifest with git commit, inputs, output hashes |
| Optimisation | Pareto trade-offs | None | Deferred until at least one candidate passes Gate 2 |
| FMEA/fault tree | Safety | Register only | After architecture selection |

**Do not install heavy tools yet.** The first question is whether the target is physically possible. CAD and multiphysics before that would be expensive decoration.

---

## 6. Proposed architecture and staged plan

### 6.1 Repository strategy

- Keep `project-e` frozen at `e75be96` as the benchmark.
- Build the engineering toolchain in `project-e_research_plan` on branch `engineering-v0`.
- Reuse the benchmark’s validated formulas as **cross-checks**, not as a runtime dependency. The new model is standalone, standard-library only, and independently testable.
- Commit generated reports and small figures; keep large artifacts out of Git.

### 6.2 Minimal package layout (only what is used now)

```
engineering/
  __init__.py
  physics.py          # units, conservation, heat rejection, fuel/energy volume
  mechanisms.py       # mechanism definitions and parameter ranges
  feasibility.py      # screen a mechanism against an envelope and duration
  report.py           # generate Markdown, plots, and a run manifest
  data/
    requirements.json # E-Micro, E-Mobility, E-Heavy targets
  tests/
    test_feasibility.py
reports/
  E_MICRO_FEASIBILITY.md
  figures/
    e_micro_volume_vs_duration.png
    e_micro_heat_rejection.png
```

Skipped for now: `components/`, `designs/`, `simulations/`, `optimisation/`, `safety/`, `visualisation/` as separate trees. They are added only when a candidate survives Gate 2. A directory tree with no validated content is not a deliverable.

### 6.3 Staged plan

| Stage | Question | Deliverable | Acceptance | Gate |
|---|---|---|---|---|
| **M0 (this)** | Is the E-Micro 3 kW / 2.16 L target physically possible? | Requirements, mechanism library, feasibility model, tests, report, plots | Tests pass; no current mechanism fits 1 h; best-case and relaxation documented | Gate 2 |
| **M1** | Which mechanism is least impossible, and what real parts exist? | Component catalogue with datasheets; compatibility engine; BOM v0 | Every mass/volume/price has a source or is labelled unknown; no invented part | Gate 3 |
| **M2** | Does the selected candidate close electrically and thermally? | Reduced-order electrical/thermal model; load profiles; test cases | Energy balance, junction temperatures, converter limits, fault cases | Gate 4 |
| **M3** | Does it fit, and what does it cost? | Package layout (2D/3D placeholder or CAD), BOM cost, sensitivity | All subsystems inside boundary; clearances; cost range | Gate 4/6 |
| **M4** | Does it survive abuse? | Adversarial tests, FMEA, Monte Carlo, Pareto | Failures documented; no hidden source; independent checks where possible | Gate 5/6 |
| **M5** | Can it be built and reviewed? | Test plan, instrumentation, risk assessment, independent-review packet | Reviewer can reproduce; physical test is safe and lawful | Gate 7/8 |

### 6.4 Gate mapping

- **Gate 0:** complete. Both repositories audited; benchmark tests pass; baseline preserved.
- **Gate 1:** partial. Mechanism register exists; nuclear/regulatory and page-level sources remain open.
- **Gate 2:** this milestone. Analytical feasibility for E-Micro; a documented negative result is acceptable.
- **Gate 3–8:** not started. They require a surviving candidate.

---

## 7. First five highest-value calculations or tests

1. **Volumetric power-density check.** 3 kWe in 2.16 L = **1.389 MW/m³**. Compare with the best current source and converter.
2. **Heat-rejection check.** For 3 kWe at 15–40% efficiency, waste heat is 4.5–17 kW. Compute the required area at \(h=100\)–\(1{,}000\) W/m²K and \(\Delta T=30\)–80 K; compare with the envelope surface **0.1008 m²**.
3. **Minimum-volume frontier.** For 1, 8, 100, 1,000, and 10,000 h, compute the complete-system volume of 10 mechanisms (battery, Li-air, diesel, Stirling, microturbine, PEM, TPV, TEG, solar, RTG, supercapacitor, ambient). Identify the lower envelope.
4. **Energy-autonomy check.** Compute fuel/energy volume for 3 kW at each duration. Show whether any chemical system can meet a long service interval in 2.16 L.
5. **Threshold sensitivity.** Find the cell energy density, fuel-cell kW/L, heat-engine L/kW, and heat-transfer coefficient needed to fit 2.16 L. State whether those values are current, advanced, or theoretical.

These are cheap, decisive, and falsifiable. They come before CAD, BOM, or control design.

---

## 8. Exact files to be created or modified in this milestone

**Created**

- `ENGINEERING_AUDIT.md` (this file)
- `engineering/__init__.py`
- `engineering/physics.py`
- `engineering/mechanisms.py`
- `engineering/feasibility.py`
- `engineering/report.py`
- `engineering/data/requirements.json`
- `engineering/tests/test_feasibility.py`
- `reports/E_MICRO_FEASIBILITY.md` (generated)
- `reports/figures/e_micro_volume_vs_duration.png` (generated)
- `reports/figures/e_micro_heat_rejection.png` (generated)
- `reports/e_micro_run.json` (generated manifest)

**Modified**

- `.gitignore` only if generated artifacts need an ignore rule. The existing file already excludes `__pycache__`.

**Not modified**

- `/home/darion-dev/project-e` — remains frozen at `e75be96`.

---

## 9. Acceptance criteria for the first implementation milestone

The milestone is complete only when all of the following are true:

1. `python3 -m unittest discover -s engineering/tests` passes on the system interpreter (no third-party imports in the model).
2. `engineering/report.py` generates `reports/E_MICRO_FEASIBILITY.md` with a run manifest, or fails loudly with a preserved log.
3. The report states, with numbers and assumptions:
   - the E-Micro volumetric power-density target;
   - the required heat-rejection area versus the envelope surface;
   - the best-case volume of each mechanism at 1, 8, 100, 1,000, and 10,000 h;
   - whether any **current commercial** mechanism fits 2.16 L at 1 h;
   - the minimum relaxation that would make a current mechanism fit;
   - the exact theoretical/advanced assumptions required for a fit.
4. Every mechanism parameter is labelled **current**, **advanced**, or **theoretical**, with a source or a note that it is an estimate. No parameter is presented as measured when it is not.
5. The result is a verdict of **pass**, **conditional**, **fail**, or **insufficient evidence** for E-Micro as stated. A fail is a valid deliverable.
6. `project-e` remains clean at `e75be96`.
7. The work is committed with a descriptive message and a run manifest that records the commit, inputs, and output hashes.

---

## 10. Initial hypothesis to test

**H-E1:** *No current commercial mechanism can deliver 3 kWe for 1 hour of continuous output inside a 2.16 L external envelope, once source, conversion, heat rejection, and packaging are counted.*

**Falsifier:** a documented current product or a complete BOM with traceable datasheets that fits 3 kWe for 1 h in ≤2.16 L.

**Prediction:** the best current system is a Li-ion buffer at ~5–6 L for 1 h, or a PEM fuel cell at ~8–10 L; both exceed 2.16 L. The envelope is plausible for a **short-duration buffer** (~15–20 min at 3 kW), not for a continuous generator.

This hypothesis is tested in `engineering/tests/` and `reports/E_MICRO_FEASIBILITY.md`.
