/**
 * Live Decision Stream — Counter animation
 */
document.addEventListener('DOMContentLoaded', () => {
  const counterEl = document.getElementById('live-stream-count');
  if (!counterEl) return;

  const targetCount = 12481;
  const durationMs = 3200;
  const startTime = performance.now();

  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  function updateCount() {
    const elapsed = performance.now() - startTime;
    const progress = Math.min(elapsed / durationMs, 1);
    const eased = easeOutQuart(progress);
    const current = Math.floor(targetCount * eased);
    counterEl.textContent = current.toLocaleString();
    if (progress < 1) requestAnimationFrame(updateCount);
    else counterEl.textContent = targetCount.toLocaleString();
  }

  const streamSection = document.getElementById('live-stream');
  if (streamSection) {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          streamSection.classList.add('is-visible');
          updateCount();
          obs.disconnect();
        }
      },
      { threshold: 0.25 }
    );
    obs.observe(streamSection);
  } else {
    updateCount();
  }
});

/**
 * HEILLON Protocol — Landing Page
 * Explore a Verified Decision — Interactive Demonstration
 */

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('demo-form');
  const pipeline = document.getElementById('demo-pipeline');
  const resultPanel = document.getElementById('demo-result');
  const resultHdr = document.getElementById('demo-result-hdr');
  const submitBtn = document.getElementById('demo-submit');
  const downloadBtn = document.getElementById('demo-download-hdr');

  if (!form || !pipeline) return;

  const STEP_DELAY_MS = 600;

  const demoLayout = document.getElementById('demo-layout');

  function resetPipeline() {
    resultPanel.classList.remove('is-visible');
    resultPanel.hidden = true;
    if (demoLayout) demoLayout.classList.remove('demo-layout--with-result');
    const outcomeLabel = pipeline.querySelector('.demo-pipeline-outcome-text');
    if (outcomeLabel) outcomeLabel.textContent = 'Decision Outcome';
    const steps = pipeline.querySelectorAll('.demo-pipeline-step');
    steps.forEach(step => {
      step.classList.remove(
        'demo-pipeline-step--active',
        'demo-pipeline-step--complete',
        'demo-pipeline-step--error',
        'demo-pipeline-step--authorized',
        'demo-pipeline-step--denied',
        'demo-pipeline-step--pending'
      );
    });
  }

  function setStepState(stepIndex, state) {
    const step = pipeline.querySelector(`[data-step="${stepIndex}"]`);
    if (!step) return;
    step.classList.remove('demo-pipeline-step--active', 'demo-pipeline-step--complete', 'demo-pipeline-step--error');
    step.classList.remove('demo-pipeline-step--processing');
    if (state === 'active') {
      step.classList.add('demo-pipeline-step--active', 'demo-pipeline-step--processing');
    }
    if (state === 'complete') step.classList.add('demo-pipeline-step--complete');
    if (state === 'error') step.classList.add('demo-pipeline-step--error');
  }

  function setOutcome(stepIndex, outcome) {
    const step = pipeline.querySelector(`[data-step="${stepIndex}"]`);
    if (!step) return;
    const labelEl = step.querySelector('.demo-pipeline-outcome-text');
    if (labelEl) labelEl.textContent = outcome;
    step.classList.remove('demo-pipeline-step--authorized', 'demo-pipeline-step--denied', 'demo-pipeline-step--pending');
    if (outcome === 'AUTHORIZED') step.classList.add('demo-pipeline-step--complete', 'demo-pipeline-step--authorized');
    if (outcome === 'DENIED') step.classList.add('demo-pipeline-step--error', 'demo-pipeline-step--denied');
    if (outcome === 'PENDING REVIEW') step.classList.add('demo-pipeline-step--active', 'demo-pipeline-step--pending');
  }

  function computeOutcome(amount) {
    const num = parseFloat(amount) || 0;
    if (num > 100000) return 'DENIED';
    if (num > 50000) return 'PENDING REVIEW';
    return 'AUTHORIZED';
  }

  function formatHDRArtifact(data) {
    const id = 'HDR-' + Math.random().toString(16).slice(2, 8).toUpperCase();
    const intentHash = Math.random().toString(16).slice(2, 12).toUpperCase();
    const ledgerEvt = 'EVT-' + Math.random().toString(16).slice(2, 6).toUpperCase();
    const timestamp = new Date().toISOString();
    const sig = 'HLLN-SIGN-' + Math.random().toString(16).slice(2, 7).toUpperCase();
    return { id, intentHash, outcome: data.outcome, ledgerEvt, timestamp, sig };
  }

  function renderHDRArtifact(hdr) {
    return `
      <div class="demo-hdr-display">
        <div class="demo-hdr-id">${hdr.id}</div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Intent Hash</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value">${hdr.intentHash}</span>
        </div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Decision Outcome</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value demo-hdr-value--outcome">${hdr.outcome}</span>
        </div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Policy Version</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value">v1.0</span>
        </div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Ledger Event</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value">${hdr.ledgerEvt}</span>
        </div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Timestamp</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value">${hdr.timestamp}</span>
        </div>
        <div class="demo-hdr-row">
          <span class="demo-hdr-key">Verification</span>
          <span class="demo-hdr-dots"></span>
          <span class="demo-hdr-value demo-hdr-value--sig">${hdr.sig}</span>
        </div>
      </div>
    `;
  }

  function getHDRTextContent(hdr) {
    return `HDR Artifact
${hdr.id}

Intent Hash:      ${hdr.intentHash}
Decision Outcome: ${hdr.outcome}
Policy Version:   v1.0
Ledger Event:     ${hdr.ledgerEvt}
Timestamp:        ${hdr.timestamp}
Verification:     ${hdr.sig}`;
  }

  let lastHDR = null;

  function runSimulation(formData) {
    const amount = formData.get('amount');
    const currency = formData.get('currency');
    const actor = formData.get('actor');

    const outcome = computeOutcome(amount);
    const hdr = formatHDRArtifact({ outcome });

    let stepIndex = 0;

    function advance() {
      if (stepIndex > 6) {
        lastHDR = hdr;
        resultHdr.innerHTML = renderHDRArtifact(hdr);
        resultPanel.hidden = false;
        if (demoLayout) demoLayout.classList.add('demo-layout--with-result');
        requestAnimationFrame(() => resultPanel.classList.add('is-visible'));
        submitBtn.disabled = false;
        return;
      }

      setStepState(stepIndex, 'active');

      if (stepIndex === 5) {
        setTimeout(() => {
          setOutcome(5, outcome);
          setStepState(stepIndex, '');
          stepIndex++;
          setTimeout(advance, STEP_DELAY_MS);
        }, STEP_DELAY_MS);
      } else {
        setTimeout(() => {
          setStepState(stepIndex, 'complete');
          stepIndex++;
          setTimeout(advance, STEP_DELAY_MS);
        }, STEP_DELAY_MS);
      }
    }

    advance();
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    resetPipeline();
    submitBtn.disabled = true;

    const formData = new FormData(form);
    runSimulation(formData);
  });

  if (downloadBtn) {
    downloadBtn.addEventListener('click', (e) => {
      if (!lastHDR) return;
      e.preventDefault();
      const blob = new Blob([getHDRTextContent(lastHDR)], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${lastHDR.id}.hdr`;
      a.click();
      URL.revokeObjectURL(url);
    });
  }
});

/**
 * Sticky navigation — active section highlight
 */
document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('main-nav');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = Array.from(document.querySelectorAll('section[id]')).filter(s => s.id);
  const hero = document.querySelector('.hero');
  const backToTop = document.getElementById('back-to-top');

  if (!nav || !navLinks.length) return;

  const sectionIds = sections.map(s => s.id);

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        navLinks.forEach((link) => {
          const href = link.getAttribute('href');
          const targetId = href && href.startsWith('#') ? href.slice(1) : '';
          link.classList.toggle('nav-link--active', targetId === id);
        });
      });
    },
    {
      rootMargin: '-40% 0px -55% 0px',
      threshold: 0
    }
  );

  sections.forEach((section) => observer.observe(section));

  navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const target = document.getElementById(href.slice(1));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  /* Back to Top */
  if (backToTop) {
    const heroObserver = new IntersectionObserver(
      ([entry]) => {
        backToTop.classList.toggle('is-visible', !entry.isIntersecting);
      },
      { threshold: 0 }
    );
    if (hero) heroObserver.observe(hero);

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});

/**
 * Cinematic scroll-driven micro-interactions
 */
document.addEventListener('DOMContentLoaded', () => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) {
    document.querySelectorAll('[data-protocol-node], [data-protocol-connector], [data-hdr-field], [data-stack-layer], [data-stack-index], [data-reveal]').forEach(el => el.classList.add('is-visible'));
    const liveStream = document.getElementById('live-stream');
    if (liveStream) liveStream.classList.add('is-visible');
    return;
  }

  const PROTOCOL_DELAY = 280;
  const HDR_FIELD_DELAY = 120;
  const STACK_DELAY = 220;

  /* Protocol build animation */
  const protocolSection = document.getElementById('infraestrutura');
  if (protocolSection) {
    const protocolObserver = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        const nodes = protocolSection.querySelectorAll('[data-protocol-node]');
        const connectors = protocolSection.querySelectorAll('[data-protocol-connector]');

        nodes.forEach((node, i) => {
          setTimeout(() => node.classList.add('is-visible'), i * PROTOCOL_DELAY);
        });
        connectors.forEach((conn, i) => {
          setTimeout(() => conn.classList.add('is-visible'), (i + 1) * PROTOCOL_DELAY - 80);
        });

        protocolObserver.disconnect();
      },
      { threshold: 0.25 }
    );
    protocolObserver.observe(protocolSection);
  }

  /* HDR artifact generation */
  const hdrSection = document.getElementById('hdr-artifact');
  if (hdrSection) {
    const hdrObserver = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        const rows = hdrSection.querySelectorAll('[data-hdr-field]');
        const badge = hdrSection.querySelector('[data-hdr-field="badge"]');
        const fields = hdrSection.querySelectorAll('.hdr-artifact-row[data-hdr-field]');

        fields.forEach((row, i) => {
          setTimeout(() => row.classList.add('is-visible'), i * HDR_FIELD_DELAY);
        });
        if (badge) {
          setTimeout(() => badge.classList.add('is-visible'), fields.length * HDR_FIELD_DELAY + 150);
        }

        hdrObserver.disconnect();
      },
      { threshold: 0.3 }
    );
    hdrObserver.observe(hdrSection);
  }

  /* Stack reveal (bottom to top: HEILLON, Execution, Applications, AI) */
  const stackSection = document.getElementById('stack-diagram');
  if (stackSection) {
    const stackObserver = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        const layers = stackSection.querySelectorAll('[data-stack-layer]');
        const lines = stackSection.querySelectorAll('[data-stack-index]');
        const order = [0, 1, 2, 3]; // HEILLON first (0), then 1,2,3

        order.forEach((idx, i) => {
          const layer = stackSection.querySelector(`[data-stack-layer="${idx}"]`);
          const line = stackSection.querySelector(`[data-stack-index="${idx}"]`);
          setTimeout(() => {
            if (layer) layer.classList.add('is-visible');
            if (line) line.classList.add('is-visible');
          }, i * STACK_DELAY);
        });

        stackObserver.disconnect();
      },
      { threshold: 0.25 }
    );
    stackObserver.observe(stackSection);
  }

  /* Protocol Paper & Founder reveal */
  document.querySelectorAll('[data-reveal]').forEach((el) => {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          el.classList.add('is-visible');
          obs.disconnect();
        }
      },
      { threshold: 0.25 }
    );
    obs.observe(el);
  });

  /* Background HDR stream */
  const streamContainer = document.getElementById('hdr-stream');
  if (streamContainer) {
    const outcomes = ['AUTHORIZED', 'AUTHORIZED', 'AUTHORIZED', 'DENIED'];
    const ids = ['HDR-7A2F', 'HDR-9B31', 'HDR-2C84', 'HDR-1D92', 'HDR-5E07', 'HDR-8F61'];
    const positions = [
      { left: '8%', top: '15%' },
      { left: '75%', top: '25%' },
      { left: '12%', top: '55%' },
      { left: '82%', top: '45%' },
      { left: '25%', top: '80%' },
      { left: '68%', top: '12%' },
      { left: '5%', top: '40%' },
      { left: '90%', top: '70%' },
      { left: '50%', top: '30%' },
      { left: '35%', top: '65%' },
    ];

    for (let i = 0; i < 10; i++) {
      const card = document.createElement('div');
      card.className = 'hdr-stream-card';
      card.innerHTML = `<div class="hdr-stream-card-id">${ids[i % ids.length]}</div><div class="hdr-stream-card-outcome">${outcomes[i % outcomes.length]}</div>`;
      const pos = positions[i % positions.length];
      card.style.left = pos.left;
      card.style.top = pos.top;
      card.style.animationDelay = `${i * 1.8}s`;
      streamContainer.appendChild(card);
    }
  }
});


/* ============================================================
   CONTACT FORM — Simulação de envio
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contact-form');
  const status = document.getElementById('cf-status');
  const submitBtn = document.getElementById('cf-submit');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('cf-name').value.trim();
    const email = document.getElementById('cf-email').value.trim();
    const message = document.getElementById('cf-message').value.trim();

    if (!name || !email || !message) {
      status.textContent = 'Please fill in all required fields.';
      status.style.color = '#ff6b6b';
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';
    status.textContent = '';
    status.style.color = '';

    // Simulação — substituir por fetch real quando backend deployado
    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Message';
      status.textContent = '✓ Message received. We will respond within 24 hours.';
      status.style.color = '#00ffc8';
      form.reset();
    }, 1400);
  });
});
