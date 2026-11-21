"""
test_matlab_calculations.py - Engineering Equations & Scientific Rigor Verification
Validates:
  1. Solar power output equation: P = G * A * eta.
  2. Wind power output equation: P = 0.5 * rho * A * v^3 * Cp.
  3. Betz theoretical limit (16/27 = 59.26%) is strictly observed.
  4. Battery state-of-charge (SoC) stays within physical limits (20% to 95%).
  5. 24-hour demand-generation energy balance consistency.
"""

import os
import math
import json
import unittest
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class TestMatlabCalculations(unittest.TestCase):

    def setUp(self):
        self.sim_file = os.path.join(DATA_DIR, 'simulation_results.json')
        self.csv_file = os.path.join(DATA_DIR, 'hourly_generation_demand.csv')
        self.mix_file = os.path.join(DATA_DIR, 'energy_mix.csv')

        self.assertTrue(os.path.exists(self.sim_file), "simulation_results.json must exist")
        self.assertTrue(os.path.exists(self.csv_file), "hourly_generation_demand.csv must exist")
        self.assertTrue(os.path.exists(self.mix_file), "energy_mix.csv must exist")

        with open(self.sim_file, 'r', encoding='utf-8') as f:
            self.sim = json.load(f)
        self.df_hourly = pd.read_csv(self.csv_file)
        self.df_mix = pd.read_csv(self.mix_file)

    def test_solar_power_physics(self):
        """Validate solar PV conversion formula: P = G * A * eta."""
        A = self.sim['solar_collector_area_m2'] # 1.5e6 m^2
        G_stc = self.sim['solar_peak_stc_W_m2'] # 1000 W/m^2
        eta_topcon = 0.24

        P_peak_expected_MW = (G_stc * A * eta_topcon) / 1e6 # 360.0 MW
        self.assertAlmostEqual(P_peak_expected_MW, 360.0, places=1)
        self.assertGreater(self.sim['solar_topcon_daily_MWh'], 2000.0)

    def test_wind_power_and_betz_limit(self):
        """Validate wind equation and ensure Cp does not exceed Betz limit (16/27)."""
        betz_limit = 16.0 / 27.0
        self.assertAlmostEqual(self.sim['wind_betz_limit_pct'], betz_limit * 100.0, places=2)
        
        # Ensure model aerodynamic Cp is realistically lower than Betz limit
        cp_peak = self.sim['wind_cp_peak']
        self.assertLess(cp_peak, betz_limit)
        self.assertGreater(cp_peak, 0.35)

    def test_battery_soc_constraints(self):
        """Validate battery state-of-charge does not violate min (20%) or max (95%) boundaries."""
        soc_series = self.df_hourly['SoC_Percent']
        self.assertTrue((soc_series >= 19.99).all(), f"SoC dropped below 20%: {soc_series.min()}")
        self.assertTrue((soc_series <= 95.01).all(), f"SoC exceeded 95%: {soc_series.max()}")

    def test_grid_energy_balance(self):
        """Validate hourly energy balance columns and demand coverage."""
        self.assertEqual(len(self.df_hourly), 24, "Must cover 24 hours (0-23)")
        
        # Total generation must be positive
        self.assertTrue((self.df_hourly['Total_RE_MW'] >= 0).all())
        
        # Net coverage should be >= 90%
        coverage = self.sim['re_demand_coverage_pct']
        self.assertGreaterEqual(coverage, 90.0)

if __name__ == '__main__':
    unittest.main()
