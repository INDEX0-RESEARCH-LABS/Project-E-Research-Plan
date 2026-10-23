# Liquid-fuel fuel-cell evidence — 3 kWe for 1 h in 2.16 L

**Version:** 0.2
**Date:** 2026-10-23
**Status:** primary-source check of manufacturer datasheets and peer-reviewed system papers; no purchase, no quote, no measurement by Project E. Version 0.2 withdraws the unverified Advent SereneU-5 126.5 L claim and corrects the H₂/methanol crossover.
**Question:** for a 3 kWe continuous generator, what is the smallest credible **complete-system** volume on a liquid fuel, and can any current or near-current system fit a **2.16 L external envelope** for 1 hour?
**Envelope:** 120 × 150 × 120 mm external, 2.16 L, surface 0.1008 m² (from `reports/E_MICRO_FEASIBILITY.md`)
**Companion:** `reports/E_MICRO_FEASIBILITY.md` (mechanism screen), `COMPONENT_EVIDENCE.md` (component datasheet method)

**Rule applied:** every number below is quoted from the linked source or labelled *calculated*. A missing value is written `unknown`. A module is never compared to the envelope as if it were a complete system; the scope of every volume is stated.

---

## 1. Verdict

**FAIL.** No documented current or near-current liquid-fuel system in this source set can deliver 3 kWe for 1 h inside a 2.16 L external envelope. The claim is limited to the products and papers found; U-13 records the market-coverage gap.

- The smallest **documented complete fuel-cell module** at ≥3 kWe on a liquid fuel is the **Serenergy HT-PEM reformed-methanol module at 81 L for 5 kW** (H3-5000 datasheet v2.0-0916, archived; current availability not verified). Derated to 3 kW and adding fuel and a start buffer, the complete system is **≈86 L — 40× the envelope**. Using the datasheet's external dimensions (266 × 483 × 702 mm ≈ 90 L geometric) gives **≈95 L (≈44×)**; the datasheet's 81 L is retained as the manufacturer's volume, and the external dimension is a sensitivity.
- The previously cited **Advent SereneU-5 126.5 L** figure is **withdrawn**: the cited URL now resolves to a Toyota Tsusho/SFC EFOY page, not an Advent product table. No unverified replacement is used.
- **DMFC is worse**: the best documented 1–2 kW units are 57–90 L/kW, so 3 kW needs **≈172–360 L (82–169×)**.
- **Reformed methanol with a low-temperature PEM stack and CO purification** is much worse: the measured IdaTech FCS1200 is 343 L for 1 kW (**479×** for 3 kW).
- **LPG reformer + PEM** is a stationary appliance: Plug Power GenSys 5C is ≈2.99 m³ (**1,387×**).
- **Diesel reformer + SOFC** has the best fuel volume (0.75–0.86 L for 1 h) but no 3 kW product. The most optimistic published design estimate is <100 L for 3–10 kW (**≈48×**, grade D); a demonstrated small unit ran at 3 W/L (**≈464×**).

**The decisive result is fuel-only.** At the best documented methanol system efficiency (42%, HT-PEM), 3 kWe for 1 h needs **1.63 L of neat methanol**; at DMFC efficiency (≈27%) it needs **2.54 L**. The envelope is 2.16 L, so at DMFC efficiency the fuel alone does not fit, and at HT-PEM efficiency it leaves **0.53 L** for a 3 kW reformer, stack, radiator, controls and packaging. No such plant exists at any scale.

**Credible relaxations:** envelope **≈86–95 L** for 3 kW/1 h (HT-PEM methanol), or a **~0.13 kW** continuous generator in 2.16 L if the best documented module power density is scaled down. Reducing duration does not help: the plant, not the tank, sets the floor.

---

## 2. Scope and method

A **complete system** is counted as: stack + reformer/CO cleanup + fuel tank + heat rejection + balance of plant (pumps, blowers, DC/DC, controls) + packaging. Startup battery is counted where the product requires one. Radiator/ducting outside the product enclosure is counted as a **known exclusion** and named, never silently dropped.

Three pathways were searched, as instructed:

| Pathway | What was searched | What exists |
|---|---|---|
| A. Direct methanol (DMFC) | 1–5 kWe commercial and demonstrated systems | Several commercial products, 125 W–2 kW per module; none above 2 kW per enclosure |
| B. Reformed methanol + PEM | Steam reforming (MSR) or autothermal reforming (ATR), with and without CO cleanup | Commercial HT-PEM modules (no CO cleanup needed) and LTPEM systems (with Pd filter or PROX) |
| C. LPG / diesel reformer + PEM/SOFC | Real products and government/peer-reviewed demonstrations | LPG: one 5 kW product line (Plug Power GenSys, 2003–2010). Diesel: DOE/DoD SOFC APU programmes, no product |

**Evidence grades** (as specified for this task):

| Grade | Meaning |
|---|---|
| **A** | Manufacturer datasheet or official product page, values read from the document |
| **B** | Peer-reviewed paper, government report, or independent test report |
| **C** | Vendor presentation, distributor listing, conference deck, or archived copy not on the manufacturer's current site |
| **D** | Estimate or design target, explicitly labelled as such by its source |
| **E** | Unverified; not used for any quantitative claim |

Mapping to the repository's E0–E3 scale: A ≈ E2–E3, B ≈ E2, C ≈ E1, D ≈ E0.

---

## 3. Source table

### 3.1 Commercial and demonstrated systems

