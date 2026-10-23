"""Re-scope limits derived from the validated Gate 2 volume screen.

The screen answers "does mechanism X fit power P for duration H in volume V?"
This module answers the inverse questions a product owner actually asks:

- At 3 kW, how long can the envelope last?
- At 1 hour, how much power can the envelope deliver?
- What cell energy density, stack power density, or engine specific volume
  would be needed to make the target close?

The functions reuse ``feasibility.screen`` rather than re-implementing the
volume model. That keeps one source of truth for the physics. The inverse
solutions are numerical bisections because the forward model includes fixed
BOP and packaging terms, so it is not exactly linear.
"""

from __future__ import annotations

import math

from .feasibility import screen
from .mechanisms import Mechanism, get

_EPS = 1e-9
_HI = 1e6
_ITERATIONS = 120


def _volume(mechanism: Mechanism, power_kw: float, hours: float, target_l: float) -> float:
    return screen(mechanism, power_kw, hours, target_l).best_volume_l


def _largest_x(fn, target: float, lo: float = _EPS, hi: float = _HI) -> float:
    """Largest x in [lo, hi] with fn(x) <= target, assuming monotonic fn."""
    if fn(lo) > target:
        return 0.0
    if fn(hi) <= target:
        return hi
    for _ in range(_ITERATIONS):
        mid = 0.5 * (lo + hi)
        if fn(mid) <= target:
            lo = mid
        else:
            hi = mid
    return lo


def max_duration_h(mechanism: Mechanism | str, power_kw: float, target_l: float) -> float:
    """Longest duration the mechanism can sustain at ``power_kw`` in ``target_l``.

    Returns 0 if even an infinitesimal duration does not fit, and ``inf`` if the
    mechanism's volume is independent of duration and already fits (RTG,
    ambient harvesting in this screening model).
    """
    m = get(mechanism) if isinstance(mechanism, str) else mechanism
    if m.kind in ("rtg", "ambient"):
        return math.inf if _volume(m, power_kw, 1.0, target_l) <= target_l else 0.0
    return _largest_x(lambda h: _volume(m, power_kw, h, target_l), target_l)


def max_power_kw(mechanism: Mechanism | str, hours: float, target_l: float) -> float:
    """Largest continuous power the mechanism can deliver for ``hours`` in ``target_l``."""
    m = get(mechanism) if isinstance(mechanism, str) else mechanism
    return _largest_x(lambda p: _volume(m, p, hours, target_l), target_l)


def required_cell_wh_l(
    power_kw: float,
    hours: float,
    target_l: float,
    packaging: float = 1.25,
    bop_l: float = 0.2,
    converter_l: float = 0.4,
) -> float:
    """Cell-level volumetric energy density needed for a battery to fit.

    Returns ``inf`` if the fixed BOP, converter and packaging leave no cell volume.
    """
    allowed_cell_l = target_l / packaging - bop_l - converter_l
    if allowed_cell_l <= 0:
        return math.inf
    return power_kw * 1000.0 * hours / allowed_cell_l


def required_stack_kw_per_l(
    power_kw: float,
    hours: float,
    target_l: float,
    eta: float,
    packaging: float = 1.25,
    bop_l: float = 1.5,
    converter_l: float = 0.4,
    h2_density_kg_per_l: float = 0.040,
    lhv_h2_kwh_per_kg: float = 33.33,
) -> float:
    """Stack power density needed for a PEM + H2 system to fit.

    Returns ``inf`` if the H2 tank plus BOP and converter already consume the
    allowed volume.
    """
    h2_l = (power_kw * hours / (eta * lhv_h2_kwh_per_kg)) / h2_density_kg_per_l
    allowed_stack_l = target_l / packaging - bop_l - converter_l - h2_l
    if allowed_stack_l <= 0:
        return math.inf
    return power_kw / allowed_stack_l


def required_engine_l_per_kw(
    power_kw: float,
    hours: float,
    target_l: float,
    eta: float,
    h_w_m2k: float = 1000.0,
    dt_k: float = 80.0,
    thickness_m: float = 0.02,
    packaging: float = 1.25,
    bop_l: float = 1.5,
    converter_l: float = 0.4,
    lhv_kwh_per_l: float = 9.94,
) -> float:
    """Engine specific volume needed for a heat engine to fit.

    Returns ``inf`` if fuel + radiator + BOP + converter already consumes the
    allowed volume.
    """
    fuel_l = power_kw * hours / (eta * lhv_kwh_per_l)
    q_w = power_kw * 1000.0 * (1.0 / eta - 1.0)
    radiator_l = q_w / (h_w_m2k * dt_k) * thickness_m * 1000.0
    allowed_engine_l = target_l / packaging - bop_l - converter_l - fuel_l - radiator_l
    if allowed_engine_l <= 0:
        return math.inf
    return allowed_engine_l / power_kw
