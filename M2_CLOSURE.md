# M2 closure: the diesel route is feasible only on a narrow engine condition

Status: **conditional pass at the screening boundary**, not a deployable design.
Date: 2026-10-23. All costs are per **delivered** kWh and include the 0.95 converter.
Evidence level: E1 (repo C2 model at dt = 60 s, run 2026-10-23: 211.8 kg, $721.58,
144.71 L, 25.03% delivered efficiency), except engine life/replacement, which is E1
with no supplier quote.

## 1. Mission and boundary

| Item | Value |
|---|---|
| Energy per mission | 360 kWh |
| Duration | 720 h (30 days) |
| Average load | 0.5 kW |
| Peak | 5 kW, duration **not defined** |
| Mass / volume | ≤500 kg / ≤1,000 L |
| Capex / LCOE | ≤$50,000 / ≤$0.50/kWh |
| Life | 10 years, 12.17 missions/year |
| Environment | −20 to +40 °C, self-contained, fuel for 30 days |

The mission is a **remote continuous power system**, not a compact core. Its
numeric targets are generous on mass and capex, which is why a diesel system can
pass them.

## 2. Baseline reconstruction (C2 diesel hybrid)

Repo model at dt = 60 s: 211.8 kg, $721.58 capex, 144.71 L fuel, 25.03% delivered
efficiency. Sizing: 0.58 kW genset, 0.3 kWh buffer, 5 kW converter. The 26.35%
figure is generator-only; 26.35% × 0.95 = 25.03% delivered.

| Case | Fuel | Mass | Capex | Capital | Fuel | O&M | Total before engine |
|---|---:|---:|---:|---:|---:|---:|---:|
| 26.35% generator | 144.7 L | **212 kg** | **$722** | $0.016 | $0.404 | $0.020 | **$0.440/kWh** |
| 35% generator | 108.9 L | 164 kg | $722 | $0.016 | $0.305 | $0.020 | **$0.341/kWh** |

Both pass 500 kg, 1,000 L, $50,000, and $0.50/kWh **before engine replacement**.
The tank is not separately massed; add ~10–15 kg for a 150 L tank, still <500 kg.
Volume from the model is ~250 L, dominated by fuel.

## 3. The binding term: engine replacement

The genset runs 720 h per mission × 12.17 missions/year = **8,760 h/year**;
**87,600 h** over 10 years. A small diesel at this duty is replaced several times.

The model's $232 replacement is the genset share of capex ($400/kW × 0.58 kW).
A real 1 kW diesel genset costs $500–$1,500, so this is optimistic. Secondary sources put a Kubota diesel at **4,500–5,500 h average, >10,000 h with maintenance** (S19, E0); the 5,000/10,000 h scenarios are the relevant range, and neither is a guarantee.

LCOE with engine replacement (10,000 h life unless stated):

| Replacement | 5,000 h | 10,000 h | 20,000 h |
|---:|---:|---:|---:|
| $232 | $0.534 | **$0.487** | $0.464 |
| $500 | $0.641 | $0.541 | $0.491 |
| $1,000 | $0.841 | $0.641 | $0.541 |
| $1,500 | $1.041 | $0.741 | $0.591 |

At **35% generator efficiency**, 10,000 h: $500 → $0.441; $1,000 → $0.541;
20,000 h with $1,500 → $0.491.

**Pass conditions for $0.50/kWh:**

- at 26.35%: replacement **≤ ~$295** at 10,000 h (or ≤$500 at 20,000 h);
- at 35%: replacement **≤ ~$795** at 10,000 h, or **≤$1,500** at 20,000 h.

A real $1,000 replacement fails at 26.35% and narrowly fails at 35% with a
10,000 h engine. **M2 is not a comfortable pass; it is a knife-edge on engine
life and replacement cost.**

**Fuel-price sensitivity.** The same 10,000 h engine, at three Delhi RSPs
(₹94.593871/USD, 2026-10-22):

| Delhi RSP | $/L | Fuel at 26.35% | Max replacement | Fuel at 35% | Max replacement |
|---:|---:|---:|---:|---:|---:|
| ₹80.00 | $0.846 | $0.340 | **$621** | $0.256 | **$1,041** |
| ₹95.20 | $1.006 | $0.404 | **$298** | $0.305 | **$797** |
| ₹110.00 | $1.163 | $0.467 | **$0** | $0.352 | **$561** |

