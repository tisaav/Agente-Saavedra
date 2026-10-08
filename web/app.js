/**
 * Frontend Application Logic — Agente Sankhya AI (Saavedra)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const chatMessages = document.getElementById('chatMessages');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const btnSend = document.getElementById('btnSend');
  const btnClearChat = document.getElementById('btnClearChat');

  const navButtons = document.querySelectorAll('.nav-item');
  const viewPanels = document.querySelectorAll('.view-panel');
  const viewTitle = document.getElementById('viewTitle');
  const viewSubtitle = document.getElementById('viewSubtitle');

  const docTabs = document.querySelectorAll('.doc-tab');
  const docContentBox = document.getElementById('docContentBox');

  const kbSearchInput = document.getElementById('kbSearchInput');
  const btnKbSearch = document.getElementById('btnKbSearch');
  const kbResultsArea = document.getElementById('kbResultsArea');

  const sqlInput = document.getElementById('sqlInput');
  const btnExecuteSql = document.getElementById('btnExecuteSql');
  const sqlResultBox = document.getElementById('sqlResultBox');

  const btnOpenSettings = document.getElementById('btnOpenSettings');
  const btnCloseSettings = document.getElementById('btnCloseSettings');
  const btnCancelSettings = document.getElementById('btnCancelSettings');
  const btnSaveSettings = document.getElementById('btnSaveSettings');
  const settingsModal = document.getElementById('settingsModal');
  const geminiApiKeyInput = document.getElementById('geminiApiKey');
  const geminiModelSelect = document.getElementById('geminiModel');

  // Image Attachment Elements
  const btnAttachImage = document.getElementById('btnAttachImage');
  const imageFileInput = document.getElementById('imageFileInput');
  const imagePreviewBar = document.getElementById('imagePreviewBar');
  const imageThumb = document.getElementById('imageThumb');
  const btnRemoveImage = document.getElementById('btnRemoveImage');
  let currentImageData = null;

  // Handle paste screenshot directly from clipboard (Ctrl + V)
  window.addEventListener('paste', (e) => {
    const items = (e.clipboardData || e.originalEvent.clipboardData).items;
    for (let index in items) {
      const item = items[index];
      if (item.kind === 'file' && item.type.startsWith('image/')) {
        const blob = item.getAsFile();
        const reader = new FileReader();
        reader.onload = (event) => {
          setImageAttachment(event.target.result);
        };
        reader.readAsDataURL(blob);
        break;
      }
    }
  });

  if (btnAttachImage && imageFileInput) {
    btnAttachImage.addEventListener('click', () => imageFileInput.click());
    imageFileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          setImageAttachment(event.target.result);
        };
        reader.readAsDataURL(file);
      }
    });
  }

  if (btnRemoveImage) {
    btnRemoveImage.addEventListener('click', () => {
      currentImageData = null;
      imagePreviewBar.style.display = 'none';
      imageThumb.src = '';
      if (imageFileInput) imageFileInput.value = '';
    });
  }

  function setImageAttachment(dataUrl) {
    currentImageData = dataUrl;
    imageThumb.src = dataUrl;
    imagePreviewBar.style.display = 'flex';
    chatInput.focus();
  }

  // Load API Key from localStorage
  if (localStorage.getItem('gemini_api_key')) {
    geminiApiKeyInput.value = localStorage.getItem('gemini_api_key');
  }
  if (localStorage.getItem('gemini_model')) {
    geminiModelSelect.value = localStorage.getItem('gemini_model');
  }

  // Auto-resize chat textarea
  chatInput.addEventListener('input', () => {
    chatInput.style.height = 'auto';
    chatInput.style.height = `${Math.min(chatInput.scrollHeight, 120)}px`;
  });

  chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      chatForm.dispatchEvent(new Event('submit'));
    }
  });

  // 1. Navigation Switcher
  const titles = {
    chat: { title: 'Assistente Sankhya & Saavedra', sub: 'Base de conhecimento inteligente com acesso ao ERP ao vivo' },
    dashboard: { title: 'Painel Gráfico & Comparativos', sub: 'Indicadores analíticos do ERP em tempo real e matriz de regras' },
    saavedra: { title: 'Regras e Playbooks Saavedra', sub: 'Normas cirúrgicas, OPME, Unimed 258 e modelos de impressão' },
    kb: { title: 'Explorador da Base de Conhecimento', sub: 'Pesquisa completa em quase 5.000 manuais oficiais do Sankhya' },
    erp: { title: 'Terminal SQL / Gateway Sankhya', sub: 'Consultas diretas à base de dados de homologação (DbExplorerSP)' },
    addkb: { title: 'Adicionar Conhecimento / Regra', sub: 'Cadastre regras personalizadas, manuais ou exceções de negócio' }
  };

  navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const view = btn.dataset.view;
      navButtons.forEach(b => b.classList.remove('active'));
      viewPanels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPanel = document.getElementById(`view${view.charAt(0).toUpperCase() + view.slice(1)}`);
      if (targetPanel) targetPanel.classList.add('active');

      if (titles[view]) {
        viewTitle.textContent = titles[view].title;
        viewSubtitle.textContent = titles[view].sub;
      }

      if (view === 'dashboard') {
        loadDashboard();
      }

      if (view === 'saavedra' && !docContentBox.dataset.loaded) {
        loadSaavedraDoc('01_perfil_e_regras_de_negocio.md');
      }
    });
  });

  // 2. Chat Send Logic
  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const prompt = chatInput.value.trim();
    if (!prompt && !currentImageData) return;

    const sentImage = currentImageData;
    // Reset image attachment preview
    currentImageData = null;
    imagePreviewBar.style.display = 'none';
    imageThumb.src = '';
    if (imageFileInput) imageFileInput.value = '';

    // Append User Message with image if present
    appendMessage('user', prompt || '(Imagem anexada para diagnóstico do Sankhya)', [], null, sentImage);
    chatInput.value = '';
    chatInput.style.height = 'auto';
    btnSend.disabled = true;

    // Append Loading Assistant Message
    const loadingId = appendLoadingMessage();

    try {
      const apiKey = localStorage.getItem('gemini_api_key') || '';
      const model = localStorage.getItem('gemini_model') || 'gemini-1.5-flash';

      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: prompt || 'Analise a imagem da tela do Sankhya e explique o erro e a solução.',
          api_key: apiKey,
          model: model,
          image: sentImage
        })
      });

      const data = await response.json();
      removeMessage(loadingId);

      if (data.error) {
        appendMessage('assistant', `⚠️ **Erro:** ${data.error}`);
      } else {
        appendMessage('assistant', data.response, data.sources, data.erp_action);
      }
    } catch (err) {
      removeMessage(loadingId);
      appendMessage('assistant', `⚠️ **Falha de rede:** Não foi possível conectar ao servidor local (${err.message}).`);
    } finally {
      btnSend.disabled = false;
      chatInput.focus();
    }
  });

  // Quick Chips & Suggestions
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('.topic-chip, .sugg-tag');
    if (chip && chip.dataset.prompt) {
      // If not in chat view, switch to chat
      document.getElementById('btnNavChat').click();
      chatInput.value = chip.dataset.prompt;
      chatForm.dispatchEvent(new Event('submit'));
    }
  });

  // Clear Chat
  btnClearChat.addEventListener('click', () => {
    if (confirm('Deseja limpar as mensagens da conversa atual?')) {
      const welcomeMsg = chatMessages.firstElementChild;
      chatMessages.innerHTML = '';
      if (welcomeMsg) chatMessages.appendChild(welcomeMsg);
    }
  });

  // 3. Document Tabs (Saavedra Docs)
  docTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      docTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      loadSaavedraDoc(tab.dataset.doc);
    });
  });

  async function loadSaavedraDoc(filename) {
    docContentBox.innerHTML = '<div class="loading-spinner">Carregando documentação...</div>';
    try {
      const resp = await fetch(`/api/doc/ambiente_saavedra/${filename}`);
      const text = await resp.text();
      docContentBox.innerHTML = parseMarkdown(text);
      docContentBox.dataset.loaded = 'true';
    } catch (err) {
      docContentBox.innerHTML = `<p style="color:var(--accent-rose)">Erro ao carregar documento: ${err.message}</p>`;
    }
  }

  // 4. Knowledge Base Search
  async function performKbSearch() {
    const q = kbSearchInput.value.trim();
    if (!q) return;

    kbResultsArea.innerHTML = '<div class="loading-spinner">Pesquisando na base local...</div>';
    try {
      const resp = await fetch(`/api/kb/search?q=${encodeURIComponent(q)}`);
      const data = await resp.json();
      const results = data.results || [];

      if (results.length === 0) {
        kbResultsArea.innerHTML = `
          <div class="kb-empty-state">
            <span class="icon">🤷‍♂️</span>
            <h3>Nenhum artigo encontrado</h3>
            <p>Tente outros termos de pesquisa como "rejeição", "TOP", "pedido" ou "imposto".</p>
          </div>
        `;
        return;
      }

      let html = '';
      results.forEach(item => {
        html += `
          <div class="kb-card" data-file="${item.file}">
            <h4>${item.title}</h4>
            <div class="kb-meta">
              <span>📁 ${item.module}</span>
              ${item.sub_section ? `<span>↳ ${item.sub_section}</span>` : ''}
              <span>🕒 ${item.updated_at ? item.updated_at.slice(0, 10) : ''}</span>
            </div>
            <p class="kb-snippet">${item.snippet || 'Clique para visualizar este manual...'}</p>
          </div>
        `;
      });
      kbResultsArea.innerHTML = html;

      // Click card to open in modal/chat
      document.querySelectorAll('.kb-card').forEach(card => {
        card.addEventListener('click', () => {
          const file = card.dataset.file;
          document.getElementById('btnNavChat').click();
          chatInput.value = `Explique em detalhes o conteúdo do manual: ${card.querySelector('h4').textContent}`;
          chatForm.dispatchEvent(new Event('submit'));
        });
      });
    } catch (err) {
      kbResultsArea.innerHTML = `<p style="color:var(--accent-rose)">Erro na pesquisa: ${err.message}</p>`;
    }
  }

  btnKbSearch.addEventListener('click', performKbSearch);
  kbSearchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') performKbSearch();
  });

  // 5. Terminal ERP SQL
  btnExecuteSql.addEventListener('click', async () => {
    const sql = sqlInput.value.trim();
    if (!sql) return;

    sqlResultBox.innerHTML = '<span style="color:var(--text-dim)">Executando consulta no ERP...</span>';
    btnExecuteSql.disabled = true;

    try {
      const resp = await fetch('/api/erp/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sql })
      });
      const data = await resp.json();

      if (data.error) {
        sqlResultBox.innerHTML = `<span style="color:var(--accent-rose)">❌ Erro ao executar SQL: ${data.error}</span>`;
      } else {
        const body = data.responseBody || {};
        const fields = body.fieldsMetadata || [];
        const rows = body.rows || [];

        if (rows.length === 0) {
          sqlResultBox.innerHTML = '<span style="color:var(--accent-cyan)">Consulta executada com sucesso. Nenhum registro retornado.</span>';
          return;
        }

        let tableHtml = '<table style="width:100%; border-collapse:collapse;"><thead><tr>';
        fields.forEach(f => {
          tableHtml += `<th style="border:1px solid #334155; padding:6px 10px; background:#1e293b; color:#94a3b8; font-size:0.75rem;">${f.name}</th>`;
        });
        tableHtml += '</tr></thead><tbody>';

        rows.forEach(r => {
          tableHtml += '<tr>';
          r.forEach(val => {
            tableHtml += `<td style="border:1px solid #334155; padding:6px 10px; color:#f8fafc; font-size:0.8rem;">${val !== null ? val : '<em>null</em>'}</td>`;
          });
          tableHtml += '</tr>';
        });
        tableHtml += '</tbody></table>';

        sqlResultBox.innerHTML = `
          <div style="margin-bottom:8px; color:var(--accent-emerald); font-size:0.75rem;">
            ✓ ${rows.length} registros retornados (Tempo: ${body.timeQuery || 'N/D'})
          </div>
          ${tableHtml}
        `;
      }
    } catch (err) {
      sqlResultBox.innerHTML = `<span style="color:var(--accent-rose)">Erro de comunicação: ${err.message}</span>`;
    } finally {
      btnExecuteSql.disabled = false;
    }
  });

  // 6. Settings Modal
  btnOpenSettings.addEventListener('click', () => settingsModal.classList.add('active'));
  btnCloseSettings.addEventListener('click', () => settingsModal.classList.remove('active'));
  btnCancelSettings.addEventListener('click', () => settingsModal.classList.remove('active'));

  btnSaveSettings.addEventListener('click', () => {
    localStorage.setItem('gemini_api_key', geminiApiKeyInput.value.trim());
    localStorage.setItem('gemini_model', geminiModelSelect.value);
    settingsModal.classList.remove('active');
    alert('Configurações salvas com sucesso!');
  });

  // 7. Dashboard & Analytics Loader
  let dashboardCharts = {};

  async function loadDashboard() {
    try {
      const resp = await fetch('/api/erp/metrics');
      const data = await resp.json();
      if (data.error) return;

      // Update KPIs
      if (data.totais) {
        const elFat = document.getElementById('kpiFaturamento');
        const elNotas = document.getElementById('kpiNotas');
        const elBancos = document.getElementById('kpiBancos');
        const elHosp = document.getElementById('kpiHospital');

        if (elFat) elFat.textContent = `R$ ${data.totais.faturamento_2026.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        if (elNotas) elNotas.textContent = data.totais.total_notas_2026.toLocaleString('pt-BR');
        if (elBancos) elBancos.textContent = `R$ ${data.totais.saldo_bancario_total.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        if (elHosp && data.top_parceiros && data.top_parceiros.length > 0) {
          elHosp.textContent = data.top_parceiros[1]?.nome?.slice(0, 16) || data.top_parceiros[0]?.nome?.slice(0, 16) || 'HOSP. CLÍNICAS';
        }
      }

      if (typeof Chart === 'undefined') return;

      // Chart 1: Vendas Mensais 2026 (Line Chart)
      const canvasVendas = document.getElementById('chartVendasMes');
      if (canvasVendas) {
        if (dashboardCharts.vendas) dashboardCharts.vendas.destroy();
        const labels = (data.vendas_mensais || []).map(v => v.mes);
        const values = (data.vendas_mensais || []).map(v => v.total);
        dashboardCharts.vendas = new Chart(canvasVendas, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              label: 'Faturamento (R$)',
              data: values,
              borderColor: '#06b6d4',
              backgroundColor: 'rgba(6, 182, 212, 0.15)',
              borderWidth: 2.5,
              fill: true,
              tension: 0.35,
              pointBackgroundColor: '#06b6d4',
              pointRadius: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `R$ ${ctx.parsed.y.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`
                }
              }
            },
            scales: {
              x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
              y: {
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: {
                  color: '#94a3b8',
                  callback: val => `R$ ${(val / 1000000).toFixed(1)}M`
                }
              }
            }
          }
        });
      }

      // Chart 2: TIPMOV (Doughnut Chart)
      const canvasTip = document.getElementById('chartTipMov');
      if (canvasTip) {
        if (dashboardCharts.tipmov) dashboardCharts.tipmov.destroy();
        const topTip = (data.tipmov || []).slice(0, 5);
        dashboardCharts.tipmov = new Chart(canvasTip, {
          type: 'doughnut',
          data: {
            labels: topTip.map(t => t.descricao),
            datasets: [{
              data: topTip.map(t => t.qtd),
              backgroundColor: ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#ec4899'],
              borderColor: '#0d111a',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: '#94a3b8', boxWidth: 12 } }
            }
          }
        });
      }

      // Chart 3: Bancos (Horizontal Bar Chart)
      const canvasBancos = document.getElementById('chartBancos');
      if (canvasBancos) {
        if (dashboardCharts.bancos) dashboardCharts.bancos.destroy();
        const topBancos = (data.bancos || []).slice(0, 6);
        dashboardCharts.bancos = new Chart(canvasBancos, {
          type: 'bar',
          data: {
            labels: topBancos.map(b => b.conta.length > 20 ? b.conta.slice(0, 18) + '...' : b.conta),
            datasets: [{
              label: 'Saldo (R$)',
              data: topBancos.map(b => b.saldo),
              backgroundColor: '#6366f1',
              borderRadius: 6
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `R$ ${ctx.parsed.x.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`
                }
              }
            },
            scales: {
              x: {
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: {
                  color: '#94a3b8',
                  callback: val => `R$ ${(val / 1000000).toFixed(1)}M`
                }
              },
              y: { grid: { display: false }, ticks: { color: '#cbd5e1', font: { size: 11 } } }
            }
          }
        });
      }

      // Chart 4: Top Clientes / Hospitais (Bar Chart)
      const canvasParc = document.getElementById('chartTopParceiros');
      if (canvasParc) {
        if (dashboardCharts.parceiros) dashboardCharts.parceiros.destroy();
        const topParc = (data.top_parceiros || []).slice(0, 5);
        dashboardCharts.parceiros = new Chart(canvasParc, {
          type: 'bar',
          data: {
            labels: topParc.map(p => p.nome.length > 18 ? p.nome.slice(0, 16) + '...' : p.nome),
            datasets: [{
              label: 'Faturamento (R$)',
              data: topParc.map(p => p.total),
              backgroundColor: ['#10b981', '#06b6d4', '#6366f1', '#f59e0b', '#8b5cf6'],
              borderRadius: 6
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => `R$ ${ctx.parsed.y.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`
                }
              }
            },
            scales: {
              x: { grid: { display: false }, ticks: { color: '#94a3b8', font: { size: 10 } } },
              y: {
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: {
                  color: '#94a3b8',
                  callback: val => `R$ ${(val / 1000000).toFixed(0)}M`
                }
              }
            }
          }
        });
      }
    } catch (e) {
      console.error('Erro ao carregar métricas:', e);
    }
  }

  // 8. Add Knowledge Form Listener
  const addKbForm = document.getElementById('addKbForm');
  const addKbStatus = document.getElementById('addKbStatus');

  if (addKbForm) {
    addKbForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const title = document.getElementById('newKbTitle').value.trim();
      const module = document.getElementById('newKbModule').value;
      const tags = document.getElementById('newKbTags').value.trim();
      const content = document.getElementById('newKbContent').value.trim();

      if (!title || !content) return;

      addKbStatus.textContent = 'Gravando e indexando...';
      addKbStatus.style.color = 'var(--accent-primary)';

      try {
        const fullContent = tags ? `**Tags:** ${tags}\n\n${content}` : content;
        const resp = await fetch('/api/kb/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            title: title,
            category: module,
            content: fullContent
          })
        });
        const res = await resp.json();
        if (res.success) {
          addKbStatus.textContent = `✓ Sucesso! Conhecimento salvo e indexado na base.`;
          addKbStatus.style.color = 'var(--accent-emerald)';
          document.getElementById('kbCount').textContent = res.total_articles.toLocaleString('pt-BR');
          addKbForm.reset();
        } else {
          addKbStatus.textContent = `Erro: ${res.error || 'Falha ao salvar'}`;
          addKbStatus.style.color = 'var(--accent-rose)';
        }
      } catch (err) {
        addKbStatus.textContent = `Erro de rede: ${err.message}`;
        addKbStatus.style.color = 'var(--accent-rose)';
      }
    });
  }

  // Helper Functions
  function appendMessage(role, text, sources = [], erpAction = null, image = null) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}-message`;

    const avatar = role === 'assistant' 
      ? '<div class="avatar assistant-avatar"><span>🤖</span></div>'
      : '<div class="avatar user-avatar"><span>👤</span></div>';

    let imageHtml = '';
    if (image) {
      imageHtml = `<a href="${image}" target="_blank" title="Clique para ampliar"><img src="${image}" class="chat-msg-image" alt="Print da tela"></a>`;
    }

    let sourcesHtml = '';
    if (sources && sources.length > 0) {
      sourcesHtml = '<div style="margin-top:12px; padding-top:8px; border-top:1px solid rgba(255,255,255,0.06); font-size:0.75rem; color:var(--text-dim);">';
      sourcesHtml += '<strong>📚 Fontes consultadas na base:</strong><br>';
      sources.slice(0, 3).forEach(s => {
        sourcesHtml += `• <em>${s.title}</em> (${s.module})<br>`;
      });
      sourcesHtml += '</div>';
    }

    let erpActionHtml = '';
    if (erpAction) {
      erpActionHtml = `<div style="margin-bottom:8px; font-size:0.75rem; color:var(--accent-cyan); background:rgba(6,182,212,0.1); padding:4px 8px; border-radius:4px; display:inline-block;">⚡ Consulta executada no ERP Sankhya ao vivo</div>`;
    }

    msgDiv.innerHTML = `
      ${avatar}
      <div class="message-bubble">
        <div class="message-header">
          <strong>${role === 'assistant' ? 'Agente Sankhya AI' : 'Você'}</strong>
        </div>
        ${erpActionHtml}
        ${imageHtml}
        <div class="message-body">${parseMarkdown(text)}</div>
        ${sourcesHtml}
      </div>
    `;

    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Render any chat charts inside msgDiv
    const chartCanvases = msgDiv.querySelectorAll('canvas[data-chart-config]');
    chartCanvases.forEach(canvas => {
      try {
        const rawJson = decodeURIComponent(canvas.dataset.chartConfig);
        const config = JSON.parse(rawJson);
        if (typeof Chart !== 'undefined') {
          new Chart(canvas, {
            type: config.type || 'bar',
            data: {
              labels: config.labels || [],
              datasets: config.datasets || []
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: { labels: { color: '#94a3b8' } },
                title: { display: !!config.title, text: config.title, color: '#f1f5f9' }
              },
              scales: config.type !== 'pie' && config.type !== 'doughnut' ? {
                x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } }
              } : {}
            }
          });
        }
      } catch (err) {
        console.error('Erro ao renderizar gráfico no chat:', err);
      }
    });
  }

  function appendLoadingMessage() {
    const id = `loading-${Date.now()}`;
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message assistant-message';
    msgDiv.id = id;
    msgDiv.innerHTML = `
      <div class="avatar assistant-avatar"><span>🤖</span></div>
      <div class="message-bubble" style="display:flex; align-items:center; gap:8px;">
        <span class="status-dot ping-active" style="background:var(--accent-primary)"></span>
        <span style="color:var(--text-muted); font-size:0.85rem;">Pesquisando na base de dados e analisando...</span>
      </div>
    `;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return id;
  }

  function removeMessage(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  // Lightweight Markdown Parser with Tables & Chart Blocks
  function parseMarkdown(md) {
    if (!md) return '';
    let html = md
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Chart Blocks: ```chart ... ```
    html = html.replace(/```chart\n([\s\S]*?)```/g, (match, jsonConfig) => {
      const chartId = 'chat-chart-' + Math.random().toString(36).substr(2, 9);
      const encoded = encodeURIComponent(jsonConfig.trim());
      return `<div class="chat-chart-card"><div class="chat-chart-header">📊 Gráfico Interativo</div><div class="chat-chart-canvas-box"><canvas id="${chartId}" data-chart-config="${encoded}"></canvas></div></div>`;
    });

    // Fenced Code Blocks (non-chart)
    html = html.replace(/```([\w]*)\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>');

    // Inline Code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Tables: lines with |
    const tableRegex = /((?:\|[^\n]+\|\r?\n)+)/g;
    html = html.replace(tableRegex, (match) => {
      const lines = match.trim().split('\n');
      if (lines.length < 2) return match;
      let tableHtml = '<div class="table-responsive"><table>';
      let inBody = false;

      lines.forEach((line, idx) => {
        if (line.includes('---')) {
          inBody = true;
          return;
        }
        const cols = line.split('|').map(c => c.trim()).filter((c, i, a) => i > 0 && i < a.length - 1);
        if (cols.length === 0) return;

        if (idx === 0) {
          tableHtml += '<thead><tr>';
          cols.forEach(c => tableHtml += `<th>${c}</th>`);
          tableHtml += '</tr></thead><tbody>';
        } else {
          tableHtml += '<tr>';
          cols.forEach(c => tableHtml += `<td>${c}</td>`);
          tableHtml += '</tr>';
        }
      });
      tableHtml += '</tbody></table></div>';
      return tableHtml;
    });

    // Headers
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

    // Bold & Italic
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');

    // Blockquotes
    html = html.replace(/^\> (.*$)/gim, '<blockquote style="border-left:3px solid var(--accent-primary); padding-left:10px; color:var(--text-muted); margin:8px 0;">$1</blockquote>');

    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" style="color:var(--accent-primary); text-decoration:underline;">$1</a>');

    // Lists
    html = html.replace(/^\- (.*$)/gim, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

    // Line breaks to paragraphs
    const paragraphs = html.split(/\n{2,}/);
    html = paragraphs.map(p => {
      p = p.trim();
      if (!p) return '';
      if (p.startsWith('<h') || p.startsWith('<pre') || p.startsWith('<ul') || p.startsWith('<blockquote') || p.startsWith('<div class="table-responsive"') || p.startsWith('<div class="chat-chart-card"')) {
        return p;
      }
      return `<p>${p.replace(/\n/g, '<br>')}</p>`;
    }).join('');

    return html;
  }
});
