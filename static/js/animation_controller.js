/**
 * animation_controller.js - 2D Vector Character & Stage Animation Controller
 * Coordinates mouth visemes, natural eye blinking, head nods, arm gestures,
 * and holographic display transitions across all 7 scenes.
 * Characters: Dr. Sebastian Clarke & Dr. Oliver Bennett
 */

class AnimationController {
  constructor() {
    this.activeSpeaker = null;
    this.blinkTimers = { sebastian: null, oliver: null };
    this.nodTimers = { sebastian: null, oliver: null };
    this.visemes = ["rest", "open", "round", "wide", "mid"];

    this.initElements();
    this.startBlinkingLoops();
  }

  initElements() {
    this.wrapSebastian = document.getElementById("char-sebastian-wrapper");
    this.wrapOliver = document.getElementById("char-oliver-wrapper");

    this.hologramFrame = document.getElementById("central-hologram-display");
    this.holoMedia = document.getElementById("holo-media-img");
    this.holoTitle = document.getElementById("holo-title");
    this.holoCaption = document.getElementById("holo-caption");
    this.stageContainer = document.getElementById("main-stage");
  }

  /**
   * Set mouth viseme for a character: 'REST', 'OPEN', 'ROUND', 'WIDE', 'MID'
   */
  setViseme(speaker, visemeName) {
    const target = (visemeName || "rest").toLowerCase();
    const prefix = (speaker === "sebastian") ? "sebastian-viseme-" : "oliver-viseme-";

    this.visemes.forEach((v) => {
      const el = document.getElementById(prefix + v);
      if (el) {
        el.style.display = (v === target) ? "inline" : "none";
      }
    });
  }

  /**
   * Update speaking/listening state between the two researchers
   */
  setSpeakerState(speaker) {
    this.activeSpeaker = speaker;

    if (speaker === "sebastian") {
      if (this.wrapSebastian) {
        this.wrapSebastian.classList.add("speaking");
        this.wrapSebastian.classList.remove("listening");
      }
      if (this.wrapOliver) {
        this.wrapOliver.classList.remove("speaking");
        this.wrapOliver.classList.add("listening");
        this.triggerNod("oliver");
      }
      this.setViseme("oliver", "REST");
      this.triggerGesture("sebastian", "explain");
    } else if (speaker === "oliver") {
      if (this.wrapOliver) {
        this.wrapOliver.classList.add("speaking");
        this.wrapOliver.classList.remove("listening");
      }
      if (this.wrapSebastian) {
        this.wrapSebastian.classList.remove("speaking");
        this.wrapSebastian.classList.add("listening");
        this.triggerNod("sebastian");
      }
      this.setViseme("sebastian", "REST");
      this.triggerGesture("oliver", "explain");
    } else {
      // Neither speaking (pause, scene transition, or finale)
      if (this.wrapSebastian) {
        this.wrapSebastian.classList.remove("speaking");
        this.wrapSebastian.classList.remove("listening");
      }
      if (this.wrapOliver) {
        this.wrapOliver.classList.remove("speaking");
        this.wrapOliver.classList.remove("listening");
      }
      this.setViseme("sebastian", "REST");
      this.setViseme("oliver", "REST");
    }
  }

  /**
   * Natural eye blinking loops with randomized physiological intervals
   */
  startBlinkingLoops() {
    const blinkSebastian = () => {
      const eyelids = [
        document.querySelector("#sebastian-eye-left .eye-lid"),
        document.querySelector("#sebastian-eye-right .eye-lid")
      ];
      eyelids.forEach(el => { if (el) el.setAttribute("stroke-width", "8"); });
      setTimeout(() => {
        eyelids.forEach(el => { if (el) el.setAttribute("stroke-width", "2"); });
        const nextInterval = 2800 + Math.random() * 2200;
        this.blinkTimers.sebastian = setTimeout(blinkSebastian, nextInterval);
      }, 130);
    };

    const blinkOliver = () => {
      const eyelids = [
        document.querySelector("#oliver-eye-left .eye-lid"),
        document.querySelector("#oliver-eye-right .eye-lid")
      ];
      eyelids.forEach(el => { if (el) el.setAttribute("stroke-width", "8"); });
      setTimeout(() => {
        eyelids.forEach(el => { if (el) el.setAttribute("stroke-width", "2"); });
        const nextInterval = 2400 + Math.random() * 2000;
        this.blinkTimers.oliver = setTimeout(blinkOliver, nextInterval);
      }, 120);
    };

    this.blinkTimers.sebastian = setTimeout(blinkSebastian, 1500);
    this.blinkTimers.oliver = setTimeout(blinkOliver, 2200);
  }

