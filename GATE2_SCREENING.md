# Project E — Gate 2 Screening

**Version:** 0.2 (provisional; **gate not passed**)  
**Date:** 2026-10-23  
**Status:** screening estimates only; not a design, quotation, validation, or selection  
**Source of calculations:** `screening.py` (stdlib only, outside the tracked repository)  
**Self-check:** all assertions pass; output captured below

---

## 1. Purpose

Gate 2 asks: *does a candidate have a closed energy balance and a plausible system mass, volume, heat, and cost at a declared mission?*

This screen checks the dominant terms by hand before any new simulation. It does **not** replace the repository's dispatch model, and it does **not** pass Gate 2. It is a provisional physics screen.

---

## 2. Method and boundary

- M1: 10 kWh / 8 h, 6 kW pulse, 35 kg / 60 L / $5,000 / $0.40 per kWh.
- Boundary for M1: unit plus one mission fuel; packaging, converter, radiator/structure allowance, and one buffer where applicable.
- Converter efficiency: 0.95 at the AC boundary.
- Converter mass: `1.5 kg/kW × 6 kW × 1.25 packaging = 11.25 kg`.
- Storage nameplate: 14.62 kWh, the repository's A1 basis (`10 / 0.95 / 0.80 / 0.90`).
- Packaging: 1.25 on component mass, applied once.
- TPV, solar, and fission are **not** M1-comparable: they have an external heat/sunlight source or a shielding/regulatory boundary. They are shown in a separate table.

All inputs are screening assumptions. The package does not yet have page-level E2 locators; most values are E1.

---

## 3. Two basis corrections

### 3.1 Converter mass

`docs/ARCHITECTURE_COMPARISON.md:27` says "converter mass 1.5 kg/kW at peak throughput (11.25 kg at 6 kW)". The code at `architectures.py:569–571` computes `6 × 1.5 × 1.25 = 11.25 kg`. The number is correct; the sentence omits the packaging factor. Audit D12. This screen uses 11.25 kg.

### 3.2 Battery specific energy: 175 Wh/kg is not cleanly “pack-level”

`configs/baseline.yaml:113` calls 175 Wh/kg "pack-level", but `architectures.py:91–95` divides by 175 and then `screen_architecture` multiplies by 1.25 packaging. That treats 175 as **pre-packaging/cell-level**.

Consequences:

- If 175 is cell-level, A1 = 83.5 kg cells → 104.4 kg packaged → 118.3 kg system. This reproduces the repository.
- If 175 is truly pack-level, A1 = 83.5 kg pack → 97.4 kg system; the 1.25 factor is a double count.
- The repository's "870 Wh/kg pack-level" claim is therefore mislabelled. With the code's packaging, 870 is cell-level and the effective pack-level is `14.62 / 21.0 = 696 Wh/kg`. Without double packaging, the required pack-level is about `690 Wh/kg`.

**This screen states the basis explicitly and does not use "870 Wh/kg pack-level" as a headline.** Audit D14.

---

## 4. Fuel-cell basis

The first draft of `screening.py` gave 48.4 kg for C1. It omitted packaging on the stack/tank/BOP group, used 1.4 kW instead of the repository's 1.447 kW, and omitted the radiator.

Corrected one-pass screen:

- source = `(10 / 8 / 0.95) × 1.1 = 1.447 kW`;
- stack = `1.447 × 8 = 11.58 kg`;
- H2 = `10 / (0.50 × 0.95 × 33.33) = 0.632 kg`;
- tank at 5 wt% = 12.63 kg;
- buffer = `0.3 × 1000 / 175 = 1.71 kg`;
- BOP = 6 kg;
- converter = 11.25 kg;
- radiator/structure = 4.8 kg.

One-pass total ≈ **56.0 kg**; the repository reports **56.5 kg**. The residual is a different radiator/BOP split. The earlier 54.7 kg text was wrong; corrected here. The script and this document now agree.

---

## 5. M1-relevant results (including a buffer-only row)

Raw output (M1 table):

```text
M1-relevant rows (same boundary unless noted)
screen                               mass_kg  note
--------------------------------------------------------------------------------------------------------------
storage @ 175 Wh/kg                    118.3  cells 83.5 kg; packaged 104.4; converter 11.2; BOP 2.6
storage @ 300 Wh/kg                     74.8  cells 48.7 kg; packaged 60.9; converter 11.2; BOP 2.6
storage @ 500 Wh/kg                     50.4  cells 29.2 kg; packaged 36.5; converter 11.2; BOP 2.6
storage @ 870 Wh/kg                     34.9  cells 16.8 kg; packaged 21.0; converter 11.2; BOP 2.6
diesel hybrid                           49.3  source 1.447 kW; fuel 4.02 L (3.34 kg); radiator 10.0; converter 11.25; repo 50.3 kg
PEM + 5 wt% H2                          56.0  source 1.447 kW; H2 0.632 kg; tank 12.6; stack 11.6; buffer 1.7; repo 56.5 kg
supercap buffer 0.05 kWh                 8.3  8.3 kg at 6 Wh/kg; fails H7 <=5 kg
```

