# E-Micro Gate 2 feasibility — 3 kWe in 2.16 L

**Version:** 0.2  
**Date:** 2026-10-23  
**Status:** analytical screen; no component quote, no CAD, no measurement. Revision 0.2 corrects the heat-rejection narrative, adds a 0.4 L converter and fuel-cell radiator, and qualifies the maturity labels; the fail is unchanged and larger.  
**Target:** E-Micro, 3 kWe continuous, external envelope 120 × 150 × 120 mm (2.16 L)  
**Model:** `engineering/`; `engineering/tests` stdlib `unittest` cases

---

## 1. Answer

**No mechanism among the twelve screened in this report — including all current commercial families represented — fits 3 kWe for 1 hour in 2.16 L once source, conversion, heat rejection and packaging are counted.**

- The best current **storage** mechanism is **Li-ion battery** at **6.11 L** for 1 h — **2.83×** the envelope.
- The best current **generator** is **PEM fuel cell + 700 bar H2** at **8.94 L** — **4.14×** the envelope.
- The best case of any mechanism is **Li-air battery (theoretical)** at **3.25 L** — theoretical, **1.50×** the envelope.
- A current Li-ion buffer fits the envelope for only about **16 min** at 3 kW with 100% DoD and no conversion loss; at 80% DoD and 95% converter it is about **12 min**. A continuous generator is a different problem.

The target is not a small margin. It is a **2.8× volume gap for the best current storage** and a **4.1–20× gap for current generation**, before any real packaging, controls, cooling loop, or safety hardware.

The failure is independent of packaging: **3 kWh ÷ 700 Wh/L = 4.29 L of cells alone**, already **1.98×** the envelope; a 1 L stack plus 3.75 L of H₂ gas is **4.75 L**, **2.20×**. No packaging or BOP assumption can rescue either. The theoretical Li-air entry would need **≥2,660 Wh/L cell** with this packaging, BOP and converter; the 1,500 Wh/L case used here does not fit. That threshold is not a commercial product.

---

## 2. Volumetric power density

| Quantity | Value |
|---|---:|
| Electrical power | 3.0 kW |
| External envelope | 2.16 L |
| Volumetric power density | **1.389 MW/m³** |
| Envelope surface area | **0.1008 m²** |

A **0.4 L converter** allowance is included in every row (0.3–0.6 L is the estimate for a 3 kW isolated DC-DC at 5–10 kW/L; it is not a datasheet). High-performance electric motors reach several kW/L and power electronics reach tens of kW/L, so the converter is a small term, not the problem. The **source** is.

---

## 3. Best-case complete-system volume (L)

The table is the **best case** of each mechanism: optimistic efficiency, volume, heat-transfer coefficient, packaging and BOP. A real system is larger. `†` = theoretical; `‡` = restricted nuclear.

| Mechanism | Maturity | 1 h | 8 h | 100 h | 1,000 h | 10,000 h |
|---|---|---|---|---|---|---|
| Li-air battery (theoretical) † | theoretical | 3.25 | 20.7 | 250.8 | 2,501 | 25,001 |
| Li-ion battery | current | 6.11 | 43.6 | 536.5 | 5,358 | 53,572 |
| PEM fuel cell + 700 bar H2 | current | 8.94 | 41.8 | 473.0 | 4,692 | 46,884 |
| Stirling engine + alternator | advanced | 23.5 | 30.1 | 116.8 | 965.7 | 9,454 |
| Thermophotovoltaic converter | advanced | 23.9 | 31.5 | 130.7 | 1,101 | 10,802 |
| Microturbine + high-speed alternator | advanced | 35.2 | 42.7 | 141.9 | 1,112 | 10,813 |
| Thermoelectric generator | advanced | 36.6 | 69.6 | 503.5 | 4,748 | 47,190 |
| Diesel genset | current | 42.7 | 50.2 | 149.4 | 1,120 | 10,821 |
| Radioisotope thermoelectric generator ‡ | restricted | 302.4 | 302.4 | 302.4 | 302.4 | 302.4 |
| Solar PV + storage | current | 307.7 | 345.2 | 838.1 | 5,660 | 53,874 |
| Supercapacitor bank | current | 375.7 | 3,001 | 37,501 | 375,001 | 3,750,001 |
| Ambient harvesting † | theoretical | 18,752 | 18,752 | 18,752 | 18,752 | 18,752 |

