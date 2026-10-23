# Project E — M1 Closure (Paper Design)

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** paper closure from the frozen repo model; **35 kg not closed**; no purchase, build, or test  
**Calculator:** `limits.py` §10; repo cross-check at `e75be96` (`diesel_hybrid`, `screen_architecture`)

---

## 1. Mission and the exact model result

M1: **10 kWh delivered / 8 h**, 1.25 kW average, 6 kW / 30 s pulse every 600 s, **≤35 kg**, ≤60 L, ≤$5,000, ≤$0.40/kWh, 10 years.

Running the repo model for this mission gives **C2 (diesel + buffer) = 50.3 kg**, efficiency **26.35%**, fuel **4.02 L/mission**. The exact breakdown:

| Term | Mass | Note |
|---|---:|---|
| Genset, 1.45 kW at 12 kg/kW | 17.4 kg | model assumption; no datasheet |
| Buffer, 0.3 kWh at 175 Wh/kg | 1.7 kg | |
| Fuel, 4.02 L (incl. 25% fuel-system allowance) | 4.2 kg | |
| Subtotal × 1.25 packaging | **29.1 kg** | |
| Radiator, 3.28 m² at 3 kg/m² | 9.8 kg | h = 10 W/m²K, ΔT = 40 K, 35% of waste to coolant |
| Converter, 6 kW at 1.5 kg/kW × 1.25 | 11.3 kg | |
| **Total** | **50.3 kg** | **15.3 kg over target** |

This is a **screened** mass: radiator and converter are included. The “~49 kg” in earlier drafts omitted one of the two 25% allowances on fuel; the difference is ~1.2 kg and does not change the verdict.

---

## 2. The 35% case

At 35% overall efficiency (a good small diesel, not the model’s 26.35%):

- Fuel falls from 4.02 L to **3.03 L** (fuel mass 3.14 kg).
- Waste heat falls, so the radiator shrinks to **2.20 m² / 6.6 kg**.
- **Total = 45.6 kg**, still **10.6 kg over 35 kg**.

So efficiency alone does not close M1. It removes 4.5 kg of the 15.3 kg gap.

---

## 3. The BOP ladder — how far can optimistic assumptions go?

Starting from the 35% case (45.6 kg):

| Step | Change | Total |
|---|---|---:|
| 35% baseline | — | **45.6 kg** |
| + PM100-class converter (7.5 kg vs 9.0 kg) | −1.9 kg | 43.7 kg |
| + forced convection, h = 50 W/m²K | −5.3 kg | 38.5 kg |
| + packaging 1.10 (vs 1.25) | −4.5 kg | **34.0 kg** |
| + 1 kg fuel tank | +1.0 kg | **35.0 kg** |

**The best-case stack lands exactly on 35.0 kg — with zero margin, and only if every assumption is simultaneously optimistic:** a 12 kg/kW genset, a 7.5 kg converter, forced convection, 1.10 packaging, and a 1 kg tank.

**Source-mass sensitivity (35%, PM100, forced, 1.10):**

| Genset specific mass | Total |
|---:|---:|
| 12 kg/kW (model assumption) | **34.0 kg** |
| 15 kg/kW | **38.8 kg** |
| 20 kg/kW | **46.8 kg** |

Commercial portable gensets are ~13–25 kg/kW (a 1 kW Honda EU1000i is 13 kg; a 2.2 kW EU2200i is 21 kg/kW). **No datasheet supports 12 kg/kW at 1.5 kW.** The genset is the binding term, not the radiator or the converter.

---

## 4. Verdict

**M1 at 35 kg is not closed.**

- At the model’s 26.35% and 12 kg/kW: **50.3 kg**.
- At a realistic 35% and 12 kg/kW: **45.6 kg**.
- At a realistic 35% and 15–20 kg/kW: **38.8–46.8 kg**.
- The only path to 35.0 kg is a **stack of four optimistic assumptions with zero margin**, and it still needs a tank.

**Honest statement:** *M1’s 35 kg is a knife-edge that requires a ≤12 kg/kW genset, forced-convection cooling, and 1.10 packaging all at once. At defensible portable-genset specific mass, M1 is a 39–47 kg system.*

---

## 5. Recommendation

1. **Re-scope the M1 mass target to ≤45 kg wet** (the 35% case), or keep 35 kg as a *stretch* target explicitly contingent on a ≤12 kg/kW genset.
2. **Make the genset the invention target.** The programme needs a 1.5 kW generator at **≤12 kg/kW (≤17.4 kg)**. That is the single number that decides M1; a 600 Wh/kg cell is a different, less likely route.
3. **Do not spend on cells for M1.** Even a 500 Wh/kg pack (10 kWh nameplate / 0.5) is 20 kg before BOP, and the 14.62 kWh nameplate at 500 Wh/kg is 29.2 kg — leaving 5.8 kg for converter, radiator, and packaging. The battery route is worse than diesel.
4. **Mass and cost pull in opposite directions.** The 45.6 kg system at 35% and $2,000 capex is **$0.385/kWh** (passes; capex ceiling $2,387). The 35 kg stack needs a PM100-class converter and forced cooling, pushing capex toward $5,000 and cost toward **$0.505** (fails). At the screened 26.35%, fuel alone is **$0.405**, above target before capital. M1’s 35 kg and $0.40/kWh targets are therefore **not simultaneously reachable** with a conventional genset. The invention must be both lighter and cheaper — a **≤12 kg/kW, ≤$1,000 genset**, not a better cell.
5. **Keep the fuel-cartridge concept:** a sealed cartridge removes the tank and refuelling hardware from the unit and is the natural way to hit a 35–40 kg *dry* mass.

---

## 6. What would change this verdict

| Evidence | Effect |
|---|---|
| A 1.5 kW genset datasheet at ≤12 kg/kW | Moves the best case from “stack of assumptions” to “measured” |
| A measured h ≥ 50 W/m²K for the enclosure | Removes 5.3 kg |
| A 10 kWh pack at ≥500 Wh/kg pack-level | Would make the battery route competitive at ~29 kg + BOP |
| A 45 kg target approved | M1 becomes closable at 35% with a conventional genset |

---

## 7. Sources and model notes

- Repo: `project-e` at `e75be96`, `src/project_e/simulation/architectures.py` (`diesel_hybrid`, `screen_architecture`), `configs/baseline.yaml`.
- `limits.py` §10 reconstructs the mass to ±0.2 kg of the repo (the repo’s dispatch gives 3.81 kW waste vs 3.74 kW here).
- Fuel is packaged twice in the repo (25% fuel-system allowance inside, then 25% system packaging). This is conservative; removing the inner allowance saves ~1.2 kg and does not change the verdict.
- The 12 kg/kW genset and h = 10 W/m²K are model assumptions, not measurements. Both are optimistic relative to commercial portables.
