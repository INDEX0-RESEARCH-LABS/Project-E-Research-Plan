# M5 closure: a cheap-electricity mission with a mass/DoD double bind

Status: **fails the LCOE target at grid charging; mass is a knife-edge**.
Date: 2026-10-23. E1/A arithmetic; no pack or PPA quote.
Related: `MISSION_MATRIX.md` §3–4, `limits.py`.

## 1. Mission and boundary

| Item | Value |
|---|---|
| Delivered energy / duration | 4 MWh / 4 h |
| Power | 1 MW |
| Mass / volume | ≤25,000 kg / ≤40 m³ |
| Capex / LCOE | ≤$120/kWh / ≤$0.08/kWh |
| Life | 15 years, 1 cycle/day (5,475 cycles) |
| Boundary | grid-connected; charging cost included |

## 2. Mass: 160 Wh/kg at 100% DoD, 170 with the converter

Simple check: 4,000 kWh / 25,000 kg = **160 Wh/kg pack** at 100% depth of
discharge (DoD), before converter and BOS.

| Assumption | Pack required |
|---|---:|
| 100% DoD, 1.5 t converter (1.5 kg/kW) | **170 Wh/kg** |
| 100% DoD, 0.5 t converter | **163 Wh/kg** |
| 90% DoD, 1.5 t converter (4,444 kWh nameplate) | **189 Wh/kg** |
| 90% DoD, no converter credit | **178 Wh/kg** |
| 80% DoD, 1.5 t converter (5,000 kWh nameplate) | **213 Wh/kg** |

Current LFP packs are ~150–170 Wh/kg; NMC packs ~180–220 Wh/kg. So the
mission is feasible only at **100% DoD with a top LFP pack**, or at **90% DoD
with an NMC pack**. The earlier matrix entry (256/242 Wh/kg) was wrong: it
implied a ~15.6 t pack, inconsistent with 4 MWh / 25 t. Corrected in
`MISSION_MATRIX.md` §3.

## 3. Cycle life: 5,475 cycles at 90% DoD is the edge

At 1 cycle/day for 15 years, the pack sees **5,475 cycles**. LFP cycle life is
typically quoted as 4,000–6,000 cycles at 80–100% DoD; 5,475 at 90% DoD is at
the edge of the warranty, and at 100% DoD it is likely short. The double bind:

- 100% DoD: mass passes (160–170 Wh/kg) but cycle life is marginal;
- 90% DoD: cycle life is plausible but mass needs **178–189 Wh/kg**;
- 80% DoD: cycle life is comfortable but mass needs **213 Wh/kg**.

No current LFP product satisfies 90% DoD and 15 years at this mass. An NMC pack
could meet the mass but costs more and has shorter cycle life. **M5 is
DoD/cycle-life-bound, not just electricity-price-bound.**

## 4. Volume

4,000 kWh / 40 m³ = **100 Wh/L** simple cap; with 12.6 m³ for BOS, **146 Wh/L**.
LFP packs are 250–400 Wh/L, so volume passes. A 20-ft container (~33 m³) plus
inverter/HVAC is close to the 40 m³ cap but not binding.

## 5. Capex and LCOE

At $120/kWh and 4,000 kWh, capex is **$480,000** ($533,000 at 90% DoD).
Capital per delivered kWh over 5,475 cycles is **$0.022** ($0.024 at 90% DoD).

| Charging price | Delivered charge cost (0.95 charger × 0.90 RTE) | + capital + O&M | Total |
|---:|---:|---:|---:|
| $0.10/kWh | $0.117 | $0.022 + $0.005 | **$0.144 (fails)** |
| $0.05/kWh | $0.058 | $0.027 | $0.085 (fails) |
| $0.04/kWh | $0.047 | $0.027 | **$0.074 (passes)** |

The threshold is **≤$0.043/kWh charging** at 100% DoD (≤$0.041 at 90% DoD).
That is off-peak/wholesale or dedicated solar, not a typical retail tariff.
**No storage breakthrough fixes a $0.10 charging price:** even zero capex
leaves $0.117/kWh.

Reproduce: `python3 limits.py`; the M5 row in `MISSION_MATRIX.md` §3.

## 6. Verdict

**M5 fails the $0.08/kWh target at $0.10 charging by ~1.8×.** It can pass only
with **≤$0.043/kWh electricity** and a pack at **≥170 Wh/kg (100% DoD)** or
**≥189 Wh/kg (90% DoD)** with ≥5,475 cycles. It is a cheap-power mission, not a
compact-core mission, and it is not a storage-technology bottleneck.

## 7. Gate test

1. **Pack datasheet:** ≥180 Wh/kg, ≥6,000 cycles at 90% DoD, ≥$120/kWh, with
   warranty and augmentation schedule.
2. **Charging contract:** ≤$0.043/kWh delivered, 15-year term, or a solar PPA
   with a capacity factor that supports 1 cycle/day.
3. **Availability:** 1 MW / 4 h dispatch, round-trip efficiency, augmentation.

## 8. Kill criteria

- Charging >$0.05/kWh with no arbitrage → M5 fails $0.08.
- Pack <178 Wh/kg at 90% DoD → mass fails.
- Cycle life <5,475 at the chosen DoD → life fails or augmentation cost rises.
- Volume >40 m³ with BOS → envelope fails.
