# Project E — Mechanism Register

**Version:** 0.1 (Gate 1 draft)  
**Date:** 2026-10-23  
**Status:** working register; not a selection  
**Rule:** every entry declares its source, conversion pathway, best credible evidence, limit, system penalty, and the evidence that would kill it.

---

## 1. Register

*E1\* = DOI/title verified; page/figure locator pending. The repository E2 labels are not adopted without a locator.*

| ID | Mechanism | Category | Primary source / pathway | Best credible demonstrated position | Fundamental or practical limit | System penalty often omitted | Evidence | Opportunity | Disproof |
|---|---|---|---|---|---|---|---|---|---|
| M01 | Li-ion battery | Storage | Grid charge → electrochemical cell → converter | Mature; ~200–300 Wh/kg cell class; high round-trip; 3,000-cycle LFP class | Intercalation chemistry; pack mass; pulse power; thermal management | Pack packaging, cooling, BMS, converter, end-of-life | S04, N01; E1* | Higher-energy chemistries, cell-to-pack, pulse optimisation | Pack <250 Wh/kg at C/2 or <500 cycles |
| M02 | Li-metal / solid-state | Storage | Grid charge → Li-metal anode / solid electrolyte → converter | Laboratory cells; commercial scale limited | Interface resistance, dendrites, stack pressure, manufacturing | Packaging, thermal management, formation/yield, cost | N02; E1* | 300–400 Wh/kg cell; safer electrolyte | <250 Wh/kg pack, <500 cycles, unsafe failure mode |
| M03 | Li–S / Li–air | Storage | Grid charge (Li–S) or O2 intake (Li–air) → cell → converter | Li–S laboratory cells; Li–air mostly research | Cycle life, self-discharge, electrolyte/air handling, round-trip | O2 handling, electrolyte, thermal, replacement | Review pending; no verified Li–S/Li–air source | High theoretical cell energy | <200 Wh/kg pack, <100 cycles, round-trip <60% |
| M04 | Supercapacitor | Power storage | Grid/source → electrostatic double layer → load | Commercial; ~6 Wh/kg class pack; high power, long cycle life | Low energy density; self-discharge; voltage swing | Packaging, balancing, converter | S03; repository E1* | Pulse buffer, not mission energy | Buffer mass >5 kg for 0.05 kWh; no system gain |
| M05 | Flywheel | Power storage | Source → motor → rotor → generator → load | Commercial UPS/grid units; high power, long life | Low specific energy; containment; gyroscopic loads; self-discharge | Vacuum, bearings, containment, safety | N05; detailed data pending | M3 pulse buffer; not M1 energy | Buffer >5 kg for 0.05 kWh; containment prohibitive |
| M06 | Diesel genset | Generation | Diesel fuel → combustion → alternator → load | Mature; ~25–35% small genset at rated load | Part-load efficiency; emissions; noise; fuel logistics | Fuel reserve, enclosure, maintenance, converter | Repository E1*; no independently verified diesel source yet | Benchmark incumbent; hybrid buffer | Cannot meet emissions/noise or fuel logistics |
| M07 | PEM fuel cell | Generation | H2 → electrochemical oxidation → electricity + heat | Commercial; ~45–60% LHV system class | H2 storage, stack cost/mass, degradation, air/cooling | Tank, compressor, humidifier, converter, thermal | S11, N03, N04, N11; E1* | M2 remote; M1 only with light tank/stack | System >35 kg for M1; H2 >$4/kg |
| M08 | SOFC | Generation | Fuel → electrochemical oxidation → electricity + heat | Commercial stationary; high electrical efficiency with heat | High temperature, startup, seals, fuel processing | Insulation, reformer, heat exchanger, BOP | Detailed review pending | M4 stationary; hybrid with turbine | <50% electrical or <5 years stack life at scale |
| M09 | High-pressure / hydride H2 storage | Storage | H2 gas or hydride → fuel cell | 350–700 bar commercial; hydride niche | Gravimetric/volumetric density; compression energy; embrittlement | Tank, compressor, cooling, leak detection | N04, N11; E1* | 5–10 wt% system target | <5 wt% system or leak/embrittlement unsafe |
| M10 | Fission / RTG | Generation | U-235 fission or Pu-238 decay → heat → Stirling/TE → electricity | Kilopower 1 kWe ground test; 10 kWe design concept; RTG W-scale (RTG source pending) | Reactor + shielding + radiator + regulation; fuel is not the mass limit | Shielding, containment, security, licensing, decommissioning | N08, N13, N14; E1* | M2 long-duration remote | System >500 kg per kWe or no regulatory path |
| M11 | Fusion | Generation | Deuterium/tritium → plasma → heat → turbine | Experimental; net electricity not demonstrated | Tritium breeding, neutron damage, containment, facility scale | Shielding, blanket, tritium handling, maintenance | N09 | Long-term option only | No net-electric pilot; no compact path |
| M12 | Solar PV | Conversion | Sunlight → semiconductor → electricity | Commercial Si modules just under 25% (2026); 1 kW/m² standard irradiance | Diurnal/seasonal; area; temperature derating | Storage, mounting, inverter, cleaning | S05 (detailed balance); N10 (module efficiency) | M2/M4 with storage; not a compact core | Cannot meet the declared M2/M4 area and mass target |
| M13 | TPV | Conversion | External heat → emitter → TPV cell → electricity | 40% cell efficiency with a 1900–2400 °C emitter; system lower | External heat source; emitter/cell temperature; heat rejection | Heat plant, insulation, emitter, cooling, converter | S01; E1* | M4 stationary heat-to-power | System <20% or store <1 kWh/kg |
| M14 | TEG | Conversion | Heat → Seebeck → electricity | ZT≈1; ~5–8% system class | Carnot × material ZT; contact resistance; heat rejection | Heat exchangers, radiator, pump, converter | S02, S07; E1* | Small waste-heat recovery, not kW core | System <8% at kW scale or radiator >10 m² |
| M15 | ORC / Stirling | Conversion | Heat → working fluid/piston → generator | Commercial ORC at low-grade heat; Stirling niche | Carnot fraction; temperature; working fluid; seals | Heat exchanger, condenser, pump, radiator | S12; E1* | M4 bottoming/stationary | <15% at 200–400 °C or >5 kg/kW |
| M16 | Thermionic / AMTEC | Conversion | Heat → electrons/electrochemical → electricity | Laboratory devices; niche space | Cathode/electrode life; high T; low power density | High-T materials, seals, radiator | Detailed review pending | M4/M2 niche | <15% or <5,000 h life |
| M17 | CAES / pumped hydro | Storage | Grid electricity → compressed air/water → turbine | Grid-scale commercial | Site/scale; containment; efficiency; geography | Pressure vessel/reservoir, turbine, generator | S06, S08, S10, N06, N07 | Grid, not portable | Cannot fit 35 kg / 60 L |
| M18 | LENR / over-unity / zero-point | Negative control | Unknown | No reproducible peer-reviewed demonstration | Conservation violation if net output; calibration/background | Unknown | N12 (negative review) | None until a reproducible claim | Any net output without source; no replication |

