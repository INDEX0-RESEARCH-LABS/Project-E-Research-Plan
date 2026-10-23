# Project E — Bottleneck Map

**Version:** 0.1 (Gate 2/3)  
**Date:** 2026-10-23  
**Status:** screening analysis; no architecture selected  
**Method:** decompose each mission into mass, volume, heat, and cost; rank the constraint whose removal changes the system verdict most per unit of evidence cost  
**Calculator:** `limits.py`

---

## 1. The constraint tree

```text
MISSION (energy, power, duration, envelope, cost)
  |
  +-- SOURCE ......... fuel / reactant / nuclear / external heat
  |     +-- specific energy, availability, cost, emissions, regulation
  |
  +-- CONVERSION ..... engine / fuel cell / TPV / TEG / thermionic
  |     +-- efficiency (Carnot-limited), part-load, specific mass, startup
  |
  +-- STORAGE ........ battery / thermal / flywheel / supercap / H2 tank
  |     +-- specific energy, specific power, round-trip, cycle life, safety
  |
  +-- THERMAL ........ conduction, convection, radiation, insulation
  |     +-- waste heat, ΔT, area, pump/fan power, ambient
  |
  +-- POWER ELECTRONICS + CONTROL
  |     +-- kg/kW, efficiency, pulse rating, EMI
  |
  +-- STRUCTURE + ENCLOSURE + BOP
        +-- packaging factor, mounts, cabling, auxiliaries
```

Every mission sits at a different point on this tree. The error to avoid is optimising one branch while another branch is binding.

---

## 2. Ranking

Ranking is by **system leverage** (how much the mission verdict moves per unit of improvement), **evidence readiness** (can the unknown be resolved cheaply?), and **mission breadth**. It is not a ranking of scientific novelty.

| Rank | Bottleneck | Quantitative evidence | Type | Missions affected | Leverage | Cheapest decisive evidence |
|---:|---|---|---|---|---|---|
| **B1** | Storage specific energy | M1 needs 510–691 Wh/kg pack (638–864 cell); best credible 150–250 pack; M2 needs 1,112–1,127 pack | Fundamental materials + engineering | M1, M2, M5 | **Very high** | Supplier datasheets + 1–2 cell tests |
| **B2** | Source energy density and fuel logistics | Diesel 3.6 kWh/kg fuel at 30% vs Li-ion 0.15–0.25 kWh/kg pack; M2 battery needs 3,770 kg vs diesel ~165 kg | Fundamental source choice + engineering | M2, M1 | **Very high** | Paper comparison + fuel-price quotes |
| **B3** | Heat rejection | M4 10 kWe at 25% rejects 30 kW → 30 m² forced air, ~150 kg; M1 diesel 3.5 kW → ΔT 76 K in 60 L | Fundamental (conservation) + engineering (h, fins) | M4, M1-diesel, M3 | **High** | Thermal bench + CFD only after lumped model |
| **B4** | Converter specific mass | Real 30 kW units span **7.5 kg** (PM100 motor inverter) to **80 kg** (Deye 50 Hz hybrid). M3 needs 166 Wh/kg pack with the former, ≥840 with the latter. The 1.5 kg/kW assumption is 6× the PM100 | Measured, but load-type-dependent | M1, M3 | **High** | One pack datasheet; define M3's load |
| **B5** | Cost and duty cycle | M2 $50k capex = $1.14/kWh before fuel; M5 charging $0.10 > $0.08 target; at verified ₹95.20/L, M1 diesel is $0.385/kWh at 35%, $2,000 capex, 250 missions/y (capex ceiling $2,387), but $0.505 at $5,000; at 26.35%, fuel alone is $0.405 | Arithmetic + market | M2, M5, M1 | **High** | Mission redesign + price quotes |
| **B6** | Volume | M1 244 Wh/L required; pack 250–400 Wh/L; converter/BOP volume excluded | Engineering | M1 | Medium | Pack + converter volume datasheets |
| **B7** | Safety and regulation | Nuclear licensing, H₂ embrittlement/leak, Li-metal fire; binary pass/fail | Regulatory + engineering | M2, M1 | **Binary** | Regulatory pathway study; no experiment |
| **B8** | Lifetime and degradation | M1 needs ≥1,667 missions; M5 4,000 cycles; no cycle-life model yet | Engineering | M1, M5 | Medium | Vendor cycle data + accelerated test |
| **B9** | Materials supply and cost | Ir/Pt/III-V for TPV/electrolysers; Li and Ni supply; not binding at research scale | Engineering/economic | M4, M1 | Low near-term | Literature + quote |

---

## 3. The four bottlenecks that actually decide missions

### B1 — Storage specific energy

