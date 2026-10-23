# M2 closure: the diesel route is feasible only on a narrow engine condition

Status: **conditional pass at the screening boundary**, not a deployable design.
Date: 2026-10-23. All costs are per **delivered** kWh and include the 0.95 converter.
Evidence level: E1 (arithmetic reconstruction of the repo's C2 model), except engine
life/replacement, which is E1 with no supplier quote.

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

Sizing: 0.58 kW genset, 0.3 kWh buffer, 5 kW converter, 144.7 L fuel.

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
A real 1 kW diesel genset costs $500–$1,500, so this is optimistic.

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

## 6. Verdict

**M2 passes all four numeric targets with a conventional diesel genset only
under a narrow condition:**

- 26.35% generator and engine replacement ≤$295 at 10,000 h; or
- 35% generator and replacement ≤$795 at 10,000 h (≤$1,500 at 20,000 h).

At the model's $232 replacement it passes at $0.487; at a realistic $500–$1,000
it fails or is marginal. **M2 is the feasibility leader among M1–M5, but it is
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
