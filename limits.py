#!/usr/bin/env python3
"""
Project E - system limits, mission consistency, and cost floors.

Screening only. Every number is E0/E1 unless a source locator is added in
SOURCE_VERIFICATION.md. This script exists so the documents can be checked
against one runnable calculation.

Run: python3 limits.py
"""

from dataclasses import dataclass

# ---------------------------------------------------------------- constants
PACK = 1.25              # packaging factor on cell/component mass, applied once
CONV_KG_PER_KW = 1.5     # screening converter mass; NOT a datasheet value
ETA_CONV = 0.95          # converter efficiency at the load boundary
DOD = 0.80               # usable depth of discharge
ROUND_TRIP = 0.90        # storage round-trip
ETA_CHAIN = ETA_CONV * DOD * ROUND_TRIP

DIESEL_KWH_PER_L = 9.94  # LHV, standard fuel property
DIESEL_USD_PER_L = 1.40  # E0 planning price (repo assumption)
DIESEL_USD_PER_L_VERIFIED = 95.20 / 94.593871  # PPAC Delhi RSP 2026-10-21, INR/USD 2026-10-22
H2_KWH_PER_KG = 33.33    # LHV, standard property
H2_USD_PER_KG = 6.00     # E0 planning price
SIGMA = 5.670374419e-8   # Stefan-Boltzmann, W/m2/K4


@dataclass(frozen=True)
class Mission:
    id: str
    energy_kwh: float
    hours: float
    peak_kw: float
    mass_kg: float
    volume_l: float
    capex_usd: float
    lcoe_usd_per_kwh: float
    life_y: float
    note: str


MISSIONS = [
    Mission("M1", 10.0, 8.0, 6.0, 35.0, 60.0, 5_000, 0.40, 10,
            "portable pulse; benchmark"),
    Mission("M2", 360.0, 720.0, 5.0, 500.0, 1_000.0, 50_000, 0.50, 10,
            "long-duration remote, 30 days"),
    Mission("M3", 10.0, 1.0, 30.0, 100.0, 150.0, 20_000, 1.00, 5,
            "high-power compact"),
    Mission("M5", 4_000.0, 4.0, 1_000.0, 25_000.0, 40_000.0, 480_000, 0.08, 15,
            "bulk stationary, 1 MW / 4 h"),
]


def nameplate_kwh(m: Mission) -> float:
    """Stored nameplate energy needed for the delivered mission energy."""
    return m.energy_kwh / ETA_CHAIN


def converter_mass(m: Mission, kg_per_kw: float = CONV_KG_PER_KW) -> float:
    return kg_per_kw * m.peak_kw * PACK


def bop_mass(m: Mission) -> float:
    """Screening balance-of-plant rule: fixed 2 kg plus 0.06 kg/kWh."""
    return 2.0 + 0.06 * m.energy_kwh


def storage_bound(m: Mission, kg_per_kw: float = CONV_KG_PER_KW):
    """Required cell and pack specific energy for an all-storage mission."""
    conv = converter_mass(m, kg_per_kw)
    bop = bop_mass(m)
    packaged_avail = m.mass_kg - conv - bop
    cells = packaged_avail / PACK
    nameplate = nameplate_kwh(m)
    cell_wh_kg = nameplate * 1000.0 / cells
    pack_wh_kg = nameplate * 1000.0 / packaged_avail
    overhead = (conv + bop) / m.mass_kg
    return cells, cell_wh_kg, pack_wh_kg, overhead


def enclosure_area_m2(volume_l: float) -> float:
    """Cube-equivalent external area; real enclosures are worse."""
    return 6.0 * (volume_l / 1000.0) ** (2.0 / 3.0)


def forced_air_rejection_w(volume_l: float, dT_k: float, h=50.0) -> float:
    return h * enclosure_area_m2(volume_l) * dT_k


def radiative_flux_w_m2(t_hot_k: float, t_amb_k=300.0, emissivity=0.9) -> float:
    return emissivity * SIGMA * (t_hot_k ** 4 - t_amb_k ** 4)


def carnot(t_hot_k: float, t_cold_k: float = 300.0) -> float:
    return 1.0 - t_cold_k / t_hot_k


def teg_fraction(zt: float, t_hot_k: float, t_cold_k: float = 300.0) -> float:
    """Ideal TEG efficiency as a fraction of Carnot (standard expression)."""
    s = (1.0 + zt) ** 0.5
    return (s - 1.0) / (s + t_cold_k / t_hot_k)


def fuel_cost_per_kwh(price_per_unit, kwh_per_unit, efficiency):
    return price_per_unit / (kwh_per_unit * efficiency)


def missions_for_target(m: Mission, fuel_usd_per_kwh: float) -> float:
    """Missions needed to amortise capex inside the LCOE target."""
    margin = m.lcoe_usd_per_kwh - fuel_usd_per_kwh
    if margin <= 0:
        return float("inf")
    return m.capex_usd / (margin * m.energy_kwh)