A 15% fuel-price rise removes the 26.35% case entirely and cuts the 35%
threshold to $561; a 16% fall makes the 26.35% case pass with a $621 engine.
The pass is a two-variable knife-edge, not a robust result.

Reproduce with `python3 limits.py` §11.

## 4. Fuel logistics

| Item | Value |
|---|---|
| Fuel per mission | 144.7 L (26.35%); 108.9 L (35%) |
| Fuel per year | ~1,761 L (26.35%); ~1,325 L (35%) |
| Fuel per 10 years | ~17,610 L; ~13,250 L |
| Fuel cost per year | ~₹1.68 lakh (~$1,772) at ₹95.20/L |
| Fuel mass per mission | ~120 kg (26.35%); ~90 kg (35%) |
| Tank | 150 L, ~15 kg, refill every 30 days |

Fuel is **72% of the LCOE** at 26.35% ($0.404 of $0.440 before engine). The
system is a fuel-logistics system: 1,761 L/year must be delivered to a remote
site, with storage, spill control, and a 30-day buffer. This is not modelled.

## 5. Operability caveats (unmodelled, potentially disqualifying)

1. **5 kW peak duration is undefined.** The 0.3 kWh buffer at 90% DoD delivers
   0.27 kWh, i.e. **3.2 min at 5 kW**. If the 5 kW load lasts longer, the
   genset must be ≥5 kW; at 10% load its efficiency collapses and fuel cost
   exceeds $1/kWh. The mission must state the peak duration and event count.
2. **Cold start at −20 °C.** Diesel cloud point requires a winter blend or a
   fuel heater; a 0.6 kW genset has a small starter battery and glow plugs.
   A grid/block heater would break the “self-contained” claim. Not tested.
3. **Emissions and noise.** ~0.8–1.1 kg CO₂ per delivered kWh; 290–390 kg per
   mission; 3.5–4.7 t/year. NOx/PM without aftertreatment. 70–85 dB(A) at 1 m.
   Acceptable only outdoors, away from occupied spaces; indoor use is
   disqualifying. Not modelled in the repo.
4. **Engine at part load.** The 0.58 kW genset runs at ~91% of its rating on
   average, so part-load efficiency is not the issue; the issue is the 5 kW
   peak and the 8,760 h/year duty.
5. **Fuel price and supply.** ₹95.20/L is the Delhi RSP (PPAC, 2026-10-21);
   remote delivery adds cost and is not included.

## 5.1 Alternative: cycle-charging a standard 3–5 kW genset

The C2 baseline runs a 0.58 kW genset continuously (8,760 h/y). An alternative
is a standard 3–5 kW genset run at rated load for a few hours per day to charge
a 13.3 kWh buffer; the buffer serves the 0.5 kW average and the 5 kW peak.
This dispatch is **not** in the repo's `diesel_hybrid` model (which is
continuous).

Assumptions: 12 kWh/day delivered; 0.95 converter × 0.90 battery round-trip;
30 days; 10,000 h engine; $400/kW genset; 175 Wh/kg, $200–300/kWh battery;
radiator 10 W/m²K, ΔT 40 K, 3 kg/m²; 1.25 packaging.

| Genset | η | Battery $/kWh | Fuel L/30 d | Engine h/y | Mass kg | Capex $ | LCOE $/kWh |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 kW | 35% | 200 | 121 | 1,708 | 317 | 4,107 | **0.499** |
| 3 kW | 35% | 300 | 121 | 1,708 | 317 | 5,440 | 0.529 |
| 3 kW | 40% | 200 | 106 | 1,708 | 295 | 4,107 | **0.457** |
| 3 kW | 40% | 300 | 106 | 1,708 | 295 | 5,440 | 0.487 |
| 5 kW | 35% | 200 | 121 | 1,025 | 361 | 5,067 | 0.521 |
| 5 kW | 35% | 300 | 121 | 1,025 | 361 | 6,400 | 0.551 |
| 5 kW | 40% | 200 | 106 | 1,025 | 337 | 5,067 | 0.479 |
| 5 kW | 40% | 300 | 106 | 1,025 | 337 | 6,400 | 0.509 |

**What it buys:** the engine runs 1,025–1,708 h/y instead of 8,760, so a
10,000 h engine lasts 6–10 years and needs 1.0–1.7 replacements, not 8.8.
**What it costs:** a 13.3 kWh battery ($2.7–4.0k) and battery round-trip losses
(fuel 121 L vs 109 L at 35%). The net at 35%/$200 is **$0.499** — a marginal
pass, not a comfortable one. At 40%/$200 it is **$0.457–0.479**, a real pass.