| ID | Source (identity) | URL | Accessed | Values used | Scope | Grade |
|---|---|---|---|---|---|---|
| LF-01 | SFC Energy, *EFOY Pro 12000 Duo* product page | https://www.efoy-pro.com/en/efoy/efoy-pro-12000-duo/ | 2026-10-23 | 500 W; 32.0 kg; 640 × 441 × 310 mm (87.5 L); 0.9 L/kWh; −20…+50 °C; air-cooled DMFC | Complete DMFC generator, excl. fuel cartridge | A |
| LF-02 | SFC Energy, *EMILY 3000* datasheet | https://zeroalphasolutions.com/wp-content/uploads/2025/01/emily-3000datasheet.pdf | 2026-10-23 | 125 W nominal; 12.5 kg; 476 × 206 × 286 mm (28.0 L); ≤0.9 L/kWh | Complete military DMFC generator, excl. cartridge | A |
| LF-03 | DMFC Corporation, *Model T-3 Technical Specifications* | http://dmfc-corp.com/wp-content/uploads/2021/08/specification_Sheet_Model_T-3_Module-1.pdf | 2026-10-23 | 2.0 kW net; 95.2 kg; 29 × 16.5 × 23 in (180.3 L); 0.85 L/kWh; 48 V; 3–55 gal tank | DMFC module, excl. external tank | A |
| LF-04 | Oorja Protonics, *Direct Methanol Fuel Cells* (Methanol Institute deck) | https://methanol.org/wp-content/uploads/2016/06/Jim-Boettcher-Oorja-Fuel-Cells-Final.pdf | 2026-10-23 | OorjaPac Model 3: 1.5 kW; 79 kg; 30.5 × 12.75 × 13.5 in (86.1 L); air-cooled; 12 L tank; 12–16 h runtime | Complete DMFC unit incl. 12 L tank | C |
| LF-05 | Oorja Protonics, DOE HTAC presentation (2011) | https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/htac_nov2011_oorja_protonics.pdf | 2026-10-23 | 1.5 kW; system power density 17.5 W/L (2011) and 26.3 W/L (claimed next-gen); 8,000 h stack life | System-level claims | C |
| LF-06 | Serenergy, *H3 2500 / H3 5000* datasheet v2.0-0916 | https://datasheet.datasheetarchive.com/originals/crawler/serenergy.com/790675706e8ff3a6c39e5cf16df095bb.pdf | 2026-10-23 | 2.5/5 kW; 65/75 kg; 266 × 483 × 702 mm; **volume 81 L**; 0.8–0.9 L/kWh; 60/40 vol methanol/water; 0–100% turn-down; 40–50% LHV | Complete RMFC **module**: integrated reformer, stack, BOP, DC/DC; excl. tank, battery, ducts | A (archived manufacturer PDF) |
| LF-07 | Serenergy, *Methanol Fuel Cells* presentation (2015) | https://eu-ems.com/event_images/presentations/Mads%20Friis%20Jensen%20presentation.pdf | 2026-10-23 | H3-5000: 5 kW; 70 kg; 435 × 700 × 253 mm (77 L); 40–50% LHV; startup <0.2 kWh, preheat ~30 min; 4–5 kW heat | Same module, earlier variant | C |
| LF-08 | Sahlin, Andreasen & Kær, *System model development for a methanol reformed 5 kW HT-PEM system* (Aalborg University) | https://vbn.aau.dk/en/publications/system-model-development-for-a-methanol-reformed-5-kw-high-temper/ | 2026-10-23 | 5 kW; system efficiency 28–30%; startup ~45 min; reformer 240–300 °C | Bench system, not a product | B |
| LF-09 | Andreasen et al., *Control and experimental characterization of a methanol reformer for a 350 W HT-PEM system*, *Int. J. Hydrogen Energy* (2012) | https://doi.org/10.1016/j.ijhydene.2012.09.032 | 2026-10-23 | H3-350: 350 W; **279 × 204 × 595 mm (33.9 L)**; 13.7 kg; CO ~1% in reformate; stack 160–180 °C | Complete small RMFC module | B |
| LF-11 | Blue World Technologies, *CellPack Stationary* datasheet | https://www.blue.world/wp-content/uploads/2023/02/202301_CellPack-Stationary_data-sheet.pdf | 2026-10-23 | 5 kW; 38–40%; **845 × 1433 × 1354 mm (1,640 L)**; 530 kg; 0.55 L/kWh methanol + 0.36 L/kWh water; 15–20 min startup; 320 kWh fuel capacity | Complete outdoor cabinet **incl. large tank** | A |
| LF-12 | CHEM / ME2Power (formerly IdaTech ElectraGen ME), *Methanol Fuel Cell Systems* datasheet | https://www.chem-me2power.com/download/Product_download/Fuel_cell/DM/CHEM_FuelCell_EN.pdf | 2026-10-23 | 5 kW; 48 VDC; **1.35 × 1.15 × 1.76 m (2,732 L)**; 295 kg; 225 L tank; 40 h @ 5 kW; −5…+46 °C | Complete outdoor cabinet incl. 225 L tank | A (image-only PDF; values from indexed page text — see VT-06) |
| LF-13 | Plug Power *GenSys 5C* as installed, Sandia National Laboratories report | https://www.osti.gov/servlets/purl/940519 | 2026-10-23 | 5 kW PEM, LPG or NG reformer; **84 × 32 × 68 in (2.99 m³)**; ≈2,700 lb (1,225 kg); DI water 10 gal/day | Complete stationary appliance | B |
| LF-14 | Texas SECO / HyRadix / Plug Power, *LPG Fuel Processor Development and Fuel Cell Demonstration* (DOE report) | https://www.osti.gov/servlets/purl/878165 | 2026-10-23 | HyRadix Agilon ATR reformer **4.25 × 1.65 × 3.9 ft (0.77 m³)**; 13.3 SLPM LPG → 90 SLPM H₂; CO <1 vppm; integrated system 2.5–3.5 kW AC net; **max efficiency 19.5%**; startup 4 h (3 h claimed achievable) | Reformer + PEM system, measured | B |
| LF-15 | Fujikura, *1 kW Direct Methanol Fuel Cell System*, Technical Report No. 128 | https://www.fujikura.co.jp/research/pdf/technical-report/128/128_R1.pdf | 2026-10-23 | 1 kW; **600 × 440 × 330 mm (87.1 L)** excl. external fuel tank; 2–3 wt% anode methanol; 70–80 °C; "fuel utilisation up to 80%" (**not** electrical efficiency) | Complete DMFC system, excl. tank | B (manufacturer technical report) |
| LF-16 | Yamaha, *Development and Operation of a 1 kW DMFC Stack*, SAE/JSAE SETC 2009 | https://go.fisita.com/store/papers/SETC2009/20097031_final | 2026-10-23 | 1 kW stack; **overall system efficiency 30% max** at 20 A; 1,500 h DSS operation | Stack + system | B |
| LF-17 | Nölke, *Entwicklung eines Direkt-Methanol-Brennstoffzellensystems < 5 kW*, Forschungszentrum Jülich | https://juser.fz-juelich.de/record/58931/files/Energietechnik_64.pdf | 2026-10-23 | 1,230 W net DMFC scooter system; **system efficiency 18.8%**; 1.7 kW stack at 110 W/kg; DOE 2007 target 200 W/L not met by any DMFC system in the survey | Demonstrated DMFC system | B |
| LF-18 | Chrenko et al., *Methanol fuel processor and PEM fuel cell modeling for mobile application*, *Int. J. Hydrogen Energy* 35 (2010) 6863 | https://hal.science/hal-02615343/document | 2026-10-23 | IdaTech FCS1200: 1 kW, 48 V; **700 × 790 × 620 mm (343 L)**; ≈100 kg; **efficiency 25.12%**; Pd H₂ filter passes <50% of H₂; 110 W auxiliaries | Complete LTPEM + MSR + H₂ purifier system | B |