`Li-air` is theoretical and does not have a commercial pack. `RTG` is a space/nuclear source and is not a 3 kW product. The `ambient` row is not a contender; it is included as a lower bound.

**Label caveat:** the `current` column labels the **mechanism family**, not every best-case parameter. Two best cases are optimistic extrapolations: PEM **3 kW/L** is an automotive large-stack metric (0.3–1.5 kW/L is closer at 3 kW), and diesel **10 L/kW** is a stripped bare engine (commercial 3 kW packages are 50–150 L/kW). They are retained because they favour the mechanism; the failure is therefore robust.

**Reading the table:** even the best current 1 h system is 6.1 L; the envelope is 2.16 L. At 8 h, the best current system is already tens of litres; at 10,000 h, no chemical system is close.

---

## 4. One-hour detail

| Mechanism | Maturity | Best case (L) | Worst case (L) | Best / 2.16 L | Verdict | Largest component (best case; share of unpackaged sum) |
|---|---|---|---|---|---|---|
| Li-air battery (theoretical) | theoretical | 3.25 | 6.01 | 1.50× | fail | cells (77%) |
| Li-ion battery | current | 6.11 | 11.1 | 2.83× | fail | cells (88%) |
| PEM fuel cell + 700 bar H2 | current | 8.94 | 40.4 | 4.14× | fail | H2 tank (52%) |
| Stirling engine + alternator | advanced | 23.5 | 135.1 | 10.87× | fail | engine/generator (80%) |
| Thermophotovoltaic converter | advanced | 23.9 | 160.5 | 11.09× | fail | engine/generator (78%) |
| Microturbine + high-speed alternator | advanced | 35.2 | 153.9 | 16.29× | fail | engine/generator (85%) |
| Thermoelectric generator | advanced | 36.6 | 541.2 | 16.95× | fail | engine/generator (51%) |
| Diesel genset | current | 42.7 | 153.9 | 19.77× | fail | engine/generator (88%) |
| Radioisotope thermoelectric generator | restricted | 302.4 | 1,353 | 139.99× | fail | shielded source (99%) |
| Solar PV + storage | current | 307.7 | 822.7 | 142.47× | fail | panel (97%) |
| Supercapacitor bank | current | 375.7 | 810.9 | 173.96× | fail | cells (100%) |
| Ambient harvesting | theoretical | 18,752 | 405,003 | 8681.66× | fail | collector (100%) |

A `conditional` verdict means the optimistic case fits but the pessimistic case does not. No mechanism in the register is a clean `pass` at 3 kWe/1 h. The `insufficient evidence` verdict is reserved for mechanisms outside the register; every screened mechanism gets pass, conditional or fail.

---

## 5. Heat rejection

At 3 kWe, a heat engine rejects 3(1/η - 1) kW. The envelope skin is only **0.1008 m²**, and a sealed box cannot reject this heat through its own skin: the skin is a boundary, not a radiator. The table uses an air-side coefficient, which is the relevant basis:

| Efficiency | Waste heat (W) | Air-side area, h=100, ΔT=30 (m²) | Air-side area, h=50, ΔT=30 (m²) | Fin-stack volume at 4 kW/L (L) | Fin area / skin area |
|---|---|---|---|---|---|
| 15% | 17,000 | 5.667 | 11.333 | 4.25 | 56.2× |
| 25% | 9,000 | 3.000 | 6.000 | 2.25 | 29.8× |
| 35% | 5,571 | 1.857 | 3.714 | 1.39 | 18.4× |
| 40% | 4,500 | 1.500 | 3.000 | 1.12 | 14.9× |
| 60% | 2,000 | 0.667 | 1.333 | 0.50 | 6.6× |

