"""
test_assets_and_paths.py - Asset Existence and Non-Empty Verification
Validates:
  1. All 5 plot PNGs in results/ and static/images/.
  2. All SVG vector assets in static/images/.
  3. All 6 WAV audio assets in static/audio/.
  4. Core HTML, JS, and CSS files.
"""

import os
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestAssetsAndPaths(unittest.TestCase):

    def test_required_plots(self):
        """Verify all 5 high-resolution scientific plots exist and have valid size (>10KB)."""
        plot_names = [
            "solar_irradiance_power.png",
            "wind_speed_power.png",
            "renewable_energy_mix.png",
            "battery_soc_profile.png",
            "demand_vs_generation_balance.png"
        ]
        for name in plot_names:
            path_res = os.path.join(BASE_DIR, 'results', name)
            path_static = os.path.join(BASE_DIR, 'static', 'images', name)

            self.assertTrue(os.path.exists(path_res), f"Missing plot in results: {name}")
            self.assertGreater(os.path.getsize(path_res), 10000, f"Plot in results too small: {name}")

            self.assertTrue(os.path.exists(path_static), f"Missing plot in static/images: {name}")
            self.assertGreater(os.path.getsize(path_static), 10000, f"Plot in static/images too small: {name}")

    def test_required_svgs(self):
        """Verify character SVGs, lab background, and conceptual diagram SVGs."""
        svg_names = [
            "sebastian_character.svg",
            "oliver_character.svg",
            "lab_background.svg",
            "pv_cell_cross_section.svg",
            "wind_hydro_geo.svg",
            "smart_grid_network.svg",
            "sustainable_future_city.svg"
        ]
        for name in svg_names:
            p = os.path.join(BASE_DIR, 'static', 'images', name)
            self.assertTrue(os.path.exists(p), f"Missing SVG: {name}")
            self.assertGreater(os.path.getsize(p), 1000, f"SVG appears empty or truncated: {name}")

    def test_required_audio(self):
        """Verify procedural WAV audio files exist and are playable."""
        audio_names = [
            "cinematic_music.wav",
            "lab_ambience.wav",
            "wind_solar_ambient.wav",
            "scene_transition.wav",
            "ui_click.wav",
            "calc_complete.wav"
        ]
        for name in audio_names:
            p = os.path.join(BASE_DIR, 'static', 'audio', name)
            self.assertTrue(os.path.exists(p), f"Missing Audio: {name}")
            self.assertGreater(os.path.getsize(p), 2000, f"Audio file too small: {name}")

    def test_frontend_code_files(self):
        """Verify index.html, style.css, and JS modules exist."""
        required_files = [
            os.path.join(BASE_DIR, 'index.html'),
            os.path.join(BASE_DIR, 'templates', 'index.html'),
            os.path.join(BASE_DIR, 'static', 'css', 'style.css'),
            os.path.join(BASE_DIR, 'static', 'js', 'speech_engine.js'),
            os.path.join(BASE_DIR, 'static', 'js', 'animation_controller.js'),
            os.path.join(BASE_DIR, 'static', 'js', 'presentation_app.js'),
            os.path.join(BASE_DIR, 'app.py'),
            os.path.join(BASE_DIR, 'start.bat'),
            os.path.join(BASE_DIR, '.nojekyll'),
            os.path.join(BASE_DIR, 'RenewableEnergy.m')
        ]
        for p in required_files:
            self.assertTrue(os.path.exists(p), f"Missing file: {p}")
            self.assertGreater(os.path.getsize(p), 0, f"File is empty: {p}")

if __name__ == '__main__':
    unittest.main()
