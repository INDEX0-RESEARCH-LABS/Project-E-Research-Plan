# Project E — Resource and Budget Plan

**Version:** 0.1  
**Date:** 2026-10-23  
**Currency:** Indian rupees (₹) primary; USD only for comparison  
**Rate:** ₹94.593871 per USD, 2026-10-22, `open.er-api.com/v6/latest/USD` (exchangerate-api; market API rate, **not** an RBI reference rate and **not** a quotation)  
**Status:** planning ranges only; no spend authorized; no supplier quotations obtained

---

## 1. What this budget is

A staged, fail-fast research budget. It buys evidence, not a device. Each tier is released only if the previous gate passes.

| Tier | Purpose | Gate | Range (₹) | USD equivalent at the stated rate |
|---|---|---|---:|---:|
| T0 | Paper, data, models, independent review | 0–3 | ₹0–₹2,00,000 | $0–$2,114 |
| T1 | Component characterization | 3–4 | ₹25,00,000–₹70,00,000 | $26,430–$74,000 |
| T2 | Bench prototype and integrated test | 4–5 | ₹55,00,000–₹1,30,00,000 | $58,145–$137,430 |
| T3 | Independent validation and field-relevant test | 6 | ₹1,06,00,000–₹2,56,00,000 | $1,12,060–$2,70,640 |

These are **ranges**, not quotations. A real budget requires vendor quotes, a facility agreement, and a safety review. The tier line items below include contingency and fall within the ranges above; cumulative if every tier is funded: about ₹1.86–4.58 crore.

---

## 2. T0 — paper, data, and review (₹0–2 lakh)

| Item | Estimate (₹) | Basis | Status |
|---|---:|---|---|
| Literature access / interlibrary | 0–15,000 | Open access + institutional access | Estimate |
| DOI/standards documents | 10,000–40,000 | Standards and paywalled papers | Unknown; quote needed |
| Independent reviewer honorarium | 40,000–70,000 | 2 reviewers, 2–3 days each | Estimate |
| Small consumables / printing | 5,000–15,000 | — | Estimate |
| Contingency 10% | — | — | — |

Most T0 work uses existing hardware and free software. The main cost is time, not cash.

---

## 3. T1 — component characterization (₹25–70 lakh)

| Line | Estimate (₹) | Assumptions | Status |
|---|---:|---|---|
| Li-ion cells, BMS, holders, fuses | 3,00,000–6,00,000 | 10 kWh class, sample cells, not a pack product | Estimate |
| Cell/pack test load and instrumentation | 5,00,000–12,00,000 | 6 kW load, DAQ, power analyzer, thermal sensors | Estimate; vendor quotes needed |
| Small diesel genset and load bank | 1,50,000–3,50,000 | 2–3 kW, used/new | Estimate |
| PEM stack + H2 tank/regulator/detection | 5,00,000–12,00,000 | 1 kW class; 5 wt% tank; safety hardware | Estimate; quotations mandatory |
| TEG/TPV sample modules and heater | 2,00,000–6,00,000 | Small-area samples, not a full converter | Estimate |
| Fire containment, ventilation, PPE | 2,00,000–5,00,000 | Li-metal/H2/diesel | Estimate; safety review |
| Labor (0.5–1 FTE-year) | 6,00,000–12,00,000 | India engineering salary range; part-time | Estimate |
| Contingency 20% | — | — | — |

**T1 stop rule:** do not buy the next line item until the previous test passes its kill criterion.

---

## 4. T2 — bench prototype (₹55–130 lakh)

| Line | Estimate (₹) | Assumptions | Status |
|---|---:|---|---|
| Integrated pack/converter/buffer | 12,00,000–25,00,000 | 10 kWh, 6 kW, instrumentation | Estimate |
| Thermal loop and radiator | 4,00,000–10,00,000 | Pumps, cold plate, sensors | Estimate |
| H2 or diesel fuel handling | 5,00,000–15,00,000 | Depends on candidate | Estimate |
| Enclosure, structure, cabling | 5,00,000–12,00,000 | 60 L class | Estimate |
| Test facility and safety | 5,00,000–12,00,000 | Fire/H2/ventilation | Estimate; facility quote needed |
| Labor (1–2 FTE-years) | 12,00,000–24,00,000 | — | Estimate |
| Independent test support | 3,00,000–8,00,000 | External lab | Unknown; quote needed |
| Contingency 20% | — | — | — |

---

## 5. T3 — independent validation (₹1.06–2.56 crore)

| Line | Estimate (₹) | Assumptions | Status |
|---|---:|---|---|
| Independent lab test | 20,00,000–50,00,000 | Environmental/performance | Unknown; quotations needed |
| Field-relevant trial | 30,00,000–80,00,000 | Site, permits, logistics | Unknown |
| Safety/regulatory review | 10,00,000–25,00,000 | Licensed assessor | Unknown |
| Labor (2–3 FTE-years) | 25,00,000–50,00,000 | — | Estimate |
| Contingency 25% | — | — | — |

T3 is not authorized by this document. It requires a passing Gate 5, a partner, and a separate budget approval.

---

## 6. Cost drivers and unknowns

| Driver | Why it matters | Current status |
|---|---|---|
| Cell chemistry and pack architecture | Dominant mass and cost at M1 | No supplier quote |
| Converter mass/power density | 11.25 kg at 6 kW in the baseline | E1 estimate; samples needed |
| H2 tank gravimetric fraction | 5 wt% is the baseline; 10 wt% would change C1 | No quote; literature pending |
| Diesel emissions/noise | May disqualify indoor/urban use | Not modeled |
| Nuclear shielding/security | May dominate M2 mass and cost | No partner; paper only |
| TPV emitter/cell life | Determines M4 viability | No vendor data |
| Indian import duty/freight | Can move landed cost 15–30% | Not estimated; quotes needed |
| Exchange rate | USD-denominated components | Fixed date only; sensitivity required |
| Labor and facility | Often underestimated | Estimate only |

---

## 7. Funding and approval

- No funding is committed.
- No purchase order, sample, lab booking, or experiment is authorized by this plan.
- T0 can proceed with existing resources and desk research.
- T1 requires: Gate 2 acceptance, a written test plan, a safety review, and three vendor quotations per major line.
- T2 requires: Gate 3 candidate selection, a facility agreement, and a costed safety case.
- T3 requires: Gate 5 pass, an independent lab, and a regulatory/ethics review where applicable.

---

## 8. Minimum credible next spend

If one spends anything, spend it on **measurement**, not a prototype:

1. A calibrated power analyzer and DAQ (or lab access).
2. A small load bank and thermal sensors.
3. One or two representative cells/stacks, not a full pack.
4. A fire-rated test enclosure.

This buys the data that can kill a candidate cheaply. It does not buy a headline.

---

## 9. Budget acceptance

- [ ] Quotes obtained for every line above ₹1 lakh.
- [ ] Landed cost includes duty, freight, and taxes.
- [ ] Exchange-rate sensitivity at ±10%.
- [ ] Safety and disposal costs included.
- [ ] Contingency is not used to hide scope.
- [ ] No spend before the relevant gate passes.
