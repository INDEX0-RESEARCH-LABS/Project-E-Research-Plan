# engineering — Gate 2 screening package

This package answers one question before any CAD, BOM or multiphysics work:

> Given a mechanism, a continuous electrical power, a duration and an external
> envelope, what is the **minimum complete-system volume**?

It is a first-principles filter, not a design. It deliberately uses the
optimistic case of each mechanism. If the optimistic case does not fit, a real
system will not fit either.

## Run

```bash
cd /home/darion-dev/project-e_research_plan

# Model tests: standard library only.
python3 -m unittest discover -s engineering/tests -t .

# Full report, figures and run manifest: needs matplotlib.
../project-e/.venv/bin/python -m engineering.report
```

Outputs:

- `reports/E_MICRO_FEASIBILITY.md`
- `reports/figures/e_micro_volume_vs_duration.png`
- `reports/figures/e_micro_heat_rejection.png`
- `reports/figures/e_micro_volume_at_1h.png`
- `reports/e_micro_run.json`

The model modules (`physics.py`, `mechanisms.py`, `feasibility.py`) import only
the standard library. `report.py` optionally imports matplotlib; without it the
Markdown report is still written and the plot step is skipped.

## Files

| File | Role |
|---|---|
| `physics.py` | Conservation, heat rejection, fuel, battery, H2, solar, RTG volume relations |
| `mechanisms.py` | 12 mechanisms with best/worst cases and evidence labels |
| `feasibility.py` | Complete-system volume screen and verdicts |
| `report.py` | Markdown report, figures, run manifest |
| `data/requirements.json` | E-Micro, E-Mobility and E-Heavy targets; unresolved fields are explicit |
| `tests/test_feasibility.py` | 18 reference-value and invariant tests |

## Evidence rules

- `current`: commercial or near-commercial at the stated scale.
- `advanced`: demonstrated at another scale or in a laboratory, not at 3 kW.
- `theoretical`: no commercial product; used to test the target boundary.
- `restricted`: nuclear/radioactive; requires legal and safety approval.

Every parameter is a screening estimate unless its note says otherwise. No value
is a supplier quote or a measured system. A best-case result is a **lower bound**
on volume; the worst case is not an upper bound on a real design.

## Adding a mechanism

Add a `Mechanism` to `MECHANISMS` with a `kind` handled by
`feasibility._volume_l`, a best case, a worst case, an evidence label, and a
note that names the source. Add a reference-value test before trusting it.
Do not add a mechanism to make a target pass.

## Scope boundary

The screen does **not** model transients, converter control, faults, vibration,
crash, lifetime, cost or manufacture. Those are later gates. The first result is
that E-Micro as stated (3 kWe, 2.16 L) fails for every current mechanism at 1 h;
see `reports/E_MICRO_FEASIBILITY.md`.
