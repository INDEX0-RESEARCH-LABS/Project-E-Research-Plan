# M4 closure: the radiator is feasible; the converter capex is not

Status: **fails the $1/W capex target by 14–18× with a commercial 10 kW Stirling**.
Date: 2026-10-23. E0 price anchor; E1 heat/mass arithmetic.
Related: `MISSION_MATRIX.md` §3–4, `SYSTEM_LIMITS.md` §8.

## 1. Mission and boundary

| Item | Value |
|---|---|
| Electric output | 10 kWe (80 MWh/y at 8,000 h) |
| Life | 20 years (160,000 h) |
| Capex target | ≤$1/W = **$10,000** |
| Boundary | external heat **excluded**; converter, cooling, grid interface included |

## 2. Heat and radiator

At 25% conversion, 40 kWth input, 30 kW rejected:

\[
A = \frac{30{,}000 \times 0.35}{10 \times 40} = 26.25\ \text{m}^2,\quad
m = 3\,\text{kg/m}^2 \times 26.25 = 78.8\ \text{kg}.
\]

At 40%, 15 kW rejected: **13.1 m², 39.4 kg**. The radiator is large but
feasible for a stationary unit; it is **not** the binding term. The matrix’s
earlier “150 kg at 25%” used a higher areal mass; the repo formula gives 79 kg.

## 3. Converter capex: the binding term

A commercial 10 kW Stirling is quoted at **$140,000–$185,000** in a 2026 buying
guide (S18, E0; not a quote), i.e. **$14–18.5/W**. The target is **$1/W**, a gap
of **14–18×**. Small ORC units are also multi-$/W; a 6–8 kW Stirling at ≤$4,000
(≈$0.5–0.7/W) appears only as an innovation challenge, not a product.

| Capex | $/W | Capital $/kWh (80 MWh/y × 20 y) | + O&M $0.01 | Total |
|---:|---:|---:|---:|---:|
| $10,000 (target) | $1.0 | $0.006 | $0.016 | $0.016/kWh |
| $140,000 | $14.0 | $0.088 | $0.098 | $0.098/kWh |
| $185,000 | $18.5 | $0.116 | $0.126 | $0.126/kWh |

The LCOE at commercial prices is not the problem; the **capex target** is. M4
is a capital-cost mission.

## 4. Lifetime

160,000 h over 20 years is far beyond a typical small Stirling/ORC service
interval. Seals, heaters, and bearings are replacement items; no replacement
schedule is quoted. This is an unmodelled lifetime cost and a second reason the
$1/W target is not a system number.

## 5. Heat-source boundary

The 40 kWth is excluded. If it is free waste heat, the converter capex is the
only cost. If it is purchased at $0.01/kWh_th, the heat cost is
4 kWh_th/kWh_e × $0.01 = **$0.04/kWh_e**, which would dominate the LCOE. The
mission must declare the heat price, not just “external heat excluded.”

## 6. Verdict

**M4 fails the $1/W target by 14–18× with a commercial 10 kW Stirling.** The
radiator (79 kg, 26 m² at 25%) is feasible and not binding. The mission is
stationary and not mass-constrained, so it is not a compact-core mission. The
invention bet is a mass-produced free-piston Stirling/ORC at ≤$1/W with a
160,000 h service plan; that is not an off-the-shelf product.

## 7. Gate test

1. One quote for a 10 kWe ORC or Stirling at **≤$10,000**, including grid
   interface and controls.
2. Measured heat-to-electric efficiency ≥20% at the declared temperatures.
3. Radiator ≤30 m² at the site ambient, with fan power included.
4. A 160,000 h service plan with replacement intervals and cost.
5. A declared heat price (zero or purchased).

## 8. Kill criteria

- Quote >$10,000 with no path to $1/W at volume → M4 fails capex.
- Efficiency <20% → radiator and heat input grow; recheck.
- No 160,000 h service plan → lifetime cost is unknown; cannot rank.
- Purchased heat >$0.01/kWh_th → LCOE dominated by heat.
