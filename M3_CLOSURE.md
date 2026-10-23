# Project E — M3 Closure (Paper Design)

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** paper closure with measured components; **conditional, not closed**; no purchase, build, or test  
**Calculator:** `limits.py` §8–9; run `python3 limits.py`

---

## 1. Mission and the one assumption that decides it

M3: **10 kWh delivered / 1 h**, 10 kW average, 30 kW / 10 s pulse, **≤100 kg**, ≤150 L, ≤$20,000, ≤$1.00/kWh, 5 years.

**Provisional load definition: DC or motor load.** This is the only branch that can fit 100 kg. The 50 Hz AC branch is computed and fails (below). The owner has not confirmed the load; this document treats it as a declared assumption, not a fact.

Nameplate at the plan's chain: \(10 / 0.95 / 0.80 / 0.90 = 14.62\) kWh.

---

## 2. Mass budget

Packaging 1.25 on the converter; BOP rule \(2 + 0.06E\) = 2.6 kg.

| Item | Mass | Note |
|---|---:|---|
| Envelope | 100.0 kg | target |
| Cascadia PM100, packaged | 9.4 kg | 7.5 kg × 1.25 |
| BOP | 2.6 kg | screening rule |
| **Available for pack** | **88.0 kg** | |
| Required pack | **166 Wh/kg** | 14.62 kWh / 88.0 kg |

**Margin sensitivity**

| Mass reserve | Pack mass available | Required pack |
|---:|---:|---:|
| 0 kg | 88.0 kg | **166 Wh/kg** |
| 10 kg (10%) | 78.0 kg | **187 Wh/kg** |
| 20 kg | 68.0 kg | **215 Wh/kg** |

**Interpretation.** 166 Wh/kg is **65% of a 257 Wh/kg state-of-the-art 21700 cell** (C-04: 118 kWh / 458.7 kg cells, Lucid Air teardown). A 65% cell-to-pack ratio is normal for a liquid-cooled EV pack, so the pack is achievable with **current cells**, not exotic chemistry. But it leaves **zero** margin for mounts, busbars, seal, and tolerance. A normal 10% margin needs **187 Wh/kg** (73% cell-to-pack), which is beyond current production packs. M3 is therefore a **knife-edge**: the chemistry is available, the packaging margin is not.

---

## 3. Heat

- Continuous 10 kW at 95% path: ~0.5 kW; with pack internal loss, allow **1.0 kW**.
- 150 L cube-equivalent area 1.69 m²; at \(h = 50\) W/m²K, \(\Delta T \approx 11.8\) K. Passive/natural convection is adequate; no radiator mass is charged.
- 30 kW / 10 s pulse, 5% loss = 15 kJ; 88 kg pack at ~1 kJ/kgK rises **0.17 K**. Thermal mass handles the pulse.
- **Verdict:** heat is not binding for M3. This is consistent with `SYSTEM_LIMITS.md` §7.

---

## 4. Volume

- Pack at 300 Wh/L: 14.62 / 0.300 = **48.7 L**.
- PM100: **5.5 L**.
- BOP, busbars, mounts: ~10 L.
- Total ≈ **64 L of 150 L**.
- **Verdict:** volume is not binding. The 100 kg mass target binds first.

---

## 5. Cost (screening, not a quote)

| Item | Cost | Basis |
|---|---:|---|
| Pack | $2,193 | 14.62 kWh × $150/kWh (E1) |
| BOP/structure | $2,000 | E0 allowance |
| Converter | ≤$15,807 | remainder of $20,000; **price not published** |
| **Total** | **≤$20,000** | plausible only if the converter is ≤$15.8k |

A 100 kW traction inverter is not a $500 item; $5–10k is a planning range (E0, no quote). The $20k target is plausible but unverified. The $1.00/kWh target is separate and depends on duty cycle; it is not established here.

---

## 6. The AC branch fails

A Deye SUN-30K 50 Hz hybrid inverter is **80 kg**. With 1.25 packaging it is 100 kg, leaving **negative** mass for the pack. Without packaging, 80 kg + 2.6 kg BOP leaves 17.4 kg for 14.62 kWh → **≥840 Wh/kg**, which no known pack approaches.

**Therefore:** if M3's 30 kW load is 50 Hz AC, **M3 fails at 100 kg** and must be re-scoped (≈180 kg or a lower peak). No cell chemistry fixes an 80 kg inverter.

---

## 7. Verdict and decision rule

**Verdict: conditional pass for a DC/motor load at zero mass margin; fail for a 50 Hz AC load; not closed.**

To close M3, three things are required:

1. **Owner declares the load**: DC/motor or 50 Hz AC.
2. **One pack datasheet at ≥166 Wh/kg pack-level**, with mass, volume, cycle life, and price. Teardown figures (C-04) set the cell anchor, not the pack claim.
3. **A margin decision**: zero margin (166 Wh/kg, top-tier current pack) or 10% margin (187 Wh/kg, next-generation pack). If 10%, either accept a ~110 kg envelope or defer M3 to a 2028+ pack.

**Do not claim M3 passes today.** The honest statement is: *M3 is the closest mission; it is feasible on paper with current 21700-class cells and no mass margin, and it becomes impossible if the load is 50 Hz AC.*

---

## 8. Sources

- Cascadia Motion PM100 spec sheet: https://stealthev.com/wp-content/uploads/2019/06/PM100-Spec-Sheet.pdf (7.5 kg, 5.5 L, 100 kW/10 s; accessed 2026-10-23).
- Deye SUN-30K-SG01HP3: https://www.deyeinverter.com/product/three-phase-high-voltage-hybrid-inverter/sun29-9-30-35-40-50ksg01hp3eubm3-4-29-950kw-three-phase-2-3-4-mppt-hybrid-inverter-hv-battery-supported-339.html (80 kg; accessed 2026-10-23).
- `limits.py` §8–9 for the arithmetic; `COMPONENT_EVIDENCE.md` for the component records.