---

## 2. Underexplored combinations worth a paper screen

These are **not** claims of novelty. They are combinations whose system-level value is not settled by the single-mechanism literature.

| Combination | Why it might matter | Critical unknown | Cheapest test | Kill criterion |
|---|---|---|---|---|
| Solid-state Li-metal + flywheel/supercap pulse buffer | High energy + high pulse power; decouple energy and power | Buffer mass and converter complexity | Paper + module data | Buffer >5 kg or round-trip <90% |
| Li–S + replaceable electrolyte/mechanical refuel | High theoretical energy; refuel instead of recharge | Cycle life, handling, cost | Literature + sample cell | <100 cycles or unsafe |
| Fission–Stirling + thermal storage for M2 | 24/7 remote power; storage handles load peaks | Shielding, regulatory, storage mass | Paper study | System >500 kg per kWe |
| TPV + latent/sensible store + ORC bottoming | Use high-grade heat twice; improve system efficiency | Emitter/cell life, heat exchanger mass | Paper + vendor data | System <25% or >$1/W |
| H2–metal hydride + PEM + recuperation | Lower pressure, compact storage; recover heat | Hydride mass, heat management, cycling | Literature + lab | System <5 wt% or <45% LHV |
| Solar PV + redox/thermal storage for M2 | External source with long duration | Storage cost/mass, area, maintenance | Paper | Area >10 m² or storage >200 kg |
| Thermionic/AMTEC + radioisotope/fission heat | Compact high-T conversion | Life, efficiency, materials | Literature + lab | <15% or <5,000 h |

---

## 3. Negative/closed entries

| Entry | Why closed for now | What would reopen it |
|---|---|---|
| TEG at kW scale for M1 | 5–8% efficiency implies large radiator and heat exchanger; portable mass fails | A measured ZT/device efficiency >2× and a <5 kg/kW system |
| Supercapacitor-only M1 | ~6 Wh/kg; 10 kWh would be tonnes | A >100 Wh/kg supercap with safe packaging |
| CAES / pumped hydro M1 | Site/scale/containment | A compact high-pressure vessel with acceptable safety and cost |
| Betavoltaics | µW–mW; not kW | A verified kW-scale beta-voltaic with shielding |
| Magnetic motors / perpetual motion | No reproducible evidence; conservation violation | A replicated, calorimeter-verified net output with accounted source |
| LENR / cold fusion | 2004 DOE review not conclusive; no accepted replication | A pre-registered, independent, full-energy-balance replication |

---

## 4. Register rules

1. A mechanism is not a source. Record the source separately.
2. A review is context, not a device performance quote.
3. A patent is prior art, not proof.
4. A laboratory result is not a product.
5. Every entry keeps its strongest counterargument and its disproof.
6. A closed entry is retained; it may be reopened only by new evidence.
