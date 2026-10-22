# Project E — Mission Matrix

**Version:** 0.2 (Gate 2)  
**Date:** 2026-10-23  
**Purpose:** define the reference missions, the common boundary, the metrics, and the pass/fail arithmetic so no candidate is compared on a different basis  
**Status:** provisional; M1 is the benchmark, M2–M5 are proposed; no mission is approved as the program definition

---

## 1. System boundary

For a **self-contained** candidate, the boundary includes:

- primary energy source or fuel;
- source containment (tank, reactor vessel, shielding, fuel handling);
- conversion stages;
- energy storage, if any;
- power electronics and converter;
- thermal management: coolant, pump/fan, radiator, insulation;
- startup, standby, control, and auxiliary power;
- structural packaging, mounts, enclosure, cabling;
- consumables for one declared mission;
- replacement items within the declared life.

Excluded only if explicitly declared:

- payload;
- spares beyond the declared mission;
- infrastructure external to the unit (grid, heat plant, refuelling station);
- decommissioning and disposal (reported separately);
- taxes, subsidies, financing.

For a **converter** (TPV, TEG, ORC, thermionic), the external heat source is outside the boundary only when the comparison is explicitly “conversion efficiency at a host facility.” The heat source cost, delivery, and availability must then be a separate line and must not be counted as free.

For a **storage** candidate, the charging source is outside the boundary during the mission, but charging efficiency and source cost are reported.

---

## 2. The mission set

| ID | Mission | Delivered energy | Average power | Peak | Targets | Life | Boundary note |
|---|---|---:|---:|---:|---|---:|---|
| **M1** | Portable pulse (benchmark) | 10 kWh / 8 h | 1.25 kW | 6 kW / 30 s every 10 min | ≤35 kg, ≤60 L, ≤$5,000, ≤$0.40/kWh | 10 y | self-contained; one mission fuel; no payload |
| **M2** | Long-duration remote | 360 kWh / 30 d | 0.50 kW | 5 kW | ≤500 kg, ≤1,000 L, ≤$50,000, ≤$0.50/kWh | 10 y | self-contained; fuel for 30 days; −20 to +40 °C |
| **M3** | High-power compact | 10 kWh / 1 h | 10 kW | 30 kW / 10 s | ≤100 kg, ≤150 L, ≤$20,000, ≤$1.00/kWh | 5 y | self-contained; pulse buffer included |
| **M4** | Stationary heat-to-power | 80 MWh/y (10 kWe × 8,000 h) | 10 kW | 10 kW | ≤$1/W, 20 y | 20 y | external heat declared but excluded; converter, cooling, grid interface included |
| **M5** | Bulk stationary | 4 MWh / 4 h | 1 MW | 1 MW | ≤25,000 kg, ≤40 m³, ≤$120/kWh, ≤$0.08/kWh | 15 y | grid-connected; charging cost included |

### 2.1 Mission energy is consistent at 10 kWh

The config's **1 kW continuous** is the base load. The 6 kW / 30 s pulse every 600 s adds 5 kW × 30/600 = **0.25 kW average**, so the mission is **8 kWh base + 2 kWh pulse = 10 kWh**, average **1.25 kW** (`dispatch.py:39–41`). The earlier “8 vs 10 kWh” flag (audit D16) is **withdrawn**; the arithmetic closes exactly. No M1 mass or pack-band number changes.

---

## 3. Per-mission closure at the screening boundary

All values are E1/A; see `SYSTEM_LIMITS.md` for the equations and `limits.py` for the run.

