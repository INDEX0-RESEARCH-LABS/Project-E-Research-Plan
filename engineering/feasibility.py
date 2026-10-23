"""Complete-system volume screen for a fixed electrical power and duration.

The screen is intentionally conservative in the *wrong* direction for a
feasibility claim: it uses the mechanism's best case and still asks whether it
fits. If the best case fails, the conclusion is robust to the uncertainty in
that direction. The worst case shows how far the answer can move.

It is not a design, a BOM, or a thermal simulation. It is a Gate 2 filter.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import physics
from .mechanisms import Case, Mechanism, MECHANISMS


@dataclass(frozen=True)
class ScreenResult:
    mechanism_id: str
    name: str
    category: str
    maturity: str
    kind: str
    hours: float
    target_volume_l: float
    best_volume_l: float
    worst_volume_l: float
    best_components_l: dict[str, float] = field(default_factory=dict)
    worst_components_l: dict[str, float] = field(default_factory=dict)
    best_limiting: str = ""
    worst_limiting: str = ""

    @property
    def best_ratio(self) -> float:
        return self.best_volume_l / self.target_volume_l

    @property
    def worst_ratio(self) -> float:
        return self.worst_volume_l / self.target_volume_l

    @property
    def passes_best(self) -> bool:
        return self.best_volume_l <= self.target_volume_l

    @property
    def passes_worst(self) -> bool:
        return self.worst_volume_l <= self.target_volume_l

    @property
    def verdict(self) -> str:
        if self.passes_best and self.passes_worst:
            return "pass"
        if self.passes_best:
            return "conditional"
        return "fail"


def _summarise(components: dict[str, float]) -> str:
    """Name the largest component, with its share of the total."""
    total = sum(components.values())
    if total <= 0:
        return "unknown"
    name, value = max(components.items(), key=lambda kv: kv[1])
    return f"{name} ({value / total:.0%})"


def _volume_l(kind: str, case: Case, power_kw: float, hours: float) -> tuple[float, dict[str, float]]:
    """Return (complete-system volume, component volumes) for one case."""
    energy_kwh = physics.energy_for_duration_kwh(power_kw, hours)

    if kind == "battery":
        if case.cell_wh_l is None:
            raise ValueError("battery case requires cell_wh_l")
        cells_l = energy_kwh * physics.W_PER_KW / case.cell_wh_l
        components = {"cells": cells_l, "bop": case.bop_l}
        total = (cells_l + case.bop_l) * case.packaging
        return total, components

    if kind == "heat_engine":
        if case.eta is None or case.engine_l_per_kw is None:
            raise ValueError("heat-engine case requires eta and engine_l_per_kw")
        fuel_l = physics.fuel_volume_l(power_kw, hours, case.eta, case.fuel_lhv)
        engine_l = power_kw * case.engine_l_per_kw
        q_w = physics.heat_engine_waste_heat_w(power_kw, case.eta)
        area_m2 = physics.heat_rejection_area_m2(q_w, case.h_w_m2k, case.dt_k)
        radiator_l = physics.radiator_volume_l(area_m2, case.thickness_m)
        components = {
            "engine/generator": engine_l,
            "fuel": fuel_l,
            "radiator": radiator_l,
            "bop": case.bop_l,
        }
        total = sum(components.values()) * case.packaging
        return total, components

    if kind == "fuel_cell":
        if case.eta is None or case.stack_kw_per_l is None:
            raise ValueError("fuel-cell case requires eta and stack_kw_per_l")
        stack_l = power_kw / case.stack_kw_per_l
        h2_l = physics.h2_storage_volume_l(energy_kwh, case.eta, packaging=1.0)
        components = {"stack": stack_l, "H2 tank": h2_l, "bop": case.bop_l}
        total = sum(components.values()) * case.packaging
        return total, components

    if kind == "solar":
        if case.module_w_m2 is None or case.cell_wh_l is None:
            raise ValueError("solar case requires module_w_m2 and cell_wh_l")
        panel_l = physics.solar_panel_volume_l(
            power_kw, case.module_w_m2, case.thickness_m, packaging=1.0
        )
        storage_l = energy_kwh * physics.W_PER_KW / case.cell_wh_l
        components = {"panel": panel_l, "storage": storage_l, "bop": case.bop_l}
        total = sum(components.values()) * case.packaging
        return total, components

    if kind == "rtg":
        if case.w_per_kg is None or case.density_kg_m3 is None:
            raise ValueError("rtg case requires w_per_kg and density_kg_m3")
        body_l = physics.rtg_volume_l(
            power_kw,
            case.w_per_kg,
            case.density_kg_m3,
            shield_factor=case.shield_factor,
            packaging=1.0,
        )
        components = {"shielded source": body_l, "bop": case.bop_l}
        total = sum(components.values()) * case.packaging
        return total, components

    if kind == "ambient":
        if case.module_w_m2 is None:
            raise ValueError("ambient case requires module_w_m2")
        area_m2 = power_kw * physics.W_PER_KW / case.module_w_m2
        collector_l = area_m2 * case.thickness_m * physics.L_PER_M3
        components = {"collector": collector_l, "bop": case.bop_l}
        total = sum(components.values()) * case.packaging
        return total, components

    raise ValueError(f"unknown mechanism kind {kind!r}")


def screen(
    mechanism: Mechanism,
    power_kw: float,
    hours: float,
    target_volume_l: float,
) -> ScreenResult:
    """Screen one mechanism at one power/duration against an external volume."""
    best_l, best_components = _volume_l(mechanism.kind, mechanism.best, power_kw, hours)
    worst_l, worst_components = _volume_l(mechanism.kind, mechanism.worst, power_kw, hours)
    return ScreenResult(
        mechanism_id=mechanism.id,
        name=mechanism.name,
        category=mechanism.category,
        maturity=mechanism.maturity,
        kind=mechanism.kind,
        hours=hours,
        target_volume_l=target_volume_l,
        best_volume_l=best_l,
        worst_volume_l=worst_l,
        best_components_l=best_components,
        worst_components_l=worst_components,
        best_limiting=_summarise(best_components),
        worst_limiting=_summarise(worst_components),
    )


def screen_all(power_kw: float, hours: float, target_volume_l: float) -> list[ScreenResult]:
    """Screen every mechanism, sorted by best-case volume."""
    return sorted(
        (screen(m, power_kw, hours, target_volume_l) for m in MECHANISMS),
        key=lambda r: r.best_volume_l,
    )


def current_commercial(results: list[ScreenResult]) -> list[ScreenResult]:
    """Mechanisms labelled current at the stated scale."""
    return [r for r in results if r.maturity == "current"]


def best_current(results: list[ScreenResult]) -> ScreenResult | None:
    current = current_commercial(results)
    return min(current, key=lambda r: r.best_volume_l) if current else None