At 25% the waste heat is 9 kW; even at an optimistic forced-air **h=100 W/m²K, ΔT=30 K**, the required fin area is **3.00 m², 30× the skin**, and a 4 kW/L fin stack is **2.25 L** — already larger than the envelope before the engine, fuel or BOP. At 35% the fin area is 1.86 m² (18×) and the fin stack is 1.39 L; at 40%, 1.50 m² (15×) and 1.13 L. At 60% (the PEM best case) the 2 kW waste heat still needs 0.67 m² (6.6×) and a 0.5 L fin stack, plus a coolant loop. **Heat rejection rules out a sealed 2.16 L heat engine independent of engine volume, and it adds a real radiator to the fuel-cell case.**

---

## 6. Minimum relaxation

| Relaxation path | Value | Interpretation | Class |
|---|---|---|---|
| Best current 1 h system (Li-ion, converter included) | 6.11 L | 2.83× the envelope | Current |
| Max duration at 2.16 L, 3 kW, 100% DoD, no conversion loss | 15.8 min | Volume-only upper bound | Current |
| Max duration at 2.16 L, 3 kW, 80% DoD, 95% converter | 12.0 min | Honest small-pack estimate | Current |
| Max power for 1 h at 2.16 L | 0.79 kW | 3.8× lower than 3 kW | Current |
| Cell energy density needed at 1.25 packaging, 0.2 L BOP, 0.4 L converter | 2,660 Wh/L | ≈3.8× a 700 Wh/L cell | Advanced/theoretical |
| Cell energy density needed at 1.10 packaging, 0.1 L BOP, 0.4 L converter | 2,050 Wh/L | ≈2.9× a 700 Wh/L cell | Advanced/theoretical |
| Cell energy density needed with zero packaging/BOP/converter | 1,389 Wh/L | ≈2.0× a 700 Wh/L cell | Theoretical |
| Cell energy density with 80% DoD and 95% converter | 3,499 Wh/L | ≈5.0× a 700 Wh/L cell | Theoretical |

The target needs one of:

1. **~2.0–3.8× better cell volumetric energy density** (1,389–2,660 Wh/L cell) for a 1 h battery, depending on packaging and converter allowance; with 80% DoD and 95% converter it is **~3,500 Wh/L (5.0×)**. Current high-energy Li-ion cells are ~700 Wh/L; Li-air is the only chemistry near the upper end, and it is not commercial.
2. **~3.8× lower power** for a 1 h system in the same envelope (0.79 kW max).
3. **~2.8× larger volume** for the best current 1 h storage system (6.1 L); the best current generator is ~4.1× (8.9 L).
4. **A short-duration buffer**, not a continuous generator: ~8–16 min at 3 kW with current Li-ion (about 12 min at 80% DoD and 95% converter).

---

## 7. What this does not prove

- It does not prove that a **new mechanism** is impossible. It bounds the current and near-current mechanisms in the register.
- It does not model transient performance, converter control, fault behaviour, vibration, crash, or lifetime.
- It uses **external** envelope volume. Internal volume is smaller after walls, insulation, clearances, connectors and mounting.
- The best case is deliberately optimistic. A real system is larger, so the failure is robust in the direction that matters.
- It does not price the system. A 6.1 L battery may meet ₹50,000 at some scale; that is a separate Gate 3/6 question.
- It does not select a mechanism. It rejects the **stated E-Micro envelope** as a continuous 3 kW generator with current technology.
- **Hardware not counted:** BMS/contactors/fuses/EMI filter beyond the 0.4 L converter allowance; fuel-cell air blower, humidifier, water separator/drain and H₂ leak detection/ventilation; diesel DPF/SCR, muffler and intake filtration (plausibly 1–3 L); Li-ion thermal-runaway venting/containment; structural walls, hardpoints, connectors and vibration isolation. These omissions make the best-case volumes lower bounds.
- **H₂ vessel:** the 3.75 L figure is **gas volume** at 700 bar, not vessel volume. A Type IV vessel is roughly 1.4–1.7× larger externally (≈5.3–6.4 L), so the PEM row is optimistic even before the radiator.
- **Touch safety:** the radiator-core best case uses an effective 4 kW/L fin stack; it does not mean the 105 °C skin at ΔT=80 K is acceptable. IEC 62368-1 touch limits for metal are far lower; a real product needs a ducted/forced-air path and a touch-safe enclosure, which breaks the sealed-box premise.