| Mission | Required pack (1.5 kg/kW) | Required pack (0.5 kg/kW) | Nameplate / envelope | Waste heat | Capex check | Binding constraint |
|---|---:|---:|---:|---:|---|---|
| M1 | 691 Wh/kg | 510 Wh/kg | 244 Wh/L | 0.16 kW battery; 3.5 kW diesel | 1,667 missions needed; 1/day feasible | **mass + volume + cost** |
| M2 | 1,127 Wh/kg | 1,112 Wh/kg | 526 Wh/L | ~1.4 kW diesel | $50k = $1.14/kWh capital alone | **source + cost arithmetic** |
| M3 | 355 Wh/kg | 186 Wh/kg | 97 Wh/L | ~1.1 kW continuous | 2,222 missions needed; 3/day feasible | **converter + heat** |
| M4 | n/a (generator) | n/a | n/a | 30 kW at 25%; 15 kW at 40% | $10k capex; radiator mass not priced | **heat rejection** |
| M5 | 256 Wh/kg | 242 Wh/kg | 146 Wh/L | ~111 kW at 90% path | charging $0.10 > $0.08 target | **electricity price + cost** |

**Reading the table:** M1 and M2 cannot be closed by known storage. M3 and M5 are close enough that a measured converter or pack could change the verdict. M4 is not a storage problem at all; it is a heat-rejection and heat-source problem.

---

## 4. Target consistency findings

These are arithmetic checks on the mission definitions, not technology claims.

1. **M2’s capex and LCOE targets are mutually inconsistent.** At 30-day missions over 10 years there are at most 122 missions. $50,000 capital over 122 × 360 kWh = 43,920 kWh is **$1.14/kWh** before fuel. To meet $0.50/kWh with zero fuel, capex must be ≤ **$21,960**. A nuclear unit will not be; a diesel genset might be, but its fuel is $0.536/kWh at $1.40/L. **M2 needs a revised target:** either capex ≤$25,000, life ≥20 years, or LCOE ≥$1.20/kWh.
2. **M5’s LCOE target is below its charging cost.** At $0.10/kWh grid charging, the target $0.08/kWh is already exceeded before capital. At $0.05/kWh charging plus $0.03/kWh capital, the result is ~$0.086/kWh. M5 is electricity-price-bound; no storage breakthrough fixes it.
3. **M1’s cost target is duty-cycle-bound.** At one mission/day, capital is $0.137/kWh and fuel $0.10 → $0.237/kWh, under target. At one mission/week, capital alone is $0.96/kWh. The mission must declare a duty cycle; “10 years” alone is not enough.
4. **M4’s “$1/W” excludes the heat source but not the radiator.** At 25% efficiency the radiator is ~30 m² and ~150 kg; at 40%, ~15 m² and ~75 kg. A $10,000 converter budget with an unpriced 150 kg radiator is not a system cost.

These findings are **proposed corrections for owner review**. They do not change any physics result and do not select an architecture.

---

## 5. Core metrics

| Metric | Definition | Unit | Notes |
|---|---|---|---|
| Delivered energy | Useful AC/DC energy at the load over the mission | kWh | includes pulse energy |
| Average power | Delivered energy / duration | kW | not the same as rated power |
| Peak power | Maximum sustained output over the declared pulse | kW | include converter and source limits |
| System mass | Dry mass + one mission fuel/consumable | kg | report dry and wet separately |
| System volume | External envelope, including radiator and insulation | L | no “component-only” volume |
| Specific energy | Delivered energy / system mass | Wh/kg | delivered, not stored |
| Energy density | Delivered energy / system volume | Wh/L | external envelope |
| Specific power | Peak power / system mass | W/kg | at declared pulse, including buffer |
| Power density | Peak power / system volume | W/L | external envelope |
| Overall efficiency | Delivered energy / primary source energy | % | product of all stages; include auxiliaries |
| Heat rejection | Waste heat at average and peak | kW | converter, storage, source |
| Radiator area | Heat rejection / flux | m² | state ambient, sink temperature, \(h\) |
| Parasitic power | Pumps, fans, controls, standby | kW | subtracted from delivered power |
| Lifetime | Cycles/years to end-of-life criterion | cycles, years | state replacement schedule |
| Capex | Unit + installation + first fuel | currency | separate from O&M |
| LCOE | Discounted cost / discounted delivered energy | currency/kWh | state discount rate, lifetime, utilisation |
| Evidence level | E0–E6 per parameter | label | no E2 without a source locator |

