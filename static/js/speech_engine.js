/**
 * speech_engine.js - Centralized Speech Synthesis & Lip-Sync Event Controller
 * Authors: Dr. Sebastian Clarke & Dr. Oliver Bennett
 * Handles voice detection, distinct male voice assignment, dialogue queue,
 * speech utterance lifecycle, and phoneme/viseme synchronization.
 */

class SpeechEngine {
  constructor(onVisemeChange, onSpeechStart, onSpeechEnd, onLogEvent) {
    this.onVisemeChange = onVisemeChange || (() => {});
    this.onSpeechStart = onSpeechStart || (() => {});
    this.onSpeechEnd = onSpeechEnd || (() => {});
    this.onLogEvent = onLogEvent || (() => {});

    this.synth = window.speechSynthesis;
    this.voices = [];
    this.voicesLoaded = false;
    this.isMuted = false;
    this.currentUtterance = null;
    this.currentSpeaker = null;
    this.currentDialogueId = null;

    // Character Voice Profiles
    this.voiceAssignments = {
      sebastian: {
        voice: null,
        pitch: 0.82,
        rate: 0.95,
        name: "Dr. Sebastian Clarke (Senior/Deep Male)"
      },
      oliver: {
        voice: null,
        pitch: 1.15,
        rate: 1.05,
        name: "Dr. Oliver Bennett (Younger/Clear Male)"
      }
    };

    this.initVoices();
  }

  initVoices() {
    if (!this.synth) {
      this.onLogEvent("Web Speech API not supported on this browser; running in simulated audio mode.", "warn");
      return;
    }

    const load = () => {
      this.voices = this.synth.getVoices();
      if (this.voices && this.voices.length > 0) {
        this.voicesLoaded = true;
        this.assignDistinctVoices();
        this.onLogEvent(`Detected ${this.voices.length} browser speech synthesis voices.`, "good");
      }
    };

    load();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = load;
    }

