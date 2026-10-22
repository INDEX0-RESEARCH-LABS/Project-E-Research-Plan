# Project E — Research Landscape v0.1

**Status:** Gate 1 draft; not complete  
**Date:** 2026-10-23  
**Method:** verified DOI/URL records plus first-principles screening; page-level extraction and full-text review are pending for most entries. E1* means DOI/title verified but no page/figure locator, so the value is not upgraded to E2.  
**Companion:** `SOURCE_VERIFICATION.md`, `MECHANISM_REGISTER.md`

This document maps what is established, what is demonstrated, what is limited, and what is still unknown. It does not select an architecture.

---

## 1. Electrochemical storage

### 1.1 Li-ion

**Established principle.** Lithium ions shuttle between host electrodes; energy is stored in chemical potential. Round-trip efficiency is high; power and energy are separate design variables.

**Best credible demonstrated position.** Mature commercial cells in the ~200–300 Wh/kg class at cell level; pack-level values are lower because of packaging, cooling, and BMS. LFP has long cycle life and good safety; NMC/NCA has higher energy. The repository uses 175 Wh/kg pack, 300 W/kg, 92% round trip, 3,000 cycles — all E1* estimates that need supplier data.

**Limits.** Intercalation chemistry limits cell energy; pack mass and pulse power dominate the portable mission; thermal management and degradation are system-level constraints.

**System penalties often omitted.** Packaging, cooling, BMS, converter, end-of-life, and replacement.

**Open questions.** What pack-level energy/power can be bought at 10 kWh and 6 kW today? What is the real cycle life at pulse C-rate and 40 °C? What is the cost at low volume?

**Opportunity.** Cell-to-pack engineering, higher-energy chemistries, and a relaxed pulse requirement. Not a new source.

**Disproof.** A measured pack below 250 Wh/kg at C/2, below 500 cycles, or above $400/kWh would kill the M1 storage case.

**Evidence.** S04, N01; E1*.

### 1.2 Li-metal / solid-state

**Established principle.** A lithium-metal anode raises cell voltage/capacity; a solid electrolyte may suppress dendrites and improve safety.

**Best credible demonstrated position.** Laboratory cells and early commercial announcements; not a mature 10 kWh pack. Interface resistance, stack pressure, dendrite growth, and manufacturing yield remain.

**Limits.** Solid-state is not automatically safer or cheaper; sulfide/oxide electrolytes have processing and moisture sensitivity; lithium-metal cycling is not solved at scale.

**System penalties.** Formation/yield, stack pressure, thermal management, packaging, cost.

**Opportunity.** 300–400 Wh/kg cell could reduce pack mass; the system still needs a converter and thermal management.

**Disproof.** <250 Wh/kg pack, <500 cycles, or a failure mode that cannot be contained.

**Evidence.** N02; E1*. Page-level performance claims pending.

### 1.3 Li–S / Li–air

**Established principle.** Li–S uses conversion chemistry; Li–air uses O2 from air. Both have high theoretical cell energy.

**Best credible demonstrated position.** Li–S laboratory cells; Li–air mostly research. Cycle life, self-discharge, electrolyte/air handling, and round-trip efficiency are unresolved.

**Limits.** Practical pack energy is far below theoretical; Li–air needs clean O2/air management and is not a sealed battery; Li–S needs electrolyte and cathode engineering.

**System penalties.** O2 handling, electrolyte, thermal management, replacement, safety.

**Opportunity.** A refuelable Li–S or metal–air semi-fuel cell could decouple energy from power; this is a system architecture question, not just a cell chemistry.

**Disproof.** <200 Wh/kg pack, <100 cycles, or round-trip <60%.

**Evidence.** Review pending; no verified Li–S/Li–air source in this package.

---

## 2. Fuel-based conversion and hydrogen

### 2.1 Diesel genset

**Established principle.** Compression ignition; chemical energy → heat → mechanical → electrical.

**Best credible demonstrated position.** Mature; small gensets are ~25–35% efficient at rated load and worse at part load. The repository uses 28% rated, 0.35 part-load floor, 12 kg/kW — E1* estimates.

**Limits.** Part-load efficiency, emissions, noise, fuel logistics, maintenance.

**System penalties.** Fuel reserve, enclosure, maintenance, converter, emissions control.

**Opportunity.** Hybrid buffer lets a small genset run near its efficient point; this is the existing C2 result.

**Disproof.** Cannot meet emissions/noise or fuel logistics for the declared mission.

**Evidence.** Repository E1*; no independently verified diesel source yet.

### 2.2 PEM fuel cell