---

## 8. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** E-Micro’s 3 kWe / 2.16 L target is not achievable with any of the twelve screened mechanisms—including every current commercial family represented—for 1 hour of continuous output.

**Evidence:** component-level energy densities, fuel LHV, heat-transfer relations and the mechanisms register. No measured system is used; the best-case parameters are optimistic estimates.

**Method:** complete-system volume = source/fuel + converter + heat rejection + BOP, multiplied by a packaging factor; compare with 2.16 L; repeat for 1–10,000 h. The fuel-cell branch now includes a radiator; the heat table uses an **air-side** coefficient, not a cold-plate coefficient applied to the envelope skin.

**Assumptions:** 1.25 packaging (1.35 worst), 1.5 L BOP (2.0 worst), 0.4 L converter (0.3–0.6 L estimate, not separately varied), 700 Wh/L cell (400 worst), 3 kW/L PEM stack (1 worst; large-stack extrapolation), 10 L/kW diesel engine (20 worst; stripped, not a commercial package), and a 4 kW/L fin-stack equivalent for the best radiator (worst h=100 W/m²K, ΔT=30 K). The 105 °C skin implied by ΔT=80 K is **not** claimed as touch-safe.

**Uncertainty:** the best-case volume is a lower bound; the worst case is 1.5–3× larger. The sign of the conclusion does not change for current mechanisms at 1 h.

**Counterargument:** a new cell chemistry, a fuel cell with a liquid fuel, or a completely different mechanism could be smaller. That is why the report labels Li-air theoretical and lists the thresholds; it does not declare the whole vision impossible. The liquid-fuel evidence review is worse than H₂ on volume: the best documented reformed-methanol module is 81 L for 5 kW (≈40× the envelope after fuel, tank and buffer), and no 3 kW/2.16 L product was found.

**Verdict:** **FAIL for E-Micro as stated, among the twelve screened mechanisms, at 1 h.** **INSUFFICIENT EVIDENCE** for mechanisms outside the register; **CONDITIONAL** only for a short buffer (~8–16 min) or a lower power (~0.79 kW for 1 h). The earlier 1.1 kW figure ignored the converter volume and is superseded.

---

## 9. Implications for the programme

1. **Do not build CAD for a 2.16 L continuous generator yet.** The first design should be a **buffer/converter** or a **re-scoped generator** at 6–9 L.
2. **The service interval is a missing requirement.** At 1 h the best current storage gap is 2.8×; at 10,000 h it is orders of magnitude. The owner must state the interval before any architecture selection.
3. **E-Micro is the hardest target, not the easiest.** A 3 kW two-wheeler core in 2.16 L is beyond current storage and generation. E-Mobility (20 kW) and E-Heavy have no envelope or duty cycle yet; they cannot be screened.
4. **The liquid-fuel route is not a shortcut.** The best documented reformed-methanol module is 81 L for 5 kW; even a 3 kW/1 h complete system is ≈86 L (≈40×). 700 bar H₂ is also not a shortcut: 3.75 L is gas volume, and a Type IV vessel is ≥5.3 L before the stack. The only credible 2.16 L object is a short buffer.
5. **Preserve the negative result.** It prevents a year of packaging work around a target that cannot close.

---

## 10. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.report
```

The report and figures are generated from `engineering/data/requirements.json` and `engineering/mechanisms.py`; the run manifest records the commit, inputs, output hashes, `model_dirty` and `model_sha256`.
