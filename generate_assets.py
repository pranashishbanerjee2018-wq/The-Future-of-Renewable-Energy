"""
generate_assets.py - Procedural Scientific Audio Synthesizer
Synthesizes professional original soundscapes and sound effects using pure Python (wave & numpy):
  1. cinematic_music.wav - Soft, inspiring cinematic scientific score (170s length)
  2. lab_ambience.wav - Subtle futuristic research lab drone & harmonics (looped)
  3. wind_solar_ambient.wav - Subtle aerodynamic wind whisper and gentle resonance
  4. scene_transition.wav - Smooth clean energy whoosh and frequency sweep
  5. ui_click.wav - Clean tactile glass/digital interface click
  6. calc_complete.wav - Dual-tone crystal chime for numerical engineering calculations
"""

import os
import wave
import math
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, 'static', 'audio')
os.makedirs(AUDIO_DIR, exist_ok=True)

SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE):
    """Write float numpy array in [-1.0, 1.0] to 16-bit PCM WAV."""
    path = os.path.join(AUDIO_DIR, filename)
    samples = np.clip(samples, -0.98, 0.98)
    int_samples = (samples * 32767).astype(np.int16)
    
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(int_samples.tobytes())
    print(f"[AUDIO] Generated: {filename} ({len(samples)/sample_rate:.1f}s, {os.path.getsize(path)/1024:.1f} KB)")

def generate_lab_ambience(duration=20.0):
    """Generate subtle futuristic research lab hum with low harmonic drone."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    hum = (0.25 * np.sin(2 * np.pi * 50.0 * t) +
           0.15 * np.sin(2 * np.pi * 100.0 * t) +
           0.07 * np.sin(2 * np.pi * 150.0 * t + 0.4) +
           0.03 * np.sin(2 * np.pi * 200.0 * t + 0.9))
    
    # Slow LFO filter modulation
    lfo1 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.10 * t)
    lfo2 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.05 * t + 1.2)
    noise = np.random.normal(0, 0.015, len(t))
    
    # Periodic soft digital telemetry pulse every 5 seconds
    pulse = 0.02 * np.sin(2 * np.pi * 960 * t) * np.exp(-((t % 5.0) / 0.12)**2)
    
    audio = (hum * (0.8 + 0.2 * lfo1) + noise * lfo2 + pulse) * 0.22
    
    # Loop-friendly fade
    fade_len = int(SAMPLE_RATE * 1.5)
    fade = np.ones(len(audio))
    fade[:fade_len] = np.linspace(0, 1, fade_len)
    fade[-fade_len:] = np.linspace(1, 0, fade_len)
    audio = audio * fade
    
    write_wav('lab_ambience.wav', audio)

def generate_wind_solar_ambient(duration=20.0):
    """Generate natural aerodynamic air flow and gentle solar resonance."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    # Filtered broadband wind noise with slow breeze modulation
    breeze_lfo = 0.5 + 0.5 * np.sin(2 * np.pi * 0.15 * t)
    wind = np.random.normal(0, 0.04, len(t)) * breeze_lfo
    
    # Gentle resonant singing tone (Aeolian harp effect at 330 Hz and 440 Hz)
    aeolian = (0.015 * np.sin(2 * np.pi * 330 * t) + 0.012 * np.sin(2 * np.pi * 440 * t + 0.5)) * breeze_lfo
    
    audio = (wind + aeolian) * 0.25
    fade_len = int(SAMPLE_RATE * 1.5)
    fade = np.ones(len(audio))
    fade[:fade_len] = np.linspace(0, 1, fade_len)
    fade[-fade_len:] = np.linspace(1, 0, fade_len)
    audio = audio * fade
    
    write_wav('wind_solar_ambient.wav', audio)