def max_missions(m: Mission, missions_per_day: float) -> float:
    """Cap the duty cycle by the mission duration, not just the assumed rate."""
    rate = min(missions_per_day, 24.0 / m.hours)
    return rate * 365.0 * m.life_y


def hdr(title):
    print("\n" + title)
    print("-" * len(title))


# ---------------------------------------------------------------- self-checks
def self_check():
    assert abs(converter_mass(MISSIONS[0]) - 11.25) < 1e-9
    assert abs(fuel_cost_per_kwh(DIESEL_USD_PER_L_VERIFIED, DIESEL_KWH_PER_L, 0.263) - 0.385) < 0.001
    cells, cell, pack, _ = storage_bound(MISSIONS[0])
    assert 860 < cell < 868, cell
    assert 688 < pack < 694, pack
    assert abs(enclosure_area_m2(60) - 0.9198) < 0.001
    assert abs(fuel_cost_per_kwh(DIESEL_USD_PER_L, DIESEL_KWH_PER_L, 0.263) - 0.536) < 0.002
    assert abs(fuel_cost_per_kwh(H2_USD_PER_KG, H2_KWH_PER_KG, 0.50) - 0.360) < 0.002
    assert abs(carnot(1800) - 0.83333) < 1e-4
    # identity: (E/eta)*eta == E
    for m in MISSIONS:
        assert abs(nameplate_kwh(m) * ETA_CHAIN - m.energy_kwh) < 1e-9
    print("self-check: PASS")


# ---------------------------------------------------------------- reports
def report_missions():
    hdr("1. All-storage mission bound (packaging 1.25, converter 1.5 kg/kW)")
    print(f"{'id':>3} {'E kWh':>7} {'namepl':>8} {'conv kg':>8} {'bop kg':>7} "
          f"{'cells kg':>9} {'cell Wh/kg':>11} {'pack Wh/kg':>11} {'overhead':>9}")
    for m in MISSIONS:
        cells, cell, pack, overhead = storage_bound(m)
        print(f"{m.id:>3} {m.energy_kwh:>7.0f} {nameplate_kwh(m):>8.1f} "
              f"{converter_mass(m):>8.2f} {bop_mass(m):>7.1f} {cells:>9.1f} "
              f"{cell:>11.0f} {pack:>11.0f} {overhead:>8.0%}")

    hdr("2. Converter-mass sensitivity (the largest single assumption)")
    for m in MISSIONS:
        row = []
        for kg_kw in (0.5, 1.0, 1.5):
            _, cell, pack, _ = storage_bound(m, kg_kw)
            row.append(f"{kg_kw:.1f}kg/kW: {pack:.0f} Wh/kg pack / {cell:.0f} cell")
        print(f"{m.id}: " + " | ".join(row))


def report_heat():
    hdr("3. Heat rejection")
    print("Cube-equivalent enclosure area:")
    for v in (60, 150, 1000, 40_000):
        print(f"  {v:>6} L -> {enclosure_area_m2(v):.2f} m2")

    print("\nForced-air rejection at h=50 W/m2K, dT=20 K:")
    for v in (60, 150, 1000):
        print(f"  {v:>6} L -> {forced_air_rejection_w(v, 20):.0f} W")

    print("\nRadiative flux (eps=0.9, sink 300 K):")
    for t in (350, 450, 600, 800):
        print(f"  {t} K -> {radiative_flux_w_m2(t):.0f} W/m2")

    print("\nM1 diesel waste heat at 26.3% overall, 1.25 kW average:")
    waste = 1.25 / 0.263 - 1.25
    print(f"  waste {waste:.2f} kW; required dT in a 60 L box at h=50: "
          f"{waste * 1000 / (50 * enclosure_area_m2(60)):.0f} K")

    print("\nM4 10 kWe waste heat and forced-air area at dT=20 K, h=50:")
    for eta in (0.20, 0.30, 0.40):
        waste = 10 / eta - 10
        area = waste * 1000 / (50 * 20)
        print(f"  eta {eta:.0%}: waste {waste:.1f} kW, area {area:.1f} m2, "
              f"mass at 5 kg/m2 {area * 5:.0f} kg")


def report_conversion():
    hdr("4. Conversion ceilings")
    for t in (800, 1200, 1800, 2200):
        print(f"  Carnot {t} K / 300 K: {carnot(t):.1%}")
    print(f"  TEG ZT=1 at 800 K: {teg_fraction(1, 800):.1%} of Carnot "
          f"= {teg_fraction(1, 800) * carnot(800):.1%} ideal")
    print(f"  H2/O2 fuel cell dG/dH at 25 C: {237.1 / 285.8:.1%} (thermodynamic)")
    print(f"  TPV 40% cell at 2200 K: {0.40 / carnot(2200):.0%} of Carnot")