**Established principle.** H2 oxidation at anode, O2 reduction at cathode; proton-exchange membrane.

**Best credible demonstrated position.** Commercial systems in the ~45–60% LHV class; stack cost/mass and H2 storage dominate.

**Limits.** H2 storage (350–700 bar or hydride), stack degradation, air/cooling, humidification.

**System penalties.** Tank, compressor, humidifier, converter, thermal management.

**Opportunity.** M2 remote power with cheap H2 and a light tank; M1 only if tank and stack mass fall.

**Disproof.** System >35 kg for M1, H2 >$4/kg, or tank <5 wt%.

**Evidence.** S11, N03, N04, N11; E1*.

### 2.3 SOFC

**Established principle.** Solid-oxide electrolyte; high-temperature electrochemical oxidation; can use hydrocarbons.

**Best credible demonstrated position.** Commercial stationary systems; high electrical efficiency, with heat available for cogeneration.

**Limits.** High temperature, startup, seals, fuel processing, stack life.

**System penalties.** Insulation, reformer, heat exchanger, BOP.

**Opportunity.** M4 stationary; hybrid with a turbine for high efficiency.

**Disproof.** <50% electrical or <5 years stack life at scale.

**Evidence.** Detailed review pending.

### 2.4 Hydrogen storage

**Established principle.** Compressed gas, cryogenic liquid, adsorption, metal hydrides, chemical carriers.

**Best credible demonstrated position.** 350–700 bar commercial gas storage; hydride niche; liquid H2 for space.

**Limits.** Gravimetric and volumetric density; compression energy; boil-off; embrittlement; cost.

**System penalties.** Tank, compressor, cooling, leak detection, safety.

**Opportunity.** 5–10 wt% system target; metal hydride may reduce pressure but adds mass/heat management.

**Disproof.** <5 wt% system or unsafe leak/embrittlement.

**Evidence.** N04, N11; E1*.

---

## 3. Nuclear fission and radioisotope power

**Established principle.** Fission of U-235 releases ~200 MeV per event; decay of Pu-238 releases heat. Heat is converted by Stirling, thermoelectric, or other converters.

**Best credible demonstrated position.** NASA’s Kilopower/KRUSTY ground test demonstrated a 1 kWe fission–Stirling system, including failure tolerance; 10 kWe is a design concept, not a ground-tested unit. RTGs provide W-scale power for decades (source pending).

**Limits.** Reactor + reflector + shielding + radiator + control + regulatory system; fuel mass is not the constraint. Security, export control, and licensing dominate.

**System penalties.** Shielding, containment, security, decommissioning, launch/site integration.

**Opportunity.** M2 long-duration remote power; not M1 portable.

**Disproof.** System >500 kg per kWe, no regulatory path, or cost above M2 budget.

**Evidence.** N08, N13, N14; E1*.

**Open questions.** What is the real system mass for a 1 kWe unit with shielding? What regulatory path exists for a non-flight, terrestrial unit? What is the cost of security and decommissioning?

---

## 4. Fusion

**Established principle.** Light nuclei fuse, releasing energy; deuterium–tritium is the lowest-temperature route.

**Best credible demonstrated position.** Experimental plasmas; net electricity not demonstrated. The U.S. consensus roadmap targets a pilot plant, not a compact core.

**Limits.** Tritium breeding, neutron damage, containment, facility scale, maintenance.

**System penalties.** Blanket, shielding, tritium handling, remote maintenance.

**Opportunity.** Long-term, not near-term. Monitor; do not fund in this program.

**Disproof.** No net-electric pilot; no credible compact path.

**Evidence.** N09.

---

## 5. Solar photovoltaics

**Established principle.** Photons excite carriers across a semiconductor junction; detailed balance limits single-junction efficiency.

**Best credible demonstrated position.** Commercial Si modules just under 25% in 2026; 1 kW/m² standard irradiance. System efficiency lower.

**Limits.** Diurnal/seasonal availability; area; temperature derating; storage.

**System penalties.** Storage, mounting, inverter, cleaning, land/area.

**Opportunity.** M2/M4 with storage; not a compact core.

**Disproof.** Cannot meet the declared M2/M4 area and mass target.

**Evidence.** S05, N10.

---

## 6. Thermal and mechanical storage

### 6.1 Pumped hydro and CAES

**Established principle.** Potential energy of water or compressed air.

**Best credible demonstrated position.** Grid-scale commercial; site-constrained.

**Limits.** Geography, containment, scale, efficiency.

**System penalties.** Reservoir/pressure vessel, turbine, generator, permitting.

