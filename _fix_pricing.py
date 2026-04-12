
with open('C:/HEILLON_PROTOCOL_HDR/index.html', encoding='utf-8') as f:
    c = f.read()

# Secção PRICING — inserir antes do footer
pricing_html = '''
<!-- PRICING SECTION -->
<section id="pricing" style="padding:4rem 2rem;background:linear-gradient(135deg,#060A10,#08101A);border-top:1px solid rgba(201,168,76,0.08)">
  <div style="max-width:960px;margin:0 auto">
    <p style="font-family:'DM Mono',monospace;font-size:.65rem;letter-spacing:.24em;text-transform:uppercase;color:rgba(201,168,76,.65);margin-bottom:.75rem">COMO COMECAR</p>
    <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(1.6rem,3.2vw,2.6rem);font-weight:300;color:#E8E4D9;line-height:1.2;margin-bottom:2.5rem">
      Tres formas de trabalhar com a HEILLON.
    </h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem">

      <!-- Free / HPC -->
      <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:2rem">
        <p style="font-family:'DM Mono',monospace;font-size:.62rem;letter-spacing:.18em;color:rgba(201,168,76,.6);margin-bottom:.5rem">GRATUITO</p>
        <p style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:#E8E4D9;margin-bottom:.75rem">HPC Personal Core</p>
        <p style="font-size:.88rem;color:#5A6478;line-height:1.7;margin-bottom:1.25rem">Para individuos e developers. Monitoriza as tuas IAs, ve os HDRs em tempo real, testa o protocolo. 30 dias gratis sem cartao.</p>
        <ul style="list-style:none;margin-bottom:1.5rem;display:flex;flex-direction:column;gap:.45rem">
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span>Agente local invisivel</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span>Dashboard de actividade IA</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span>HDRs em tempo real</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#22C55E">&#10003;</span>27+ AIs detectaveis</li>
        </ul>
        <a href="https://hpc.heillon.com" style="display:inline-block;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;padding:.65rem 1.4rem;background:rgba(201,168,76,.12);border:1px solid rgba(201,168,76,.35);color:#C9A84C;text-decoration:none;border-radius:5px">Comecar gratis &rarr;</a>
      </div>

      <!-- API / Integracao -->
      <div style="background:rgba(255,255,255,.04);border:1px solid rgba(201,168,76,.2);border-radius:12px;padding:2rem;position:relative">
        <p style="position:absolute;top:-1px;left:50%;transform:translateX(-50%);background:#C9A84C;color:#050810;font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:.14em;padding:.2rem .75rem;border-radius:0 0 5px 5px">MAIS POPULAR</p>
        <p style="font-family:'DM Mono',monospace;font-size:.62rem;letter-spacing:.18em;color:rgba(201,168,76,.6);margin-bottom:.5rem;margin-top:.5rem">DEMO / PROVA DE CONCEITO</p>
        <p style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:#E8E4D9;margin-bottom:.75rem">Integracao via API</p>
        <p style="font-size:.88rem;color:#5A6478;line-height:1.7;margin-bottom:1.25rem">1 endpoint. Sem contrato inicial. O teu sistema passa a gerar HDRs em dias. Validamos juntos antes de qualquer compromisso.</p>
        <ul style="list-style:none;margin-bottom:1.5rem;display:flex;flex-direction:column;gap:.45rem">
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span>POST /lc2s/execute</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span>HDRs imutaveis e verificaveis</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span>Suporte tecnico directo</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#C9A84C">&#10003;</span>Sem mudancas no teu sistema</li>
        </ul>
        <a href="https://heillon.com/#cta" style="display:inline-block;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;padding:.65rem 1.4rem;background:#C9A84C;color:#050810;font-weight:600;text-decoration:none;border-radius:5px">Pedir demo &rarr;</a>
      </div>

      <!-- Enterprise -->
      <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:2rem">
        <p style="font-family:'DM Mono',monospace;font-size:.62rem;letter-spacing:.18em;color:rgba(123,127,196,.65);margin-bottom:.5rem">ENTERPRISE</p>
        <p style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;color:#E8E4D9;margin-bottom:.75rem">Infraestrutura Dedicada</p>
        <p style="font-size:.88rem;color:#5A6478;line-height:1.7;margin-bottom:1.25rem">Para fintechs, governos e sistemas criticos. Infraestrutura dedicada, SLA definido, compliance BR/UAE/EU e suporte a integracao com os teus sistemas existentes.</p>
        <ul style="list-style:none;margin-bottom:1.5rem;display:flex;flex-direction:column;gap:.45rem">
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#7B7FC4">&#10003;</span>Deployment dedicado</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#7B7FC4">&#10003;</span>SLA e uptime garantidos</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#7B7FC4">&#10003;</span>Compliance LGPD/GDPR/DORA</li>
          <li style="font-size:.83rem;color:#8A95A8;display:flex;gap:.5rem"><span style="color:#7B7FC4">&#10003;</span>Onboarding + suporte dedicado</li>
        </ul>
        <a href="mailto:contact@heillon.com?subject=Enterprise%20-%20Infraestrutura%20Dedicada" style="display:inline-block;font-family:'DM Mono',monospace;font-size:.72rem;letter-spacing:.1em;padding:.65rem 1.4rem;background:rgba(123,127,196,.12);border:1px solid rgba(123,127,196,.3);color:#7B7FC4;text-decoration:none;border-radius:5px">Falar com equipa &rarr;</a>
      </div>

    </div>
  </div>
</section>
'''

# Inserir antes do banner HPC (que está antes do footer)
# O banner HPC foi adicionado antes do <footer>
insert_marker = '<!-- === HEILLON HPC BANNER ==='
if insert_marker in c:
    c = c.replace(insert_marker, pricing_html + '\n' + insert_marker, 1)
    print('Pricing inserted before HPC banner')
else:
    # Tentar antes do footer directamente
    footer_marker = '<footer>'
    idx = c.rfind(footer_marker)
    if idx >= 0:
        c = c[:idx] + pricing_html + '\n' + c[idx:]
        print('Pricing inserted before footer')
    else:
        print('ERROR: no insertion point found')

print('Pricing section present:', 'COMO COMECAR' in c)

with open('C:/HEILLON_PROTOCOL_HDR/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Saved vitrine')
