# Project E — Component Evidence

**Version:** 0.1  
**Date:** 2026-10-23  
**Status:** primary-source datasheet check; not a quotation, not a purchase, not a design  
**Rule:** every number below is quoted from the linked source or labelled *calculated*. No number is inferred from a blog.

---

## 1. Why this file exists

The Gate 2 screen left one decision-critical unknown: converter specific mass. `SYSTEM_LIMITS.md` used **1.5 kg/kW** as an assumption and showed that M3 flips between 355 and 186 Wh/kg pack over 0.5–1.5 kg/kW. This file replaces the guess with two real 30 kW-class products and records what they do to M3.

---

## 2. Verified components

### C-01 — Cascadia Motion PM100 propulsion inverter

| Item | Value | Source |
|---|---|---|
| Model | PM100DX / PM100DZ | PM100 spec sheet, p. 1 |
| Peak output power | 100 kW (10 s) | same |
| Continuous motor current | 300 A (DX) / 150 A (DZ) | same |
| DC bus | 50–400 V (DX), 100–800 V (DZ) | same |
| Mass | **7.5 kg** | same |
| Volume | **5.5 L** (200 × 87 × 314 mm) | same |
| Cooling | liquid, 8–10 L/min | same |
| Efficiency | not stated on the spec sheet | — |

**Source:** Cascadia Motion, *PM100 Propulsion Inverter* spec sheet, https://stealthev.com/wp-content/uploads/2019/06/PM100-Spec-Sheet.pdf (accessed 2026-10-23); product family: https://www.cascadiamotion.com/inverters.

**What it is:** a traction inverter that drives a 3-phase motor. It is **not** a 50/60 Hz grid-forming AC supply. Its 100 kW/10 s rating covers M3's 30 kW/10 s pulse with margin, and 7.5 kg is **0.25 kg/kW at 30 kW** (the unit does not scale down linearly; the whole unit is 7.5 kg).

### C-02 — Deye SUN-30K-SG01HP3 hybrid inverter

| Item | Value | Source |
|---|---|---|
| Model | SUN-30K-SG01HP3 | Deye product page |
| Rated AC power | 30 kW | same |
| Mass | **80 kg** | same |
| Type | three-phase hybrid inverter, 50/60 Hz, grid-forming | same |

**Source:** Deye, *SUN-29.9/30/35/40/50K-SG01HP3-EU-BM3/BM4*, https://www.deyeinverter.com/product/three-phase-high-voltage-hybrid-inverter/sun29-9-30-35-40-50ksg01hp3eubm3-4-29-950kw-three-phase-2-3-4-mppt-hybrid-inverter-hv-battery-supported-339.html (accessed 2026-10-23). A distributor lists 60 kg; the manufacturer page lists **80 kg**. Use the manufacturer figure.

### C-03 — Delhi diesel retail price

| Item | Value | Source |
|---|---|---|
| Diesel RSP, Delhi | **₹95.20/L** on 2026-10-21 | PPAC, Government of India |
| Converted | **$1.006/L** at ₹94.593871/USD | calculation |

**Source:** PPAC, *Archive — Important News*, https://ppac.gov.in/archives/impnews (accessed 2026-10-23).

### C-04 — Lucid Air cell-level energy density (teardown, E1)

| Item | Value | Source |
|---|---|---|
| Pack energy | 118 kWh (Dream Edition) | BatteryDesign teardown |
| Cell count / mass | 6,600 cells × 69.5 g = **458.7 kg** | same |
| Cell-level specific energy | **257 Wh/kg** (118,000 / 458.7) | calculated |
| Pack mass | not published | — |
| Pack at 65% cell-to-pack | **167 Wh/kg** | calculated |

**Source:** BatteryDesign.net, *Lucid Motors*, https://www.batterydesign.net/lucid-motors/ (updated 2026-10-08; accessed 2026-10-23). This is a teardown analysis, **E1**, not a manufacturer datasheet. The pack mass is not published, so no pack-level figure is claimed.

**What it means:** M3's **166 Wh/kg pack is 65% of a 257 Wh/kg state-of-the-art 21700 cell**. A 65% cell-to-pack ratio is normal for a liquid-cooled EV pack, so M3's pack is **achievable with current cells**, not exotic. The problem is the zero mass margin, not the chemistry.

---

## 3. What this does to M3

M3: 10 kWh delivered, 10 kW average, 30 kW/10 s pulse, ≤100 kg, ≤150 L.

Nameplate at the plan's chain (0.95 converter, 0.80 DoD, 0.90 round-trip) is **14.62 kWh**. BOP allowance 2.6 kg; packaging 1.25 on the converter.

| Converter | Packaged converter mass | Mass left for pack | Required pack |
|---|---:|---:|---:|
| PM100 (motor load) | 9.4 kg | 88.0 kg | **166 Wh/kg** |
| Deye 30K (50 Hz AC load) | 100 kg | negative | **≥840 Wh/kg**, i.e. impossible |

**Findings**

1. **M3's verdict depends on the load type, not on a new technology.** For a motor or DC load, a 7.5 kg PM100-class inverter leaves 88 kg for the pack, so **166 Wh/kg pack** is enough. That is at the edge of current EV packs (150–170 Wh/kg, E1) but not beyond them.
2. **The pack is not exotic.** 166 Wh/kg is 65% of a 257 Wh/kg 21700 cell (C-04), a normal cell-to-pack ratio. The remaining risk is the zero margin, not the cell chemistry.
3. **For a 50 Hz AC load, the same mission fails outright.** An 80 kg hybrid inverter consumes the entire 100 kg budget before the pack. No pack chemistry fixes that.
4. **Therefore the first M3 action is a one-line mission decision:** is the 30 kW load a motor/DC load or a 50 Hz AC load? Until that is fixed, the M3 pass/fail is undefined.

---

## 4. What is still missing

| Gap | Why it matters | Cheapest closure |
|---|---|---|
| A 10 kWh pack datasheet at ≥166 Wh/kg **pack-level** | M3's remaining mass is the pack; EV pack figures are teardown-level, not a product sheet | One supplier datasheet (EV or marine NMC) |
| PM100 efficiency at 10–30 kW | The 0.95 converter assumption is unverified | Manufacturer efficiency map or one bench point |
| PM100 production price | M3 capex ≤$20,000 | Quote; not a list price |
| 6 kW inverter mass | M1 uses 1.5 kg/kW; the same class of unit may be lighter | One datasheet |

**Evidence grade:** C-01 and C-02 are **E2** for mass, volume, and rated power (manufacturer documents). C-03 is **E2** (government source). The pack remains **E1**. No component has been purchased or tested.
