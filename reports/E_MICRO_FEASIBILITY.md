# E-Micro Gate 2 feasibility — 3 kWe in 2.16 L

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** analytical screen; no component quote, no CAD, no measurement  
**Target:** E-Micro, 3 kWe continuous, external envelope 120 × 150 × 120 mm (2.16 L)  
**Model:** `engineering/`; tests: 18 stdlib `unittest` cases

---

## 1. Answer

**No current commercial mechanism fits 3 kWe for 1 hour in 2.16 L once source, conversion, heat rejection and packaging are counted.**

- The best current **storage** mechanism is **Li-ion battery** at **5.61 L** for 1 h — **2.60×** the envelope.
- The best current **generator** is **PEM fuel cell + 700 bar H2** at **7.81 L** — **3.62×** the envelope.
- The best case of any mechanism is **Li-air battery (theoretical)** at **2.75 L** — theoretical, **1.27×** the envelope.
- A current Li-ion buffer fits the envelope for only about **21 min** at 3 kW. A continuous generator is a different problem.

The target is not a small margin. It is a **2.6× volume gap for the best current storage** and a **3.6–20× gap for current generation**, before any real packaging, controls, cooling loop, or safety hardware.

The theoretical Li-air entry would fit only at **≥1,963 Wh/L cell** with this packaging and BOP; the 1,500 Wh/L case used here does not. That threshold is not a commercial product.

---

## 2. Volumetric power density

| Quantity | Value |
|---|---:|
| Electrical power | 3.0 kW |
| External envelope | 2.16 L |
| Volumetric power density | **1.389 MW/m³** |
| Envelope surface area | **0.1008 m²** |

For comparison, high-performance electric motors reach several kW/L; power electronics reach tens of kW/L. The 3 kW **converter** is not the problem. The **source** is.

---

## 3. Best-case complete-system volume (L)

The table is the **best case** of each mechanism: optimistic efficiency, volume, heat-transfer coefficient, packaging and BOP. A real system is larger. `†` = theoretical; `‡` = restricted nuclear.

| Mechanism | Maturity | 1 h | 8 h | 100 h | 1,000 h | 10,000 h |
|---|---|---|---|---|---|---|
| Li-air battery (theoretical) † | theoretical | 2.75 | 20.2 | 250.2 | 2,500 | 25,000 |
| Li-ion battery | current | 5.61 | 43.1 | 536.0 | 5,357 | 53,572 |
| PEM fuel cell + 700 bar H2 | current | 7.81 | 40.6 | 471.9 | 4,691 | 46,883 |
| Stirling engine + alternator | advanced | 23.0 | 29.6 | 116.3 | 965.2 | 9,454 |
| Thermophotovoltaic converter | advanced | 23.4 | 31.0 | 130.2 | 1,100 | 10,801 |
| Microturbine + high-speed alternator | advanced | 34.7 | 42.2 | 141.4 | 1,112 | 10,813 |
| Thermoelectric generator | current | 36.1 | 69.1 | 503.0 | 4,747 | 47,189 |
| Diesel genset | current | 42.2 | 49.7 | 148.9 | 1,119 | 10,820 |
| Radioisotope thermoelectric generator ‡ | restricted | 301.9 | 301.9 | 301.9 | 301.9 | 301.9 |
| Solar PV + storage | current | 307.2 | 344.7 | 837.6 | 5,659 | 53,873 |
| Supercapacitor bank | current | 375.2 | 3,000 | 37,500 | 375,000 | 3,750,000 |
| Ambient harvesting † | theoretical | 18,752 | 18,752 | 18,752 | 18,752 | 18,752 |

`Li-air` is theoretical and does not have a commercial pack. `RTG` is a space/nuclear source and is not a 3 kW product. The `ambient` row is not a contender; it is included as a lower bound.

**Reading the table:** even the best current 1 h system is 5.6 L; the envelope is 2.16 L. At 8 h, the best current system is already tens of litres; at 10,000 h, no chemical system is close.

---

## 4. One-hour detail