The mass equation is dominated by \((1+f)E/(\eta e_\text{cell})\). At M1, a 10% improvement in cell specific energy reduces system mass by ~7.5% (5.6 kg of 74.8 kg at 300 Wh/kg); a 10% converter improvement reduces it by ~1.5%. Storage is ~5× more leveraged than converter mass **once the converter is not the dominant term**.

But leverage is not feasibility. The required values are 2–4× the best credible pack. A 10% gain does not close a 3× gap. The decisive question is not “can we improve Li-ion by 10%?” but “is there any chemistry that reaches ~500–700 Wh/kg pack with acceptable cycle life and safety?” Current evidence says no; the hypothesis register keeps the question open (H1, H2).

### B2 — Source energy density and fuel logistics

At M2, the battery mass is ~3,770 kg against a 500 kg target. Diesel fuel plus a 5 kW genset is ~165 kg. The source, not the converter, decides M2. The same logic explains why M1 diesel is lighter than M1 battery (49 vs 118 kg) yet still misses 35 kg and loses on fuel cost and heat.

The source hierarchy is:

1. **Nuclear** — 22.8 GWh/kg fuel; system mass is engine, shield, radiator, regulation.
2. **Chemical fuel** — 3.6 kWh/kg fuel for diesel at 30%; 16.7 kWh/kg for H₂ at 50%, but tank mass cuts system value to 0.8–1.7 kWh/kg.
3. **Electrochemical storage** — 0.15–0.25 kWh/kg pack.
4. **Thermal storage** — ~0.1 kWh/kg usable.
5. **Electrostatic/electromechanical** — 0.006–0.1 kWh/kg.

A “compact core” that claims >1 kWh/kg system must use nuclear or chemical fuel. There is no fourth option in established physics. This is the single most important sentence in the bottleneck map.

### B3 — Heat rejection

Heat is conserved; it does not disappear with a smaller enclosure. Two regimes:

- **Forced air (terrestrial):** \(Q=hA\Delta T\). A 60 L box rejects ~0.9 kW at 20 K; a 10 kWe 25%-efficient generator rejects 30 kW, requiring ~30 m² and ~150 kg of radiator at 5 kg/m².
- **Radiation (vacuum/sealed):** \(q''=\varepsilon\sigma(T^4-T_0^4)\). At 350 K, 352 W/m²; at 800 K, 20,490 W/m². A low-temperature radiator is enormous; a high-temperature radiator is compact but drives materials and insulation.

Heat is the bottleneck that most often converts a “compact generator” claim into a non-compact system. It is also the one where a measured \(h\) and a real fin design can change the answer by 2×, so it is worth a bench test after the paper stage.

### B4 — Converter specific mass (the cheapest unknown to resolve)

The package uses 1.5 kg/kW. This is not a datasheet. It is 11.25 kg at 6 kW and 56.25 kg at 30 kW. At 0.5 kg/kW, M3 requires 186 Wh/kg pack — inside current premium Li-ion — while at 1.5 kg/kW it requires 355 Wh/kg, outside. **A single supplier datasheet can flip the M3 verdict.** That makes B4 the highest information-per-rupee item in the program.

The pulse-buffer trade is a trap:

- Converter rated at average 1.25 kW instead of 6 kW saves \(1.5(6-1.25)1.25 = 8.9\) kg.
- A 0.05 kWh supercapacitor buffer at 6 Wh/kg adds ~8.3 kg (9.3 kg with 90% round-trip).
- Net saving: **~0.6 kg**, or 0.5% of a 118 kg system.

The buffer only becomes worthwhile above ~13 Wh/kg supercapacitor (for a 5 kg net gain) or if it also removes a thermal transient penalty. H7 is therefore a negative result at current components, not a design option.

---

## 4. Bottleneck interactions

Solving one constraint moves the binding constraint. This is why single-component claims are misleading.

| If this improves… | …the next binding constraint becomes | Evidence |
|---|---|---|
| Pack reaches ~690 Wh/kg | **Volume**: 14.62 kWh at 300 Wh/L is 48.7 L of a 60 L envelope before converter/BOP; at 250 Wh/L it does not fit | Arithmetic |
| Converter falls to 0.5 kg/kW | **Heat and cost** for M3; **volume** for M1 | `limits.py` sensitivity |
| Nuclear mass falls to 100 kg/kWe | **Regulation, shielding, security, cost**; not a portable unit | N08/N13; regulatory study pending |
| TPV cell reaches 50% | **External heat source and 484–806 kg store** remain; TPV is a converter, not a source | S01; Gate 2 H4 |
| H₂ tank reaches 10 wt% | **Stack mass, H₂ price, leak safety**; C1 is still ~45–50 kg before margin | Gate 2 C1 |
| Supercap reaches 13 Wh/kg | **Converter pulse rating** becomes worth decoupling; still no mission-energy gain | `limits.py` buffer trade |
| Diesel efficiency reaches 35% | Fuel cost $0.40/kWh at $1.40/L — exactly at target before capital | Arithmetic L4 |
| Graphite store reaches 0.14 kWh/kg | Still 3–5× short of 1 kWh/kg; TPV store remains 300–600 kg | `limits.py` source table |

