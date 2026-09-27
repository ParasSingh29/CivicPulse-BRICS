/**
 * CIVICPULSE-BRICS: CURSOR-REACTIVE ANIMATED BACKGROUND
 * Floating particle network that reacts to mouse movement.
 * Particles drift, connect with lines when close, and are repelled by cursor.
 * Uses the active BRICS node accent color palette.
 */

(function () {
  'use strict';

  // ─── 1. CANVAS SETUP ────────────────────────────────────────────────────────
  const canvas = document.createElement('canvas');
  canvas.id = 'bg-particle-canvas';
  canvas.style.cssText = `
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 0;
    opacity: 0;
    transition: opacity 1.2s ease;
  `;
  document.body.prepend(canvas);

  // Fade in after a short delay so page content renders first
  setTimeout(() => { canvas.style.opacity = '1'; }, 300);

  const ctx = canvas.getContext('2d');

  // ─── 2. CONFIG ──────────────────────────────────────────────────────────────
  const CONFIG = {
    particleCount: 80,          // Number of floating particles
    connectionDistance: 140,    // Max px distance to draw a line
    cursorRepelRadius: 110,     // px radius where cursor pushes particles
    cursorRepelStrength: 0.022, // How hard the cursor pushes
    particleBaseSpeed: 0.28,    // Normal drift speed
    minRadius: 1.2,
    maxRadius: 2.8,
    glowRadius: 5,              // Soft glow around each particle
  };

  // ─── 3. GET ACCENT COLOR FROM CSS VARIABLE ──────────────────────────────────
  function getAccentColor() {
    const style = getComputedStyle(document.documentElement);
    const hex = (style.getPropertyValue('--accent-primary') || '#06b6d4').trim();
    return hexToRgb(hex) || { r: 6, g: 182, b: 212 };
  }

  function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }

  // ─── 4. CURSOR TRACKING ─────────────────────────────────────────────────────
  const mouse = { x: -9999, y: -9999, active: false };

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.active = true;
  });

  window.addEventListener('mouseleave', () => {
    mouse.x = -9999;
    mouse.y = -9999;
    mouse.active = false;
  });

  // ─── 5. PARTICLE CLASS ──────────────────────────────────────────────────────
  class Particle {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = Math.random() * canvas.width;
      this.y = initial ? Math.random() * canvas.height : -10;
      this.radius = CONFIG.minRadius + Math.random() * (CONFIG.maxRadius - CONFIG.minRadius);
      this.opacity = 0.2 + Math.random() * 0.5;
      const angle = Math.random() * Math.PI * 2;
      const speed = CONFIG.particleBaseSpeed * (0.5 + Math.random());
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.pulsePhase = Math.random() * Math.PI * 2;
      this.pulseSpeed = 0.015 + Math.random() * 0.02;
    }

    update() {
      // Pulse opacity gently
      this.pulsePhase += this.pulseSpeed;
      const pulseFactor = 0.85 + 0.15 * Math.sin(this.pulsePhase);

      // Cursor repulsion
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < CONFIG.cursorRepelRadius && dist > 0) {
        const force = (CONFIG.cursorRepelRadius - dist) / CONFIG.cursorRepelRadius;
        const angle = Math.atan2(dy, dx);
        this.vx += Math.cos(angle) * force * CONFIG.cursorRepelStrength * 18;
        this.vy += Math.sin(angle) * force * CONFIG.cursorRepelStrength * 18;
      }

      // Dampen velocity to prevent runaway
      this.vx *= 0.985;
      this.vy *= 0.985;

      // Clamp max speed
      const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
      if (speed > 2.5) {
        this.vx = (this.vx / speed) * 2.5;
        this.vy = (this.vy / speed) * 2.5;
      }

      this.x += this.vx;
      this.y += this.vy;
      this._pulseFactor = pulseFactor;

      // Wrap around edges
      const pad = 20;
      if (this.x < -pad) this.x = canvas.width + pad;
      if (this.x > canvas.width + pad) this.x = -pad;
      if (this.y < -pad) this.y = canvas.height + pad;
      if (this.y > canvas.height + pad) this.y = -pad;
    }

    draw(color) {
      const alpha = this.opacity * (this._pulseFactor || 1);

      // Outer soft glow
      const grd = ctx.createRadialGradient(
        this.x, this.y, 0,
        this.x, this.y, this.radius * CONFIG.glowRadius
      );
      grd.addColorStop(0, `rgba(${color.r},${color.g},${color.b},${alpha * 0.6})`);
      grd.addColorStop(1, `rgba(${color.r},${color.g},${color.b},0)`);

      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius * CONFIG.glowRadius, 0, Math.PI * 2);
      ctx.fillStyle = grd;
      ctx.fill();

      // Core particle dot
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${color.r},${color.g},${color.b},${Math.min(alpha * 1.4, 1)})`;
      ctx.fill();
    }
  }

  // ─── 6. CURSOR GLOW RING ────────────────────────────────────────────────────
  const cursorGlow = { x: mouse.x, y: mouse.y };

  function drawCursorGlow(color) {
    if (!mouse.active) return;

    // Smooth follow
    cursorGlow.x += (mouse.x - cursorGlow.x) * 0.12;
    cursorGlow.y += (mouse.y - cursorGlow.y) * 0.12;

    const grd = ctx.createRadialGradient(
      cursorGlow.x, cursorGlow.y, 0,
      cursorGlow.x, cursorGlow.y, CONFIG.cursorRepelRadius
    );
    grd.addColorStop(0,   `rgba(${color.r},${color.g},${color.b},0.10)`);
    grd.addColorStop(0.4, `rgba(${color.r},${color.g},${color.b},0.04)`);
    grd.addColorStop(1,   `rgba(${color.r},${color.g},${color.b},0)`);

    ctx.beginPath();
    ctx.arc(cursorGlow.x, cursorGlow.y, CONFIG.cursorRepelRadius, 0, Math.PI * 2);
    ctx.fillStyle = grd;
    ctx.fill();
  }

  // ─── 7. CONNECTION LINES ────────────────────────────────────────────────────
  function drawConnections(particles, color) {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i];
        const b = particles[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < CONFIG.connectionDistance) {
          const alpha = (1 - dist / CONFIG.connectionDistance) * 0.18;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(${color.r},${color.g},${color.b},${alpha})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }
  }

  // ─── 8. CANVAS RESIZE ───────────────────────────────────────────────────────
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // ─── 9. INITIALIZE PARTICLES ────────────────────────────────────────────────
  let particles = [];
  function initParticles() {
    particles = [];
    const count = Math.min(CONFIG.particleCount, Math.floor(window.innerWidth / 14));
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }
  initParticles();
  window.addEventListener('resize', initParticles);

  // ─── 10. ANIMATION LOOP ─────────────────────────────────────────────────────
  let colorCache = getAccentColor();
  let colorTick = 0;

  function animate() {
    // Refresh accent color periodically (handles BRICS node switches)
    colorTick++;
    if (colorTick % 120 === 0) {
      colorCache = getAccentColor();
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawCursorGlow(colorCache);
    drawConnections(particles, colorCache);
    particles.forEach(p => {
      p.update();
      p.draw(colorCache);
    });

    requestAnimationFrame(animate);
  }

  animate();

  // ─── 11. REACT TO BRICS NODE THEME CHANGES ──────────────────────────────────
  const observer = new MutationObserver(() => {
    colorCache = getAccentColor();
  });
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-node'] });

})();
