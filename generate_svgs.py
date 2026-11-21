"""
generate_svgs.py - High-Quality 2D Vector Graphic Generator
Generates clean, scalable SVG assets for characters, laboratory environment,
and specialized renewable energy scientific diagrams:
  1. sebastian_character.svg (Dr. Sebastian Clarke, 36yo, charcoal research suit)
  2. oliver_character.svg (Dr. Oliver Bennett, 29yo, cobalt-blue smart-casual shirt)
  3. lab_background.svg (Futuristic Clean Energy Systems Laboratory)
  4. pv_cell_cross_section.svg (Photovoltaic physics & semiconductor p-n junction)
  5. wind_hydro_geo.svg (Wind turbine aerodynamics, hydro turbine & geothermal loop)
  6. smart_grid_network.svg (Intelligent bidirectional smart grid architecture)
  7. sustainable_future_city.svg (Futuristic eco-metropolis powered by clean energy)
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'static', 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(IMAGES_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"[SVG] Generated: {filename} ({os.path.getsize(path)/1024:.1f} KB)")

def generate_character_sebastian():
    """Dr. Sebastian Clarke: Senior Renewable Energy Scientist (~36 yrs, charcoal suit, composed)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 900" width="100%" height="100%" id="char-sebastian-svg">
  <defs>
    <linearGradient id="suitGradSeb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2d3748" />
      <stop offset="50%" stop-color="#1a202c" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
    <linearGradient id="skinGradSeb" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbd38d" />
      <stop offset="100%" stop-color="#ed8936" />
    </linearGradient>
    <linearGradient id="hairGradSeb" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b2b1a" />
      <stop offset="100%" stop-color="#1e140a" />
    </linearGradient>
    <linearGradient id="tieGradSeb" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
  </defs>

  <g id="sebastian-root">
    <!-- SHADOW ON FLOOR -->
    <ellipse cx="250" cy="870" rx="145" ry="25" fill="#000000" opacity="0.45" />

    <!-- LEGS & TROUSERS (Dark Charcoal Suit Trousers) -->
    <g id="sebastian-lower-body">
      <path d="M 175 580 L 188 850 L 228 850 L 240 580 Z" fill="#1a202c" />
      <path d="M 260 580 L 272 850 L 312 850 L 325 580 Z" fill="#171923" />
      <!-- Polished Dress Shoes -->
      <path d="M 178 845 L 232 845 L 238 865 L 172 865 Z" fill="#0f1117" />
      <path d="M 268 845 L 322 845 L 328 865 L 262 865 Z" fill="#0f1117" />
    </g>

    <!-- TORSO & CHARCOAL SUIT -->
    <g id="sebastian-torso">
      <!-- White Collared Shirt -->
      <polygon points="215,300 250,420 285,300 250,330" fill="#f8fafc" />
      <!-- Silk Cyan/Navy Tie -->
      <polygon points="244,330 256,330 258,450 250,470 242,450" fill="url(#tieGradSeb)" />

      <!-- Charcoal Suit Jacket -->
      <path d="M 160 300 Q 140 440 155 580 L 345 580 Q 360 440 340 300 Q 250 280 160 300 Z" fill="url(#suitGradSeb)" stroke="#374151" stroke-width="1.5" />
      <!-- Left Lapel -->
      <polygon points="160,300 220,440 240,440 195,300" fill="#2d3748" />
      <!-- Right Lapel -->
      <polygon points="340,300 280,440 260,440 305,300" fill="#2d3748" />

      <!-- Senior Scientist Badge -->
      <rect x="290" y="380" width="32" height="46" rx="3" fill="#ffffff" opacity="0.9" stroke="#94a3b8" stroke-width="1" />
      <rect x="294" y="385" width="24" height="15" fill="#0284c7" />
      <line x1="294" y1="406" x2="318" y2="406" stroke="#0f172a" stroke-width="2" />
      <line x1="294" y1="412" x2="312" y2="412" stroke="#64748b" stroke-width="1.5" />
    </g>

    <!-- ARMS & GESTURES -->
    <g id="sebastian-arms">
      <!-- Left arm (Composed analytical gesture) -->
      <g id="sebastian-left-arm-group" class="arm-gesture">
        <path id="sebastian-left-arm" d="M 160 310 Q 120 420 135 510 Q 145 535 175 525" fill="none" stroke="#2d3748" stroke-width="42" stroke-linecap="round" />
        <g id="sebastian-left-hand" transform="translate(170, 520)">
          <circle cx="0" cy="0" r="15" fill="url(#skinGradSeb)" />
          <path d="M 0 -8 C 10 -15, 18 -6, 10 5" fill="none" stroke="url(#skinGradSeb)" stroke-width="5" stroke-linecap="round" />
        </g>
      </g>

      <!-- Right arm (Senior scientist explanatory gesture) -->
      <g id="sebastian-right-arm-group" class="arm-gesture">
        <path id="sebastian-right-arm" d="M 340 310 Q 380 420 365 505 Q 345 540 315 540" fill="none" stroke="#2d3748" stroke-width="42" stroke-linecap="round" />
        <g id="sebastian-right-hand" transform="translate(315, 540)">
          <circle cx="0" cy="0" r="15" fill="url(#skinGradSeb)" />
          <path d="M 5 -8 C 16 -18, 24 -6, 14 5" fill="none" stroke="url(#skinGradSeb)" stroke-width="5" stroke-linecap="round" />
        </g>
      </g>
    </g>

    <!-- NECK & HEAD GROUP (can tilt/nod) -->
    <g id="sebastian-head-group" class="head-container">
      <!-- Neck -->
      <rect x="232" y="240" width="36" height="50" rx="6" fill="url(#skinGradSeb)" />

      <!-- Head Base -->
      <path d="M 200 160 C 200 80, 300 80, 300 160 C 300 240, 280 265, 250 265 C 220 265, 200 240, 200 160 Z" fill="url(#skinGradSeb)" />

      <!-- Ears -->
      <ellipse cx="196" cy="170" rx="8" ry="16" fill="url(#skinGradSeb)" />
      <ellipse cx="304" cy="170" rx="8" ry="16" fill="url(#skinGradSeb)" />

      <!-- Neatly styled dark brown hair (36yo Senior Scientist) -->
      <path d="M 194 150 C 190 90, 230 65, 250 65 C 275 65, 310 85, 306 150 C 298 120, 280 110, 250 110 C 220 110, 202 125, 194 150 Z" fill="url(#hairGradSeb)" />
      <path d="M 194 135 C 190 165, 205 165, 205 145 Z" fill="url(#hairGradSeb)" />
      <path d="M 306 135 C 310 165, 295 165, 295 145 Z" fill="url(#hairGradSeb)" />

      <!-- Eyebrows (Composed, analytical) -->
      <g id="sebastian-eyebrows" class="eyebrows">
        <path d="M 215 145 Q 230 140 242 144" fill="none" stroke="#261b11" stroke-width="4.5" stroke-linecap="round" />
        <path d="M 258 144 Q 270 140 285 145" fill="none" stroke="#261b11" stroke-width="4.5" stroke-linecap="round" />
      </g>

      <!-- Eyes (Natural Blinking System) -->
      <g id="sebastian-eyes" class="eyes-container">
        <!-- Left eye -->
        <g id="sebastian-eye-left">
          <ellipse cx="230" cy="160" rx="9" ry="6" fill="#ffffff" />
          <circle cx="231" cy="160" r="4.2" fill="#2d1d11" />
          <circle cx="232" cy="158" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 221 160 Q 230 152 239 160" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
        <!-- Right eye -->
        <g id="sebastian-eye-right">
          <ellipse cx="270" cy="160" rx="9" ry="6" fill="#ffffff" />
          <circle cx="269" cy="160" r="4.2" fill="#2d1d11" />
          <circle cx="270" cy="158" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 261 160 Q 270 152 279 160" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
      </g>

      <!-- Nose -->
      <path d="M 250 158 L 246 185 L 254 186" fill="none" stroke="#c05621" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />

      <!-- 5 MOUTH VISEMES (REST, OPEN, ROUND, WIDE, MID) -->
      <g id="sebastian-mouth" class="mouth-container">
        <!-- 1. REST (Default closed lips) -->
        <g id="sebastian-viseme-rest" class="viseme" style="display: inline;">
          <path d="M 238 214 Q 250 216 262 214" fill="none" stroke="#9c4221" stroke-width="3.5" stroke-linecap="round" />
          <path d="M 242 216 Q 250 220 258 216" fill="none" stroke="#b0624e" stroke-width="2" />
        </g>
        <!-- 2. OPEN ('ah', 'aa') -->
        <g id="sebastian-viseme-open" class="viseme" style="display: none;">
          <ellipse cx="250" cy="216" rx="13" ry="10" fill="#4a1515" stroke="#9c4221" stroke-width="2" />
          <path d="M 240 212 Q 250 214 260 212" fill="#ffffff" />
          <path d="M 243 222 Q 250 218 257 222" fill="#e06666" />
        </g>
        <!-- 3. ROUND ('oh', 'oo', 'w') -->
        <g id="sebastian-viseme-round" class="viseme" style="display: none;">
          <ellipse cx="250" cy="216" rx="9" ry="11" fill="#4a1515" stroke="#9c4221" stroke-width="2.5" />
          <ellipse cx="250" cy="217" rx="6" ry="7" fill="#2d0b0b" />
        </g>
        <!-- 4. WIDE ('ee', 'ih', 'ae') -->
        <g id="sebastian-viseme-wide" class="viseme" style="display: none;">
          <path d="M 235 214 Q 250 211 265 214 Q 250 222 235 214 Z" fill="#4a1515" stroke="#9c4221" stroke-width="2" />
          <rect x="240" y="213" width="20" height="4" rx="1" fill="#ffffff" />
        </g>
        <!-- 5. MID ('m', 'b', 'p', 'th', 's') -->
        <g id="sebastian-viseme-mid" class="viseme" style="display: none;">
          <path d="M 236 215 Q 250 218 264 215" fill="none" stroke="#883c2a" stroke-width="4.5" stroke-linecap="round" />
        </g>
      </g>
    </g> <!-- end head group -->
  </g>
