# Project E — System Limits

**Version:** 0.1 (Gate 2/3 boundary document)  
**Date:** 2026-10-23  
**Status:** screening mathematics; **not** a design, measurement, quotation, or gate pass  
**Calculator:** `limits.py` (stdlib only); `python3 limits.py` prints every table below  
**Repository:** Project-E frozen at `e75be96`; this document is outside the tracked tree

---

## 1. Purpose and rules

This document derives the quantitative envelope **before** any architecture is chosen. It answers four questions:

1. What mass, volume, heat, and cost does each mission force, independent of technology?
2. Which limits are fundamental, which are engineering, and which are only artefacts of a screening assumption?
3. How large is the gap between the requirement and the best credible demonstrated component?
4. What measurement or analysis would move the answer?

Rules:

- Every number is labelled **F** (fundamental), **E** (engineering/conditional), or **A** (assumption).
- A single headline number is never used where an assumption drives it; a band is given.
- The source is declared before the conversion chain. No converter is counted as a generator.
- The screening converter mass of **1.5 kg/kW** is an assumption, not a datasheet value. It is varied explicitly because it changes verdicts.
- Packaging **1.25** is applied once to cell/component mass.
- No E2 upgrade is claimed: page/figure locators are still pending for most inputs (`SOURCE_VERIFICATION.md`).

---

## 2. Conservation and source closure

For any candidate:

\[
E_\text{delivered} = E_\text{source} - E_\text{rejected} - E_\text{stored} - E_\text{auxiliary} - E_\text{losses}
\]

A candidate that reports output without naming and metering an input is rejected before scoring. The only known sources with system-level specific energy above 1 kWh/kg are:

| Source | Specific energy (LHV/theoretical) | At practical conversion | Status |
|---|---:|---:|---|
| U-235 fission | 22.8 GWh/kg | engine/shield mass dominates | F; not portable, regulatory |
| H₂ oxidation | 33.3 kWh/kg | 16.7 kWh/kg fuel at 50% LHV | F; tank mass dominates |
| Diesel | 11.9 kWh/kg (9.94 kWh/L) | 3.6 kWh/kg fuel at 30% | F; engine/emissions dominate |
| Li-ion cell | 0.25–0.30 kWh/kg | 0.15–0.25 kWh/kg pack | E1; no datasheet archived |
| Graphite sensible heat | ~0.10 kWh/kg usable (500 K swing) | ~0.06–0.10 kWh/kg system | F; cp-limited |
| Supercapacitor | ~0.006 kWh/kg | ~0.005 kWh/kg pack | E1; source S03 |

The span is four to six orders of magnitude. **Source choice dominates every downstream optimisation.** A storage improvement of 20% cannot close a gap that a different source closes by 30×.

---

## 3. The mass equation

For an all-storage mission:

\[
E_\text{nameplate} = \frac{E_\text{delivered}}{\eta_\text{conv}\,\eta_\text{DoD}\,\eta_\text{RT}}
\]

\[
m_\text{sys} = (1+f)\frac{E_\text{nameplate}}{e_\text{cell}} + p_c P_\text{peak}(1+f) + m_\text{BOP}
\]

where \(f=0.25\) (packaging), \(p_c=1.5\) kg/kW (converter, **assumption**), \(\eta_\text{conv}=0.95\), \(\eta_\text{DoD}=0.80\), \(\eta_\text{RT}=0.90\), so \(\eta_\text{chain}=0.684\).

Rearranged, the required cell specific energy is:

\[
e_\text{cell,req} = \frac{(1+f)E_\text{nameplate}}{m_\text{target} - p_c P_\text{peak}(1+f) - m_\text{BOP}}
\]

The converter term is **power**-proportional; the storage term is **energy**-proportional. That single fact explains most of the mission-to-mission variation.

### 3.1 All-storage bound at the stated assumptions

```text
 id   E kWh   namepl  conv kg  bop kg  cells kg  cell Wh/kg  pack Wh/kg  overhead
 M1      10     14.6    11.25     2.6      16.9         864         691      40%
 M2     360    526.3     9.38    23.6     373.6        1409        1127       7%
 M3      10     14.6    56.25     2.6      32.9         444         355      59%
 M5    4000   5848.0  1875.00   242.0   18306.4         319         256       8%
```

`overhead` = (converter + BOP) / target mass. At M1 it is 40%; at M3 it is 59%. Small, high-power systems are **overhead-dominated**, not chemistry-dominated. At M2 and M5 energy dominates.

### 3.2 Converter-mass sensitivity

The 1.5 kg/kW value is the largest single assumption in the package. Varying it from 0.5 to 1.5 kg/kW:

