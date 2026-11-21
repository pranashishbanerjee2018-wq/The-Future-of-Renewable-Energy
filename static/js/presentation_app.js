/**
 * presentation_app.js - Master Scientific Presentation Coordinator
 * Authors: Dr. Sebastian Clarke & Dr. Oliver Bennett
 * Orchestrates 165-second timeline, exactly 7 scenes, two-character dialogue queue,
 * speech synthesis lip-sync, MATLAB dashboard, audio layers, and user controls.
 */

class PresentationApp {
  constructor() {
    this.TOTAL_DURATION = 165; // Exactly 165 seconds (2 min 45 sec)
    this.currentTime = 0;
    this.isPlaying = false;
    this.currentSceneIndex = 0;
    this.currentDialogueIndex = -1;
    this.subtitlesEnabled = true;
    this.soundEnabled = true;

    this.scenesData = null;
    this.matlabData = null;

    this.timelineInterval = null;
    this.isSpeakingDialogue = false;

    // Audio Elements
    this.audioMusic = null;
    this.audioAmbience = null;
    this.sfxClick = null;
    this.sfxTransition = null;
    this.sfxCalc = null;

    this.init();
  }

  async init() {
    this.initAudioElements();
    this.initControllers();
    await this.loadData();
    this.bindUIEvents();
    this.updateTimelineUI();
    this.updateDiagnostics();
    this.logDiagnostic("Renewable Energy Presentation initialized and ready.", "good");
  }

  initAudioElements() {
    this.audioMusic = new Audio("static/audio/cinematic_music.wav");
    this.audioMusic.loop = true;
    this.audioMusic.volume = 0.12;

    this.audioAmbience = new Audio("static/audio/lab_ambience.wav");
    this.audioAmbience.loop = true;
    this.audioAmbience.volume = 0.08;

    this.sfxClick = new Audio("static/audio/ui_click.wav");
    this.sfxClick.volume = 0.25;

    this.sfxTransition = new Audio("static/audio/scene_transition.wav");
    this.sfxTransition.volume = 0.3;

    this.sfxCalc = new Audio("static/audio/calc_complete.wav");
    this.sfxCalc.volume = 0.35;
  }

  initControllers() {
    this.animCtrl = new AnimationController();

    this.speechEngine = new SpeechEngine(
      // onVisemeChange
      (speaker, viseme) => {
        this.animCtrl.setViseme(speaker, viseme);
      },
      // onSpeechStart
      (speaker, dialogueId) => {
        this.animCtrl.setSpeakerState(speaker);
        this.updateActiveSpeakerUI(speaker);
        this.logDiagnostic(`Speaking: [${speaker.toUpperCase()}] Dialogue ID: ${dialogueId}`);
      },
      // onSpeechEnd
      (speaker, dialogueId) => {
        this.animCtrl.setSpeakerState(null);
        this.updateActiveSpeakerUI(null);
        this.isSpeakingDialogue = false;
      },
      // onLogEvent
      (msg, level) => {
        this.logDiagnostic(msg, level);
      }
    );
  }

  async loadData() {
    try {
      const sRes = await fetch("data/scenes.json");
      this.scenesData = await sRes.json();
    } catch (e) {
      console.warn("Could not load scenes.json; using built-in fallback", e);
    }

    try {
      const mRes = await fetch("data/simulation_results.json");
      this.matlabData = await mRes.json();
      this.populateMatlabDashboard();
    } catch (e) {
      console.warn("Could not load simulation_results.json", e);
    }

    this.renderSceneMarkers();
    this.renderSceneNavMenu();
  }