---

## 6. Efficiency chain

For a generation system:

\[
\eta_\text{overall} =
\eta_\text{source} \times \eta_\text{conversion} \times \eta_\text{storage}
\times \eta_\text{power electronics} \times (1 - \text{auxiliary fraction})
\]

For a storage system:

\[
\eta_\text{overall} = \eta_\text{charge} \times \eta_\text{discharge}
\times \eta_\text{converter} \times (1 - \text{self-discharge})
\]

For a thermal converter:

\[
\eta_\text{conversion} \le \eta_\text{Carnot} = 1 - \frac{T_\text{cold}}{T_\text{hot}}
\]

Do not equate Carnot with practical efficiency. A practical heat engine is a fraction of Carnot; a TEG has its own \(ZT\) relation; TPV is bounded by detailed balance and cell temperature.

---

## 7. Mass and volume accounting

\[
m_\text{system} = m_\text{source} + m_\text{converter} + m_\text{storage}
+ m_\text{thermal} + m_\text{power electronics} + m_\text{structure}
+ m_\text{fuel} + m_\text{consumables}
\]

\[
V_\text{system} = V_\text{source} + V_\text{converter} + V_\text{storage}
+ V_\text{thermal} + V_\text{electronics} + V_\text{structure}
\]

Rules:

- Apply one packaging factor to component mass/volume, not multiple times.
- Include radiator and insulation in both mass and volume.
- Include fuel for the declared mission; report dry mass separately.
- Do not count a battery’s cells as the pack; include packaging, BMS, cooling.
- Do not count a reactor core as the system; include shielding, reflector, radiator, control.
- Do not count a TPV cell as the system; include emitter, heat source, insulation, cooling.

---

## 8. Heat rejection

\[
Q_\text{reject} = P_\text{source} - P_\text{delivered} - P_\text{stored}
\]

For a steady generator, \(Q_\text{reject} \approx P_\text{source}(1-\eta_\text{overall})\).

**Terrestrial forced convection:**

\[
Q = hA\Delta T, \qquad A \approx 6V^{2/3}
\]

**Vacuum/sealed radiation:**

\[
Q = \varepsilon\sigma A(T_\text{rad}^4 - T_\text{amb}^4)
\]

State \(h\), emissivity, view factor, coolant temperature, and fan/pump penalty. Do not use a single “3 kg/m²” without a source and a sensitivity range. Do not apply Stefan–Boltzmann to a fan-cooled terrestrial unit, and do not apply a convection coefficient in vacuum.

---

## 9. Cost

\[
\mathrm{LCOE} =
\frac{\mathrm{Capex} + \sum_t \frac{\mathrm{O\&M}_t + \mathrm{Fuel}_t + \mathrm{Replacement}_t}{(1+r)^t}}
{\sum_t \frac{E_t}{(1+r)^t}}
\]

State:

- discount rate;
- lifetime and replacement schedule;
- utilisation (missions/year or hours/year);
- fuel price and delivery;
- capex source (quote vs estimate);
- currency and exchange-rate date;
- disposal/decommissioning, if any.

An E0 cost cannot win a ranking. A cost conclusion that depends on an E0 input is conditional.

---

## 10. Uncertainty and evidence

| Level | Meaning | Use |
|---|---|---|
| E0 | Assumption or unsourced estimate | sensitivity only; never a result |
| E1 | Engineering estimate with stated basis | preliminary design |
| E2 | Published/datasheet value with citation and locator | parameter input |
| E3 | Model verified against analytical/independent numerical check | comparative conclusion within model |
| E4 | Component measured on a bench by this project | component claim |
| E5 | Integrated system measured in a relevant environment | system performance claim |
| E6 | Independently replicated or field-validated | external claim |