```text
M1: 0.5kg/kW: 510 Wh/kg pack / 638 cell | 1.0kg/kW: 587 / 734 | 1.5kg/kW: 691 / 864
M2: 0.5kg/kW: 1112 / 1390            | 1.0kg/kW: 1119 / 1399 | 1.5kg/kW: 1127 / 1409
M3: 0.5kg/kW: 186 / 232              | 1.0kg/kW: 244 / 305  | 1.5kg/kW: 355 / 444
M5: 0.5kg/kW: 242 / 303              | 1.0kg/kW: 249 / 311  | 1.5kg/kW: 256 / 319
```

**Consequence:** the widely quoted “M1 needs ~690 Wh/kg pack” is *conditional* on 1.5 kg/kW. At a measured 0.5 kg/kW converter it is ~510 Wh/kg. Both are above current packs, so the M1 verdict does not flip — but the M3 verdict does: at 0.5 kg/kW, M3 needs 186 Wh/kg pack, which is inside current premium Li-ion. **M3 is the mission where a conventional system is closest to feasible, and its verdict depends on a missing datasheet.**

The band uses the benchmark's **10 kWh** mission: 8 kWh base plus 2 kWh of pulses (`dispatch.py:39–41`). That is internally consistent.

A supplier-grade converter mass is therefore a Gate 3 priority, not a detail.

---

## 4. Thermodynamic conversion ceilings

\[
\eta \le \eta_\text{Carnot} = 1 - \frac{T_\text{cold}}{T_\text{hot}}
\]

| Hot side | Carnot at 300 K sink | Comment |
|---:|---:|---|
| 800 K | 62.5% | TEG/ORC territory |
| 1200 K | 75.0% | Stirling/SOFC/advanced |
| 1800 K | 83.3% | TPV emitter floor |
| 2200 K | 86.4% | TPV 40% cell is 46% of Carnot |

- **TEG:** the standard expression gives 23.2% of Carnot at \(ZT=1\), i.e. **14.5% ideal** at 800 K; contacts and heat exchangers put practical systems at 5–8% (S02, S07; E1).
- **Fuel cell:** \(\Delta G/\Delta H = 237.1/285.8 = 83.0\%\) at 25 °C is the thermodynamic ceiling; practical system efficiency is 45–60% LHV (S11, N03; E1).
- **TPV:** 40% cell efficiency at 1900–2400 °C is verified at cell level (S01); the system value used here is \(0.32 \times 0.85 \times 0.95 = 25.8\%\) before insulation and pumping.
- **Solar:** the single-junction detailed-balance limit is 33.7% at one sun (S05); commercial modules are just under 25% in 2026 (N10); system efficiency is lower.

No architecture in this program may claim a conversion efficiency above Carnot. A claim above the relevant material/device ceiling requires a measured device and an independent replication, not a model.

---

## 5. Heat rejection: two regimes, not one number

This is the most common silent error in compact-system claims. A terrestrial fan-cooled unit and a vacuum/closed unit obey different laws.

### 5.1 Terrestrial forced convection

\[
Q = h A \Delta T, \qquad A \approx 6V^{2/3}
\]

At \(h=50\) W/m²K and \(\Delta T=20\) K:

| Envelope | Cube-equivalent area | Rejection |
|---:|---:|---:|
| 60 L | 0.92 m² | 920 W |
| 150 L | 1.69 m² | 1,694 W |
| 1,000 L | 6.00 m² | 6,000 W |

These are **optimistic**: a real enclosure has less effective area, fins add mass, and \(h\) falls in still air.

### 5.2 Radiative (vacuum or sealed high-temperature)

\[
q'' = \varepsilon\sigma(T^4 - T_0^4)
\]

At \(\varepsilon=0.9\), sink 300 K:

| Surface temperature | Flux |
|---:|---:|
| 350 K | 352 W/m² |
| 450 K | 1,679 W/m² |
| 600 K | 6,201 W/m² |
| 800 K | 20,490 W/m² |

The \(T^4\) dependence is why a 350 K radiator is ~58× larger than an 800 K radiator for the same heat. A low-temperature nuclear or TPV design that ignores this is not a design.

### 5.3 Mission consequences

- **M1 diesel:** 1.25 kW average at 26.3% overall rejects **3.50 kW**. In a 60 L box at \(h=50\), that needs \(\Delta T = 76\) K, or an external ducted area of **3.5 m²** at \(\Delta T=20\) K. The box surface is 0.92 m². The diesel option is thermally stressed even before noise, emissions, and fuel logistics.
- **M1 battery:** ~163 W average (round-trip plus pulse duty) needs \(\Delta T \approx 3.5\) K. Thermally easy.
- **M3:** 10 kW continuous at ~90% path efficiency rejects ~1.1 kW; a 150 L enclosure gives \(\Delta T \approx 13\) K. The 30 kW/10 s pulse is handled by thermal mass, not steady area. Feasible, but the converter and buffer must be co-designed.
- **M4:** 10 kWe at 25% rejects **30 kW**. Forced air at \(h=50\), \(\Delta T=20\) needs **30 m²** and ~150 kg at 5 kg/m². At 40% it is 15 m² and ~75 kg. A “$1/W” target that omits this heat-rejection mass is not a system cost.