**Opportunity.** Grid, not portable.

**Evidence.** S06, S08, S10, N06, N07.

### 6.2 Flywheel

**Established principle.** Rotational kinetic energy; motor/generator.

**Best credible demonstrated position.** Commercial UPS/grid units; high power, long cycle life, low specific energy.

**Limits.** Containment, gyroscopic loads, self-discharge, cost.

**Opportunity.** M3 pulse buffer; not M1 energy.

**Evidence.** N05.

### 6.3 Thermal storage

**Established principle.** Sensible or latent heat.

**Best credible demonstrated position.** Commercial PCM/thermal stores; graphite sensible heat at high temperature.

**Limits.** Insulation loss, heat-transfer rate, containment, volume.

**Opportunity.** M4 TPV/ORC storage; B3's 0.28 kWh/kg is optimistic without standby loss.

**Evidence.** S08, S09.

---

## 7. Heat engines and direct conversion

### 7.1 TEG

**Established principle.** Seebeck effect; efficiency depends on ZT and temperatures.

**Best credible demonstrated position.** ZT≈1; ~5–8% system class. The repository computes 6.2% at 230/50 °C.

**Limits.** Carnot × material ZT; contact resistance; heat rejection.

**System penalties.** Heat exchangers, radiator, pump, converter.

**Opportunity.** Small waste-heat recovery; not a kW core.

**Disproof.** <8% at kW scale or radiator >10 m².

**Evidence.** S02, S07.

### 7.2 TPV

**Established principle.** A hot emitter radiates; a photovoltaic cell converts photons above bandgap.

**Best credible demonstrated position.** 40% cell efficiency with a 1900–2400 °C emitter; system lower. Repository uses 32% cell × 0.85 spectral × 0.95 output = 25.8%.

**Limits.** External heat source; emitter/cell temperature; heat rejection; cell cost.

**System penalties.** Heat plant, insulation, emitter, cooling, converter.

**Opportunity.** M4 stationary heat-to-power.

**Disproof.** System <20% or store <1 kWh/kg.

**Evidence.** S01.

### 7.3 ORC / Stirling

**Established principle.** Heat engine with a working fluid or piston.

**Best credible demonstrated position.** Commercial ORC for low-grade heat; Stirling niche.

**Limits.** Carnot fraction; temperature; working fluid; seals.

**Opportunity.** M4 bottoming/stationary.

**Disproof.** <15% at 200–400 °C or >5 kg/kW.

**Evidence.** S12.

### 7.4 Thermionic / AMTEC

**Established principle.** Thermionic emission or alkali-metal electrochemical conversion at high temperature.

**Best credible demonstrated position.** Laboratory/space niche; life and efficiency uncertain.

**Limits.** Cathode/electrode life, high temperature, low power density.

**Opportunity.** M4/M2 niche; detailed review pending.

**Disproof.** <15% or <5,000 h life.

**Evidence.** Pending.

---

## 8. Electromagnetic and electromechanical conversion

**Established principle.** Generators convert mechanical to electrical; motors do the reverse. Supercapacitors store charge electrostatically.

**Best credible demonstrated position.** Mature; power density high, energy density low for supercaps.

**Limits.** Energy density, converter, control, losses.

**Opportunity.** Pulse buffer; no new source.

**Disproof.** No system-level gain for the declared mission.

**Evidence.** S03, N05.

---

## 9. Negative and boundary cases

- **LENR / cold fusion:** 2004 DOE review found the evidence not conclusive; no accepted independent replication. The archival copy used here needs official DOE provenance confirmation. Not a funded track.
- **Over-unity / perpetual motion / zero-point:** no reproducible evidence; a net-output claim requires a closed energy balance and an accounted source. Screen out.
- **Patents:** prior art, not proof. A patent does not establish performance, safety, or cost.
- **Betavoltaics:** µW–mW; not kW.
- **Magnetic motors:** no credible physics.

---

## 10. What is still pending

1. Full-text/page-level verification of all performance numbers.
2. SMR and regulatory review.
3. Thermionic/AMTEC, metal-air, Li–S, SOFC detailed reviews.
4. Solar system mass and storage comparison.
5. Nuclear shielding/system mass.
6. Supplier quotations for cells, gensets, stacks, tanks, converters.
7. Negative-results register with primary sources.
8. Independent review of the screening calculations.

No entry in this landscape is a selection. The next step is Gate 2 completion: volume, heat, cost, lifetime, and page-level evidence for each candidate. A provisional Gate 2 screen already exists and is not yet accepted.