### 3.1a Source-verification status

- **Page-checked in this revision:** LF-03 (DMFC T-3 PDF), LF-06 (Serenergy H3-5000 archived PDF), and the former LF-10 URL. The Serenergy PDF confirms 5/2.5 kW, 81 L, 0.8–0.9 L/kWh and 60/40 methanol/water; its external dimensions imply ≈90 L geometric. The DMFC T-3 PDF confirms 2 kW, 29 × 16.5 × 23 in (180 L), 0.85 L/kWh and 48 V.
- **Withdrawn:** the former LF-10 (Advent SereneU-5, 126.5 L). The cited URL resolves to a Toyota Tsusho/SFC EFOY page, not an Advent product table. No 126.5 L claim appears in the verdict or tables.
- **Not independently page-checked:** all other rows are recorded as the source reports them; grades reflect source type, not a fresh page check. Grade C rows are claim-level and should not carry a verdict alone.
- **Current availability:** the 81 L H3-5000 is an archived 2016 datasheet. "Current" in this file means the source family, not a 2026 orderability claim.

### 3.2 Diesel and LPG reformer evidence

| ID | Source | URL | Accessed | Values used | Scope | Grade |
|---|---|---|---|---|---|---|
| LF-19 | Dobbs, Krause & Krumpelt (TACOM / Argonne), *Diesel-Fueled SOFC APUs for Heavy-Duty Vehicles* (2000) | https://www.osti.gov/servlets/purl/755881 | 2026-10-23 | 3–10 kW; c-ATR + spent-gas burner/air preheater; **"probably less than 100 litres"**; ~40% LHV | **Design estimate**, no build | B paper / **D volume** |
| LF-20 | Delphi, *SOFC Diesel APU Demonstration*, DOE FY2011 progress report | https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/progress11/xii_4_rosenblatt_2011.pdf | 2026-10-23 | 3–5 kW targets: ≥15 W/kg, **≥10 W/L**, ≥35% net; DPS3000 3.4 kW at 25%, 2.4 kW peak at 30% | Targets + design | B |
| LF-21 | Cummins Power Generation / Protonex, *Diesel-Fueled SOFC APU* final report (2010) | https://www.osti.gov/servlets/purl/1083010 | 2026-10-23 | Demonstrated 1.1 kW net DC; **power density 3 W/L** (target 8 W/L); 820 W AC | Measured small unit | B |

### 3.3 What was not found

- No **published price** for any of these systems. All vendors say "contact sales". The only number found is Blue World's EUDP **target** of 2,000 €/kW (LF-11 project report), which is a target, not a price. Recorded as `unknown`.
- No **stack-only kW/L** figure from any manufacturer in this set. Published data are W/kg (Jülich 110 W/kg, LANL 150 W/kg) or W/cm² (Delphi 0.45 W/cm²). Stack-only volume is `unknown` for every candidate; only module/system W/L is comparable.
- No **3 kW-class** reformed-methanol product from any vendor. The market floor is a 5 kW module; the 350 W module is the only smaller one.

---

## 4. Pathway A — direct methanol (DMFC), 1–5 kWe

