
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/HEILLON_PROTOCOL_HDR/index.html', encoding='utf-8') as f:
    content = f.read()

footer_idx = content.rfind('<footer')
print('Footer at:', footer_idx)

# Pricing section HTML to inject before footer
pricing = '''
<!-- PRICING / COMO COMECAR -->
<section style="padding:4rem 2rem;background:linear-gradient(135deg,#060A12,#0A0F1A);border-top:1px solid rgba(201,168,76,.1)">
<div style="max-width:1000px;margin:0 auto">
  <p style="font-family:'DM Mono',monospace;font-size:.65rem;letter-spacing:.25em;color:rgba(201,168,76,.7);text-transform:uppercase;margin-bottom:.6rem">Como comecar</p>
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(1.6rem,3.5vw,2.6rem);font-weight:300;color:#E8E4D9;margin-bottom:.6rem;line-height:1.2">
    Zero atrito. Um endpoint.<br><em style="color:rgba(201,168,76,.85)">Prova soberana desde o primeiro request.</em>
  </h2>
  <p style="font-family:'DM Sans',sans-serif;font-size:.95rem;color:#6A7590;max-width:580px;line-height:1.7;margin-bottom:3rem">
    O seu sistema nao muda. Apenas passa a gerar prova. Tres formas de comecar — hoje.
  </p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem;margin-bottom:2.5rem">
    <!-- Free -->
    <div style="background:rgba(10,15,25,.8);border:1px solid rgba(123,127,196,.18);border-radius:12px;padding:2rem">
      <div style="font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:.22em;color:rgba(123,127,196,.7);text-transform:uppercase;margin-bottom:.8rem">Explorar</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:300;color:#E8E4D9;margin-bottom:.4rem">Gratis</div>
      <div style="font-family:'DM Mono',monospace;font-size:.72rem;color:#4A5568;margin-bottom:1.4rem">HPC Personal Core — 30 dias</div>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.6rem">
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span> Monitoriza IAs no teu PC</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span> HDRs pessoais imutaveis</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span> Alertas de ficheiros sensiveis</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span> Dashboard em tempo real</li>
      </ul>
      <a href="https://hpc.heillon.com" style="display:block;text-align:center;padding:.65rem;background:rgba(123,127,196,.12);border:1px solid rgba(123,127,196,.3);border-radius:7px;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;color:#9BA3D4;text-decoration:none;text-transform:uppercase">Comecar gratis</a>
    </div>
    <!-- API -->
    <div style="background:rgba(10,15,25,.8);border:1px solid rgba(201,168,76,.28);border-radius:12px;padding:2rem;position:relative">
      <div style="position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:#C9A84C;color:#050810;font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:.15em;padding:3px 14px;border-radius:20px;text-transform:uppercase;white-space:nowrap">Mais popular</div>
      <div style="font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:.22em;color:rgba(201,168,76,.7);text-transform:uppercase;margin-bottom:.8rem">Integrar</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:300;color:#E8E4D9;margin-bottom:.4rem">Demo</div>
      <div style="font-family:'DM Mono',monospace;font-size:.72rem;color:#4A5568;margin-bottom:1.4rem">1 endpoint — Sem contrato inicial</div>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.6rem">
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span> POST /lc2s/execute no teu sistema</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span> HDRs com prova criptografica</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span> Corpus normativo BR + UAE + EU</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span> Suporte de integracao</li>
      </ul>
      <a href="https://heillon.com#cta" style="display:block;text-align:center;padding:.65rem;background:rgba(201,168,76,.15);border:1px solid rgba(201,168,76,.4);border-radius:7px;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;color:#C9A84C;text-decoration:none;text-transform:uppercase">Falar com a equipa</a>
    </div>
    <!-- Enterprise -->
    <div style="background:rgba(10,15,25,.8);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:2rem">
      <div style="font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:.22em;color:rgba(188,140,255,.6);text-transform:uppercase;margin-bottom:.8rem">Escalar</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:300;color:#E8E4D9;margin-bottom:.4rem">Enterprise</div>
      <div style="font-family:'DM Mono',monospace;font-size:.72rem;color:#4A5568;margin-bottom:1.4rem">Infraestrutura dedicada — SLA garantido</div>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.6rem">
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#9580C8">&#10003;</span> Instancia dedicada e isolada</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#9580C8">&#10003;</span> SLA customizado + suporte 24h</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#9580C8">&#10003;</span> Compliance BR/UAE/EU/US</li>
        <li style="font-size:.85rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#9580C8">&#10003;</span> Integracao white-label disponivel</li>
      </ul>
      <a href="https://heillon.com#cta" style="display:block;text-align:center;padding:.65rem;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:7px;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;color:#8A95A8;text-decoration:none;text-transform:uppercase">Contactar</a>
    </div>
  </div>
  <p style="font-family:'DM Mono',monospace;font-size:.68rem;color:#3D4A5C;text-align:center">
    Precos sob consulta para volumes empresariais &nbsp;&middot;&nbsp; contact@heillon.com
  </p>
</div>
</section>
'''

new_content = content[:footer_idx] + pricing + '\n' + content[footer_idx:]
print('Pricing injected:', 'Como comecar' in new_content)
print('Pricing cards:', new_content.count('border-radius:12px'))

with open('C:/HEILLON_PROTOCOL_HDR/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Saved OK')
