"""Mechanism definitions for the first feasibility screen.

Each mechanism is a *source plus conversion pathway*, not a product. The
parameters are deliberately optimistic best cases and pessimistic worst cases;
the screen is useful only if the optimistic case is handled honestly.

Evidence labels
---------------
``current``       commercial or near-commercial at the stated scale
``advanced``      demonstrated in a laboratory or at a larger scale, not at 3 kW
``theoretical``   no commercial product; included to test the target's boundary
``restricted``    nuclear/radioactive; requires legal and safety approval

All values are screening estimates unless a note says otherwise. No value here
is a supplier quote or a measured system performance.
"""

from __future__ import annotations

from dataclasses import dataclass

from .physics import LHV_DIESEL_KWH_PER_L, LHV_H2_KWH_PER_KG


@dataclass(frozen=True)
class Case:
    """One optimistic or pessimistic parameter set for a mechanism."""

    eta: float | None = None
    engine_l_per_kw: float | None = None
    fuel_lhv: float = LHV_DIESEL_KWH_PER_L
    cell_wh_l: float | None = None
    stack_kw_per_l: float | None = None
    bop_l: float = 1.5
    packaging: float = 1.25
    converter_l: float = 0.4
    dod: float = 1.0
    converter_eta: float = 1.0
    h_w_m2k: float = 1000.0
    dt_k: float = 80.0
    module_w_m2: float | None = None
    thickness_m: float = 0.02
    w_per_kg: float | None = None
    density_kg_m3: float | None = None
    shield_factor: float = 2.0


@dataclass(frozen=True)
class Mechanism:
    id: str
    name: str
    category: str
    source: str
    evidence: str
    maturity: str
    kind: str
    best: Case
    worst: Case
    notes: str


