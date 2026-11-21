"""
test_live_server.py - Tests live HTTP socket binding and static asset delivery
"""

import sys
import time
import requests
import json
import threading
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from app import app

def run_server():
    app.run(host='127.0.0.1', port=5015, debug=False, use_reloader=False)

def test_live_server():
    print("[TEST] Starting background Flask thread on port 5015...")
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1.5)

    base_url = 'http://127.0.0.1:5015'
    print(f"[TEST] Probing live server at {base_url} (trust_env=False for local loopback)...")

    session = requests.Session()
    session.trust_env = False # Bypass sandbox outbound proxy for local loopback

    # 1. Test Root Presentation
    res = session.get(f"{base_url}/")
    print(f"[TEST] Root URL (/) responded with HTTP {res.status_code}")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    assert "THE FUTURE OF RENEWABLE ENERGY" in res.text, "Page title missing"
    assert "Dr. Sebastian Clarke" in res.text, "Character 1 missing"
    assert "Dr. Oliver Bennett" in res.text, "Character 2 missing"

    # 2. Test /api/scenes
    res_scenes = session.get(f"{base_url}/api/scenes")
    assert res_scenes.status_code == 200, "Scenes API failed"
    scenes_json = res_scenes.json()
    assert len(scenes_json) == 7, f"Expected 7 scenes, got {len(scenes_json)}"
    print("[TEST] /api/scenes OK (7 scenes verified)")

    # 3. Test /api/simulation
    res_sim = session.get(f"{base_url}/api/simulation")
    assert res_sim.status_code == 200, "Simulation API failed"
    sim_json = res_sim.json()
    assert "solar_standard_daily_MWh" in sim_json, "Missing solar calculations"
    assert "wind_betz_limit_pct" in sim_json, "Missing Betz limit calculations"
    assert "re_demand_coverage_pct" in sim_json, "Missing coverage calculation"
    print(f"[TEST] /api/simulation OK (RE Coverage: {sim_json['re_demand_coverage_pct']}%)")

    # 4. Test High-Res Plot Asset Delivery
    res_img = session.get(f"{base_url}/static/images/solar_irradiance_power.png")
    assert res_img.status_code == 200, "Static plot delivery failed"
    assert len(res_img.content) > 50000, "Plot bytes too small"
    print(f"[TEST] Static plot delivery OK ({len(res_img.content)} bytes)")

    print("\n[TEST] ALL LIVE SERVER TESTS PASSED PERFECTLY!")

if __name__ == '__main__':
    test_live_server()