| Mechanism | Maturity | Best case (L) | Worst case (L) | Best / 2.16 L | Verdict | Largest component (best case) |
|---|---|---|---|---|---|---|
| Li-air battery (theoretical) | theoretical | 2.75 | 5.47 | 1.27× | fail | cells (91%) |
| Li-ion battery | current | 5.61 | 10.5 | 2.60× | fail | cells (96%) |
| PEM fuel cell + 700 bar H2 | current | 7.81 | 12.8 | 3.62× | fail | H2 tank (60%) |
| Stirling engine + alternator | advanced | 23.0 | 134.6 | 10.64× | fail | engine/generator (82%) |
| Thermophotovoltaic converter | advanced | 23.4 | 160.0 | 10.85× | fail | engine/generator (80%) |
| Microturbine + high-speed alternator | advanced | 34.7 | 153.4 | 16.06× | fail | engine/generator (86%) |
| Thermoelectric generator | current | 36.1 | 540.7 | 16.72× | fail | engine/generator (52%) |
| Diesel genset | current | 42.2 | 153.4 | 19.53× | fail | engine/generator (89%) |
| Radioisotope thermoelectric generator | restricted | 301.9 | 1,352 | 139.76× | fail | shielded source (99%) |
| Solar PV + storage | current | 307.2 | 822.2 | 142.24× | fail | panel (98%) |
| Supercapacitor bank | current | 375.2 | 810.4 | 173.73× | fail | cells (100%) |
| Ambient harvesting | theoretical | 18,752 | 405,002 | 8681.42× | fail | collector (100%) |

A `conditional` verdict means the optimistic case fits but the pessimistic case does not. No current mechanism is a clean `pass`.

---

## 5. Heat rejection

At 3 kWe, a heat engine rejects 3(1/η - 1) kW. The envelope surface is only **0.1008 m²**. Required area:

| Heat-engine efficiency | Waste heat (W) | Area h=100, ΔT=30 (m²) | Area h=500, ΔT=50 (m²) | Area h=1,000, ΔT=80 (m²) | Cold-plate area / envelope surface |
|---|---|---|---|---|---|
| 15% | 17,000 | 5.667 | 0.680 | 0.212 | 2.11× |
| 25% | 9,000 | 3.000 | 0.360 | 0.113 | 1.12× |
| 35% | 5,571 | 1.857 | 0.223 | 0.070 | 0.69× |
| 40% | 4,500 | 1.500 | 0.180 | 0.056 | 0.56× |

At 25% efficiency and a very aggressive cold plate (h=1,000 W/m²K, ΔT=80 K), the required area is **0.1125 m²**, already larger than the envelope surface. At 35% it is 0.0696 m², below the surface — but the engine itself is 15–30 L, so heat rejection is not the only failure. The heat-rejection result rules out low-efficiency converters; it does not rescue high-efficiency ones.

---

## 6. Minimum relaxation

| Relaxation path | Value | Interpretation | Class |
|---|---|---|---|
| Best current 1 h system (Li-ion) | 5.61 L | 2.60× the envelope | Current |
| Max duration at 2.16 L, 3 kW, best case | 21.4 min | Short buffer only | Current |
| Max duration at 2.16 L, 3 kW, worst case | 10.4 min | Short buffer only | Current |
| Max power for 1 h at 2.16 L, best case | 1.07 kW | 2.8× lower than 3 kW | Current |
| Max power for 1 h at 2.16 L, worst case | 0.52 kW | 5.8× lower than 3 kW | Current |
| Cell energy density needed for 3 kW/1 h at 1.25 packaging, 0.2 L BOP | 1,963 Wh/L | ≈2.8× a 700 Wh/L cell | Advanced/theoretical |
| Cell energy density needed at 1.10 packaging, 0.1 L BOP | 1,610 Wh/L | ≈2.3× a 700 Wh/L cell | Advanced/theoretical |
| Cell energy density needed with zero packaging/BOP | 1,389 Wh/L | ≈2.0× a 700 Wh/L cell | Theoretical |

