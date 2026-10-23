"""First-principles volume, heat-rejection and energy relations.

The model is deliberately small and dependency-free. It answers one question:
*given a power, a duration and a mechanism, what is the minimum complete-system
volume?* It does not claim that a mechanism is buildable.

Units are explicit in every name. Temperatures are kelvin. Volumes are litres
unless the name ends in ``_m3``. Powers are kW unless the name ends in ``_w``.

Provenance of constants
-----------------------
``LHV_DIESEL_KWH_PER_L`` and ``LHV_H2_KWH_PER_KG`` are standard lower heating
values used by the frozen benchmark (``project_e.models.conversion``).
``H2_700BAR_KG_PER_L`` is the approximate density of hydrogen **gas** at
700 bar, 15 C (E0), not the density of a complete storage system. A Type IV
pressure vessel has an external/internal volume ratio of roughly 1.4-1.7, so
the gas volume must not be presented as the vessel volume. The ``packaging``
factor in ``h2_storage_volume_l`` is a separate, blunt enclosure multiplier;
it is not a Type IV vessel calculation. Every mechanism-specific value lives
in ``mechanisms.py`` with its own evidence label.
"""

from __future__ import annotations

import math

LHV_DIESEL_KWH_PER_L = 9.94
LHV_H2_KWH_PER_KG = 33.33
H2_700BAR_KG_PER_L = 0.040
W_PER_KW = 1000.0
L_PER_M3 = 1000.0


def _positive(name: str, value: float) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and > 0, got {value!r}")
    return float(value)


def _fraction(name: str, value: float) -> float:
    if not math.isfinite(value) or not 0.0 < value <= 1.0:
        raise ValueError(f"{name} must be in (0, 1], got {value!r}")
    return float(value)


def box_volume_l(x_m: float, y_m: float, z_m: float) -> float:
    """External box volume in litres."""
    for name, value in (("x_m", x_m), ("y_m", y_m), ("z_m", z_m)):
        _positive(name, value)
    return x_m * y_m * z_m * L_PER_M3


def box_surface_area_m2(x_m: float, y_m: float, z_m: float) -> float:
    """External box surface area in square metres."""
    for name, value in (("x_m", x_m), ("y_m", y_m), ("z_m", z_m)):
        _positive(name, value)
    return 2.0 * (x_m * y_m + x_m * z_m + y_m * z_m)


def volumetric_power_density_mw_m3(power_kw: float, volume_l: float) -> float:
    """Power per external volume, in MW/m^3 (1 kW/L = 1 MW/m^3)."""
    p = _positive("power_kw", power_kw)
    v = _positive("volume_l", volume_l)
    return p / v


def carnot_efficiency(t_hot_k: float, t_cold_k: float) -> float:
    """Carnot limit, 1 - Tc/Th. Absolute temperatures only."""
    th = _positive("t_hot_k", t_hot_k)
    tc = _positive("t_cold_k", t_cold_k)
    if th <= tc:
        raise ValueError(f"hot reservoir ({th} K) must exceed cold ({tc} K)")
    return 1.0 - tc / th


def heat_engine_waste_heat_w(power_kw: float, eta: float) -> float:
    """Waste heat for a heat engine delivering ``power_kw`` at efficiency ``eta``."""
    p = _positive("power_kw", power_kw)
    e = _fraction("eta", eta)
    return p * W_PER_KW * (1.0 / e - 1.0)


def heat_rejection_area_m2(heat_w: float, h_w_m2k: float, delta_t_k: float) -> float:
    """Area needed for Newton cooling: Q = h A dT.

    ``h`` is an effective coefficient, not a material property. The caller must
    supply its basis (natural convection, forced air, liquid cold plate).
    """
    q = _positive("heat_w", heat_w)
    h = _positive("h_w_m2k", h_w_m2k)
    dt = _positive("delta_t_k", delta_t_k)
    return q / (h * dt)