</svg>'''
    write_svg('sebastian_character.svg', svg)

def generate_character_oliver():
    """Dr. Oliver Bennett: Energy Systems & Computational Researcher (~29 yrs, cobalt-blue shirt, energetic)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 900" width="100%" height="100%" id="char-oliver-svg">
  <defs>
    <linearGradient id="shirtGradOliver" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1d4ed8" />
      <stop offset="50%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1e40af" />
    </linearGradient>
    <linearGradient id="skinGradOliver" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" />
      <stop offset="100%" stop-color="#fbb686" />
    </linearGradient>
    <linearGradient id="hairGradOliver" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#33241b" />
      <stop offset="100%" stop-color="#19120d" />
    </linearGradient>
  </defs>

  <g id="oliver-root">
    <!-- SHADOW ON FLOOR -->
    <ellipse cx="250" cy="870" rx="140" ry="24" fill="#000000" opacity="0.45" />

    <!-- LEGS & LOWER BODY (Dark Slate Smart-Casual Trousers) -->
    <g id="oliver-lower-body">
      <path d="M 180 570 L 192 850 L 228 850 L 238 570 Z" fill="#1e293b" />
      <path d="M 262 570 L 272 850 L 308 850 L 320 570 Z" fill="#182234" />
      <!-- Leather Boots / Shoes -->
      <path d="M 182 845 L 232 845 L 238 865 L 176 865 Z" fill="#2d2218" />
      <path d="M 268 845 L 318 845 L 324 865 L 262 865 Z" fill="#2d2218" />
    </g>

    <!-- TORSO & COBALT-BLUE SMART-CASUAL SHIRT -->
    <g id="oliver-torso">
      <!-- Dark belt -->
      <rect x="180" y="555" width="140" height="18" rx="2" fill="#111827" />
      <rect x="238" y="553" width="24" height="22" rx="2" fill="#94a3b8" />

      <!-- Cobalt-Blue Smart-Casual Shirt -->
      <path d="M 165 300 Q 145 440 160 560 L 340 560 Q 355 440 335 300 Q 250 285 165 300 Z" fill="url(#shirtGradOliver)" stroke="#1d4ed8" stroke-width="1.2" />
      <!-- Open Smart Collar -->
      <polygon points="215,295 240,360 250,330 230,295" fill="#3b82f6" />
      <polygon points="285,295 260,360 250,330 270,295" fill="#3b82f6" />
      <polygon points="240,330 260,330 250,365" fill="#fbb686" />

      <!-- Center Button Placket -->
      <line x1="250" y1="360" x2="250" y2="555" stroke="#1e3a8a" stroke-width="2.5" />
      <circle cx="250" cy="385" r="3" fill="#dbeafe" />
      <circle cx="250" cy="430" r="3" fill="#dbeafe" />
      <circle cx="250" cy="475" r="3" fill="#dbeafe" />
      <circle cx="250" cy="520" r="3" fill="#dbeafe" />

      <!-- Lab Researcher Badge -->
      <rect x="285" y="380" width="30" height="45" rx="3" fill="#ffffff" opacity="0.9" stroke="#94a3b8" stroke-width="1" />
      <rect x="290" y="385" width="20" height="14" fill="#2563eb" />
      <line x1="290" y1="405" x2="310" y2="405" stroke="#0f172a" stroke-width="1.8" />
      <line x1="290" y1="411" x2="305" y2="411" stroke="#64748b" stroke-width="1.4" />
    </g>

    <!-- ARMS & GESTURES -->
    <g id="oliver-arms">
      <!-- Left arm (Holding computing tablet) -->
      <g id="oliver-left-arm-group" class="arm-gesture">
        <path id="oliver-left-arm" d="M 165 310 Q 125 410 145 490 Q 155 520 180 515" fill="none" stroke="#2563eb" stroke-width="40" stroke-linecap="round" />
        <!-- Futuristic Computational Tablet -->
        <g id="oliver-left-hand" transform="translate(170, 500)">
          <rect x="-10" y="-15" width="45" height="30" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" transform="rotate(-15)" />
          <line x1="-5" y1="-8" x2="20" y2="-8" stroke="#10b981" stroke-width="2" transform="rotate(-15)" />
          <line x1="-5" y1="-2" x2="15" y2="-2" stroke="#38bdf8" stroke-width="1.5" transform="rotate(-15)" />
          <circle cx="5" cy="0" r="14" fill="url(#skinGradOliver)" />
        </g>
      </g>

      <!-- Right arm (Expressive explanatory gestures) -->
      <g id="oliver-right-arm-group" class="arm-gesture">
        <path id="oliver-right-arm" d="M 335 310 Q 365 410 345 500 Q 330 535 310 545" fill="none" stroke="#2563eb" stroke-width="40" stroke-linecap="round" />
        <g id="oliver-right-hand" transform="translate(305, 545)">
          <circle cx="0" cy="0" r="14" fill="url(#skinGradOliver)" />
          <path d="M 5 -8 C 15 -18, 22 -6, 12 5" fill="none" stroke="url(#skinGradOliver)" stroke-width="5" stroke-linecap="round" />
        </g>
      </g>
    </g>

    <!-- NECK & HEAD GROUP (Curious, energetic 29yo researcher) -->
    <g id="oliver-head-group" class="head-container">
      <!-- Neck -->
      <rect x="233" y="240" width="34" height="50" rx="5" fill="url(#skinGradOliver)" />

      <!-- Head Base -->
      <path d="M 205 165 C 205 90, 295 90, 295 165 C 295 240, 275 260, 250 260 C 225 260, 205 240, 205 165 Z" fill="url(#skinGradOliver)" />

      <!-- Ears -->
      <ellipse cx="201" cy="172" rx="8" ry="15" fill="url(#skinGradOliver)" />
      <ellipse cx="299" cy="172" rx="8" ry="15" fill="url(#skinGradOliver)" />

      <!-- Textured modern short dark hair -->
      <path d="M 198 150 C 195 85, 235 60, 255 60 C 280 60, 305 80, 302 150 C 292 115, 270 105, 250 105 C 225 105, 208 120, 198 150 Z" fill="url(#hairGradOliver)" />
      <!-- Textured hair tufts -->
      <path d="M 220 70 Q 235 55 245 68" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" />
      <path d="M 245 62 Q 260 50 270 65" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" />

      <!-- Eyebrows (Curious, enthusiastic) -->
      <g id="oliver-eyebrows" class="eyebrows">
        <path d="M 218 144 Q 232 138 244 142" fill="none" stroke="#241a13" stroke-width="4.2" stroke-linecap="round" />
        <path d="M 256 142 Q 268 138 282 144" fill="none" stroke="#241a13" stroke-width="4.2" stroke-linecap="round" />
      </g>

      <!-- Eyes (Natural Blinking System) -->
      <g id="oliver-eyes" class="eyes-container">
        <!-- Left eye -->
        <g id="oliver-eye-left">
          <ellipse cx="232" cy="159" rx="8.5" ry="6" fill="#ffffff" />
          <circle cx="233" cy="159" r="4.0" fill="#2d1d11" />
          <circle cx="234" cy="157" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 223 159 Q 232 151 241 159" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
        <!-- Right eye -->
        <g id="oliver-eye-right">
          <ellipse cx="268" cy="159" rx="8.5" ry="6" fill="#ffffff" />
          <circle cx="267" cy="159" r="4.0" fill="#2d1d11" />
          <circle cx="268" cy="157" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 259 159 Q 268 151 277 159" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
      </g>

      <!-- Nose -->
      <path d="M 250 157 L 247 183 L 253 184" fill="none" stroke="#dd6b20" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" />

      <!-- 5 MOUTH VISEMES -->
      <g id="oliver-mouth" class="mouth-container">
        <!-- 1. REST (Default closed lips) -->
        <g id="oliver-viseme-rest" class="viseme" style="display: inline;">
          <path d="M 239 212 Q 250 215 261 212" fill="none" stroke="#9c4221" stroke-width="3.2" stroke-linecap="round" />
          <path d="M 243 214 Q 250 218 257 214" fill="none" stroke="#b0624e" stroke-width="2" />
        </g>
        <!-- 2. OPEN ('ah', 'aa') -->
        <g id="oliver-viseme-open" class="viseme" style="display: none;">
          <ellipse cx="250" cy="214" rx="12" ry="9" fill="#4a1515" stroke="#9c4221" stroke-width="2" />
          <path d="M 241 210 Q 250 212 259 210" fill="#ffffff" />
          <path d="M 244 219 Q 250 216 256 219" fill="#e06666" />
        </g>
        <!-- 3. ROUND ('oh', 'oo', 'w') -->
        <g id="oliver-viseme-round" class="viseme" style="display: none;">
          <ellipse cx="250" cy="214" rx="8.5" ry="10" fill="#4a1515" stroke="#9c4221" stroke-width="2.5" />
          <ellipse cx="250" cy="215" rx="5.5" ry="6" fill="#2d0b0b" />
        </g>
        <!-- 4. WIDE ('ee', 'ih', 'ae') -->
        <g id="oliver-viseme-wide" class="viseme" style="display: none;">
          <path d="M 236 212 Q 250 209 264 212 Q 250 220 236 212 Z" fill="#4a1515" stroke="#9c4221" stroke-width="2" />
          <rect x="241" y="211" width="18" height="3.5" rx="1" fill="#ffffff" />
        </g>
        <!-- 5. MID ('m', 'b', 'p', 'th', 's') -->
        <g id="oliver-viseme-mid" class="viseme" style="display: none;">
          <path d="M 237 213 Q 250 216 263 213" fill="none" stroke="#883c2a" stroke-width="4.2" stroke-linecap="round" />
        </g>
      </g>
    </g> <!-- end head group -->
  </g>
</svg>'''
    write_svg('oliver_character.svg', svg)