| Candidate | Screen mass | M1 mass | Binding term | Hypothesis verdict |
|---|---:|---|---|---|
| A1 Li-ion, 175 Wh/kg basis | 118.3 kg | Fail | 83.5 kg cells + converter | Benchmark; not a discovery candidate |
| A1 with 300 Wh/kg | 74.8 kg | Fail | cells 48.7 kg | H1's ≥250 Wh/kg pack milestone is a component gate, not an M1 pass; M1 needs 510–691 Wh/kg pack |
| A1 with 500 Wh/kg | 50.4 kg | Fail | cells 29.2 kg | still above 35 kg before margin |
| A1 with 870 Wh/kg (cell-level; ~696 pack) | 34.9 kg | Barely | no demonstrated pack at this level | **Not a candidate; a sensitivity** |
| C2 diesel hybrid | 49.3 kg | Fail | genset + converter + fuel | Fails M1 mass and $0.40/kWh at $1.40/L; H5 (fuel cell) not applicable |
| C1 PEM + 5 wt% H2 | 56.0 kg | Fail | tank + stack + converter | **Fails H5 at $6/kg H2** (> $4/kg); park unless H2 price falls |
| Supercapacitor 0.05 kWh buffer | 8.3 kg | Buffer only; not a full M1 candidate | 6 Wh/kg | **Fails H7** (>5 kg); A2 buffer is not viable as stated |

The supercapacitor row is buffer-only: its charging source is the parent system, so it is not counted as a self-contained M1 source. It is included to test H7.

### Diesel fuel target

At $1.40/L, C2 uses ~4.02 L per 10 kWh mission, or ~$5.63 of fuel, i.e. **~$0.56/kWh before capex**. The M1 target is $0.40/kWh. Diesel is fuel-limited at the benchmark price; this is a negative result, not a rounding issue.

---

## 6. Other mission / boundary results (not M1-comparable)

```text
Other mission / boundary (not comparable to M1)
screen                               mass_kg  note
--------------------------------------------------------------------------------------------------------------
TPV usable store @ 0.10 kWh/kg         483.7  eta 0.258; thermal 38.7 kWh; graphite 387.0 kg; vessel 25%; excludes emitter/cells/radiator
TPV usable store @ 0.06 kWh/kg         806.2  eta 0.258; thermal 38.7 kWh; graphite 645.0 kg; vessel 25%; excludes emitter/cells/radiator
solar + 14.62 kWh storage              135.7  area 4.0 m2; panel 20.0 kg; pack 104.4 kg; converter 11.25; mounting/MPPT excluded
fission-Stirling 1 kWe (M2)            550.0  concept range 100-1000 kg; midpoint only; shielding/regulatory not modeled; not M1
```

| Candidate | Boundary | Result | Verdict |
|---|---|---|---|
| B3 TPV + graphite store | M4 converter; external ≥1500 °C heat | 484–806 kg store alone; 0.06–0.10 kWh/kg usable | **Fails H4** (<1 kWh/kg); park for M4 until a higher-density store exists |
| Solar + storage | M2/M4; external sunlight | 135.7 kg before mounting/MPPT | Not a compact core; M2/M4 only |
| Fission–Stirling | M2; licensed site required | 100–1,000 kg per kWe concept range; midpoint 550 | **Unresolved against H3** (>500 kg/kWe); no lawful path yet |

The repository's 0.28 kWh/kg graphite figure is a full-swing sensible-heat number. A TPV emitter at ≥1500 °C can use only the top slice of that swing; using 0.28 understates the store by roughly 3–5×. This is the largest physics correction in Gate 2.

The TPV 40% source is a **cell** result at 1900–2400 °C; the design point uses 32% cell × 0.85 spectral × 0.95 converter = 25.8%, before system losses. That is consistent with the source, not a contradiction.

---

## 7. A1 sensitivity