    // Safety polling if onvoiceschanged doesn't trigger immediately
    let attempts = 0;
    const poll = setInterval(() => {
      attempts++;
      if (this.voicesLoaded || attempts > 10) {
        clearInterval(poll);
        if (!this.voicesLoaded) {
          this.assignDistinctVoices();
        }
      } else {
        load();
      }
    }, 250);
  }

  assignDistinctVoices() {
    if (!this.voices || this.voices.length === 0) {
      this.onLogEvent("No system TTS voices reported by browser; applying distinct acoustic pitch modulation.", "warn");
      return;
    }

    // Filter English voices
    const enVoices = this.voices.filter(v => v.lang && v.lang.startsWith("en"));
    const candidateVoices = enVoices.length > 0 ? enVoices : this.voices;

    // Male and female name tokens for heuristic gender separation
    const maleNames = ["david", "mark", "guy", "george", "oliver", "daniel", "ryan", "arthur", "james", "male", "microsoft david", "google us english", "richard", "paul", "andrew"];
    const femaleNames = ["zira", "jenny", "samantha", "susan", "victoria", "female", "karen", "aria", "hazel", "linda", "catherine"];

    let malePool = candidateVoices.filter(v => {
      const n = v.name.toLowerCase();
      const isFemale = femaleNames.some(fn => n.includes(fn));
      const isMale = maleNames.some(mn => n.includes(mn));
      return isMale && !isFemale;
    });

    if (malePool.length < 2) {
      // Relax filter to all non-strictly female voices
      malePool = candidateVoices.filter(v => !femaleNames.some(fn => v.name.toLowerCase().includes(fn)));
    }

    if (malePool.length >= 2) {
      // Assign two genuinely distinct male voices
      this.voiceAssignments.sebastian.voice = malePool[0];
      this.voiceAssignments.oliver.voice = malePool[1];
      this.onLogEvent(`Assigned distinct male voices: Sebastian -> "${malePool[0].name}", Oliver -> "${malePool[1].name}"`, "good");
    } else if (malePool.length === 1) {
      // Only 1 male voice available: assign to both with strict pitch separation
      this.voiceAssignments.sebastian.voice = malePool[0];
      this.voiceAssignments.oliver.voice = malePool[0];
      this.onLogEvent(`Single male voice ("${malePool[0].name}") detected; applying distinct pitch modulation (Sebastian: 0.82, Oliver: 1.15).`, "warn");
    } else {
      // Fallback to distinct voices from candidate pool
      this.voiceAssignments.sebastian.voice = candidateVoices[0] || null;
      this.voiceAssignments.oliver.voice = candidateVoices[Math.min(1, candidateVoices.length - 1)] || null;
      this.onLogEvent("Generic voice pool used with pitch separation.", "warn");
    }
  }

  getVoiceDiagnostics() {
    return {
      voicesLoaded: this.voicesLoaded,
      totalVoices: this.voices.length,
      sebastianVoice: this.voiceAssignments.sebastian.voice ? this.voiceAssignments.sebastian.voice.name : "System Default (Deep Pitch 0.82)",
      sebastianPitch: this.voiceAssignments.sebastian.pitch,
      oliverVoice: this.voiceAssignments.oliver.voice ? this.voiceAssignments.oliver.voice.name : "System Default (Energetic Pitch 1.15)",
      oliverPitch: this.voiceAssignments.oliver.pitch,
      isDistinct: (this.voiceAssignments.sebastian.voice !== this.voiceAssignments.oliver.voice) || (this.voiceAssignments.sebastian.pitch !== this.voiceAssignments.oliver.pitch)
    };
  }

  setMuted(muted) {
    this.isMuted = muted;
    if (this.isMuted) {
      this.cancelSpeech();
    }
  }

  /**
   * Speak a dialogue item with precise event tracking and viseme animations.
   * @param {Object} dialogue { id, speaker: 'sebastian'|'oliver', text, start_sec, end_sec }
   * @param {Function} onComplete Callback when speech finishes
   */
  speakDialogue(dialogue, onComplete) {
    if (!dialogue || !dialogue.text) {
      if (onComplete) onComplete();
      return;
    }

    // Cancel any active utterance first
    this.cancelSpeech();

    this.currentSpeaker = dialogue.speaker;
    this.currentDialogueId = dialogue.id;

    if (this.isMuted || !this.synth) {
      // Simulated silent timing fallback
      const durationMs = Math.max(2500, (dialogue.end_sec - dialogue.start_sec) * 1000);
      this.simulateLipSync(dialogue.speaker, durationMs, onComplete);
      return;
    }

    const utterance = new SpeechSynthesisUtterance(dialogue.text);
    const profile = this.voiceAssignments[dialogue.speaker] || this.voiceAssignments.sebastian;

    if (profile.voice) {
      utterance.voice = profile.voice;
    }
    utterance.pitch = profile.pitch;
    utterance.rate = profile.rate;
    utterance.lang = "en-US";

    let visemeInterval = null;
    const visemes = ["OPEN", "ROUND", "WIDE", "MID"];

    utterance.onstart = () => {
      this.onSpeechStart(dialogue.speaker, dialogue.id);
      this.onLogEvent(`Speech Started: [${dialogue.speaker.toUpperCase()}] "${dialogue.text.substring(0, 35)}..."`, "good");

      // Viseme modulation loop during active speech
      let vIndex = 0;
      visemeInterval = setInterval(() => {
        const nextV = visemes[vIndex % visemes.length];
        this.onVisemeChange(dialogue.speaker, nextV);
        vIndex++;
      }, 140);
    };

    utterance.onboundary = (event) => {
      // Switch viseme on word boundary
      const randomV = visemes[Math.floor(Math.random() * visemes.length)];
      this.onVisemeChange(dialogue.speaker, randomV);
    };

    const cleanup = () => {
      if (visemeInterval) {
        clearInterval(visemeInterval);
        visemeInterval = null;
      }
      this.onVisemeChange(dialogue.speaker, "REST");
      this.onSpeechEnd(dialogue.speaker, dialogue.id);
      this.currentUtterance = null;
      this.currentSpeaker = null;
      this.currentDialogueId = null;
    };

    utterance.onend = () => {
      cleanup();
      this.onLogEvent(`Speech Completed: [${dialogue.speaker.toUpperCase()}] ID: ${dialogue.id}`);
      if (onComplete) onComplete();
    };

    utterance.onerror = (e) => {
      cleanup();
      this.onLogEvent(`Speech Error: ${e.error || "Synthesis interrupted"}`, "warn");
      if (onComplete) onComplete();
    };

    this.currentUtterance = utterance;

    try {
      this.synth.speak(utterance);
    } catch (err) {
      cleanup();
      this.onLogEvent(`Speech invoke failed: ${err.message}`, "warn");
      if (onComplete) onComplete();
    }
  }

  simulateLipSync(speaker, durationMs, onComplete) {
    this.onSpeechStart(speaker, this.currentDialogueId);
    const visemes = ["OPEN", "ROUND", "WIDE", "MID"];
    let count = 0;
    const interval = setInterval(() => {
      const v = visemes[count % visemes.length];
      this.onVisemeChange(speaker, v);
      count++;
    }, 140);

    setTimeout(() => {
      clearInterval(interval);
      this.onVisemeChange(speaker, "REST");
      this.onSpeechEnd(speaker, this.currentDialogueId);
      if (onComplete) onComplete();
    }, durationMs);
  }

  cancelSpeech() {
    if (this.synth) {
      try {
        this.synth.cancel();
      } catch (e) {}
    }
    if (this.currentSpeaker) {
      this.onVisemeChange(this.currentSpeaker, "REST");
      this.onSpeechEnd(this.currentSpeaker, this.currentDialogueId);
    }
    this.currentUtterance = null;
    this.currentSpeaker = null;
    this.currentDialogueId = null;
  }
}

window.SpeechEngine = SpeechEngine;