**No single improvement makes M1 pass.** M1 needs storage, converter, volume, and cost to improve together. That is a portfolio problem, not a hero-component problem.

---

## 5. Claims that fail once the full boundary is included

| Claim | What it omits | Result at full boundary |
|---|---|---|
| “10 kWh in 1 kg” | Chemistry | Needs 10,000 Wh/kg; ~40× best cell |
| “40% TPV = compact generator” | External heat, emitter, store, cooling | Cell result; store alone 484–806 kg for 10 kWh electric |
| “Lightweight H₂ tank” | Stack, BOP, H₂ price | 5 wt% tank is 12.6 kg for 0.63 kg H₂; C1 ~56 kg |
| “Supercap solves the pulse” | Buffer mass and converter saving | 8.3 kg buffer vs 8.9 kg converter saving; net 0.6 kg |
| “1 kWe nuclear is compact” | Shield, radiator, regulation | 100–1,000 kg/kWe concept range; no lawful portable path |
| “Solar plus battery is compact” | Area, mounting, MPPT, storage | 135.7 kg before mounting; ~4 m² panel |
| “LENR/zero-point” | Source and calorimetry | No reproducible net output; conservation violation if claimed |

---

## 6. Where to spend the next rupee

Ordered by expected information value per unit cost, not by excitement:

1. **Converter datasheet + one measured inverter (B4).** Resolves the assumption that flips M3. Cost: ₹0–50,000; time: days.
2. **Pack datasheet and one cell characterization (B1).** Converts 150–250 Wh/kg from E1 to E2; tests H1/H2 cheaply. Cost: ₹50,000–2,00,000; time: weeks.
3. **Lumped thermal model with measured \(h\) (B3).** Decides whether M4’s 30 kW waste heat is 75 kg or 200 kg. Cost: ₹0–1,00,000 (model + small bench); time: 2–4 weeks.
4. **Mission-definition repair (B5).** M2 and M5 targets are arithmetically inconsistent; fixing them costs nothing and prevents a false “failure.” Cost: ₹0; time: days.
5. **Nuclear regulatory paper study (B7).** High cost, long time, but it is the only path to >1 kWh/kg system at M2. Do it only if M2 is prioritised.
6. **LENR/over-unity (H8).** Zero spend until a specific, reproducible, calorimeter-verified claim is identified. A negative control is not a research program.

**Do not** start with a prototype, a cell purchase, or a nuclear partner. The cheapest three items above can change the mission ranking.

---

## 7. What would make this map wrong

- A measured pack at ≥500 Wh/kg with ≥1,000 cycles and safe failure would move B1 from “gap” to “near-feasible” for M1.
- A measured converter at ≤0.5 kg/kW would move M3 to “conventional feasible” and shift the program to M1/M2.
- A measured \(h\) above 100 W/m²K with a compact fin array would cut M4 radiator mass by ~2×.
- A verified nuclear unit at ≤100 kg/kWe with a lawful path would make M2 a systems/regulatory problem, not a physics problem.
- A replicated net-output anomaly would invalidate the source hierarchy and require a new branch; until then it is a negative control.

Each of these is a measurement, not an opinion. The map is designed to be revised by evidence.

---

## 8. Bottom line

- **M1 is storage-, volume-, and cost-bound simultaneously.** No known component closes it; the gap is 2–4×, not 10%.
- **M2 is mass-feasible with diesel; its binding term is engine life/replacement.** Batteries are impossible; diesel is 212 kg and $0.441/kWh at 26.35%, passing only with a ≤$295 replacement (or ≤$795 at 35%); fuel logistics, emissions, and cold start are unmodelled; nuclear is regulation-bound.
- **M3 is converter- and heat-bound.** It is the closest to conventional feasibility and the most sensitive to a missing datasheet.
- **M4 is converter-capex-bound.** The radiator is 13–26 m² and 39–79 kg; a commercial 10 kW Stirling is $14–18.5/W against a $1/W target. The external heat price is also undeclared.
- **M5 is electricity-price- and DoD-bound.** 170 Wh/kg at 100% DoD (189 at 90%); 5,475 cycles; $0.144/kWh at $0.10 charging, needing ≤$0.043. The technology exists; the power price decides it.

The highest-leverage scientific question is not “which battery is best?” It is: **is there a source-and-conversion pair that reaches >1 kWh/kg system at the mission’s power scale without a regulatory or thermal penalty?** Only nuclear and chemical fuels answer yes today. The program’s job is to establish whether either can be made compact, safe, and lawful — or to prove that neither can.