---

## 6. Volumetric bound

Nameplate energy per external litre (not cell volume):

| Mission | Nameplate / envelope | Best credible pack | Verdict |
|---|---:|---:|---|
| M1 | 244 Wh/L | 250–400 Wh/L (E1) | marginal; converter/BOP volume not yet included |
| M2 | 526 Wh/L | 250–400 Wh/L | fails by 1.3–2.1× |
| M3 | 97 Wh/L | 250–400 Wh/L | volume not binding |
| M5 | 146 Wh/L | 250–400 Wh/L | volume not binding |

M1 is **co-bound by mass and volume**. A pack that meets the mass target at 691 Wh/kg may still not fit 60 L with converter, BOP, and cooling. This is why a mass-only claim is not a system claim.

---

## 7. Scale crossover: fixed overhead versus energy-proportional mass

At the M1 power scale, a simple two-term model (E1, illustrative only):

\[
m_\text{battery} \approx 10.44E + 13.85 \quad \text{kg}
\]
\[
m_\text{diesel} \approx 0.278E + 51 \quad \text{kg}
\]

The battery term is the 175 Wh/kg pack basis plus fixed converter/BOP. The diesel term is 0.278 kg fuel/kWh plus a 6 kW engine, radiator, converter, and enclosure. They cross at **~3.7 kWh**.

- Below ~3.7 kWh, a battery is lighter.
- Above ~3.7 kWh, a chemical fuel is lighter **at this power scale**.
- At M1 (10 kWh), diesel is ~49 kg vs battery ~118 kg: the benchmark’s mass problem is not a battery problem, it is a **source** problem. Diesel then still misses 35 kg by ~14 kg and fails on fuel cost ($0.536/kWh), heat (3.5 kW), emissions, and noise.
- At M2 (360 kWh), diesel is ~165 kg vs battery ~3,770 kg: chemical wins by ~23×.
- At M5 (4 MWh), a 1 MW engine is 5–10 t, so the linear model no longer applies; stationary batteries win on cost, emissions, and maintenance.

**The binding constraint changes with mission scale.** A single “best architecture” is therefore incoherent without a mission.

---

## 8. Economic floors

### 8.1 Fuel floor

\[
c_\text{fuel} = \frac{\text{price per unit}}{\text{LHV per unit} \times \eta_\text{overall}}
\]

| Fuel | Price (E0) | Efficiency | Fuel cost |
|---|---:|---:|---:|
| Diesel | $1.40/L | 26.3% | **$0.536/kWh** |
| H₂ | $6.00/kg | 50% LHV | **$0.360/kWh** |
| H₂ | $4.00/kg | 50% LHV | **$0.240/kWh** |

- Diesel at $1.40/L cannot meet the M1 $0.40/kWh target below **35.2% overall efficiency**, before any capital cost. The screened 26.3% is already $0.536.
- H₂ at $6/kg consumes 90% of the M1 target on fuel alone. The CSV’s H5 threshold of $4/kg is the price at which fuel leaves room for capital.

### 8.2 Capital amortisation

\[
N_\text{required} = \frac{C_\text{capex}}{(c_\text{target} - c_\text{fuel})E_\text{mission}}
\]

| Mission | Required missions at $0.10/kWh fuel | Maximum missions in life at 3/day | Verdict |
|---|---:|---:|---|
| M1 | 1,667 | 10,950 (10 y) | feasible at daily use |
| M2 | 347 | **122** (30-day mission, 10 y) | **target inconsistent** |
| M3 | 2,222 | 5,475 (5 y) | feasible |
| M5 | — (charging $0.10 > target $0.08) | 16,425 (15 y) | **target below charging cost** |

Two mission definitions fail their own arithmetic:

- **M2:** $50,000 capex over 122 lifetime missions and 43,920 kWh gives **$1.14/kWh capital alone**, before fuel. To meet $0.50/kWh with zero fuel, capex must be ≤ **$21,960**. A nuclear unit will not be. M2 must either lower capex, extend life beyond ~23 years, or raise the LCOE target to ~$1.20/kWh. This is a mission-definition defect, not a physics result.
- **M5:** charging at $0.10/kWh already exceeds the $0.08/kWh target. At $0.05/kWh charging, capital $0.03/kWh gives $0.086/kWh — still above target. M5 is **electricity-price-bound**, not technology-bound.

M1’s cost target is achievable only with high utilisation (~1 mission/day). At one mission per week, capital alone is ~$0.96/kWh. Duty cycle belongs in the mission, not in the cost model’s fine print.

---

## 9. Gap table: requirement versus best credible component

