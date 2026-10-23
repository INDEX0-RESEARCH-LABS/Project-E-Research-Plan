"""Reference-value and invariant tests for the Gate 2 volume screen.

Run from the repository root:

    python3 -m unittest discover -s engineering/tests -t .

The tests use only the standard library. They encode hand-calculable numbers so
a failure indicates a model error, not merely a changed result.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engineering import physics  # noqa: E402
from engineering.feasibility import (  # noqa: E402
    best_current,
    screen,
    screen_all,
)
from engineering.mechanisms import get  # noqa: E402


class EnvelopeTests(unittest.TestCase):
    def test_envelope_volume(self) -> None:
        self.assertAlmostEqual(physics.box_volume_l(0.120, 0.150, 0.120), 2.16, places=9)

    def test_envelope_surface_area(self) -> None:
        self.assertAlmostEqual(
            physics.box_surface_area_m2(0.120, 0.150, 0.120), 0.1008, places=9
        )

    def test_volumetric_power_density(self) -> None:
        self.assertAlmostEqual(
            physics.volumetric_power_density_mw_m3(3.0, 2.16), 1.3888888889, places=6
        )


class ThermodynamicsTests(unittest.TestCase):
    def test_carnot_reference(self) -> None:
        self.assertAlmostEqual(physics.carnot_efficiency(800.0, 300.0), 0.625, places=12)

    def test_carnot_rejects_inverted_reservoirs(self) -> None:
        with self.assertRaises(ValueError):
            physics.carnot_efficiency(300.0, 800.0)

    def test_heat_rejection_area(self) -> None:
        self.assertAlmostEqual(
            physics.heat_rejection_area_m2(9000.0, 100.0, 50.0), 1.8, places=9
        )

    def test_heat_engine_waste_heat(self) -> None:
        self.assertAlmostEqual(
            physics.heat_engine_waste_heat_w(3.0, 0.25), 9000.0, places=9
        )


class VolumeReferenceTests(unittest.TestCase):
    def test_diesel_fuel_one_hour(self) -> None:
        # 3 kW / (0.30 * 9.94 kWh/L) = 1.006 L
        self.assertAlmostEqual(
            physics.fuel_volume_l(3.0, 1.0, 0.30, physics.LHV_DIESEL_KWH_PER_L),
            1.0060362173,
            places=6,
        )

    def test_battery_pack_one_hour(self) -> None:
        # 3 kWh / 700 Wh/L = 4.2857 L cells; +0.2 L BOP; *1.25 = 5.607 L
        self.assertAlmostEqual(
            physics.battery_pack_volume_l(3.0, 700.0, packaging=1.25, bop_l=0.2),
            5.6071428571,
            places=6,
        )

    def test_h2_storage_one_hour(self) -> None:
        # 3 kWh / (0.60 * 33.33 kWh/kg) = 0.150 kg; /0.040 kg/L = 3.75 L
        self.assertAlmostEqual(
            physics.h2_storage_volume_l(3.0, 0.60, packaging=1.0), 3.750375, places=5
        )


class ScreenTests(unittest.TestCase):
    def test_all_current_mechanisms_exceed_envelope_at_one_hour(self) -> None:
        results = screen_all(3.0, 1.0, 2.16)
        for result in results:
            if result.maturity != "current":
                continue
            self.assertGreater(
                result.best_volume_l,
                2.16,
                f"{result.mechanism_id} unexpectedly fits 2.16 L at 3 kW/1 h",
            )

    def test_best_current_is_li_ion_at_one_hour(self) -> None:
        result = best_current(screen_all(3.0, 1.0, 2.16))
        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result.mechanism_id, "li_ion")
        self.assertAlmostEqual(result.best_volume_l, 6.1071428571, places=5)

    def test_li_air_theoretical_still_exceeds_envelope_at_one_hour(self) -> None:
        result = screen(get("li_air"), 3.0, 1.0, 2.16)
        self.assertGreater(result.best_volume_l, 2.16)
        self.assertAlmostEqual(result.best_volume_l, 3.25, places=6)

    def test_short_battery_buffer_fits(self) -> None:
        result = screen(get("li_ion"), 3.0, 0.25, 2.16)
        self.assertLess(result.best_volume_l, 2.16)
        self.assertEqual(result.verdict, "conditional")  # worst case does not fit

    def test_one_hour_battery_verdict_is_fail(self) -> None:
        result = screen(get("li_ion"), 3.0, 1.0, 2.16)
        self.assertEqual(result.verdict, "fail")

    def test_li_ion_buffer_duration_at_envelope(self) -> None:
        # 2.16 L, 1.25 packaging, 0.2 L BOP, 0.4 L converter, 700 Wh/L, 3 kW.
        allowed_kwh = (2.16 / 1.25 - 0.2 - 0.4) * 700.0 / physics.W_PER_KW
        self.assertAlmostEqual(physics.max_duration_h(allowed_kwh, 3.0) * 60.0, 15.8, places=1)

    def test_volume_grows_with_duration(self) -> None:
        for mechanism_id in ("li_ion", "pem_fuel_cell", "diesel"):
            mechanism = get(mechanism_id)
            one_h = screen(mechanism, 3.0, 1.0, 2.16).best_volume_l
            ten_h = screen(mechanism, 3.0, 10.0, 2.16).best_volume_l
            self.assertGreater(ten_h, one_h, mechanism_id)

    def test_unknown_kind_rejected(self) -> None:
        mechanism = get("li_ion")
        broken = mechanism.__class__(**{**mechanism.__dict__, "kind": "unobtainium"})
        with self.assertRaises(ValueError):
            screen(broken, 3.0, 1.0, 2.16)


if __name__ == "__main__":
    unittest.main()
