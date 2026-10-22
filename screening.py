"""Project E Gate 2 screening calculations (outside the tracked repository).

Purpose: first-principles mass/energy screens for the provisional missions.
All inputs are declared; results are screening estimates, not product data.
Run: python3 screening.py
"""

from __future__ import annotations

from dataclasses import dataclass


DELIVERED_KWH = 10.0
CONVERTER_EFF = 0.95
CONVERTER_KG_PER_KW = 1.5
PEAK_KW = 6.0
PACKAGING = 1.25
CONVERTER_KG = CONVERTER_KG_PER_KW * PEAK_KW * PACKAGING  # 11.25 kg
H2_LHV_KWH_PER_KG = 33.33
DIESEL_LHV_KWH_PER_L = 9.94
DIESEL_DENSITY_KG_PER_L = 0.83


@dataclass(frozen=True)
class Screen:
    name: str
    mass_kg: float
    note: str


def storage_pack(
    pack_wh_kg: float,
    nameplate_kwh: float = 14.62,
    packaging: float = PACKAGING,
    converter_kg: float = CONVERTER_KG,
    label: str | None = None,
) -> Screen:
    """M1 A1-style storage screen using the repository's nameplate basis.

    14.62 kWh = 10 kWh delivered / 0.95 converter / 0.80 degradation,
    divided by the 5-95% SOC window. This matches the repo's A1 basis.
    The 175 Wh/kg input is treated as pre-packaging (cell-level) because the
    repository applies a 1.25 packaging factor to it; if 175 is truly
    pack-level, the packaging factor is a double count (audit D14).
    """
    cells_kg = nameplate_kwh * 1000.0 / pack_wh_kg
    packaged_kg = cells_kg * packaging
    balance_kg = 2.6  # radiator/structure allowance used by the repo's A1
    total = packaged_kg + converter_kg + balance_kg
    return Screen(
        label or f"storage @ {pack_wh_kg:.0f} Wh/kg",
        total,
        f"cells {cells_kg:.1f} kg; packaged {packaged_kg:.1f}; converter {converter_kg:.1f}; BOP {balance_kg:.1f}",
    )


def diesel_hybrid() -> Screen:
    """C2-style diesel + 0.3 kWh buffer, one packaging pass, fuel included.

    source_kw = (10 / 8 / 0.95) * 1.1 = 1.447 kW.
    Fuel = 10 / (eta_lhv * 0.95) / 9.94 L/kWh, with part-load eta.
    Radiator = 3.33 m2 * 3 kg/m2 (repo C2 term).
    The repo's 50.3 kg double-packages the fuel; the corrected one-pass screen
    is ~49.3 kg. The difference is recorded, not hidden.
    """
    avg_dc_kw = DELIVERED_KWH / 8.0 / CONVERTER_EFF
    source_kw = avg_dc_kw * 1.1
    load_fraction = avg_dc_kw / source_kw
    eta = 0.28 * (0.35 + 0.65 * load_fraction)
    fuel_kwh = DELIVERED_KWH / (eta * CONVERTER_EFF)
    litres = fuel_kwh / DIESEL_LHV_KWH_PER_L
    fuel_kg = litres * DIESEL_DENSITY_KG_PER_L
    genset_kg = source_kw * 12.0
    buffer_kg = 0.3 * 1000.0 / 175.0
    radiator_kg = 3.33 * 3.0
    base = (genset_kg + buffer_kg + fuel_kg) * PACKAGING
    total = base + radiator_kg + CONVERTER_KG
    return Screen(
        "diesel hybrid",
        total,
        f"source {source_kw:.3f} kW; fuel {litres:.2f} L ({fuel_kg:.2f} kg); radiator {radiator_kg:.1f}; converter {CONVERTER_KG:.2f}; repo 50.3 kg",
    )


def tpv_store(usable_kwh_per_kg: float) -> Screen:
    """M4 TPV + graphite store; usable delta-T, not full-swing 0.28 kWh/kg.

    Thermal input = 10 / (0.32 * 0.85 * 0.95) = 38.7 kWh.
    Usable store density is the top slice of the graphite sensible heat, not
    the full 1800 K-to-ambient swing. 0.06-0.10 kWh/kg is a screening range;
    the repo's 0.28 kWh/kg is a full-swing number and is not usable at a
    >=1500 C emitter.
    """
    eta = 0.32 * 0.85 * 0.95
    thermal_kwh = DELIVERED_KWH / eta
    graphite_kg = thermal_kwh / usable_kwh_per_kg
    vessel_kg = graphite_kg * 0.25
    return Screen(
        f"TPV usable store @ {usable_kwh_per_kg:.2f} kWh/kg",
        graphite_kg + vessel_kg,
        f"eta {eta:.3f}; thermal {thermal_kwh:.1f} kWh; graphite {graphite_kg:.1f} kg; vessel 25%; excludes emitter/cells/radiator",
    )


def fuel_cell() -> Screen:
    """C1-style PEM + 0.3 kWh buffer + 5 wt% H2 tank, average-sized stack.

    source_kw = 1.447 kW (1.1x average); stack 8 kg/kW; tank 5 wt%;
    converter 11.25 kg; buffer 1.71 kg; BOP 6 kg; radiator 4.8 kg.
    The repo reports 56.5 kg; this one-pass screen gives ~56.0 kg.
    """
    avg_dc_kw = DELIVERED_KWH / 8.0 / CONVERTER_EFF
    source_kw = avg_dc_kw * 1.1
    stack_kg = source_kw * 8.0
    h2_kg = DELIVERED_KWH / (0.50 * CONVERTER_EFF * H2_LHV_KWH_PER_KG)
    tank_kg = h2_kg / 0.05
    buffer_kg = 0.3 * 1000.0 / 175.0
    bop_kg = 6.0
    base = (stack_kg + tank_kg + buffer_kg + bop_kg) * PACKAGING
    total = base + CONVERTER_KG + 4.8
    return Screen(
        "PEM + 5 wt% H2",
        total,
        f"source {source_kw:.3f} kW; H2 {h2_kg:.3f} kg; tank {tank_kg:.1f}; stack {stack_kg:.1f}; buffer {buffer_kg:.1f}; repo 56.5 kg",
    )


