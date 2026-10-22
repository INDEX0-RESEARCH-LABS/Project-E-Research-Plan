# Project E — Safety and Risk Register

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** active; reviewed at every gate  
**Rule:** a kill criterion is written before the test, not after the result.

---

## 1. Program-level risks

| ID | Risk | Likelihood | Impact | Early warning | Mitigation | Kill/stop trigger |
|---|---|---|---|---|---|---|
| R01 | The benchmark is mistaken for the mission | High | High | Team optimises only 35 kg / 6 kW / 8 h | Keep Track A separate; use M1–M5 | No mission diversity by Gate 3 |
| R02 | A converter is counted as a generator | Medium | High | “Free heat” or missing heat plant | Boundary register; source declaration | Any candidate without a declared source |
| R03 | A model is presented as a measurement | High | High | E0/E1 values in headline table | Evidence labels; independent review | Headline claim with no E2+ input |
| R04 | Cost estimates are treated as quotations | High | High | “$5,000” without quote date/vendor | Separate estimate/quote/unknown columns | Cost ranking built only on E0 |
| R05 | Safety/regulatory path is deferred | Medium | High | Shielding/H2/fire omitted | Gate 5 safety review | No containment plan for Li-metal/H2/nuclear |
| R06 | IP pressure distorts publication | Medium | Medium | “Patent before test” | Prior-art review; defensive publication where appropriate | Refusal to disclose a safety-relevant result |
| R07 | Sunk-cost continuation | High | High | “We already built it” | Pre-registered kill criteria | A failed criterion is rationalised, not recorded |
| R08 | Supplier data is unobtainable | Medium | Medium | Only marketing numbers | Buy samples; independent test | No datasheet or sample by Gate 3 |
| R09 | Nuclear/regulatory path is infeasible | High | High | No licensed site/partner | Early regulator consultation | No lawful path for M2 |
| R10 | The program finds nothing novel | Medium | Medium | All candidates are known | Negative result is acceptable | Evidence says stop; stop |
| R11 | Unit/bookkeeping error changes the ranking | High | High | Double packaging, omitted fuel, wrong basis | Independent identity checks; one boundary register | Any headline that cannot be rebuilt from its terms |
| R12 | Mission targets are internally inconsistent | High (already observed) | Medium | M2 capex/LCOE and M5 charging/LCOE fail their own arithmetic | Repair targets before Gate 3; record the change | A mission is scored against a target it cannot meet by construction |
| R13 | A screening assumption is treated as measured | High | High | 1.5 kg/kW converter, 1.25 packaging, \(h=50\) used as facts | Label A/E/F; obtain datasheets; show sensitivity bands | A verdict flips inside the stated assumption range and is not reported |

---

## 2. Hypothesis kill criteria

| ID | Hypothesis | Cheapest decisive test | Continue if | Kill/park if |
|---|---|---|---|---|
| H1 | Advanced Li-metal / solid-state pack | Literature + datasheet + 1–2 cells | ≥250 Wh/kg pack at C/2 (component milestone; M1 needs 510–691 Wh/kg pack); ≥500 cycles; ≤$400/kWh; contained failure | <250 Wh/kg pack; <500 cycles; >$400/kWh; uncontrolled thermal runaway |
| H2 | Li–S / Li–air | Literature + sample cell | ≥200 Wh/kg pack; ≥100 cycles; round-trip ≥60%; safe handling | <200 Wh/kg; <100 cycles; <60% round-trip; unsafe |
| H3 | Micro-fission Stirling for M2 | Paper + regulator/partner consultation | Lawful path; ≤500 kg per kWe; security/cost inside M2 | No lawful path; >500 kg/kWe; security cost prohibitive |
| H4 | TPV + thermal store for M4 | Paper + vendor data | ≥25% system; store ≥1 kWh/kg; ≤$1/W; 5,000 h | <20% system; <1 kWh/kg; >$1/W; <5,000 h |
| H5 | H2 fuel cell + advanced tank | Paper + stack/tank data | ≥45% LHV; ≥5 wt% system; ≤$4/kg H2; ≤35 kg M1 (60 kg is only an intermediate milestone) | <40% LHV; <5 wt%; >$4/kg; >35 kg M1 |
| H6 | Thermionic / AMTEC / advanced Stirling | Literature + lab | ≥15%; ≥5,000 h; ≤5 kg/kW | <15%; <5,000 h; >5 kg/kW |
| H7 | Flywheel / supercapacitor buffer | Paper + module test | ≥0.05 kWh in ≤5 kg; ≥90% round-trip; safe containment | >5 kg; <90%; containment unsafe |
| H8 | LENR / over-unity / zero-point | Pre-registered calorimetry + independent replication | Net output with closed balance and accounted source | No replication; calibration/background explains result |
| H9 | SOFC + reformer | Vendor data + 1–5 kW module test | ≥50% electrical; ≥5 y stack life; ≤$1/W; reformer ≤10 kg/kW | <50%; <5 y; >$1/W; reformer >10 kg/kW |
| H10 | Free-piston / microturbine | Literature + bench data | ≥30%; ≤3 kg/kW; multi-fuel; acceptable emissions | <20%; >5 kg/kW; unacceptable emissions/noise; <100 h |
| H11 | Phase-change thermal store | Coupon + cycling test | ≥0.15 kWh/kg usable; ≥20% system; heat exchanger ≤30% | <0.10 kWh/kg usable; <20% system; heat exchanger >30% |