| Product | Power | Volume | W/L | Mass | Fuel | Efficiency | Grade |
|---|---:|---:|---:|---:|---|---|---|
| SFC EMILY 3000 | 125 W | 28.0 L | 4.5 | 12.5 kg | ≤0.9 L/kWh | unknown (not stated) | A |
| SFC EFOY Pro 12000 Duo | 500 W | 87.5 L | 5.7 | 32.0 kg | 0.9 L/kWh | unknown | A |
| OorjaPac Model 3 | 1,500 W | 86.1 L | 17.4 | 79 kg | unknown | unknown | C |
| DMFC Corp Model T3 | 2,000 W | 180.3 L | 11.1 | 95.2 kg | 0.85 L/kWh | unknown | A |
| Fujikura 1 kW | 1,000 W | 87.1 L | 11.5 | unknown | unknown | 80% is **fuel utilisation**, not electrical | B |
| Yamaha 1 kW | 1,000 W | unknown | unknown | unknown | unknown | **30%** system | B |
| Jülich scooter | 1,230 W | unknown | unknown | unknown | unknown | **18.8%** system | B |

**Findings**

1. DMFC system power density is **5–17 W/L** across five independent products. The best is Oorja at 17.4 W/L. None approaches the 1,389 W/L the envelope requires.
2. The best route to 3 kW is **2 × OorjaPac Model 3 = 172 L**. The worst credible route is 2 × DMFC T3 = 361 L.
3. **Efficiency is not published** for the commercial DMFC products; the only measured figures are 18.8–30% (LF-16, LF-17). This matters for fuel volume (§7).
4. DMFC heat rejection is the hidden cost: at 27% and a 60–70 °C stack, 8.1 kW must be rejected at ΔT ≈ 45 K, requiring ≈3.6 m² of air-side area at h = 50 W/m²K — **36× the envelope surface**. The products are large because they are air-cooled at low ΔT.
5. The SFC EMILY 3000 is 28 L for 125 W. This is the correct scale reference for "a DMFC in a small box": it is **13×** the envelope and delivers **4%** of the required power.

---

## 5. Pathway B — reformed methanol + PEM

### 5.1 HT-PEM with integrated steam reformer (no CO cleanup)

HT-PEM (PBI/phosporic acid) tolerates 1–3% CO, so the reformer needs **no WGS/PROX stage**. This is the architectural reason it is the smallest liquid-fuel system.

| System | Power | Volume | W/L | Mass | η (LHV) | Startup | Grade |
|---|---:|---:|---:|---:|---|---|---|
| Serenergy H3-350 | 350 W | 33.9 L | 10.3 | 13.7 kg | unknown | unknown | B |
| Serenergy H3-5000 | 5,000 W | **81 L** | **61.7** | 75 kg | 40–50% | ~30 min preheat; <0.2 kWh | A |
| Serenergy H3-5000 (2015 variant) | 5,000 W | 77 L | 64.9 | 70 kg | 40–50% | ~30 min | C |
| Blue World CellPack (cabinet) | 5,000 W | 1,640 L (incl. 320 kWh tank) | 3.0 | 530 kg | 38–40% | 15–20 min | A |

**Volume-scope note:** the H3-5000 datasheet quotes **81 L**, but its external dimensions (266 × 483 × 702 mm) multiply to **≈90 L** geometric. The 81 L figure is the manufacturer's volume and is used in the main table; the geometric value is carried as a sensitivity (≈95 L total, ≈44×). Neither changes the verdict.

**Findings**

1. **81 L at 5 kW is the best documented liquid-fuel complete-system density found anywhere: 61.7 W/L.** Derated to 3 kW in the same enclosure it is 37 W/L. The envelope requires 1,389 W/L — a **22.5× gap at 5 kW, 37.5× at 3 kW**.
2. **No sub-81 L product was verified.** The earlier 126.5 L "current successor" claim is withdrawn because its source was not an Advent product table. The 81 L datasheet is archived; current orderability is unknown. A market scan is still needed before claiming "smallest anywhere."
3. All these are **modules**, not complete systems: they exclude the fuel tank, the start/peak battery (H3-5000 requires an external 48 V battery), and the hot-air/exhaust ducting (Ø80 mm hot air, Ø60 mm exhaust on the H3-5000). Their real installed volume is larger than the datasheet number.
4. The Blue World 1,640 L cabinet is **not** comparable to a module: it contains 320 kWh of fuel. It is listed to show the complete-station scale, and to warn against quoting cabinet volume as hardware volume.
5. Startup is 15–45 min depending on architecture (LF-07, LF-08, LF-11). For a 1 h mission this is a mission-level constraint, not just a parasitic loss: a cold system cannot deliver 1 h of output within the hour it is switched on.

### 5.2 LTPEM with steam reformer and CO cleanup

| System | Power | Volume | W/L | Mass | η | CO cleanup | Grade |
|---|---:|---:|---:|---:|---|---|---|
| IdaTech FCS1200 (Ballard Nexa stack) | 1,000 W | **343 L** | 2.9 | ≈100 kg | **25.12%** measured | Pd membrane H₂ filter (<50% H₂ recovery); not WGS+PROX | B |
| Plug Power GenSys 5C (LPG ATR) | 5,000 W | 2,990 L | 1.7 | ≈1,225 kg | **19.5%** max measured | Desulfurisation + ATR + shift; CO <1 ppm | B |

**Findings**