Best credible values are E1 planning ranges; no datasheet is archived.

| Mission | Required pack (1.5 kg/kW) | Required pack (0.5 kg/kW) | Best credible pack | Gap (pack) | Binding? |
|---|---:|---:|---:|---:|---|
| M1 | 691 Wh/kg | 510 Wh/kg | 150–250 Wh/kg | 2.0–4.6× | **yes** |
| M2 | 1,127 Wh/kg | 1,112 Wh/kg | 150–250 Wh/kg | 4.4–7.5× | **yes; battery impossible** |
| M3 | 355 Wh/kg | 186 Wh/kg | 150–250 Wh/kg | 0.7–2.4× | **conditional on converter mass** |
| M5 | 256 Wh/kg | 242 Wh/kg | 150–250 Wh/kg | 1.0–1.7× | marginal; premium cells only |

Cell-level equivalents are 1.25× the pack values. The M1 gap is ~2.1–3.5× at cell level (638–864 vs 250–300 Wh/kg).

**The honest conclusion:** M1 and M2 are not closed by known storage. M3 and M5 are close enough that a measured converter/pack could change the verdict. That is where a paper-and-datasheet program can still produce a decision.

---

## 10. Fundamental, engineering, and assumption

| Limit | Type | Why |
|---|---|---|
| Conservation of energy | **F** | No candidate may close a balance by omission |
| Carnot bound | **F** | Applies to every heat engine, including TPV/TEG/thermionic |
| Fuel LHV and fission binding energy | **F** | Source-specific, not improvable by design |
| Stefan–Boltzmann radiative flux | **F** | Sets vacuum radiator area |
| Graphite sensible-heat density | **F** | \(c_p\Delta T\), ~0.1 kWh/kg usable |
| Electrochemical Gibbs energy | **F** | Sets fuel-cell and battery voltage ceiling |
| Pack packaging factor 1.25 | **E** | Real packs range ~1.15–1.40; must be measured |
| Converter 1.5 kg/kW | **A** | Not a datasheet; 0.5–1.5 changes M3's verdict |
| \(h=50\) W/m²K | **A** | Depends on fan, fins, altitude, ambient |
| Cost and fuel price | **A** | E0 planning values; quotations absent |
| Cycle life, degradation | **E** | Vendor- and chemistry-specific |
| Nuclear shielding/regulatory mass | **E** | Site- and licence-specific; not modelled |

A claim that a fundamental limit can be engineered away is rejected. A claim that an assumption is a fundamental limit is also rejected; that is why the converter band is shown.

---

## 11. Falsifiable limit statements

These are the statements the program should test, not defend:

1. **L1:** With \(p_c \ge 0.5\) kg/kW and 1.25 packaging, no electrochemical storage at ≤300 Wh/kg cell meets M1 at 35 kg. *(Arithmetic; falsified only by a measured cell above the threshold or a different mission boundary.)*
2. **L2:** M1 at 35 kg with a 1.5 kg/kW converter requires ≥864 Wh/kg cell (691 Wh/kg pack); with 0.5 kg/kW, ≥638 Wh/kg cell (510 Wh/kg pack). *(Arithmetic; conditional on the stated assumptions.)*
3. **L3:** Any 10 kWe converter at ≤40% efficiency rejects ≥15 kW; in still air at 1 kW/m² that needs ≥15 m². *(Conservation plus heat transfer.)*
4. **L4:** Diesel at $1.40/L needs ≥35.2% overall efficiency to reach $0.40/kWh before capital. *(Arithmetic.)*
5. **L5:** H₂ at $6/kg cannot meet M1 at $0.40/kWh even at 100% duty: fuel is $0.36/kWh and the capital requires 12,500 missions, above the 10,950 maximum. *(Arithmetic under stated assumptions.)*
6. **L6:** A graphite sensible store cannot exceed ~0.14 kWh/kg usable over a 1500→800 K swing. *(Material property.)*
7. **L7:** A battery-only M2 requires ≥1,100 Wh/kg pack. *(Arithmetic.)*
8. **L8:** No converter may exceed Carnot at its stated hot and cold temperatures; a 2200 K claim above 86.4% is impossible. *(Second law.)*

If any of L1–L8 is contradicted by a measurement, the mission definition or the assumption set must be re-examined before the result is celebrated.

---

## 12. What this document does not establish

- No transient dispatch, degradation, or control model.
- No volume build-up at the same boundary (only nameplate/envelope).
- No CFD, fin analysis, or altitude/ambient sensitivity.
- No nuclear shielding, criticality, or licensing model.
- No supplier quotation, datasheet, or measured converter mass.
- No independent review of these calculations yet.
- No architecture selection, and no Gate 2 pass.

**Gate 3 may use these bounds to reject candidates. It may not use them to select a winner without the missing measured inputs.**