  /**
   * Subtle listening nod for the attentive non-speaking researcher
   */
  triggerNod(speaker) {
    const head = document.getElementById(`${speaker}-head-group`);
    if (!head) return;

    head.style.transition = "transform 0.4s ease-in-out";
    head.style.transformOrigin = "250px 240px";
    head.style.transform = "rotate(2.5deg) translateY(4px)";

    setTimeout(() => {
      head.style.transform = "rotate(-1deg) translateY(0)";
      setTimeout(() => {
        head.style.transform = "rotate(0deg) translateY(0)";
      }, 350);
    }, 400);
  }

  /**
   * Arm & hand explanatory gesture
   */
  triggerGesture(speaker, type) {
    const armGroup = document.getElementById(`${speaker}-right-arm-group`);
    if (!armGroup) return;

    armGroup.style.transition = "transform 0.5s ease-in-out";
    armGroup.style.transformOrigin = "340px 310px";

    if (type === "explain") {
      armGroup.style.transform = "rotate(-6deg) translateY(-8px)";
      setTimeout(() => {
        armGroup.style.transform = "rotate(0deg) translateY(0)";
      }, 1200);
    }
  }

  /**
   * Update central holographic display for a scene
   */
  updateSceneVisuals(sceneData) {
    if (!sceneData) return;

    if (this.hologramFrame) {
      this.hologramFrame.style.opacity = "0.2";
      this.hologramFrame.style.transform = "translate(-50%, -50%) scale(0.96)";
    }

    setTimeout(() => {
      if (this.holoTitle) {
        this.holoTitle.textContent = sceneData.hologram_title || sceneData.title.toUpperCase();
      }
      if (this.holoCaption) {
        this.holoCaption.textContent = sceneData.hologram_caption || sceneData.subtitle;
      }

      if (this.holoMedia) {
        let mediaSrc = "static/images/pv_cell_cross_section.svg";
        if (sceneData.hologram_type === "earth_energy_globe") {
          mediaSrc = "static/images/demand_vs_generation_balance.png";
        } else if (sceneData.hologram_type === "pv_cell_cross_section") {
          mediaSrc = "static/images/pv_cell_cross_section.svg";
        } else if (sceneData.hologram_type === "wind_hydro_geo") {
          mediaSrc = "static/images/wind_hydro_geo.svg";
        } else if (sceneData.hologram_type === "smart_grid_network") {
          mediaSrc = "static/images/smart_grid_network.svg";
        } else if (sceneData.hologram_type === "matlab_dashboard_view") {
          mediaSrc = "static/images/battery_soc_profile.png";
        } else if (sceneData.hologram_type === "sustainable_future_city" || sceneData.hologram_type === "grand_finale_city") {
          mediaSrc = "static/images/sustainable_future_city.svg";
        }
        this.holoMedia.src = mediaSrc;
      }

      if (this.hologramFrame) {
        this.hologramFrame.style.opacity = "1";
        this.hologramFrame.style.transform = "translate(-50%, -50%) scale(1)";
      }
    }, 250);
  }

  destroy() {
    clearTimeout(this.blinkTimers.sebastian);
    clearTimeout(this.blinkTimers.oliver);
    clearTimeout(this.nodTimers.sebastian);
    clearTimeout(this.nodTimers.oliver);
  }
}

window.AnimationController = AnimationController;