For every metric, report value, range, evidence level, source, and whether it is measured, modelled, or assumed.

**Current status:** `SOURCE_VERIFICATION.md` verifies DOI/title/venue, not every page or figure. No parameter in this package is upgraded to E2 until a page/figure locator is added. The repository’s E2 labels are not adopted wholesale (audit D3).

No single number is a forecast. Sensitivity and scenario results are required for any decision.

---

## 11. Comparison rules

1. Same mission, same boundary, same ambient, same fuel/consumable count.
2. Same converter efficiency and mass treatment across candidates.
3. Same packaging factor; no candidate gets a free enclosure.
4. Same radiator model; no candidate gets a free heat sink.
5. Same lifetime and replacement assumptions; no candidate gets a free overhaul.
6. Same cost year and exchange rate.
7. A converter with external heat must declare the heat source separately.
8. A storage candidate must declare the charging source and efficiency.
9. A candidate cannot win by omitting a subsystem.
10. A candidate cannot win on a headline number without system mass, volume, heat, and cost.

---

## 12. Scorecard

Hard pass/fail before scoring:

- closed energy balance with a named source;
- no conservation violation;
- safety/regulatory path;
- all subsystems inside the boundary.

Score (100), for triage only:

| Dimension | Points | Rule |
|---|---:|---|
| System-level improvement vs incumbent | 35 | ≥1.5× on at least one axis; not worse than 0.8× on the others; measured > modelled > paper |
| Evidence quality | 25 | E2 without citation = 0; E3 = partial; E4/E5 = full |
| Mass and volume | 15 | full boundary; penalties for omissions |
| Efficiency and heat rejection | 10 | Carnot check; radiator and pump power |
| Cost and LCOE | 10 | quotations > estimates; E0 cannot win |
| Lifetime/manufacturability | 5 | cycle life, replacement, materials |

Penalties: −20 per omitted subsystem; −10 per unsupported headline; −10 for no independent check.

The scorecard is not a substitute for a gate. A high score cannot rescue a failed energy balance.

---

## 13. Mission–mechanism fit matrix

Legend: **✓** plausible at this mission; **~** conditional on a measured improvement; **✗** fails the screening bound; **—** not applicable; **N** negative control.

| Mechanism | M1 | M2 | M3 | M4 | M5 | Reason |
|---|:---:|:---:|:---:|:---:|:---:|---|
| M01 Li-ion | ✗ | ✗ | ~ | — | ✓ | mass at M1/M2; M3 depends on converter; M5 near-term |
| M02 Li-metal/solid-state | ~ | ✗ | ~ | — | ✓ | needs 500+ Wh/kg pack for M1; M5 plausible |
| M03 Li–S / Li–air | ~ | ✗ | ~ | — | ~ | cycle life and round-trip unresolved |
| M04 Supercapacitor | — | — | ~ | — | — | buffer only; 8.3 kg for 0.05 kWh |
| M05 Flywheel | — | — | ~ | — | — | buffer only; containment |
| M06 Diesel genset | ✗ | ~ | ~ | — | ✗ | M1 cost/heat; M2 mass OK, fuel cost; emissions |
| M07 PEM fuel cell | ✗ | ~ | ✗ | ~ | — | M1 56 kg; M2 tank mass; M4 needs H₂ |
| M08 SOFC | — | ~ | — | ✓ | — | stationary high-efficiency; reformer mass |
| M09 H₂ storage | ✗ | ~ | ✗ | ~ | — | 5 wt% tank; 10 wt% needed for M2 |
| M10 Fission/RTG | ✗ | ~ | ✗ | ~ | — | M2 mass/regulation; M4 heat source |
| M11 Fusion | ✗ | ✗ | ✗ | ✗ | ✗ | no net-electric compact path |
| M12 Solar PV | ✗ | ~ | ✗ | ~ | — | area/diurnal; M2/M4 with storage |
| M13 TPV | ✗ | ✗ | ✗ | ~ | — | external ≥1500 °C heat; store 484–806 kg |
| M14 TEG | ✗ | ✗ | ✗ | ~ | — | 5–8% at kW scale; radiator |
| M15 ORC/Stirling | — | ~ | ~ | ✓ | — | stationary heat engine; M2 niche |
| M16 Thermionic/AMTEC | — | ~ | — | ~ | — | life and efficiency unproven |
| M17 CAES/pumped hydro | ✗ | ✗ | ✗ | — | ✓ | grid scale only |
| M18 LENR/over-unity | N | N | N | N | N | no reproducible net output |
| M19 Free-piston/microturbine | ~ | ~ | ~ | — | — | multi-fuel compact generator; no measured kg/kW yet |
| M20 PCM thermal store | — | — | — | ~ | — | M4 store; 0.10–0.20 kWh/kg usable |