**Genset capex is the second knife-edge.** Market listings put brand-name
8–20 kW diesel sets at **$775–$1,000/kW**; a generic 3 kW set may be
$400–$700/kW. The replacement term scales with the same capex, so the table’s
$400/kW assumption is optimistic:

| Genset $/kW | Capex | LCOE at 35% | LCOE at 40% |
|---:|---:|---:|---:|
| 400 | $4,107 | **0.499** | **0.457** |
| 700 | $5,007 | 0.555 | 0.512 |
| 1,000 | $5,907 | 0.610 | 0.568 |

At $700–$1,000/kW, **both 35% and 40% fail**. The pass needs a ≤$600/kW set at
40%, or ≤$400/kW at 35% — a narrow, unquoted corner.

**Caveats:** (1) the battery cycles 3,650 times in 10 years at 90% DoD, at the
LFP limit; a replacement adds ~$0.06/kWh and fails the 35% case; (2) the 5 kW
peak is battery-supported, but a 5 kW **continuous** load invalidates the 3 kW
genset; (3) 35% efficiency is still an assumption, not a quoted engine; (4) the
converter/charger is one 0.95 block; two conversions would cut efficiency and
raise fuel ~5%.

**Verdict on the alternative:** it does **not** turn M2 into a comfortable
pass. At the optimistic $400/kW and 35%/$200 it reaches $0.499; at realistic
$700–$1,000/kW it fails even at 40%. The continuous path with a $232–$500
engine is better ($0.387–$0.441) if such an engine exists. The alternative adds
two new knife-edges — genset capex and battery life — without removing the
efficiency one. **Recorded as a hedge, not a preferred architecture.**

## 6. Verdict

**M2 passes all four numeric targets with a conventional diesel genset only
under a narrow condition:**

- 26.35% generator and engine replacement ≤$295 at 10,000 h; or
- 35% generator and replacement ≤$795 at 10,000 h (≤$1,500 at 20,000 h).

At the model's $232 replacement it passes at $0.487; at a realistic $500–$1,000
it fails or is marginal. A cycle-charging alternative (standard 3 kW genset + 13.3 kWh
buffer) reaches $0.499 at 35%, $200/kWh, and $400/kW, but fails at realistic
$700–$1,000/kW genset prices even at 40%; it is a hedge, not a robust pass. **M2 is the feasibility leader among M1–M5, but it is
conditional, and its binding term is the engine, not the battery.** It is not a
compact-core mission: 212 kg and 250 L.

## 7. Gate 3 test (cheapest decisive experiment)

1. **Engine life and replacement.** Quote and test one 1 kW diesel genset at
   8,760 h/year equivalent; measure fuel at 10/50/100% load; obtain a
   replacement price and a rebuild interval. Pass if ≤$295 at 26.35% or ≤$795
   at 35% (10,000 h).
2. **Peak definition.** Measure the 5 kW load duration and event count; confirm
   ≤3 min per event or re-size the genset and recompute.
3. **Cold start.** −20 °C start with winter blend, no grid; record time and
   battery/glow-plug energy.
4. **Emissions/noise.** CO, NOx, PM, dB(A) at 1 m; siting envelope.

Estimated cost: one genset ($500–$1,500), fuel, a load bank, and a cold chamber
or a winter-site trial. This is cheaper than an M3 pack build and decides the
feasibility axis.

## 8. Kill criteria

- Replacement >$295 at 26.35% **and** >$795 at 35% (10,000 h) → M2 fails $0.50.
- Routine 5 kW peak >3 min → the 0.58 kW genset is invalid; re-size, and if
  fuel at part load exceeds $0.50, M2 fails.
- −20 °C start requires grid/block heat → “self-contained” fails.
- Emissions/noise cannot be sited → M2 is not deployable, even if the arithmetic
  passes.

## 9. What would change the verdict

- A 20,000 h engine at ≤$1,500 (35%) makes M2 a comfortable pass.
- A $300–$500 replacement at 10,000 h makes the 26.35% case pass.
- A 35% generator at ≤$800 replacement makes the baseline pass.
- A 5 kW continuous load invalidates the small-genset architecture.
- A fuel-cell or free-piston source with ≥20,000 h life and ≤$800 replacement
  would remove the engine term; that is a mechanism question, not a mission one.