1. Adding a **low-temperature** PEM stack forces CO cleanup. In the FCS1200 this is a palladium membrane that passes **less than 50% of the hydrogen**, and the measured system efficiency is **25.1%**. The box is **343 L for 1 kW**.
2. Three FCS1200 units for 3 kW = **1,029 L (479× the envelope)**. Even one unit is 159× the envelope for 1 kW.
3. The LTPEM route is not a candidate at any scale relevant to E-Micro. It is recorded because it is the only *measured* reformed-methanol + CO-cleanup system in the source set, and it quantifies the cost of the cleanup step.

---

## 6. Pathway C — LPG and diesel reformer systems

**LPG.** The only real 5 kW product found is the Plug Power GenSys 5C, demonstrated on propane by Sandia and in the Texas SECO/HyRadix programme.

- Complete appliance: 84 × 32 × 68 in = **2.99 m³**, ≈1,225 kg.
- Reformer module alone: **0.77 m³** (4.25 × 1.65 × 3.9 ft).
- Measured integrated efficiency: **19.5%** maximum, at 2.5–3.5 kW AC net.
- Startup: **4 h** measured (3 h claimed achievable after controls changes).
- CO <1 vppm after the fuel processor; sulphur removal is a consumable bed.

This is a stationary outdoor appliance, not a portable generator. It fails the envelope by **1,387×** and would fail a 1 h mission on startup alone.

**Diesel.** No product; three government programmes define the state of the art.

| Evidence | Power | Volume basis | W/L | η | Grade |
|---|---|---:|---:|---|---|
| Dobbs/Argonne design study (2000) | 3–10 kW | "<100 L" **estimate** | 30–100 | ~40% LHV | D |
| Delphi targets | 3–5 kW | ≥10 W/L target | ≥10 | ≥35% | B (target) |
| Cummins/Protonex demonstrated | 1.1 kW | 3 W/L measured | 3 | unknown | B |

**Findings**

1. Diesel has by far the best **fuel** number: 0.75–0.86 L for 3 kWh_e at 35–40%. Fuel is not the constraint.
2. The plant is the constraint. The optimistic design estimate (<100 L for 3–10 kW) is **≈48×** the envelope and is a paper study from 2000, not a build. The only measured small diesel SOFC APU ran at **3 W/L** — scaling that to 3 kW gives **≈1,000 L**.
3. **No 3 kW diesel reformer + SOFC product exists.** The programmes were truck APUs (idle-reduction), stationary, 3–5 kW, and were not commercialised.

---

## 7. Fuel-only calculation (the decisive check)

### 7.1 Constants

| Quantity | Value | Basis |
|---|---:|---|
| Methanol LHV | 19.9 MJ/kg = **5.528 kWh/kg** | standard thermophysical property |
| Methanol density | **0.792 kg/L** | standard |
| Methanol LHV, volumetric | **4.378 kWh/L** | calculated |
| 60/40 vol methanol/water mix | **2.627 kWh/L** | calculated (0.6 × 0.792 kg × 5.528 kWh/kg) |
| Diesel LHV | **9.94 kWh/L** | repository constant (`engineering/physics.py`), from the frozen benchmark |
| Propane LPG | **6.6 kWh/L** | 46.3 MJ/kg × 0.51 kg/L; standard property, grade D for this use |

**Consistency check on the methanol constants.** Serenergy quotes 0.8–0.9 L/kWh of 60/40 mix and 40–50% LHV. At 0.9 L/kWh the implied efficiency is 1/0.9 = 1.111 kWh_e per L ÷ 2.627 kWh/L = **42.3%** — inside the quoted band. The constants and the vendor's fuel figure are mutually consistent, so the 60/40 interpretation is correct for the HT-PEM products.

**DMFC interpretation.** A DMFC at 0.85 L/kWh of 60/40 mix would imply 44.8% efficiency, which no DMFC achieves. Interpreting 0.85–0.9 L/kWh as **neat methanol** gives 27–29%, matching the measured 18.8–30% (LF-16, LF-17). Therefore DMFC fuel figures are per litre of methanol, not per litre of mix. This is an inference and is flagged as VT-01.

### 7.2 Fuel volume for 3 kWe × 1 h = 3 kWh_e

| Pathway | η | Chemical energy | Neat methanol | 60/40 mix | Diesel | LPG |
|---|---:|---:|---:|---:|---:|---:|
| HT-PEM RMFC (best documented) | 42% | 7.14 kWh | **1.63 L** | **2.72 L** | — | — |
| HT-PEM RMFC (band top) | 45% | 6.67 kWh | 1.52 L | 2.54 L | — | — |
| LTPEM + MSR (measured) | 25.1% | 11.95 kWh | 2.73 L | 4.55 L | — | — |
| DMFC (inferred from 0.85 L/kWh) | 26.9% | 11.15 kWh | **2.54 L** | 4.23 L | — | — |
| DMFC (Yamaha measured) | 30% | 10.0 kWh | 2.28 L | 3.81 L | — | — |
| DMFC (Jülich measured) | 18.8% | 15.96 kWh | 3.64 L | 6.07 L | — | — |
| Diesel SOFC | 40% | 7.5 kWh | — | — | **0.75 L** | — |
| Diesel SOFC | 35% | 8.57 kWh | — | — | **0.86 L** | — |
| Diesel SOFC (Delphi achieved) | 25% | 12.0 kWh | — | — | 1.21 L | — |
| LPG ATR + PEM (measured) | 19.5% | 15.4 kWh | — | — | — | **2.33 L** |

### 7.3 What the envelope can hold

If the **entire** 2.16 L were fuel (no tank walls, no ullage, no hardware):