The matrix is a screening aid, not a selection. A “✓” means “not excluded by the mass/heat/cost screen,” not “demonstrated.”

### 13.1 Mission ranking

Ranked by **plausibility of a meaningful improvement**, not by ambition alone. “Improvement” means ≥1.5× system specific energy or power, or ≥30% LCOE, at the full boundary.

| Rank | Mission | Plausibility | Potential improvement | Evidence readiness | Why |\n|---:|---|---|---|---|---|\n| **1** | **M3** high-power compact | **High** | High (30 kW in 100 kg) | E1; converter missing | A conventional pack plus a measured converter may already pass; the decisive unknown is cheap |\n| **2** | **M4** stationary heat-to-power | Medium–high | High (efficiency and radiator) | E1; heat source external | Mature ORC/Stirling/SOFC physics; the binding term is engineering (radiator, heat exchanger) |\n| **3** | **M2** long-duration remote | Medium (diesel) / low (nuclear) | **Very high** (source) | E1; no fuel/regulatory data | Largest system-level gap; diesel is mass-feasible but cost/heat-limited; nuclear is regulation-bound |\n| **4** | **M5** bulk stationary | **High** (technology) | Low–medium (cost only) | E1; pack data available | Conventional storage already works; the target is electricity-price-bound, not physics-bound |\n| **5** | **M1** portable pulse | **Low** | High (35 kg) | E1; no 500+ Wh/kg pack | The hardest mass/volume/cost combination; keep as the ambition and the benchmark, not the first bet |\n\nThe ranking is provisional and evidence-driven: a converter datasheet can move M3 up or down; an H₂ price below $4/kg moves M2 up; a 500 Wh/kg pack moves M1 up.

---

## 14. What counts as a meaningful improvement

| Result | Label | Requirement |
|---|---|---|
| 10–30% better on one axis | incremental | not a breakthrough; useful only if cost and life hold |
| ≥1.5× system specific energy at equal power, safety, life, cost | meaningful | measured at E4/E5, full boundary |
| ≥2× system specific energy or specific power | **breakthrough candidate** | E5 plus independent replication (E6) |
| ≥30% lower LCOE with quotes | economic improvement | full LCOE, same duty cycle |
| A new source with a closed, replicated energy balance | **genuine breakthrough** | E6; no conventional explanation |
| A better conventional system with an omitted subsystem | **not a result** | rejected before scoring |

A 2× improvement in a cell is not a 2× improvement in a system. The claim must be made at the mission boundary.

---

## 15. Acceptance for Gate 2

This document is accepted when:

- [ ] every candidate uses the same M1–M5 definitions;
- [ ] the M1 1 kW vs 1.25 kW inconsistency is resolved;
- [ ] M2 and M5 target inconsistencies are resolved or explicitly accepted;
- [ ] mass, volume, heat, and cost build-ups are explicit;
- [ ] every E2 value has a source locator;
- [ ] the scorecard is applied after hard pass/fail;
- [ ] an independent reviewer has checked the units and at least three calculations.

**Current status:** not accepted. The mission definitions are provisional; the target inconsistencies above are open.