def radiator_volume_l(area_m2: float, thickness_m: float = 0.02) -> float:
    """Volume of a flat heat exchanger of the given face area and thickness."""
    a = _positive("area_m2", area_m2)
    t = _positive("thickness_m", thickness_m)
    return a * t * L_PER_M3


def fuel_volume_l(
    power_kw: float,
    hours: float,
    eta: float,
    lhv_kwh_per_l: float = LHV_DIESEL_KWH_PER_L,
) -> float:
    """Liquid fuel volume for a heat engine over ``hours`` at ``power_kw``."""
    p = _positive("power_kw", power_kw)
    h = _positive("hours", hours)
    e = _fraction("eta", eta)
    lhv = _positive("lhv_kwh_per_l", lhv_kwh_per_l)
    return p * h / (e * lhv)


def battery_pack_volume_l(
    energy_kwh: float,
    cell_wh_l: float,
    packaging: float = 1.25,
    bop_l: float = 0.2,
) -> float:
    """Cell volume plus BOP, multiplied by a packaging factor.

    ``cell_wh_l`` is cell-level volumetric energy density. The packaging factor
    accounts for modules, cooling, enclosure and clearances; it is an explicit
    assumption, not a measured pack value.
    """
    e = _positive("energy_kwh", energy_kwh)
    cell = _positive("cell_wh_l", cell_wh_l)
    pkg = _positive("packaging", packaging)
    bop = _positive("bop_l", bop_l)
    cell_l = e * W_PER_KW / cell
    return (cell_l + bop) * pkg


def h2_storage_volume_l(
    energy_kwh: float,
    eta: float,
    density_kg_per_l: float = H2_700BAR_KG_PER_L,
    packaging: float = 1.25,
) -> float:
    """H2 gas volume at the given gas density, times a blunt packaging factor.

    This is **not** a Type IV vessel calculation. ``density_kg_per_l`` is gas
    density at the storage pressure; the vessel wall, liner and domes add
    roughly 1.4-1.7x in external volume and are not modeled here.
    """
    e = _positive("energy_kwh", energy_kwh)
    eff = _fraction("eta", eta)
    rho = _positive("density_kg_per_l", density_kg_per_l)
    pkg = _positive("packaging", packaging)
    h2_kg = e / (eff * LHV_H2_KWH_PER_KG)
    return h2_kg / rho * pkg


def solar_panel_volume_l(
    power_kw: float,
    module_w_m2: float,
    thickness_m: float = 0.02,
    packaging: float = 1.25,
) -> float:
    """Panel volume only; storage and electronics are added by the caller."""
    p = _positive("power_kw", power_kw)
    flux = _positive("module_w_m2", module_w_m2)
    t = _positive("thickness_m", thickness_m)
    pkg = _positive("packaging", packaging)
    area_m2 = p * W_PER_KW / flux
    return area_m2 * t * L_PER_M3 * pkg


def rtg_volume_l(
    power_kw: float,
    specific_power_w_kg: float,
    density_kg_m3: float,
    shield_factor: float = 2.0,
    packaging: float = 1.25,
) -> float:
    """RTG system volume including a shielding multiplier.

    ``shield_factor`` is a blunt multiplier on the unshielded volume. It is not a
    shielding calculation; it exists to keep the screen honest about a subsystem
    that is often omitted.
    """
    p = _positive("power_kw", power_kw)
    sp = _positive("specific_power_w_kg", specific_power_w_kg)
    rho = _positive("density_kg_m3", density_kg_m3)
    shield = _positive("shield_factor", shield_factor)
    pkg = _positive("packaging", packaging)
    mass_kg = p * W_PER_KW / sp
    return mass_kg / rho * L_PER_M3 * shield * pkg


def energy_for_duration_kwh(power_kw: float, hours: float) -> float:
    p = _positive("power_kw", power_kw)
    h = _positive("hours", hours)
    return p * h


def max_duration_h(energy_kwh: float, power_kw: float) -> float:
    e = _positive("energy_kwh", energy_kwh)
    p = _positive("power_kw", power_kw)
    return e / p