- neat methanol: 2.16 × 4.378 = **9.46 kWh** chemical → **1.42 h** at 45%, **1.32 h** at 42%, **0.85 h** at 27%;
- 60/40 mix: 2.16 × 2.627 = **5.67 kWh** → **0.79 h** at 42%.

**Consequence:** with the premixed 60/40 fuel that the HT-PEM products actually consume, a 2.16 L tank holds **48 minutes** of fuel for a 3 kW load, before any hardware is counted. With neat methanol at the best efficiency, it holds 1.3 h and leaves 0.53 L for the plant.

The conclusion does **not** depend on the fuel-figure interpretation: under every reading, the fuel alone consumes 75–125% of the envelope for a 1 h mission.

---

## 8. Complete-system volume comparison

### 8.1 Method

For each pathway:

```
V_total = V_module (documented) + 1.25 × V_fuel + V_start_buffer (2 L)
```

- `V_module` is the documented product volume and its scope is stated. No packaging factor is applied on top, because a datasheet enclosure is already packaged. This is deliberately generous.
- `1.25 × V_fuel` allows 25% for tank walls, ullage and fittings.
- `2 L` is a 0.2 kWh buffer at ≈100 Wh/L pack level, needed for the H3-5000's <0.2 kWh start and for load transients. Estimated (grade D).
- **Excluded and named:** external radiator/ducting, fuel cartridges larger than 1 h, water supply, and the fact that part-load efficiency on a 5 kW module at 3 kW is likely below the datasheet figure.

### 8.2 Results

| Pathway | Basis | V_module | V_fuel | Tank | Buffer | **V_total** | **× 2.16 L** | W/L at 3 kW |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **HT-PEM RMFC, H3-5000 (2016)** | 5 kW module at 3 kW | **81.0** | 2.70 | 3.38 | 2.0 | **86.4 L** | **40.0×** | 34.7 |
| HT-PEM RMFC, H3-5000 external dimensions | 266 × 483 × 702 mm geometric | 90.1 | 2.70 | 3.38 | 2.0 | 95.5 L | 44.2× | 31.4 |
| DMFC, 2 × OorjaPac Model 3 | 1.5 kW each | 172.2 | 2.70 | 3.38 | 2.0 | 177.6 L | 82.2× | 16.9 |
| DMFC, 2 × DMFC Corp T3 | 2.0 kW each | 360.6 | 2.70 | 3.38 | 2.0 | 366.0 L | 169.4× | 8.2 |
| LTPEM + MSR, 3 × IdaTech FCS1200 | 1 kW each | 1,029 | 2.73 | 3.41 | 2.0 | 1,034 L | 478.9× | 2.9 |
| LPG ATR + LTPEM, GenSys 5C | 5 kW appliance | 2,990 | 2.33 | 2.91 | 2.0 | 2,995 L | 1,386.5× | 1.0 |
| Diesel SOFC, design estimate (D) | <100 L for 3–10 kW | 100 | 0.86 | 1.07 | 2.0 | 103.1 L | 47.7× | 29.1 |
| Diesel SOFC, demonstrated class | 3 W/L at 1.1 kW | 1,000 | 0.86 | 1.07 | 2.0 | 1,003 L | 464.4× | 3.0 |
| **Target envelope** | — | — | — | — | — | **2.16 L** | **1.0×** | **1,389** |

### 8.3 Reading the table

1. The **best credible complete system is ≈86 L**: a reformed-methanol HT-PEM module (81 L documented) plus 1 h of fuel and a start buffer. That is **40×** the envelope. Using the datasheet's external dimensions (≈90 L geometric) gives **≈95 L, 44×**; the conclusion is unchanged.
2. The **best possible liquid fuel** for volume (diesel, 0.75–0.86 L) does not help, because its plant is 48–464× the envelope.
3. Even the **most optimistic paper estimate** in the literature (<100 L for 3–10 kW) is **48×** the envelope, and it is not a product.
4. The envelope's required power density is **1,389 W/L**. The best documented liquid-fuel module is **61.7 W/L at 5 kW** (37 W/L at 3 kW in the same box). The gap is **22.5–37.5×** — the same order as the volume ratio, as it must be.
5. **Stack-only comparison would be invalid and is not made.** No manufacturer publishes stack kW/L in this set, and the stack is not the binding component: the reformer, evaporator, burner, heat exchangers and DC/DC are inside the 81 L. A bare HT-PEM stack might be 5–15 L; that number would be meaningless against a complete-system envelope.

---

## 9. Heat rejection and startup

**Heat rejection at 3 kWe, 42% (best case):** waste heat = 3 × (1/0.42 − 1) = **4.14 kW**.

| Air-side h (W/m²K) | ΔT (K) | Area required | vs envelope surface (0.1008 m²) |
|---:|---:|---:|---:|
| 50 | 120 (160 °C stack → 40 °C ambient) | **0.69 m²** | **6.8×** |
| 100 | 120 | 0.35 m² | **3.4×** |
| 50 | 60 | 1.38 m² | 13.7× |

**DMFC at 27%, ΔT ≈ 45 K, h = 50:** 8.11 kW → **3.60 m²** (35.7× the envelope surface).

HT-PEM's 160–170 °C operating temperature is a genuine advantage (it roughly halves the radiator versus a 70 °C DMFC), but it does not close a 3.4–6.8× area gap. The H3-5000 datasheet's Ø80 mm hot-air and Ø60 mm exhaust connections confirm that the heat is ducted **out of** the module: the 81 L excludes the radiator/duct volume.