  bindUIEvents() {
    // Start button on splash screen
    const startBtn = document.getElementById("btn-start-presentation");
    if (startBtn) {
      startBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        const splash = document.getElementById("splash-overlay");
        if (splash) splash.classList.add("hidden");
        this.startPresentation();
      });
    }

    // Play / Pause Toggle
    const playPauseBtn = document.getElementById("btn-play-pause");
    if (playPauseBtn) {
      playPauseBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        if (this.isPlaying) {
          this.pausePresentation();
        } else {
          this.resumePresentation();
        }
      });
    }

    // Restart Button
    const restartBtn = document.getElementById("btn-restart");
    if (restartBtn) {
      restartBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.restartPresentation();
      });
    }

    // Previous / Next Scene
    const prevBtn = document.getElementById("btn-prev-scene");
    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.jumpToScene(this.currentSceneIndex - 1);
      });
    }
    const nextBtn = document.getElementById("btn-next-scene");
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.jumpToScene(this.currentSceneIndex + 1);
      });
    }

    // Subtitles Toggle
    const subBtn = document.getElementById("toggle-subtitles");
    if (subBtn) {
      subBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.subtitlesEnabled = !this.subtitlesEnabled;
        subBtn.classList.toggle("active", this.subtitlesEnabled);
        const overlay = document.getElementById("subtitles-overlay");
        if (overlay) overlay.style.display = this.subtitlesEnabled ? "flex" : "none";
      });
    }

    // Sound Toggle
    const soundBtn = document.getElementById("toggle-sound");
    if (soundBtn) {
      soundBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.soundEnabled = !this.soundEnabled;
        soundBtn.classList.toggle("active", this.soundEnabled);
        this.speechEngine.setMuted(!this.soundEnabled);
        if (!this.soundEnabled) {
          this.audioMusic.pause();
          this.audioAmbience.pause();
        } else if (this.isPlaying) {
          this.audioMusic.play().catch(() => {});
          this.audioAmbience.play().catch(() => {});
        }
      });
    }

    // Fullscreen Toggle
    const fsBtn = document.getElementById("toggle-fullscreen");
    if (fsBtn) {
      fsBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        } else {
          document.exitFullscreen().catch(() => {});
        }
      });
    }

    // MATLAB Modal Open / Close
    const openMatlabBtn = document.getElementById("btn-open-matlab");
    if (openMatlabBtn) {
      openMatlabBtn.addEventListener("click", () => {
        this.playSfx(this.sfxCalc);
        const modal = document.getElementById("matlab-modal");
        if (modal) modal.classList.add("active");
      });
    }

    const closeMatlabBtn = document.getElementById("btn-close-matlab");
    if (closeMatlabBtn) {
      closeMatlabBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        const modal = document.getElementById("matlab-modal");
        if (modal) modal.classList.remove("active");
      });
    }

    // Diagnostics Drawer Toggle
    const diagBtn = document.getElementById("btn-toggle-diagnostics");
    if (diagBtn) {
      diagBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        const drawer = document.getElementById("diagnostics-drawer");
        if (drawer) drawer.classList.toggle("active");
        this.updateDiagnostics();
      });
    }

    // Timeline Scrubbing / Seeking
    const track = document.getElementById("timeline-track");
    if (track) {
      track.addEventListener("click", (e) => {
        const rect = track.getBoundingClientRect();
        const clickRatio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        const seekTime = clickRatio * this.TOTAL_DURATION;
        this.seekToTime(seekTime);
      });
    }
  }

  startPresentation() {
    this.isPlaying = true;
    this.currentTime = 0;
    this.currentDialogueIndex = -1;

    if (this.soundEnabled) {
      this.audioMusic.currentTime = 0;
      this.audioMusic.play().catch(() => {});
      this.audioAmbience.currentTime = 0;
      this.audioAmbience.play().catch(() => {});
    }

    this.updatePlayPauseUI();
    this.startTimelineTicker();
    this.onTimelineTick(true);
    this.logDiagnostic("Presentation playback started from 0:00", "good");
  }

  resumePresentation() {
    this.isPlaying = true;
    if (this.soundEnabled) {
      this.audioMusic.play().catch(() => {});
      this.audioAmbience.play().catch(() => {});
    }
    this.updatePlayPauseUI();
    this.startTimelineTicker();
    this.onTimelineTick(false);
    this.logDiagnostic(`Presentation resumed at ${this.formatTime(this.currentTime)}`);
  }

  pausePresentation() {
    this.isPlaying = false;
    this.stopTimelineTicker();
    this.speechEngine.cancelSpeech();
    this.audioMusic.pause();
    this.audioAmbience.pause();
    this.updatePlayPauseUI();
    this.animCtrl.setSpeakerState(null);
    this.logDiagnostic(`Presentation paused at ${this.formatTime(this.currentTime)}`);
  }

  restartPresentation() {
    this.speechEngine.cancelSpeech();
    this.currentTime = 0;
    this.currentSceneIndex = 0;
    this.currentDialogueIndex = -1;
    this.isSpeakingDialogue = false;
    this.updateTimelineUI();
    this.startPresentation();
  }

  startTimelineTicker() {
    this.stopTimelineTicker();
    this.timelineInterval = setInterval(() => {
      if (!this.isPlaying) return;

      this.currentTime += 0.25;

      if (this.currentTime >= this.TOTAL_DURATION) {
        this.currentTime = this.TOTAL_DURATION;
        this.completePresentation();
        return;
      }

      this.onTimelineTick(false);
      this.updateTimelineUI();
    }, 250);
  }

  stopTimelineTicker() {
    if (this.timelineInterval) {
      clearInterval(this.timelineInterval);
      this.timelineInterval = null;
    }
  }

  onTimelineTick(forceCheck = false) {
    if (!this.scenesData || this.scenesData.length === 0) return;

    // 1. Identify current scene
    let newSceneIdx = 0;
    for (let i = 0; i < this.scenesData.length; i++) {
      if (this.currentTime >= this.scenesData[i].start_time && this.currentTime < this.scenesData[i].end_time) {
        newSceneIdx = i;
        break;
      }
    }
    if (this.currentTime >= this.TOTAL_DURATION) {
      newSceneIdx = this.scenesData.length - 1;
    }

    if (newSceneIdx !== this.currentSceneIndex || forceCheck) {
      this.currentSceneIndex = newSceneIdx;
      this.onSceneTransition(newSceneIdx);
    }

    // 2. Identify active dialogue item across all scenes
    const allDialogues = [];
    this.scenesData.forEach(scene => {
      if (scene.dialogues) {
        scene.dialogues.forEach(d => allDialogues.push(d));
      }
    });

    let activeDlgIdx = -1;
    for (let i = 0; i < allDialogues.length; i++) {
      const d = allDialogues[i];
      if (this.currentTime >= d.start_sec && this.currentTime < d.end_sec) {
        activeDlgIdx = i;
        break;
      }
    }

    if (activeDlgIdx !== -1 && activeDlgIdx !== this.currentDialogueIndex) {
      this.currentDialogueIndex = activeDlgIdx;
      const dlg = allDialogues[activeDlgIdx];
      this.triggerDialogue(dlg);
    }
  }

  onSceneTransition(sceneIdx) {
    const scene = this.scenesData[sceneIdx];
    if (!scene) return;

    this.playSfx(this.sfxTransition);
    this.animCtrl.updateSceneVisuals(scene);

    // Update Top Banner
    const counterEl = document.getElementById("banner-scene-counter");
    if (counterEl) counterEl.textContent = `SCENE ${scene.id} OF 7`;
    const titleEl = document.getElementById("banner-scene-title");
    if (titleEl) titleEl.textContent = scene.title.toUpperCase();

    // Update Scene Pills
    const pills = document.querySelectorAll(".scene-pill");
    pills.forEach((p, idx) => {
      p.classList.toggle("active", idx === sceneIdx);
    });

    // Special sound cue on Scene 5 (MATLAB scene)
    if (scene.id === 5) {
      setTimeout(() => this.playSfx(this.sfxCalc), 800);
    }

    this.logDiagnostic(`Scene ${scene.id}: "${scene.title}" (${scene.start_time}s - ${scene.end_time}s)`, "good");
  }

  triggerDialogue(dialogue) {
    if (!dialogue) return;

    // Update Subtitles
    const subOverlay = document.getElementById("subtitles-overlay");
    const subSpeaker = document.getElementById("subtitle-speaker-name");
    const subText = document.getElementById("subtitle-dialogue-text");

    if (subSpeaker) subSpeaker.textContent = dialogue.speaker_title || dialogue.speaker.toUpperCase();
    if (subText) subText.textContent = dialogue.text;
    if (subOverlay && this.subtitlesEnabled) subOverlay.style.display = "flex";

    this.isSpeakingDialogue = true;
    this.speechEngine.speakDialogue(dialogue, () => {
      this.isSpeakingDialogue = false;
    });
  }

  seekToTime(seconds) {
    this.speechEngine.cancelSpeech();
    this.currentTime = Math.max(0, Math.min(this.TOTAL_DURATION, seconds));
    this.currentDialogueIndex = -1;
    this.updateTimelineUI();
    this.onTimelineTick(true);
    this.logDiagnostic(`Seeked to ${this.formatTime(this.currentTime)}`);
  }

  jumpToScene(index) {
    if (!this.scenesData) return;
    const targetIdx = Math.max(0, Math.min(this.scenesData.length - 1, index));
    const targetScene = this.scenesData[targetIdx];
    if (targetScene) {
      this.seekToTime(targetScene.start_time);
    }
  }

  completePresentation() {
    this.isPlaying = false;
    this.stopTimelineTicker();
    this.speechEngine.cancelSpeech();
    this.updatePlayPauseUI();
    this.animCtrl.setSpeakerState(null);

    // Final scene graphics
    const finalScene = this.scenesData[this.scenesData.length - 1];
    if (finalScene) {
      this.animCtrl.updateSceneVisuals(finalScene);
    }

    this.logDiagnostic("Presentation reached 165s completion point successfully!", "good");
  }

  renderSceneMarkers() {
    const track = document.getElementById("timeline-track");
    if (!track || !this.scenesData) return;

    this.scenesData.forEach(scene => {
      if (scene.start_time > 0) {
        const marker = document.createElement("div");
        marker.className = "scene-marker";
        marker.style.left = `${(scene.start_time / this.TOTAL_DURATION) * 100}%`;
        track.appendChild(marker);
      }
    });
  }

  renderSceneNavMenu() {
    const container = document.getElementById("scene-pills-bar");
    if (!container || !this.scenesData) return;
    container.innerHTML = "";

    this.scenesData.forEach((scene, idx) => {
      const pill = document.createElement("button");
      pill.className = `scene-pill ${idx === 0 ? "active" : ""}`;
      pill.textContent = `S${scene.id}: ${scene.title.split(" ")[0]}`;
      pill.title = `${scene.title} (${this.formatTime(scene.start_time)} - ${this.formatTime(scene.end_time)})`;
      pill.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.jumpToScene(idx);
      });
      container.appendChild(pill);
    });
  }

  populateMatlabDashboard() {
    if (!this.matlabData) return;

    const data = this.matlabData;
    const engineBadge = document.getElementById("modal-engine-badge");
    if (engineBadge) {
      engineBadge.textContent = data.engine || "MATLAB R2026 Engine";
    }

    const metricsContainer = document.getElementById("modal-metrics-bar");
    if (metricsContainer) {
      metricsContainer.innerHTML = `
        <div class="metric-pill">Daily Demand: <span>${data.total_daily_demand_MWh || 11915} MWh</span></div>
        <div class="metric-pill">RE Generation: <span>${data.total_daily_re_gen_MWh || 12302} MWh</span></div>
        <div class="metric-pill">RE Coverage: <span>${data.re_demand_coverage_pct || 99.52}%</span></div>
        <div class="metric-pill">Battery Capacity: <span>${data.battery_capacity_MWh || 1200} MWh</span></div>
        <div class="metric-pill">Roundtrip η: <span>${data.battery_roundtrip_efficiency_pct || 88.36}%</span></div>
      `;
    }

    // Bind tab clicks
    const plotTabs = document.querySelectorAll(".tab-btn");
    const plotImg = document.getElementById("modal-plot-img");
    const plotDesc = document.getElementById("modal-plot-description");

    const plotDetails = {
      solar: {
        img: "static/images/solar_irradiance_power.png",
        desc: "Solar irradiance G(t) [W/m²] vs. power output across Standard Silicon (20%), TOPCon (24%), and Perovskite Tandem (32%). Peak output reaches 360 MW."
      },
      wind: {
        img: "static/images/wind_speed_power.png",
        desc: "Wind speed vs. turbine power output. Validates the Betz theoretical aerodynamic limit (Cp = 16/27 ≈ 59.3%) against realistic turbine curve (Cp = 0.46, rated 6 MW)."
      },
      mix: {
        img: "static/images/renewable_energy_mix.png",
        desc: "24-Hour regional energy generation mix: Solar PV, Wind Fleet, Dispatchable Hydro, and Geothermal baseload."
      },
      battery: {
        img: "static/images/battery_soc_profile.png",
        desc: "1.2 GWh / 300 MW Battery Storage state-of-charge (SoC %) and charge/discharge dispatch profile over 24 hours."
      },
      balance: {
        img: "static/images/demand_vs_generation_balance.png",
        desc: "Regional electricity demand curve vs. renewable generation and storage dispatch, showing 99.52% direct and buffered demand coverage."
      }
    };

    plotTabs.forEach(tab => {
      tab.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        plotTabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");

        const plotKey = tab.dataset.plotKey || "solar";
        if (plotDetails[plotKey] && plotImg) {
          plotImg.src = plotDetails[plotKey].img;
          if (plotDesc) plotDesc.textContent = plotDetails[plotKey].desc;
        }
      });
    });
  }

  updateTimelineUI() {
    const fill = document.getElementById("progress-fill");
    if (fill) {
      const pct = (this.currentTime / this.TOTAL_DURATION) * 100;
      fill.style.width = `${Math.min(100, Math.max(0, pct))}%`;
    }

    const timeReadout = document.getElementById("time-readout");
    if (timeReadout) {
      timeReadout.textContent = `${this.formatTime(this.currentTime)} / ${this.formatTime(this.TOTAL_DURATION)}`;
    }
  }

  updatePlayPauseUI() {
    const playPauseBtn = document.getElementById("btn-play-pause");
    if (playPauseBtn) {
      playPauseBtn.innerHTML = this.isPlaying
        ? `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg> Pause`
        : `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg> Play`;
    }
  }

  updateActiveSpeakerUI(speaker) {
    const sebWrap = document.getElementById("char-sebastian-wrapper");
    const oliWrap = document.getElementById("char-oliver-wrapper");

    if (speaker === "sebastian") {
      if (sebWrap) sebWrap.classList.add("speaking");
      if (oliWrap) oliWrap.classList.remove("speaking");
    } else if (speaker === "oliver") {
      if (oliWrap) oliWrap.classList.add("speaking");
      if (sebWrap) sebWrap.classList.remove("speaking");
    } else {
      if (sebWrap) sebWrap.classList.remove("speaking");
      if (oliWrap) oliWrap.classList.remove("speaking");
    }
  }

  updateDiagnostics() {
    const diagList = document.getElementById("diag-log-list");
    if (!diagList) return;

    const diagInfo = this.speechEngine.getVoiceDiagnostics();
    const infoEl = document.getElementById("diag-voice-info");
    if (infoEl) {
      infoEl.innerHTML = `
        <div>Total Detected Voices: <strong>${diagInfo.totalVoices}</strong></div>
        <div>Sebastian Voice: <strong>${diagInfo.sebastianVoice}</strong> (Pitch: ${diagInfo.sebastianPitch})</div>
        <div>Oliver Voice: <strong>${diagInfo.oliverVoice}</strong> (Pitch: ${diagInfo.oliverPitch})</div>
        <div>Distinct Voices Verified: <strong style="color: ${diagInfo.isDistinct ? '#10b981' : '#f59e0b'}">${diagInfo.isDistinct ? 'YES (Confirmed)' : 'PITCH SEPARATED'}</strong></div>
      `;
    }
  }

  logDiagnostic(msg, level = "info") {
    const diagList = document.getElementById("diag-log-list");
    if (!diagList) return;

    const entry = document.createElement("div");
    entry.className = `diag-log-entry ${level}`;
    const timestamp = new Date().toLocaleTimeString();
    entry.textContent = `[${timestamp}] ${msg}`;
    diagList.insertBefore(entry, diagList.firstChild);

    while (diagList.children.length > 25) {
      diagList.removeChild(diagList.lastChild);
    }
  }

  playSfx(audio) {
    if (!this.soundEnabled || !audio) return;
    try {
      audio.currentTime = 0;
      audio.play().catch(() => {});
    } catch (e) {}
  }

  formatTime(totalSec) {
    const sec = Math.floor(totalSec);
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }
}

// Global bootstrap on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  window.app = new PresentationApp();
});