def generate_cinematic_music(duration=170.0):
    """
    Generate 170-second soft, inspiring, contemplative cinematic score for scientific presentation.
    Hopeful, clean energy progression: D minor -> Bb major -> F major -> C major (Lydian/Major feel)
    Warm soft sine/triangle pads and gentle bell-like arpeggios that never compete with voice dialogue.
    """
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    
    # Chord frequencies (Hz):
    # Dm: D3 (146.83), F3 (174.61), A3 (220.00), C4 (261.63)
    # Bb: Bb2 (116.54), D3 (146.83), F3 (174.61), A3 (220.00)
    # F:  F2 (87.31), A2 (110.00), C3 (130.81), F3 (174.61)
    # C:  C3 (130.81), E3 (164.81), G3 (196.00), C4 (261.63)
    chords = [
        [146.83, 174.61, 220.00, 261.63],  # Dm7
        [116.54, 146.83, 174.61, 220.00],  # Bbmaj7
        [87.31,  110.00, 130.81, 174.61],  # Fmaj
        [130.81, 164.81, 196.00, 261.63]   # Cmaj
    ]
    chord_len = 10.0  # 10 seconds per chord -> 40s cycle, repeats 4.25 times
    
    for i in range(int(duration / chord_len) + 1):
        c_idx = i % len(chords)
        chord_freqs = chords[c_idx]
        start_idx = int(i * chord_len * SAMPLE_RATE)
        end_idx = min(len(t), int((i + 1) * chord_len * SAMPLE_RATE))
        if start_idx >= len(t):
            break
        
        seg_len = end_idx - start_idx
        seg_t = np.linspace(0, seg_len / SAMPLE_RATE, seg_len, endpoint=False)
        
        # Soft envelope (smooth rise and fall)
        env = np.sin(np.pi * (seg_t / (seg_len / SAMPLE_RATE))) ** 1.4
        
        chord_wave = np.zeros(seg_len)
        for freq in chord_freqs:
            # Fundamental + soft second harmonic for warmth
            w = 0.65 * np.sin(2 * np.pi * freq * seg_t) + 0.22 * np.sin(4 * np.pi * freq * seg_t + 0.3)
            chord_wave += w
        
        # Gentle celestial arpeggio note
        arp_freq = chord_freqs[(i % len(chord_freqs))] * 2.0
        arp_env = np.exp(-((seg_t % 2.5) / 1.1)) * 0.12
        arp_wave = np.sin(2 * np.pi * arp_freq * seg_t) * arp_env
        
        audio[start_idx:end_idx] += (chord_wave * 0.18 + arp_wave) * env
    
    # Master volume (keep soft: -20 dB to guarantee speech clarity)
    audio = audio * 0.12
    
    # Overall fade in and fade out
    fade_in_len = int(SAMPLE_RATE * 3.0)
    fade_out_len = int(SAMPLE_RATE * 5.0)
    audio[:fade_in_len] *= np.linspace(0, 1, fade_in_len)
    audio[-fade_out_len:] *= np.linspace(1, 0, fade_out_len)
    
    write_wav('cinematic_music.wav', audio)

def generate_scene_transition(duration=1.8):
    """Generate smooth sci-fi harmonic sweep and soft whoosh for scene transition."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    freq = np.linspace(120, 540, len(t))
    sweep = np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, 0.12, len(t))
    env = np.sin(np.pi * (t / duration)) ** 2
    audio = (sweep * 0.18 + noise * 0.08) * env * 0.35
    write_wav('scene_transition.wav', audio)

def generate_ui_click(duration=0.08):
    """Generate clean tactical interface click."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    click = np.sin(2 * np.pi * 1800 * t) * np.exp(-t / 0.012)
    pop = np.sin(2 * np.pi * 320 * t) * np.exp(-t / 0.02)
    audio = (click * 0.6 + pop * 0.4) * 0.4
    write_wav('ui_click.wav', audio)

def generate_calc_complete(duration=1.4):
    """Generate dual-tone harmonic crystal chime for engineering calculations."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    chime1 = np.sin(2 * np.pi * 880.0 * t) * np.exp(-t / 0.45)   # A5
    chime2 = np.sin(2 * np.pi * 1318.5 * t) * np.exp(-t / 0.55)  # E6
    chime3 = np.sin(2 * np.pi * 1760.0 * t) * np.exp(-t / 0.35)  # A6
    audio = (chime1 * 0.4 + chime2 * 0.45 + chime3 * 0.25) * 0.32
    write_wav('calc_complete.wav', audio)

def main():
    print("=" * 65)
    print(" PROCEDURAL SCIENTIFIC AUDIO SYNTHESIZER")
    print(" Generating original audio assets for Future of Renewable Energy...")
    print("=" * 65)
    generate_lab_ambience()
    generate_wind_solar_ambient()
    generate_cinematic_music()
    generate_scene_transition()
    generate_ui_click()
    generate_calc_complete()
    print("\n[AUDIO] All audio assets synthesized successfully!")

if __name__ == '__main__':
    main()
