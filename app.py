"""
app.py - Local Flask Web Application for The Future of Renewable Energy
Provides local HTTP serving, live REST API routes for simulation telemetry,
dynamic MATLAB/Python execution trigger, and static asset delivery.
Address: http://127.0.0.1:5000/
"""

import os
import json
import subprocess
from flask import Flask, render_template, send_from_directory, jsonify, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

@app.route('/')
def index():
    """Render the master presentation."""
    return render_template('index.html')

@app.route('/data/<path:filename>')
def serve_data(filename):
    """Serve data files (JSON, CSV)."""
    return send_from_directory(os.path.join(BASE_DIR, 'data'), filename)

@app.route('/results/<path:filename>')
def serve_results(filename):
    """Serve high-resolution scientific plot files."""
    return send_from_directory(os.path.join(BASE_DIR, 'results'), filename)

@app.route('/api/scenes')
def get_scenes():
    """Return presentation scenes and dialogue timing data."""
    scenes_path = os.path.join(BASE_DIR, 'data', 'scenes.json')
    if os.path.exists(scenes_path):
        with open(scenes_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "scenes.json not found"}), 404

@app.route('/api/simulation')
def get_simulation():
    """Return engineering simulation results and physical metrics."""
    sim_path = os.path.join(BASE_DIR, 'data', 'simulation_results.json')
    if os.path.exists(sim_path):
        with open(sim_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "simulation_results.json not found"}), 404

@app.route('/api/run-matlab', methods=['POST'])
def run_matlab():
    """Trigger MATLAB/Python computational execution pipeline on-demand."""
    runner_script = os.path.join(BASE_DIR, 'matlab_runner.py')
    try:
        res = subprocess.run(['python', runner_script], capture_output=True, text=True, cwd=BASE_DIR)
        return jsonify({
            "status": "success" if res.returncode == 0 else "error",
            "returncode": res.returncode,
            "stdout": res.stdout,
            "stderr": res.stderr
        })
    except Exception as e:
        return jsonify({"status": "exception", "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("=" * 65)
    print(" THE FUTURE OF RENEWABLE ENERGY — LOCAL FLASK SERVER")
    print(f" Web Address: http://127.0.0.1:{port}/")
    print(" Static Standalone Mode: file:///.../index.html or python -m http.server 8000")
    print(" Authors: Dr. Sebastian Clarke & Dr. Oliver Bennett")
    print("=" * 65)
    app.run(host='127.0.0.1', port=port, debug=False)
