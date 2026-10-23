"""Reference tests for the inverse re-scope limits."""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engineering import rescope  # noqa: E402
from engineering.mechanisms import get  # noqa: E402


class DurationTests(unittest.TestCase):
    def test_li_ion_duration_at_three_kw(self) -> None:
        # 2.16 L, 1.25 packaging, 0.2 L BOP, 700 Wh/L: 0.3565 h = 21.4 min.
        hours = rescope.max_duration_h("li_ion", 3.0, 2.16)
        self.assertAlmostEqual(hours, 0.3565, places=3)

    def test_pem_cannot_start_at_three_kw_in_envelope(self) -> None:
        # Stack + BOP alone exceed 2.16 L at 3 kW before any H2 is added.
        self.assertEqual(rescope.max_duration_h("pem_fuel_cell", 3.0, 2.16), 0.0)

    def test_diesel_cannot_start_at_three_kw_in_envelope(self) -> None:
        self.assertEqual(rescope.max_duration_h("diesel", 3.0, 2.16), 0.0)

    def test_rtg_duration_is_unbounded_when_it_fits(self) -> None:
        self.assertTrue(math.isinf(rescope.max_duration_h("rtg", 3.0, 400.0)))

    def test_rtg_does_not_fit_small_envelope(self) -> None:
        self.assertEqual(rescope.max_duration_h("rtg", 3.0, 2.16), 0.0)


class PowerTests(unittest.TestCase):
    def test_li_ion_power_for_one_hour(self) -> None:
        # 2.16 L, 1.25 packaging, 0.2 L BOP, 700 Wh/L: 1.0696 kWh = 1.07 kW.
        power = rescope.max_power_kw("li_ion", 1.0, 2.16)
        self.assertAlmostEqual(power, 1.0696, places=3)

    def test_pem_power_for_one_hour_is_small(self) -> None:
        # 2.16 L leaves 0.228 L after BOP; H2 is 1.25 L/kW and stack 0.333 L/kW.
        power = rescope.max_power_kw("pem_fuel_cell", 1.0, 2.16)
        self.assertGreater(power, 0.0)
        self.assertLess(power, 0.20)

    def test_stirling_power_for_one_hour_is_small(self) -> None:
        power = rescope.max_power_kw("stirling", 1.0, 2.16)
        self.assertGreater(power, 0.0)
        self.assertLess(power, 0.10)


class ThresholdTests(unittest.TestCase):
    def test_cell_density_for_three_kw_one_hour(self) -> None:
        value = rescope.required_cell_wh_l(3.0, 1.0, 2.16, packaging=1.25, bop_l=0.2)
        self.assertAlmostEqual(value, 1963.35, places=1)

    def test_cell_density_with_less_packaging(self) -> None:
        value = rescope.required_cell_wh_l(3.0, 1.0, 2.16, packaging=1.10, bop_l=0.1)
        self.assertAlmostEqual(value, 1609.8, places=1)

    def test_pem_stack_density_is_infeasible_with_h2_tank(self) -> None:
        value = rescope.required_stack_kw_per_l(
            3.0, 1.0, 2.16, eta=0.60, packaging=1.25, bop_l=1.5
        )
        self.assertTrue(math.isinf(value))

    def test_heat_engine_specific_volume_is_infeasible(self) -> None:
        value = rescope.required_engine_l_per_kw(
            3.0, 1.0, 2.16, eta=0.40, h_w_m2k=1000.0, dt_k=80.0
        )
        self.assertTrue(math.isinf(value))


if __name__ == "__main__":
    unittest.main()