```text
A1 sensitivity (one-at-a-time, not Monte Carlo)
storage @ 140 Wh/kg                    144.4
storage @ 175 Wh/kg                    118.3
storage @ 200 Wh/kg                    105.2
storage @ 175 Wh/kg (package 1.15)     109.9
storage @ 175 Wh/kg (package 1.40)     130.8
storage @ 175 Wh/kg (converter 0.8)    113.0
storage @ 175 Wh/kg (converter 3.0)    129.5
```

Range ≈ **110–144 kg** from declared input ranges alone. The 35 kg target is not reached anywhere in this range. A Monte Carlo is not justified until the input distributions have evidence levels.

---

## 8. Unit and identity checks

- kWh × 1000 / (Wh/kg) = kg; all storage terms used this form.
- kW × kg/kW = kg for converter and genset terms.
- Efficiency product: `0.32 × 0.85 × 0.95 = 0.2584`; thermal input 38.7 kWh × 0.2584 = 10.0 kWh delivered.
- H2 LHV: `0.632 kg × 33.33 kWh/kg = 21.06 kWh`; `21.06 × 0.50 × 0.95 = 10.0 kWh`.
- Diesel: `4.02 L × 9.94 kWh/L = 39.96 kWh`; `39.96 × 0.263 × 0.95 = 10.0 kWh`.
- Self-check includes the independent identity `(10/eta) × eta = 10`; it is not only a band around the output.

---

## 9. Volume, heat, cost, lifetime

- **Volume:** the repository reports A1 52.2 L, C1 31.7 L, C2 21.3 L, all under 60 L. This screen did not recompute volume; it is not a Gate 2 pass.
- **Heat:** only a radiator mass allowance is included. Radiator area, coolant temperature, pump/fan power, and ambient sensitivity are not modeled here.
- **Cost:** no quotation exists. C1/H2 and C2/diesel are fuel-price-sensitive; no cost ranking is decision-grade.
- **Lifetime:** no cycle-life or replacement model in this screen. The 10-year M1 life is not tested.
- **E2 locators:** not yet present; most inputs are E1. `SOURCE_VERIFICATION.md` verifies DOI/title, not every page/figure.

---

## 10. What this screen establishes

1. The repository's A1 result is reproducible at the dominant-term level under its stated 175 Wh/kg basis and 1.25 packaging: ~118 kg.
2. The M1 35 kg target requires roughly **690–700 Wh/kg pack-level or ~865–870 Wh/kg cell-level** at 1.5 kg/kW and 10 kWh, with no margin, cooling, or 10-year degradation. The band is **510–691 Wh/kg pack** over 0.5–1.5 kg/kW. No such pack is demonstrated or purchasable as a system.
3. Under the repository's 300 W/kg **continuous** pack rating, A1's floor is ~40 kg at 0.5 h and ~118 kg at 8 h. The 8 h M1 mission cannot reach 35 kg; this is a model assumption, not a universal physical limit. A pulse-rated sensitivity (600–1,000 W/kg for 30 s) is required before treating the floor as universal.
4. C2 diesel is ~49–50 kg and fuel-limited above $0.40/kWh at $1.40/L.
5. C1 PEM is ~56 kg and fails H5 at $6/kg H2; it is a benchmark row, not a viable M1 candidate at current price.
6. B3 TPV store is 484–806 kg before emitter/cells/radiator and fails H4 (<1 kWh/kg).
7. Solar and fission are not M1 candidates; they belong to M2/M4 with a different boundary.

---

## 11. What this screen does not establish

- No transient dispatch; pulses are treated as energy and buffer mass.
- No volume, heat, cost, or lifetime closure.
- No supplier data; every mass is a screening or repository estimate.
- No independent verification yet.
- No safety or regulatory assessment.
- No architecture selection.

---

## 12. Gate 2 acceptance

**Gate 2 is not passed.** The screen is provisional.

- [x] Energy balance closed for each full M1 candidate; the supercapacitor row is buffer-only and is not counted as a source.
- [x] Converter, packaging, buffer, and radiator/structure included where applicable.
- [x] Unit checks and independent rounded-number energy identities performed.
- [x] Self-checks pass and are runnable (`python3 screening.py`).
- [x] Converter-mass and battery-basis ambiguities reconciled against the repository.
- [ ] Volume build-up at the same boundary.
- [ ] Heat rejection/radiator model with pump/fan power.
- [ ] Cost/LCOE scenario with quotes vs estimates.
- [ ] Lifetime/replacement check.
- [ ] E2 page/figure locators for every non-screening input.
- [ ] Independent reviewer confirms units and at least three calculations.
- [ ] Supplier data for the two closest candidates (Li-ion pack, diesel hybrid).

The gate may be accepted only after the unchecked items are complete.