The target needs one of:

1. **~2.0–2.8× better cell volumetric energy density** (1,389–1,963 Wh/L cell) for a 1 h battery, depending on packaging. Current high-energy Li-ion cells are ~700 Wh/L; Li-air is the only chemistry near the upper end, and it is not commercial.
2. **~2.8–5.8× lower power** for a 1 h system in the same envelope.
3. **~2.6× larger volume** for the best current 1 h storage system (5.6 L).
4. **A short-duration buffer**, not a continuous generator: ~10–21 min at 3 kW with current Li-ion.

---

## 7. What this does not prove

- It does not prove that a **new mechanism** is impossible. It bounds the current and near-current mechanisms in the register.
- It does not model transient performance, converter control, fault behaviour, vibration, crash, or lifetime.
- It uses **external** envelope volume. Internal volume is smaller after walls, insulation, clearances, connectors and mounting.
- The best case is deliberately optimistic. A real system is larger, so the failure is robust in the direction that matters.
- It does not price the system. A 5.6 L battery may meet ₹50,000 at some scale; that is a separate Gate 3/6 question.
- It does not select a mechanism. It rejects the **stated E-Micro envelope** as a continuous 3 kW generator with current technology.

---

## 8. Claim → evidence → method → assumptions → uncertainty → counterargument → verdict

**Claim:** E-Micro’s 3 kWe / 2.16 L target is not achievable with a current commercial mechanism for 1 hour of continuous output.

**Evidence:** component-level energy densities, fuel LHV, heat-transfer relations and the mechanisms register. No measured system is used; the best-case parameters are optimistic estimates.

**Method:** complete-system volume = source/fuel + converter + heat rejection + BOP, multiplied by a packaging factor; compare with 2.16 L; repeat for 1–10,000 h.

**Assumptions:** 1.25 packaging (1.35 worst), 1.5 L BOP (2.0 worst), 700 Wh/L cell (400 worst), 3 kW/L PEM stack (1 worst), 10 L/kW diesel genset (20 worst), h=1,000 W/m²K and ΔT=80 K best heat rejection (100 and 30 worst).

**Uncertainty:** the best-case volume is a lower bound; the worst case is 1.5–3× larger. The sign of the conclusion does not change for current mechanisms at 1 h.

**Counterargument:** a new cell chemistry, a fuel cell with a liquid fuel, or a completely different mechanism could be smaller. That is why the report labels Li-air theoretical and lists the thresholds; it does not declare the whole vision impossible.

**Verdict:** **FAIL for E-Micro as stated, with current commercial mechanisms, at 1 h.** **INSUFFICIENT EVIDENCE** for a new mechanism; **CONDITIONAL** only for a short buffer (~10–21 min) or a lower power (~1.1 kW for 1 h).

---

## 9. Implications for the programme

1. **Do not build CAD for a 2.16 L continuous generator yet.** The first design should be a **buffer/converter** or a **re-scoped generator** at 5–10 L.
2. **The service interval is a missing requirement.** At 1 h the gap is 2.6×; at 10,000 h it is orders of magnitude. The owner must state the interval before any architecture selection.
3. **E-Micro is the hardest target, not the easiest.** A 3 kW two-wheeler core in 2.16 L is beyond current storage and generation. E-Mobility (20 kW) and E-Heavy have no envelope or duty cycle yet; they cannot be screened.
4. **The next mechanism to examine is a liquid-fuel fuel cell or a reformed-methanol system**, because 700 bar H2 alone is 3.75 L for 1 h — larger than the envelope before the stack. This is a concrete Gate 3 question, not a CAD question.
5. **Preserve the negative result.** It prevents a year of packaging work around a target that cannot close.

---

## 10. Reproduce

```bash
cd /home/darion-dev/project-e_research_plan
python3 -m unittest discover -s engineering/tests -t .
../project-e/.venv/bin/python -m engineering.report
```

The report and figures are generated from `engineering/data/requirements.json` and `engineering/mechanisms.py`; the run manifest records the commit, inputs and output hashes.