### Current kill applications (Gate 2 v0.2)

| ID | Verdict | Basis |
|---|---|---|
| H3 | **Parked / unresolved** | 1 kWe concept range 100–1,000 kg spans the 500 kg/kWe criterion; midpoint 550 is not a measurement; no lawful path yet |
| H4 | **Killed for now** | Usable TPV store 0.06–0.10 kWh/kg, below the ≥1 kWh/kg criterion; B3 parked |
| H5 | **Parked at baseline price** | C1 uses $6/kg H2, above the ≤$4/kg criterion; C1 remains a benchmark row, not a viable M1 candidate |
| H7 | **Killed as stated** | 0.05 kWh supercap buffer is 8.3 kg, above the ≤5 kg criterion; A2 buffer is not viable |
| H1/H2/H6/H8 | Open / paper only | No decisive test has been run |
| H9 | Open / paper | No verified SOFC source yet; vendor stack data needed |
| H10 | Open / paper | No verified free-piston/microturbine source yet; E0/E1 |
| H11 | Open / paper | S09 supports PCM potential; no usable-density measurement |

A killed hypothesis is retained in `NEGATIVE_RESULTS.md`; it is not deleted.

---

## 3. Gate-specific stop rules

### Gate 0
- Stop if the owner treats the Arc Reactor as proof or requires a 35 kg result regardless of evidence.
- Stop if storage/conversion/generation are not separated.

### Gate 1
- Stop if no mission beyond M1 is accepted.
- Stop if sources cannot be verified.
- Stop if the landscape is a list of claims with no limits or disproof.

### Gate 2
- Stop if any candidate lacks a closed energy balance.
- Stop if system mass/volume/heat/cost are not built up at the same boundary.
- Stop if E2 values lack a locator.
- Stop if the 35 kg result is quoted without its assumptions.

### Gate 3
- Stop if no candidate has an independent reviewer and a quantified uncertainty.
- Stop if the “novel” combination is already published or patented without a new angle.

### Gate 4
- Stop if the model has no analytical limit check.
- Stop if verification against the repository fails without explanation.
- Stop if sensitivity changes the ranking.

### Gate 5
- Stop if the experiment cannot be made safe with the available facility.
- Stop if the measurement cannot distinguish success from artefact.
- Stop if the test is not the cheapest decisive one.

### Gate 6
- Stop if a scale-up claim rests on a single un-replicated test.
- Stop if cost/manufacturing/safety are not addressed.

---

## 4. Safety and regulatory red lines

- No unattended high-temperature (>600 °C) test without fire suppression and remote monitoring.
- No H2 test without detection, ventilation, and a pressure-relief review.
- No Li-metal cell abuse without a fire-rated enclosure and a written emergency plan.
- No nuclear material, RTG, or fission experiment in this program without a licensed partner, site, and regulator approval. Paper study only until then.
- No “over-unity” claim without a closed calorimeter and an independent witness.
- No SOFC or reformer test without CO/H₂ detection, ventilation, and a thermal shutdown.
- No free-piston/microturbine test outside a rated test cell with noise and emissions control.
- No PCM/salt test without corrosion, splash, and thermal-burn controls.
- No export-controlled technology transfer without legal review.

---

## 5. Review cadence

- Before each gate: update likelihood/impact and evidence level.
- After each gate: record what was killed and why.
- Annually: re-open parked entries only if new peer-reviewed evidence appears.
- Any safety incident: stop the program and review before restart.