def solar() -> Screen:
    """M1 solar + 14.62 kWh storage on the same basis as A1.

    External sunlight; 1 kW average, 25% module, 1 kW/m2 -> 4 m2.
    Panel 20 kg/kW screening allowance; pack 104.4 kg; converter 11.25 kg.
    Mounting, MPPT, and charge controller are excluded and would add mass.
    """
    area_m2 = 1.0 / (0.25 * 1.0)
    panel_kg = 20.0
    battery_cells = 14.62 * 1000.0 / 175.0
    battery_pack = battery_cells * PACKAGING
    total = panel_kg + battery_pack + CONVERTER_KG
    return Screen(
        "solar + 14.62 kWh storage",
        total,
        f"area {area_m2:.1f} m2; panel {panel_kg:.1f} kg; pack {battery_pack:.1f} kg; converter {CONVERTER_KG:.2f}; mounting/MPPT excluded",
    )


def supercap_buffer() -> Screen:
    """0.05 kWh pulse buffer at 6 Wh/kg; no mission energy."""
    mass = 0.05 * 1000.0 / 6.0
    return Screen("supercap buffer 0.05 kWh", mass, f"{mass:.1f} kg at 6 Wh/kg; fails H7 <=5 kg")


def nuclear_range() -> Screen:
    """M2 concept screen, not a design and not comparable to M1.

    1 kWe fission-Stirling; published concept range 100-1000 kg. The midpoint
    is shown only to expose the spread; it is not a system mass.
    """
    low, high = 100.0, 1000.0
    return Screen(
        "fission-Stirling 1 kWe (M2)",
        (low + high) / 2.0,
        f"concept range {low:.0f}-{high:.0f} kg; midpoint only; shielding/regulatory not modeled; not M1",
    )


def a1_sensitivity() -> list[Screen]:
    """One-at-a-time sensitivity around A1 at 175 Wh/kg."""
    return [
        storage_pack(140),
        storage_pack(175),
        storage_pack(200),
        storage_pack(175, packaging=1.15, label="storage @ 175 Wh/kg (package 1.15)"),
        storage_pack(175, packaging=1.40, label="storage @ 175 Wh/kg (package 1.40)"),
        storage_pack(175, converter_kg=6.0 * 0.8 * PACKAGING, label="storage @ 175 Wh/kg (converter 0.8)"),
        storage_pack(175, converter_kg=6.0 * 3.0 * PACKAGING, label="storage @ 175 Wh/kg (converter 3.0)"),
    ]


def main() -> None:
    print("M1 self-contained candidates (same boundary)")
    print(f"{'screen':34s} {'mass_kg':>9s}  note")
    print("-" * 110)
    for r in [
        storage_pack(175),
        storage_pack(300),
        storage_pack(500),
        storage_pack(870),
        diesel_hybrid(),
        fuel_cell(),
        supercap_buffer(),
    ]:
        print(f"{r.name:34s} {r.mass_kg:9.1f}  {r.note}")

    print("\nOther mission / boundary (not comparable to M1)")
    print(f"{'screen':34s} {'mass_kg':>9s}  note")
    print("-" * 110)
    for r in [
        tpv_store(0.10),
        tpv_store(0.06),
        solar(),
        nuclear_range(),
    ]:
        print(f"{r.name:34s} {r.mass_kg:9.1f}  {r.note}")

    print("\nA1 sensitivity (one-at-a-time, not Monte Carlo)")
    print(f"{'screen':34s} {'mass_kg':>9s}  note")
    print("-" * 110)
    for r in a1_sensitivity():
        print(f"{r.name:34s} {r.mass_kg:9.1f}  {r.note}")

    # Self-checks: fail loudly if the screening logic breaks.
    a1 = storage_pack(175)
    assert 115.0 < a1.mass_kg < 121.0, a1.mass_kg
    assert storage_pack(870).mass_kg < 36.0
    assert tpv_store(0.10).mass_kg > 400.0
    assert 55.0 < fuel_cell().mass_kg < 58.0
    assert 47.0 < diesel_hybrid().mass_kg < 52.0
    assert solar().mass_kg > 120.0
    assert supercap_buffer().mass_kg > 5.0
    # Golden values: catch a formula change, not just a shifted band.
    assert abs(storage_pack(175).mass_kg - 118.3) < 0.1
    assert abs(fuel_cell().mass_kg - 56.0) < 0.1
    assert abs(diesel_hybrid().mass_kg - 49.3) < 0.1
    assert abs(tpv_store(0.10).mass_kg - 483.7) < 0.5
    # Independent rounded-number identities: H2 and diesel energy closure.
    assert abs(0.632 * H2_LHV_KWH_PER_KG * 0.50 * 0.95 - DELIVERED_KWH) < 0.02
    assert abs(4.02 * DIESEL_LHV_KWH_PER_L * 0.263 * 0.95 - DELIVERED_KWH) < 0.05
    print("\nself-checks passed")


if __name__ == "__main__":
    main()