def report_cost():
    hdr("5. Fuel-cost floors")
    diesel = fuel_cost_per_kwh(DIESEL_USD_PER_L, DIESEL_KWH_PER_L, 0.263)
    h2 = fuel_cost_per_kwh(H2_USD_PER_KG, H2_KWH_PER_KG, 0.50)
    h2_cheap = fuel_cost_per_kwh(4.0, H2_KWH_PER_KG, 0.50)
    print(f"  diesel ${DIESEL_USD_PER_L}/L at 26.3%: ${diesel:.3f}/kWh")
    print(f"  H2 ${H2_USD_PER_KG}/kg at 50% LHV: ${h2:.3f}/kWh")
    print(f"  H2 $4/kg at 50% LHV: ${h2_cheap:.3f}/kWh")

    hdr("6. Capex amortisation inside the mission LCOE target")
    for m in MISSIONS:
        for fuel in (0.05, 0.10, 0.20, 0.36, 0.54):
            n = missions_for_target(m, fuel)
            limit = max_missions(m, 3.0)  # generous: 3 missions/day
            verdict = "ok" if n <= limit else "IMPOSSIBLE at 3/day"
            print(f"  {m.id} fuel ${fuel:.2f}/kWh -> {n:>9.0f} missions "
                  f"(3/day over {m.life_y:.0f} y = {limit:.0f}) {verdict}")
        print()


def m3_pack_required(converter_kg: float, margin_kg: float = 0.0):
    """M3 pack specific energy for an absolute converter mass and mass margin."""
    m = MISSIONS[2]
    avail = m.mass_kg - converter_kg * PACK - bop_mass(m) - margin_kg
    if avail <= 0:
        return float("inf"), avail
    return nameplate_kwh(m) * 1000.0 / avail, avail


def report_m3_closure():
    hdr("9. M3 closure: converter, pack, margin, heat, volume")
    m = MISSIONS[2]
    print(f"  nameplate {nameplate_kwh(m):.2f} kWh; envelope {m.mass_kg:.0f} kg / {m.volume_l:.0f} L")
    for label, conv in (("PM100 7.5 kg", 7.5), ("assumed 15 kg", 15.0), ("Deye 80 kg", 80.0)):
        for margin in (0.0, 10.0):
            pack, avail = m3_pack_required(conv, margin)
            print(f"  {label:14s} margin {margin:2.0f} kg: avail {avail:6.1f} kg -> pack {pack:6.1f} Wh/kg")
    area = enclosure_area_m2(m.volume_l)
    print(f"  enclosure area {area:.2f} m2; 1.0 kW loss -> dT {1000/(50*area):.1f} K")
    print(f"  pulse 30 kW/10 s, 5% loss = {0.05*30*10:.1f} kJ; 88 kg pack at 1 kJ/kgK -> "
          f"{0.05*30*10/(88*1.0):.2f} K")
    print(f"  pack volume at 300 Wh/L: {nameplate_kwh(m)/0.300:.1f} L of {m.volume_l:.0f} L")


def report_diesel_sensitivity():
    hdr("8. Diesel cost: verified Delhi price, efficiency, capex, duty")
    price = DIESEL_USD_PER_L_VERIFIED
    print(f"  verified Delhi RSP: Rs 95.20/L / 94.593871 = ${price:.4f}/L")
    for eta in (0.263, 0.30, 0.35, 0.40):
        print(f"  eta {eta:.1%}: fuel ${fuel_cost_per_kwh(price, DIESEL_KWH_PER_L, eta):.3f}/kWh")
    print("  total $/kWh = fuel + capex/(missions_per_year * 10 kWh * 10 y)")
    for missions in (250, 500, 750):
        for capex in (2000, 3000, 5000):
            cap = capex / (missions * 10.0 * 10.0)
            fuel = fuel_cost_per_kwh(price, DIESEL_KWH_PER_L, 0.35)
            print(f"    {missions:4d}/y  ${capex:5d}  capital ${cap:.3f}  "
                  f"+ fuel(35%) ${fuel:.3f} = ${cap + fuel:.3f}")
    print("  max capex for $0.40 at 250 missions/y:")
    for eta in (0.263, 0.30, 0.35, 0.40):
        fuel = fuel_cost_per_kwh(price, DIESEL_KWH_PER_L, eta)
        print(f"    eta {eta:.1%}: ${max(0.0, (0.40 - fuel)) * 250 * 10 * 10:,.0f}")


def report_sources():
    hdr("7. Source energy density at system level")
    print("  diesel LHV 9.94 kWh/L, 11.9 kWh/kg; at 30% = 3.6 kWh/kg fuel")
    print("  H2 LHV 33.33 kWh/kg; at 50% = 16.7 kWh/kg fuel;")
    print("    5 wt% system tank -> 0.83 kWh/kg fuel+tank; 10 wt% -> 1.67")
    print("  U-235 fission 8.2e13 J/kg = 22.8 GWh/kg; engine+shield dominate")
    print("  Li-ion cell 250-300 Wh/kg; pack 150-250 Wh/kg (E1, no datasheet)")
    print("  graphite sensible heat, cp 0.72 kJ/kgK, 500 K usable = 0.10 kWh/kg")


if __name__ == "__main__":
    self_check()
    report_missions()
    report_heat()
    report_conversion()
    report_cost()
    report_sources()
    report_diesel_sensitivity()
    report_m3_closure()