MECHANISMS: tuple[Mechanism, ...] = (
    Mechanism(
        id="li_ion",
        name="Li-ion battery",
        category="storage",
        source="grid/electric charging before use",
        evidence="E1/E2: commercial cells; pack figures are estimates",
        maturity="current",
        kind="battery",
        best=Case(cell_wh_l=700.0, packaging=1.25, bop_l=0.2),
        worst=Case(cell_wh_l=400.0, packaging=1.35, bop_l=0.3),
        notes=(
            "3 kWh at 700 Wh/L cell = 4.29 L of cells; packaging and a 0.4 L converter "
            "bring it to ~6.1 L. The envelope is a better fit for a short buffer than "
            "for 1 h of storage. 700 Wh/L is cell-level; 1.25 packaging is aggressive. "
            "An 80% DoD / 95% converter case is shown as a sensitivity, not the base."
        ),
    ),
    Mechanism(
        id="li_air",
        name="Li-air battery (theoretical)",
        category="storage",
        source="Li-air cell with O2 intake",
        evidence="E0: theoretical/ laboratory; no commercial pack",
        maturity="theoretical",
        kind="battery",
        best=Case(cell_wh_l=1500.0, packaging=1.25, bop_l=0.2),
        worst=Case(cell_wh_l=800.0, packaging=1.35, bop_l=0.3),
        notes=(
            "Only the extreme theoretical case approaches 2.16 L for 1 h. "
            "Cycle life, O2 handling and round-trip efficiency are unresolved. "
            "If air-breathing, CO2 scrubbing is not counted; if primary, it is not "
            "a rechargeable storage mechanism."
        ),
    ),
    Mechanism(
        id="diesel",
        name="Diesel genset",
        category="generation",
        source="diesel fuel",
        evidence="E0/E1: small genset performance and volume are estimates",
        maturity="current",
        kind="heat_engine",
        best=Case(eta=0.35, engine_l_per_kw=10.0, h_w_m2k=1000.0, dt_k=80.0),
        worst=Case(eta=0.25, engine_l_per_kw=20.0, h_w_m2k=100.0, dt_k=30.0),
        notes=(
            "10 L/kW is a stripped bare-engine figure, not a current 3 kW commercial "
            "package; off-the-shelf units are 50-150 L/kW. It is retained because it "
            "favours the mechanism. Fuel scales linearly with duration and dominates "
            "at long intervals."
        ),
    ),
    Mechanism(
        id="stirling",
        name="Stirling engine + alternator",
        category="generation",
        source="diesel/combustion heat",
        evidence="E0/E1: 5-15 L/kW is a screening range, not a product",
        maturity="advanced",
        kind="heat_engine",
        best=Case(eta=0.40, engine_l_per_kw=5.0, h_w_m2k=1000.0, dt_k=80.0),
        worst=Case(eta=0.25, engine_l_per_kw=15.0, h_w_m2k=100.0, dt_k=30.0),
        notes=(
            "The best case assumes a compact, high-temperature, high-effectiveness "
            "machine. A 3 kW Stirling at 5 L/kW is not a catalogue item."
        ),
    ),
    Mechanism(
        id="microturbine",
        name="Microturbine + high-speed alternator",
        category="generation",
        source="diesel/combustion heat",
        evidence="E0: 8-20 L/kW at 3 kW is an extrapolation from larger units",
        maturity="advanced",
        kind="heat_engine",
        best=Case(eta=0.35, engine_l_per_kw=8.0, h_w_m2k=1000.0, dt_k=80.0),
        worst=Case(eta=0.25, engine_l_per_kw=20.0, h_w_m2k=100.0, dt_k=30.0),
        notes="Recuperation and high-speed alternator are not modeled; both add volume.",
    ),
    Mechanism(
        id="pem_fuel_cell",
        name="PEM fuel cell + 700 bar H2",
        category="generation",
        source="H2 in a 700 bar tank",
        evidence="E1/E2: commercial stacks; 1-3 kW/L and 4.5 L/kg H2 are estimates",
        maturity="current",
        kind="fuel_cell",
        best=Case(eta=0.60, stack_kw_per_l=3.0, bop_l=1.5, packaging=1.25),
        worst=Case(
            eta=0.50,
            stack_kw_per_l=1.0,
            bop_l=2.0,
            packaging=1.35,
            h_w_m2k=100.0,
            dt_k=30.0,
        ),
        notes=(
            "3 kW/L is an automotive large-stack extrapolation; at 3 kW, end plates "
            "and manifolds dominate and 0.3-1.5 kW/L is closer to reality. The 1 kW/L "
            "worst case is the realistic lower bound. H2 at 0.040 kg/L is gas density, "
            "not vessel density; a Type IV vessel is ~1.4-1.7x larger. The tank, "
            "humidifier, air blower, coolant loop, radiator and controls are in BOP "
            "or added explicitly; the 0.4 L converter is separate."
        ),
    ),
    Mechanism(
        id="tpv",
        name="Thermophotovoltaic converter",
        category="conversion",
        source="fuel/combustion heat at 1,500-2,000 C",
        evidence="E1*: cell-level 40% claimed; system efficiency and volume are estimates",
        maturity="advanced",
        kind="heat_engine",
        best=Case(eta=0.35, engine_l_per_kw=5.0, h_w_m2k=1000.0, dt_k=80.0),
        worst=Case(eta=0.20, engine_l_per_kw=15.0, h_w_m2k=100.0, dt_k=30.0),
        notes="Emitter, insulation, filter and cell cooling are folded into the engine volume.",
    ),
    Mechanism(
        id="teg",
        name="Thermoelectric generator",
        category="conversion",
        source="fuel/combustion heat",
        evidence="E1*: ZT~1; 3-5% is current, 8% is laboratory-class",
        maturity="advanced",
        kind="heat_engine",
        best=Case(eta=0.08, engine_l_per_kw=5.0, h_w_m2k=1000.0, dt_k=80.0),
        worst=Case(eta=0.05, engine_l_per_kw=15.0, h_w_m2k=100.0, dt_k=30.0),
        notes="Low efficiency makes the heat exchanger and radiator, not the TE material, dominant.",
    ),
    Mechanism(
        id="solar_pv",
        name="Solar PV + storage",
        category="conversion",
        source="sunlight",
        evidence="E2: 200-250 W/m2 module class; storage is an added battery",
        maturity="current",
        kind="solar",
        best=Case(module_w_m2=250.0, thickness_m=0.02, cell_wh_l=700.0, packaging=1.25),
        worst=Case(module_w_m2=200.0, thickness_m=0.04, cell_wh_l=400.0, packaging=1.35),
        notes=(
            "The screen assumes enough storage for the mission duration only; that is "
            "optimistic for a solar system, because night-time storage would multiply "
            "the storage term by ~5 for diurnal duty. Even the panel alone is many "
            "square metres at 3 kW."
        ),
    ),
    Mechanism(
        id="rtg",
        name="Radioisotope thermoelectric generator",
        category="generation",
        source="Pu-238 decay heat",
        evidence="E0/E1: 3-5 W/kg system class; shielding multiplier is a blunt estimate",
        maturity="restricted",
        kind="rtg",
        best=Case(w_per_kg=5.0, density_kg_m3=5000.0, shield_factor=2.0, packaging=1.25),
        worst=Case(w_per_kg=3.0, density_kg_m3=4000.0, shield_factor=4.0, packaging=1.35),
        notes=(
            "A 3 kWe RTG is ~600-1,000 kg before a real shield. It is included as a "
            "long-duration nuclear proxy, not as a deployable product."
        ),
    ),
    Mechanism(
        id="supercapacitor",
        name="Supercapacitor bank",
        category="storage",
        source="grid/electric charging before use",
        evidence="E1/E2: ~5-10 Wh/L class",
        maturity="current",
        kind="battery",
        best=Case(cell_wh_l=10.0, packaging=1.25, bop_l=0.2),
        worst=Case(cell_wh_l=5.0, packaging=1.35, bop_l=0.3),
        notes="High power, negligible mission energy; not a 1 h source.",
    ),
    Mechanism(
        id="ambient",
        name="Ambient harvesting",
        category="conversion",
        source="light/thermal/vibration gradients",
        evidence="E0: 0.1-1 W/m2 is an optimistic outdoor class",
        maturity="theoretical",
        kind="ambient",
        best=Case(module_w_m2=1.0, thickness_m=0.005, packaging=1.25),
        worst=Case(module_w_m2=0.1, thickness_m=0.01, packaging=1.35),
        notes="Included as a lower bound; kW-scale ambient harvesting is not a product.",
    ),
)

BY_ID = {m.id: m for m in MECHANISMS}


def get(mechanism_id: str) -> Mechanism:
    try:
        return BY_ID[mechanism_id]
    except KeyError as exc:
        raise KeyError(f"unknown mechanism {mechanism_id!r}; known: {sorted(BY_ID)}") from exc


# Constants re-exported for report prose; the values live in physics.py.
__all__ = ["Case", "Mechanism", "MECHANISMS", "BY_ID", "get", "LHV_H2_KWH_PER_KG"]