def generate_lab_background():
    """Futuristic Clean Energy Systems Laboratory."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <defs>
    <linearGradient id="labBgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040711" />
      <stop offset="50%" stop-color="#0a1020" />
      <stop offset="100%" stop-color="#03050b" />
    </linearGradient>
    <linearGradient id="wallPanel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111827" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0.95" />
    </linearGradient>
    <radialGradient id="holoGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.45" />
      <stop offset="40%" stop-color="#10b981" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#040711" stop-opacity="0" />
    </radialGradient>
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8" stroke-opacity="0.4" />
    </pattern>
  </defs>

  <!-- Deep Lab Space -->
  <rect width="1920" height="1080" fill="url(#labBgGrad)" />

  <!-- Laboratory Ceiling Architecture -->
  <polygon points="0,0 1920,0 1800,130 120,130" fill="#0b1120" />
  <line x1="160" y1="130" x2="1760" y2="130" stroke="#38bdf8" stroke-width="2" opacity="0.4" filter="url(#neonGlow)" />
  <line x1="380" y1="0" x2="330" y2="130" stroke="#1e293b" stroke-width="2" />
  <line x1="960" y1="0" x2="960" y2="130" stroke="#1e293b" stroke-width="2" />
  <line x1="1540" y1="0" x2="1590" y2="130" stroke="#1e293b" stroke-width="2" />

  <!-- Back Wall Structural Panels -->
  <rect x="80" y="130" width="1760" height="630" fill="url(#gridPattern)" />
  <rect x="110" y="160" width="410" height="560" rx="8" fill="url(#wallPanel)" stroke="#1e293b" stroke-width="1.5" />
  <rect x="1400" y="160" width="410" height="560" rx="8" fill="url(#wallPanel)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Central Scientific Visualization Aperture -->
  <circle cx="960" cy="430" r="330" fill="#030611" stroke="#1e293b" stroke-width="2" />
  <circle cx="960" cy="430" r="310" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.6" />
  <circle cx="960" cy="430" r="270" fill="none" stroke="#10b981" stroke-width="1.2" stroke-dasharray="14 10" opacity="0.5" />
  <circle cx="960" cy="430" r="220" fill="url(#holoGlow)" />

  <!-- Holographic Clean Energy Rings -->
  <ellipse cx="960" cy="430" rx="280" ry="85" fill="none" stroke="#38bdf8" stroke-width="1.2" opacity="0.5" transform="rotate(-20 960 430)" />
  <ellipse cx="960" cy="430" rx="280" ry="85" fill="none" stroke="#10b981" stroke-width="1.2" opacity="0.4" transform="rotate(30 960 430)" />

  <!-- Left Column Telemetry -->
  <g opacity="0.75" font-family="'Consolas', 'Courier New', monospace" font-size="12" fill="#38bdf8">
    <text x="130" y="200" font-weight="bold">CLEAN ENERGY TELEMETRY NODE 01</text>
    <text x="130" y="225">P_solar = G * A * eta</text>
    <text x="130" y="245">G_STC = 1000 W/m^2 | A = 1.5e6 m^2</text>
    <text x="130" y="265">Si Standard: 20% | TOPCon: 24%</text>
    <text x="130" y="285">Perovskite Tandem: 32% (Lab: 33.7%)</text>
    <path d="M 130 305 L 490 305" stroke="#38bdf8" stroke-width="1" opacity="0.5" />
    <text x="130" y="330">P_wind = 0.5 * rho * A * v^3 * Cp</text>
    <text x="130" y="350">Betz Limit Max: 16/27 = 59.26%</text>
    <text x="130" y="370">Fleet Rotor Swept: 17,671 m^2</text>
    <text x="130" y="390">Aerodynamic Rotor Cp: 0.46</text>
    <path d="M 130 410 L 490 410" stroke="#38bdf8" stroke-width="1" opacity="0.5" />
    <text x="130" y="435">BESS STORAGE DISPATCH: ONLINE</text>
    <text x="130" y="455">Capacity: 1.2 GWh | Rating: 300 MW</text>
    <text x="130" y="475">Roundtrip Efficiency: 88.36%</text>
  </g>

  <!-- Right Column Telemetry -->
  <g opacity="0.75" font-family="'Consolas', 'Courier New', monospace" font-size="12" fill="#10b981">
    <text x="1420" y="200" font-weight="bold">GRID DISPATCH & MATLAB SOLVER</text>
    <text x="1420" y="225">SCRIPT: RenewableEnergy.m</text>
    <text x="1420" y="245">STATUS: SOLVED (dt = 0.1 hr)</text>
    <text x="1420" y="265">REGIONAL LOAD PEAK: 680.0 MW</text>
    <text x="1420" y="285">TOTAL RE GENERATION: 12,302 MWh</text>
    <path d="M 1420 305 L 1780 305" stroke="#10b981" stroke-width="1" opacity="0.5" />
    <text x="1420" y="330">RE DEMAND COVERAGE: 99.52%</text>
    <text x="1420" y="350">CURTAILMENT MITIGATION: 98.4%</text>
    <text x="1420" y="370">V2G DISTRIBUTED RESERVE: READY</text>
    <text x="1420" y="390">GREEN H2 ELECTROLYSIS: 45 MW</text>
    <path d="M 1420 410 L 1780 410" stroke="#10b981" stroke-width="1" opacity="0.5" />
    <text x="1420" y="435">EMISSIONS REDUCTION: -94.2%</text>
    <text x="1420" y="455">GRID FREQUENCY: 50.00 Hz +/- 0.02</text>
    <text x="1420" y="475">AI LOAD FORECAST ERROR: 1.8% MAPE</text>
  </g>

  <!-- Floor Platform with Perspective -->
  <polygon points="0,760 1920,760 1920,1080 0,1080" fill="#070a14" />
  <line x1="0" y1="760" x2="1920" y2="760" stroke="#1e293b" stroke-width="2" />
  <!-- Floor Grid Lines -->
  <line x1="300" y1="760" x2="100" y2="1080" stroke="#1e293b" stroke-width="1.2" opacity="0.6" />
  <line x1="600" y1="760" x2="500" y2="1080" stroke="#1e293b" stroke-width="1.2" opacity="0.6" />
  <line x1="960" y1="760" x2="960" y2="1080" stroke="#38bdf8" stroke-width="1.5" opacity="0.4" />
  <line x1="1320" y1="760" x2="1420" y2="1080" stroke="#1e293b" stroke-width="1.2" opacity="0.6" />
  <line x1="1620" y1="760" x2="1820" y2="1080" stroke="#1e293b" stroke-width="1.2" opacity="0.6" />
</svg>'''
    write_svg('lab_background.svg', svg)

def generate_pv_cell_cross_section():
    """Photovoltaic conversion physics: semiconductor p-n junction, photon excitation, electron-hole flow."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" height="100%">
  <defs>
    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="100%" stop-color="#f59e0b" />
    </linearGradient>
    <linearGradient id="nTypeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="pTypeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f766e" />
      <stop offset="100%" stop-color="#115e59" />
    </linearGradient>
    <linearGradient id="depletionGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#10b981" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#0d9488" stop-opacity="0.3" />
    </linearGradient>
  </defs>

  <!-- Dark Background Panel -->
  <rect width="900" height="600" rx="12" fill="#090d16" stroke="#1e293b" stroke-width="2" />

  <!-- Diagram Header -->
  <text x="450" y="45" font-family="'Consolas', 'Courier New', monospace" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">PHOTOVOLTAIC CONVERSION: SEMICONDUCTOR P-N JUNCTION</text>
  <text x="450" y="70" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Incident photon (hν > Eg) creates electron-hole pair; internal electric field drives DC current</text>

  <!-- Incident Solar Rays -->
  <g>
    <!-- Sun symbol -->
    <circle cx="100" cy="110" r="30" fill="url(#sunGrad)" />
    <!-- Rays -->
    <path d="M 140 120 L 220 180" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 3" marker-end="url(#arrow)" />
    <path d="M 150 140 L 270 210" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 3" />
    <path d="M 120 150 L 320 220" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 3" />
    <text x="190" y="145" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#f59e0b">Incident Photons (hν > E_g)</text>
  </g>

  <!-- Front Contact Metal Fingers (Silver grid) -->
  <rect x="220" y="195" width="20" height="15" fill="#e2e8f0" stroke="#94a3b8" />
  <rect x="360" y="195" width="20" height="15" fill="#e2e8f0" stroke="#94a3b8" />
  <rect x="500" y="195" width="20" height="15" fill="#e2e8f0" stroke="#94a3b8" />
  <rect x="640" y="195" width="20" height="15" fill="#e2e8f0" stroke="#94a3b8" />
  <text x="680" y="206" font-family="sans-serif" font-size="11" fill="#cbd5e1">Front Metal Contact Grid</text>

  <!-- Antireflective Coating Layer -->
  <rect x="200" y="210" width="500" height="12" fill="#0284c7" opacity="0.8" />
  <text x="715" y="220" font-family="sans-serif" font-size="11" fill="#38bdf8">Antireflective Coating (SiNx, ~75 nm)</text>

  <!-- n-Type Emitter Layer (Silicon doped with Phosphorus) -->
  <rect x="200" y="222" width="500" height="50" fill="url(#nTypeGrad)" stroke="#0284c7" stroke-width="1" />
  <text x="450" y="252" font-family="'Consolas', monospace" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">n-Type Silicon Layer (Free Electrons e⁻)</text>

  <!-- Depletion Region / P-N Junction -->
  <rect x="200" y="272" width="500" height="45" fill="url(#depletionGrad)" stroke="#10b981" stroke-width="1.5" />
  <text x="450" y="295" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">DEPLETION REGION: Built-in Electric Field E ➔</text>
  <text x="450" y="310" font-family="sans-serif" font-size="10" fill="#e2e8f0" text-anchor="middle">Space charge separates electrons (up) and holes (down)</text>

  <!-- p-Type Base Layer (Silicon doped with Boron) -->
  <rect x="200" y="317" width="500" height="110" fill="url(#pTypeGrad)" stroke="#0f766e" stroke-width="1" />
  <text x="450" y="375" font-family="'Consolas', monospace" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">p-Type Silicon Base (Holes h⁺)</text>

  <!-- Rear Metal Contact (Aluminum) -->
  <rect x="200" y="427" width="500" height="16" fill="#94a3b8" stroke="#64748b" />
  <text x="715" y="438" font-family="sans-serif" font-size="11" fill="#cbd5e1">Rear Full-Area Contact (Al BSF)</text>

  <!-- External Electric Circuit with Load & Electron Flow -->
  <path d="M 230 195 L 230 150 L 780 150 L 780 435 L 700 435" fill="none" stroke="#38bdf8" stroke-width="2.5" />
  <!-- Electrical Load Symbol -->
  <circle cx="780" cy="280" r="22" fill="#111827" stroke="#10b981" stroke-width="2" />
  <text x="780" y="284" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">LOAD</text>
  <text x="780" y="320" font-family="'Consolas', monospace" font-size="11" fill="#38bdf8" text-anchor="middle">P_out = V * I</text>

  <!-- Flow Arrows -->
  <circle cx="500" cy="150" r="5" fill="#38bdf8" />
  <text x="500" y="142" font-family="'Consolas', monospace" font-size="11" fill="#38bdf8" text-anchor="middle">e⁻ flow ➔</text>

  <!-- Physics Formula Box -->
  <rect x="180" y="480" width="540" height="90" rx="8" fill="#111827" stroke="#1e293b" />
  <text x="200" y="505" font-family="'Consolas', monospace" font-size="12" font-weight="bold" fill="#38bdf8">KEY PHOTOVOLTAIC EQUATION: P_solar = G × A × η</text>
  <text x="200" y="525" font-family="sans-serif" font-size="11" fill="#cbd5e1">• G: Solar irradiance [W/m²] (1000 W/m² Standard Test Conditions)</text>
  <text x="200" y="542" font-family="sans-serif" font-size="11" fill="#cbd5e1">• A: Active panel surface area [m²] | η: Solar-to-electrical conversion efficiency</text>
  <text x="200" y="559" font-family="sans-serif" font-size="11" fill="#10b981">• Silicon Bandgap: Eg ≈ 1.12 eV | Max Theoretical Shockley-Queisser Limit: ~33.7%</text>
</svg>'''
    write_svg('pv_cell_cross_section.svg', svg)

def generate_wind_hydro_geo():
    """Fluid dynamics, Betz limit wind turbine, hydro dam, and geothermal loop."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" height="100%">
  <!-- Dark Background Panel -->
  <rect width="900" height="600" rx="12" fill="#090d16" stroke="#1e293b" stroke-width="2" />

  <!-- Diagram Header -->
  <text x="450" y="45" font-family="'Consolas', 'Courier New', monospace" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">WIND AERODYNAMICS, HYDRO TURBINES &amp; GEOTHERMAL ENTHALPY</text>

  <!-- SECTION 1: WIND TURBINE AERODYNAMICS (Left Side) -->
  <g transform="translate(40, 70)">
    <rect width="250" height="380" rx="8" fill="#111827" stroke="#1e293b" />
    <text x="125" y="30" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">WIND AERODYNAMICS</text>

    <!-- Turbine Tower -->
    <polygon points="120,130 115,340 135,340 130,130" fill="#64748b" />
    <ellipse cx="125" cy="340" rx="30" ry="8" fill="#334155" />

    <!-- Nacelle & Hub -->
    <rect x="110" y="118" width="40" height="20" rx="4" fill="#94a3b8" />
    <ellipse cx="110" cy="128" rx="8" ry="10" fill="#0284c7" />

    <!-- 3 Rotor Blades -->
    <line x1="110" y1="128" x2="110" y2="45" stroke="#f8fafc" stroke-width="6" stroke-linecap="round" />
    <line x1="110" y1="128" x2="45" y2="185" stroke="#f8fafc" stroke-width="6" stroke-linecap="round" />
    <line x1="110" y1="128" x2="175" y2="185" stroke="#f8fafc" stroke-width="6" stroke-linecap="round" />

    <!-- Aerodynamic Wind Flow Streamlines -->
    <path d="M 20 70 Q 70 85 100 80 Q 140 75 220 90" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.7" />
    <path d="M 20 120 Q 70 128 100 125 Q 140 120 220 130" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="4 3" opacity="0.85" />
    <path d="M 20 170 Q 70 165 100 170 Q 140 175 220 170" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.7" />

    <text x="125" y="270" font-family="'Consolas', monospace" font-size="11" fill="#cbd5e1" text-anchor="middle">P = 0.5 * rho * A * v^3 * Cp</text>
    <text x="125" y="295" font-family="'Consolas', monospace" font-size="11" fill="#10b981" text-anchor="middle">Betz Limit: Cp &lt;= 59.3%</text>
    <text x="125" y="320" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Modern Fleet Cp: ~46%</text>
  </g>

  <!-- SECTION 2: HYDROELECTRIC RESERVOIR & TURBINE (Center) -->
  <g transform="translate(325, 70)">
    <rect width="250" height="380" rx="8" fill="#111827" stroke="#1e293b" />
    <text x="125" y="30" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#0284c7" text-anchor="middle">HYDROELECTRIC STORAGE</text>

    <!-- Water Reservoir -->
    <path d="M 20 80 L 100 80 L 100 240 L 20 240 Z" fill="#0369a1" opacity="0.7" />
    <text x="60" y="130" font-family="'Consolas', monospace" font-size="11" fill="#e0f2fe" text-anchor="middle">Upper Reservoir</text>
    <text x="60" y="145" font-family="sans-serif" font-size="10" fill="#bae6fd" text-anchor="middle">(Potential Head H)</text>

    <!-- Concrete Dam Structure -->
    <polygon points="100,60 170,240 100,240" fill="#475569" />

    <!-- Penstock Tube -->
    <path d="M 90 200 L 150 250 L 180 250" fill="none" stroke="#0ea5e9" stroke-width="8" stroke-linecap="round" />

    <!-- Francis / Pelton Turbine -->
    <circle cx="180" cy="250" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
    <path d="M 172 245 L 188 255 M 172 255 L 188 245" stroke="#38bdf8" stroke-width="2.5" />

    <!-- Generator & Power Line -->
    <rect x="170" y="210" width="20" height="20" fill="#f59e0b" />
    <text x="180" y="200" font-family="'Consolas', monospace" font-size="10" fill="#f59e0b" text-anchor="middle">Generator</text>

    <text x="125" y="295" font-family="'Consolas', monospace" font-size="11" fill="#cbd5e1" text-anchor="middle">P_hydro = rho * g * Q * H * eta</text>
    <text x="125" y="320" font-family="sans-serif" font-size="10" fill="#10b981" text-anchor="middle">Rapid dispatchable inertia</text>
    <text x="125" y="340" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Pumped hydro: 80%+ roundtrip</text>
  </g>

  <!-- SECTION 3: GEOTHERMAL CLOSED LOOP (Right Side) -->
  <g transform="translate(610, 70)">
    <rect width="250" height="380" rx="8" fill="#111827" stroke="#1e293b" />
    <text x="125" y="30" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">DEEP GEOTHERMAL</text>

    <!-- Surface Plant -->
    <rect x="80" y="80" width="90" height="45" rx="4" fill="#334155" stroke="#10b981" stroke-width="1.5" />
    <text x="125" y="105" font-family="'Consolas', monospace" font-size="10" fill="#10b981" text-anchor="middle">Flash Turbine Plant</text>

    <!-- Earth Stratum -->
    <rect x="20" y="140" width="210" height="130" fill="#1c1917" opacity="0.9" />
    <text x="125" y="165" font-family="sans-serif" font-size="10" fill="#a8a29e" text-anchor="middle">Impermeable Rock Layer</text>

    <!-- Deep Magmatic Heat Reservoir -->
    <rect x="20" y="220" width="210" height="50" fill="#7f1d1d" opacity="0.8" />
    <text x="125" y="248" font-family="'Consolas', monospace" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Hot Rocks / Reservoir (250°C+)</text>

    <!-- Production Well (Hot Steam Up) -->
    <line x1="95" y1="125" x2="95" y2="235" stroke="#ef4444" stroke-width="4" stroke-dasharray="6 3" />
    <!-- Reinjection Well (Cold Water Down) -->
    <line x1="155" y1="125" x2="155" y2="235" stroke="#0ea5e9" stroke-width="4" stroke-dasharray="6 3" />

    <text x="125" y="295" font-family="'Consolas', monospace" font-size="11" fill="#cbd5e1" text-anchor="middle">P_geo = m_dot * delta_h * eta</text>
    <text x="125" y="320" font-family="sans-serif" font-size="10" fill="#10b981" text-anchor="middle">Continuous 24/7 baseload</text>
    <text x="125" y="340" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Zero meteorological dependence</text>
  </g>

  <!-- Summary Footer -->
  <rect x="40" y="475" width="820" height="95" rx="8" fill="#111827" stroke="#1e293b" />
  <text x="450" y="505" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">SYSTEM COMPLEMENTARITY: GEOGRAPHICAL DIVERSITY</text>
  <text x="450" y="528" font-family="sans-serif" font-size="11" fill="#e2e8f0" text-anchor="middle">High wind output during nocturnal hours balances diurnal solar generation.</text>
  <text x="450" y="548" font-family="sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Hydro reservoirs and geothermal turbines provide synchronous physical inertia, stabilizing grid frequency.</text>
</svg>'''
    write_svg('wind_hydro_geo.svg', svg)

def generate_smart_grid_network():
    """Intelligent bidirectional smart grid architecture."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" height="100%">
  <!-- Dark Background Panel -->
  <rect width="900" height="600" rx="12" fill="#090d16" stroke="#1e293b" stroke-width="2" />

  <!-- Diagram Header -->
  <text x="450" y="45" font-family="'Consolas', 'Courier New', monospace" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTELLIGENT SMART GRID: MULTI-TIMESCALE ENERGY ARCHITECTURE</text>
  <text x="450" y="70" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Real-time balancing of variable generation, battery storage, and dynamic load</text>

  <!-- Central Digital Smart Substation / AI Dispatch Hub -->
  <circle cx="450" cy="300" r="65" fill="#111827" stroke="#38bdf8" stroke-width="3" />
  <circle cx="450" cy="300" r="50" fill="#0c1a30" stroke="#10b981" stroke-width="1.5" stroke-dasharray="6 4" />
  <text x="450" y="295" font-family="'Consolas', monospace" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CENTRAL AI</text>
  <text x="450" y="312" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">DISPATCH HUB</text>

  <!-- Node 1: Solar Farm (Top Left) -->
  <g transform="translate(140, 140)">
    <circle cx="0" cy="0" r="45" fill="#111827" stroke="#f59e0b" stroke-width="2" />
    <text x="0" y="-8" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">SOLAR FARM</text>
    <text x="0" y="10" font-family="sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">330 MW Peak</text>
    <line x1="35" y1="25" x2="250" y2="120" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4" />
  </g>

  <!-- Node 2: Offshore Wind (Top Right) -->
  <g transform="translate(760, 140)">
    <circle cx="0" cy="0" r="45" fill="#111827" stroke="#38bdf8" stroke-width="2" />
    <text x="0" y="-8" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">WIND FLEET</text>
    <text x="0" y="10" font-family="sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">360 MW Rated</text>
    <line x1="-35" y1="25" x2="-250" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4" />
  </g>

  <!-- Node 3: Battery Energy Storage System (BESS) (Left) -->
  <g transform="translate(110, 320)">
    <circle cx="0" cy="0" r="48" fill="#111827" stroke="#10b981" stroke-width="2" />
    <text x="0" y="-10" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">BESS STORAGE</text>
    <text x="0" y="8" font-family="sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">1.2 GWh / 300 MW</text>
    <text x="0" y="24" font-family="'Consolas', monospace" font-size="8" fill="#34d399" text-anchor="middle">η_rt = 88.4%</text>
    <line x1="48" y1="0" x2="275" y2="-15" stroke="#10b981" stroke-width="3" />
  </g>

  <!-- Node 4: Green Hydrogen Electrolyzer (Right) -->
  <g transform="translate(790, 320)">
    <circle cx="0" cy="0" r="48" fill="#111827" stroke="#a855f7" stroke-width="2" />
    <text x="0" y="-10" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#a855f7" text-anchor="middle">GREEN H2</text>
    <text x="0" y="8" font-family="sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">Electrolyzer</text>
    <text x="0" y="24" font-family="sans-serif" font-size="8" fill="#d8b4fe" text-anchor="middle">Seasonal Buffer</text>
    <line x1="-48" y1="0" x2="-275" y2="-15" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="6 4" />
  </g>

  <!-- Node 5: Modern Eco-City Load & V2G (Bottom Center) -->
  <g transform="translate(450, 480)">
    <circle cx="0" cy="0" r="50" fill="#111827" stroke="#f43f5e" stroke-width="2" />
    <text x="0" y="-10" font-family="'Consolas', monospace" font-size="11" font-weight="bold" fill="#f43f5e" text-anchor="middle">REGIONAL DEMAND</text>
    <text x="0" y="8" font-family="sans-serif" font-size="9" fill="#cbd5e1" text-anchor="middle">Peak: 680 MW</text>
    <text x="0" y="24" font-family="'Consolas', monospace" font-size="8" fill="#fb7185" text-anchor="middle">V2G EV Fleet Connected</text>
    <line x1="0" y1="-50" x2="0" y2="-115" stroke="#f43f5e" stroke-width="3" />
  </g>

  <!-- Active Telemetry Status Banner -->
  <rect x="180" y="540" width="540" height="42" rx="6" fill="#111827" stroke="#1e293b" />
  <text x="450" y="565" font-family="'Consolas', monospace" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">REAL-TIME GRID STATUS: BALANCED | FREQUENCY: 50.00 Hz | COVERAGE: 99.5%</text>
</svg>'''
    write_svg('smart_grid_network.svg', svg)

def generate_sustainable_future_city():
    """Futuristic sustainable eco-city powered by clean renewable energy."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#020617" />
      <stop offset="60%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="seaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f2b46" />
      <stop offset="100%" stop-color="#06121e" />
    </linearGradient>
    <linearGradient id="bldgGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#334155" />
    </linearGradient>
  </defs>

  <!-- Sky -->
  <rect width="900" height="600" rx="12" fill="url(#skyGrad)" stroke="#1e293b" stroke-width="2" />

  <!-- Clean Ocean Horizon -->
  <rect x="0" y="380" width="900" height="220" fill="url(#seaGrad)" />
  <line x1="0" y1="380" x2="900" y2="380" stroke="#38bdf8" stroke-width="1.5" opacity="0.6" />

  <!-- Offshore Floating Wind Turbines on Horizon -->
  <g opacity="0.85">
    <!-- Turbine 1 -->
    <line x1="120" y1="380" x2="120" y2="310" stroke="#94a3b8" stroke-width="2.5" />
    <circle cx="120" cy="310" r="3" fill="#e2e8f0" />
    <line x1="120" y1="310" x2="120" y2="275" stroke="#f8fafc" stroke-width="1.8" />
    <line x1="120" y1="310" x2="90" y2="325" stroke="#f8fafc" stroke-width="1.8" />
    <line x1="120" y1="310" x2="150" y2="325" stroke="#f8fafc" stroke-width="1.8" />

    <!-- Turbine 2 -->
    <line x1="220" y1="380" x2="220" y2="325" stroke="#94a3b8" stroke-width="2" />
    <circle cx="220" cy="325" r="2.5" fill="#e2e8f0" />
    <line x1="220" y1="325" x2="220" y2="295" stroke="#f8fafc" stroke-width="1.5" />
    <line x1="220" y1="325" x2="195" y2="338" stroke="#f8fafc" stroke-width="1.5" />
    <line x1="220" y1="325" x2="245" y2="338" stroke="#f8fafc" stroke-width="1.5" />

    <!-- Turbine 3 -->
    <line x1="800" y1="380" x2="800" y2="315" stroke="#94a3b8" stroke-width="2.2" />
    <circle cx="800" cy="315" r="2.8" fill="#e2e8f0" />
    <line x1="800" y1="315" x2="800" y2="282" stroke="#f8fafc" stroke-width="1.6" />
    <line x1="800" y1="315" x2="772" y2="330" stroke="#f8fafc" stroke-width="1.6" />
    <line x1="800" y1="315" x2="828" y2="330" stroke="#f8fafc" stroke-width="1.6" />
  </g>

  <!-- Futuristic Sustainable City Skyline -->
  <!-- Building 1 (Left Tower) -->
  <polygon points="280,380 280,180 340,140 340,380" fill="url(#bldgGrad1)" stroke="#38bdf8" stroke-width="1" />
  <line x1="295" y1="180" x2="295" y2="380" stroke="#38bdf8" stroke-width="1.2" opacity="0.6" stroke-dasharray="8 6" />
  <line x1="320" y1="160" x2="320" y2="380" stroke="#10b981" stroke-width="1.2" opacity="0.6" stroke-dasharray="8 6" />

  <!-- Building 2 (Central Eco-Spire with Rooftop Perovskite Array) -->
  <polygon points="400,380 400,100 450,60 500,100 500,380" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <polygon points="420,100 450,65 480,100" fill="#0284c7" opacity="0.8" />
  <text x="450" y="95" font-family="'Consolas', monospace" font-size="8" fill="#ffffff" text-anchor="middle">PV ROOF</text>
  <!-- Vertical Forest Green Balconies -->
  <rect x="415" y="140" width="70" height="8" rx="2" fill="#10b981" opacity="0.8" />
  <rect x="415" y="180" width="70" height="8" rx="2" fill="#10b981" opacity="0.8" />
  <rect x="415" y="220" width="70" height="8" rx="2" fill="#10b981" opacity="0.8" />
  <rect x="415" y="260" width="70" height="8" rx="2" fill="#10b981" opacity="0.8" />
  <rect x="415" y="300" width="70" height="8" rx="2" fill="#10b981" opacity="0.8" />

  <!-- Building 3 (Right Sleek Tower) -->
  <polygon points="560,380 560,160 620,200 620,380" fill="url(#bldgGrad1)" stroke="#38bdf8" stroke-width="1" />
  <line x1="580" y1="180" x2="580" y2="380" stroke="#38bdf8" stroke-width="1.2" opacity="0.6" stroke-dasharray="8 6" />
  <line x1="605" y1="200" x2="605" y2="380" stroke="#f59e0b" stroke-width="1.2" opacity="0.6" stroke-dasharray="8 6" />

  <!-- Clean Maglev / Electric Transit Sky-Bridge -->
  <path d="M 180 340 Q 450 310 720 340" fill="none" stroke="#38bdf8" stroke-width="5" opacity="0.8" />
  <path d="M 400 322 L 440 322" stroke="#ffffff" stroke-width="7" stroke-linecap="round" />

  <!-- Header Banner -->
  <text x="450" y="45" font-family="'Consolas', 'Courier New', monospace" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE SUSTAINABLE METROPOLIS OF TOMORROW</text>
  <text x="450" y="70" font-family="sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Integrated photovoltaics, floating offshore wind, green hydrogen, and automated AI dispatch</text>

  <!-- Title Card for Scene 7 -->
  <rect x="150" y="430" width="600" height="110" rx="10" fill="#0b1120" opacity="0.9" stroke="#38bdf8" stroke-width="2" />
  <text x="450" y="468" font-family="'Consolas', monospace" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">THE FUTURE OF RENEWABLE ENERGY</text>
  <text x="450" y="495" font-family="sans-serif" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">POWERING A CLEANER, SMARTER, AND MORE SUSTAINABLE WORLD</text>
  <text x="450" y="522" font-family="sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Dr. Sebastian Clarke &amp; Dr. Oliver Bennett — Clean Energy Systems Research Group</text>
</svg>'''
    write_svg('sustainable_future_city.svg', svg)

def main():
    print("=" * 65)
    print(" 2D VECTOR SVG ASSET GENERATOR")
    print(" Generating characters, laboratory background, and scientific diagrams...")
    print("=" * 65)
    generate_character_sebastian()
    generate_character_oliver()
    generate_lab_background()
    generate_pv_cell_cross_section()
    generate_wind_hydro_geo()
    generate_smart_grid_network()
    generate_sustainable_future_city()
    print("\n[SVG] All vector graphics successfully generated!")

if __name__ == '__main__':
    main()
