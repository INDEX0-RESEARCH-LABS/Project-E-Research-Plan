# Project E — System Boundaries and Metrics

**Version:** 0.1 (Gate 2 draft)  
**Purpose:** make every comparison use the same boundary, units, and evidence rules.

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

For a **converter** (e.g., TPV, TEG, ORC), the external heat source is outside the boundary only when the comparison is explicitly “conversion efficiency at a host facility.” The heat source cost, delivery, and availability must then be stated as a separate line and must not be counted as free.

For a **storage** candidate, the charging source is outside the boundary during the mission, but charging efficiency and source cost are reported.

---

## 2. Missions

| ID | Mission | Delivered energy | Peak | Targets | Boundary note |
|---|---|---:|---:|---|---|
| M1 | Portable pulse | 10 kWh / 8 h | 6 kW / 30 s every 10 min | ≤35 kg, ≤60 L, ≤$5,000, ≤$0.40/kWh, 10 years | Self-contained unit; one mission fuel; no payload |
| M2 | Long-duration remote | 360 kWh / 30 days at 0.5 kW | 5 kW | ≤500 kg, ≤1,000 L, ≤$50,000, ≤$0.50/kWh | Self-contained; fuel for 30 days; −20 to +40 °C |
| M3 | High-power compact | 10 kWh / 1 h at 10 kW | 30 kW / 10 s | ≤100 kg, ≤150 L, ≤$20,000, ≤$1.00/kWh, 5 years | Self-contained; pulse buffer included |
| M4 | Stationary heat-to-power | 10 kW electric, 8,000 h/year | 10 kW | ≤$1/W, 20 years | Heat source excluded but declared; converter, cooling, grid interface included |

M1 is the existing benchmark. M2–M4 are provisional. A candidate may be compared only at the same mission and boundary.

---

## 3. Core metrics

| Metric | Definition | Unit | Notes |
|---|---|---|---|
| Delivered energy | Useful AC/DC energy at the load over the mission | kWh | Includes pulse energy |
| Average power | Delivered energy / duration | kW | Not the same as rated power |
| Peak power | Maximum sustained output over the declared pulse | kW | Include converter and source limits |
| System mass | Dry mass + one mission fuel/consumable | kg | Report dry and wet separately |
| System volume | External envelope, including radiator and insulation | L | No “component-only” volume |
| Specific energy | Delivered energy / system mass | Wh/kg | Use delivered, not stored, energy |
| Energy density | Delivered energy / system volume | Wh/L | Use external envelope |
| Specific power | Peak power / system mass | W/kg | At declared pulse, including buffer |
| Power density | Peak power / system volume | W/L | External envelope |
| Overall efficiency | Delivered energy / primary source energy | % | Product of all stages; include auxiliaries |
| Heat rejection | Waste heat at average and peak | kW | Include converter, storage, source |
| Radiator area | Heat rejection / flux | m² | State ambient, sink temperature, h |
| Parasitic power | Pumps, fans, controls, standby | kW | Subtracted from delivered power |
| Lifetime | Cycles/years to end-of-life criterion | cycles, years | State replacement schedule |
| Capex | Unit + installation + first fuel | currency | Separate from O&M |
| LCOE | Discounted cost / discounted delivered energy | currency/kWh | State discount rate, lifetime, utilization |
| Evidence level | E0–E6 per parameter | label | No E2 without source |

---

## 4. Efficiency chain

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

For a thermal converter, check:

\[
\eta_\text{conversion} \le \eta_\text{Carnot}
= 1 - \frac{T_\text{cold}}{T_\text{hot}}
\]

and do not equate Carnot with practical efficiency. A practical heat engine is a fraction of Carnot; a TEG has its own ZT relation; TPV is bounded by detailed balance and cell temperature.

---

## 5. Mass and volume accounting

Minimum build-up:

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

## 6. Heat rejection

\[
Q_\text{reject} = P_\text{source} - P_\text{delivered} - P_\text{stored}
\]

For a steady generator, \(Q_\text{reject} \approx P_\text{source}(1-\eta_\text{overall})\).

Radiator sizing:

\[
A_\text{rad} = \frac{Q_\text{reject}}{h_\text{eff}(T_\text{rad}-T_\text{ambient})}
\]

State \(h_\text{eff}\), emissivity, view factor, coolant temperature, and fan/pump penalty. Do not use a single “3 kg/m²” without a source and a sensitivity range.

---

## 7. Cost

\[
\mathrm{LCOE} =
\frac{\mathrm{Capex} + \sum_t \frac{\mathrm{O\&M}_t + \mathrm{Fuel}_t + \mathrm{Replacement}_t}{(1+r)^t}}
{\sum_t \frac{E_t}{(1+r)^t}}
\]

State:

- discount rate;
- lifetime and replacement schedule;
- utilization (missions/year or hours/year);
- fuel price and delivery;
- capex source (quote vs estimate);
- currency and exchange-rate date;
- disposal/decommissioning, if any.

An E0 cost cannot win a ranking. A cost conclusion that depends on an E0 input is conditional.

---

## 8. Uncertainty and evidence

| Level | Meaning | Use |
|---|---|---|
| E0 | Assumption or unsourced estimate | Sensitivity only; never a result |
| E1 | Engineering estimate with stated basis | Preliminary design |
| E2 | Published/datasheet value with citation | Parameter input |
| E3 | Model verified against analytical/independent numerical check | Comparative conclusion within model |
| E4 | Component measured on a bench by this project | Component claim |
| E5 | Integrated system measured in a relevant environment | System performance claim |
| E6 | Independently replicated or field-validated | External claim |

For every metric, report:

- value;
- range or uncertainty;
- evidence level;
- source;
- whether it is measured, modeled, or assumed.

**Current status:** `SOURCE_VERIFICATION.md` verifies DOI/title/venue, not every page or figure. No parameter in the Gate 2 package is upgraded to E2 until a page/figure locator is added. The repository's E2 labels are not adopted wholesale (audit D3).

No single number is a forecast. Sensitivity and scenario results are required for any decision.

---

## 9. Comparison rules

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

## 10. Scorecard

Hard pass/fail before scoring:

- closed energy balance with a named source;
- no conservation violation;
- safety/regulatory path;
- all subsystems inside the boundary.

Score (100), for triage only:

| Dimension | Points | Rule |
|---|---:|---|
| System-level improvement vs incumbent | 35 | ≥1.5× on at least one axis; not worse than 0.8× on the others; measured > modeled > paper |
| Evidence quality | 25 | E2 without citation = 0; E3 = partial; E4/E5 = full |
| Mass and volume | 15 | Full boundary; penalties for omissions |
| Efficiency and heat rejection | 10 | Carnot check; radiator and pump power |
| Cost and LCOE | 10 | Quotations > estimates; E0 cannot win |
| Lifetime/manufacturability | 5 | Cycle life, replacement, materials |

Penalties: −20 per omitted subsystem; −10 per unsupported headline; −10 for no independent check.

The scorecard is not a substitute for a gate. A high score cannot rescue a failed energy balance.

---

## 11. Acceptance for Gate 2

This document is accepted when:

- [ ] every candidate uses the same M1–M4 definitions;
- [ ] mass, volume, heat, and cost build-ups are explicit;
- [ ] every E2 value has a source;
- [ ] the scorecard is applied after hard pass/fail;
- [ ] an independent reviewer has checked the units and at least three calculations.