**Startup:** 15–20 min (Blue World), ~30 min preheat (Serenergy H3-5000), 45 min (Sahlin 5 kW bench), 4 h (LPG GenSys). For a 1 h mission, a cold start consumes 25–100% of the mission window. Any honest E-Micro concept must either run continuously or carry a battery that covers the start.

---

## 10. Price

`unknown` for every system. No manufacturer publishes a list price for these products; all pages say "contact sales". The only number in the source set is Blue World's EUDP project **target** of 2,000 €/kW (LF-11 project report), which is a development target, not a transaction price. It is not used in any calculation.

---

## 11. Verdict

| Criterion | Result |
|---|---|
| 3 kWe continuous, 1 h, liquid fuel, **complete system** | **FAIL** |
| Smallest credible complete-system volume | **≈86 L** (81 L HT-PEM RMFC module + 2.7 L fuel + 3.4 L tank + 2 L buffer) |
| Ratio to 2.16 L envelope | **40×** (≈44× on external dimensions; range 40–1,387× across credible pathways) |
| Best fuel-only case | 1.63 L neat methanol at 42%; **2.54 L at DMFC efficiency** |
| Best plant power density found | **61.7 W/L** (5 kW/81 L); 37 W/L at 3 kW |
| Required power density | **1,389 W/L** |
| Heat rejection | 4.14 kW needs 0.35–0.69 m² vs 0.1008 m² envelope surface |
| Confidence in the verdict | High. Five independent product families, several measured systems, and a fuel-only bound that is interpretation-independent. The weakest link is market coverage (U-13), not the arithmetic. |

**Verdict: FAIL for 3 kWe / 1 h in 2.16 L.** This is not a marginal call: the best candidate is 40× the envelope, and the fuel alone is 75–125% of it.

**Conditional alternatives** (not passes):

| Alternative | Condition | Volume |
|---|---|---|
| Reformed-methanol HT-PEM at 3 kW, 1 h | Envelope ≥ 86–95 L | ≈86–95 L |
| Liquid-fuel generator inside 2.16 L | Accept ≈**0.13 kW** continuous (81 L/5 kW scaled by volume) | 2.16 L |
| Short buffer, not a generator | Battery only, ~8–16 min at 3 kW (already in `E_MICRO_FEASIBILITY.md`) | 2.16 L |

**Why this differs from the H₂ result.** `E_MICRO_FEASIBILITY.md` (revision 0.2) finds **8.94 L** for PEM + 700 bar H₂ at 1 h, with a 3.75 L H₂ gas volume and a 0.5 L radiator. Liquid methanol shrinks the fuel volume to 1.6–2.7 L but grows the plant from ~3 L to 81 L. Using the report's assumptions, the rough volume curves are:

- H₂: **3.6 + 4.7 h L** (1 L stack + 1.5 L BOP + 0.4 L converter + 3.75 h L H₂ gas, ×1.25 packaging).
- Methanol: **83 + 3.4 h L** (81 L module + 2 L buffer + 1.25 × 2.7 h L fuel).

They cross at **≈61 h**, not 37 h: below that, compressed H₂ is smaller; above it, methanol wins. This crossover is rough and **not verdict-bearing**; it assumes the 5 kW module can be part-loaded at the same L/kWh and ignores the radiator/duct. For a 1 h mission, liquid fuel is the **worse** choice on volume, not the better one.

---

## 12. Unknowns

| # | Unknown | Why it matters | Status |
|---|---|---|---|
| U-01 | Whether DMFC "L/kWh" is neat methanol or 60/40 mix | Changes fuel volume by 1.67×; does not change the verdict (both exceed 2.16 L) | inference only |
| U-02 | Part-load efficiency of the 5 kW HT-PEM module at 3 kW | 0.8–0.9 L/kWh may be a full-load figure; part-load is likely worse | unknown |
| U-03 | Stack-only kW/L for any HT-PEM or DMFC stack | Needed only to show the plant, not the stack, is binding | unknown, not published |
| U-04 | SereneU-5 module-only volume | The 126.5 L claim was withdrawn; the cited URL was not an Advent product table | withdrawn, no replacement |
| U-05 | Blue World module-only volume | 1,640 L includes 320 kWh of fuel; module volume not published | unknown |
| U-06 | CHEM/ME2Power datasheet is image-only | Values came from indexed page text, not a text layer | page-check needed |
| U-07 | DMFC T3 dimensions | Datasheet says 29 × 16.5 × 23 in (180 L); a second vendor PDF says 34 × 19 × 25 in (265 L) | conflicting |
| U-08 | OorjaPac Model 3 availability and price in 2026 | Product may be discontinued; the deck is 2016 | unknown |
| U-09 | Whether the 81 L H3-5000 is still orderable | 81 L is an archived 2016 datasheet; current orderability is not established. The 126.5 L successor claim is withdrawn | unknown |
| U-10 | Radiator/duct volume for all modules | Excluded from every datasheet volume; makes real installs larger | unknown |
| U-11 | Cold-start energy and time at −20 °C | 1 h mission may be undeliverable in winter regardless of volume | unknown |
| U-12 | Price of every system | Gate 3/6 cannot start without it | unknown |
| U-13 | Whether any sub-81 L 3 kW HT-PEM module exists outside this source set | The claim "smallest credible" depends on market coverage | market scan needed |

---

## 13. Verification tasks

| ID | Task | Method | Closes |
|---|---|---|---|
| VT-01 | Resolve the DMFC fuel-unit ambiguity | Request the fuel specification and a measured fuel-consumption curve from SFC and DMFC Corp; or measure gravimetrically on a rented unit | U-01 |
| VT-02 | Get the part-load curve of a 5 kW HT-PEM module (3 kW point) | Written request to Advent (SereneU-5) and Blue World; ask for L/kWh at 25/50/75/100% load | U-02, U-09 |
| VT-03 | Obtain stack-only datasheets (kW/L, kW/kg, cell count, active area) | Request from Advent, Blue World, SFC; record as stack-only and never compare to the envelope | U-03 |
| VT-04 | Find a verified SereneU-5 product table | Locate Advent's own current datasheet; the previously cited URL was not an Advent table. Record volume scope with page locator | U-04 |
| VT-05 | Separate Blue World module volume from the 1,640 L cabinet | Request the CellPack module drawing; the 320 kWh tank must be excluded | U-05 |
| VT-06 | Page-check the CHEM/ME2Power datasheet | Render the PDF and transcribe the specification table with page locator | U-06 |
| VT-07 | Resolve DMFC T3 dimensions | Ask DMFC Corp for the current drawing; treat 180 L as provisional | U-07 |
| VT-08 | Confirm 2026 availability of OorjaPac Model 3 and the H3-5000/SereneU | Direct vendor enquiry; if discontinued, mark the 81 L figure as historical | U-08, U-09 |
| VT-09 | Measure the external duct/radiator volume of one HT-PEM module | From vendor installation drawing; add to the 81 L before any envelope claim | U-10 |
| VT-10 | Scan for a sub-81 L 3 kW liquid-fuel product | Search: Advent, Blue World, SFC, Bosch, Toshiba, Fujikura, DMFC Corp, Korean/Japanese telecom backup vendors; 12-month window | U-13 |
| VT-11 | Request budgetary quotes | One per pathway; record as quote, not list price | U-12 |
| VT-12 | Cold-start test data at −20 °C | Vendor data or test report; record time-to-power and energy | U-11 |

**Stop rule:** VT-10 is the only task that could overturn the verdict. Everything else refines the numbers by tens of percent, not by the 40× required. Run VT-10 before any CAD or packaging work.

---

## 14. Reproduce

The arithmetic in §7 and §8 is reproduced by this self-check (stdlib only):

```python
meoh = 19.9 / 3.6 * 0.792          # kWh per L neat methanol
mix = 0.6 * 0.792 * (19.9 / 3.6)   # kWh per L of 60/40 vol mix
assert abs(meoh - 4.378) < 0.01 and abs(mix - 2.627) < 0.01

def fuel_kwh(kwh_e, eta):
    return kwh_e / eta

assert abs(fuel_kwh(3, 0.42) / meoh - 1.63) < 0.02      # neat methanol
assert abs(fuel_kwh(3, 0.42) / mix - 2.72) < 0.02       # 60/40 mix
assert abs(fuel_kwh(3, 0.269) / meoh - 2.54) < 0.03     # DMFC
assert abs(fuel_kwh(3, 0.35) / 9.94 - 0.86) < 0.01      # diesel

# envelope-only fuel
assert abs(2.16 * meoh * 0.42 / 3 - 1.32) < 0.02        # hours at 42%, neat
assert abs(2.16 * mix * 0.42 / 3 - 0.79) < 0.02         # hours at 42%, mix

# complete system
def total(v_module, v_fuel):
    return v_module + 1.25 * v_fuel + 2.0

assert abs(total(81.0, 2.70) - 86.4) < 0.2
assert abs(total(81.0, 2.70) / 2.16 - 40.0) < 0.3
assert abs(3000 / 81 - 37.0) < 0.1
assert abs(3000 / 2.16 - 1389) < 2

# datasheet external dimensions as a sensitivity
geom = 0.266 * 0.483 * 0.702 * 1000.0
assert abs(geom - 90.1) < 0.5
assert abs(total(geom, 2.70) - 95.5) < 0.5
assert abs(total(geom, 2.70) / 2.16 - 44.2) < 0.3

# rough H2/methanol crossover, using the report's assumptions
# H2: 1.25 * (1 + 1.5 + 0.4 + 3.75h); methanol: 81 + 2 + 1.25 * 2.7h
h_cross = (81.0 + 2.0 - 1.25 * (1.0 + 1.5 + 0.4)) / (1.25 * 3.75 - 1.25 * 2.7)
assert abs(h_cross - 60.5) < 1.0
print("all checks pass")
```

---

## 15. What this does not prove

- It does not prove that a **new** liquid-fuel chemistry or a **non-reformer** direct-liquid architecture is impossible. It bounds the current and near-current reformer/DMFC families.
- It does not use a Project E measurement. Every efficiency is from a vendor datasheet or a peer-reviewed bench test; none is field-qualified.
- It uses **external** volumes. Internal volume is smaller after walls, insulation, clearances and connections.
- It assumes the documented module can be derated to 3 kW at the same volume. That is favourable to the candidate: a purpose-built 3 kW module would not be much smaller, since reformer and heat-exchanger volume scale with fuel flow, not just stack power.
- The 2 L buffer and 1.25 tank factor are estimates (grade D). Removing them entirely changes the best case from 86 L to 84 L — it does not change the verdict.

---

**Bottom line:** the smallest credible complete liquid-fuel system for 3 kWe is **≈86 L**, a reformed-methanol HT-PEM module plus fuel and a start buffer, at **40×** the 2.16 L envelope. The 2.16 L target is **not credible** for a 1 h continuous generator on any liquid fuel in the current or near-current evidence base. The only credible 2.16 L object remains a short-duration battery buffer.
