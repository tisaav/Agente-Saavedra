# 📖 Histórico Central de Melhorias, Ajustes e Consertos no Sankhya e TI

> **Objetivo deste documento:** Registrar de forma simples, clara e acessível para qualquer usuário, diretor ou gestor todas as correções, melhorias, automações e manutenções realizadas no ecossistema de TI e ERP Sankhya da **Saavedra Representações**.

---

## 🧭 Índice Rápido de Ocorrências e Melhorias Implementadas

| Caso / Doc | Módulo / Área | O que aconteceu? (Problema) | O que foi feito? (Solução) | Link do Documento |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **Institucional / Negócio** — Visão Geral | Necessidade de centralizar as regras de operação hospitalar e distribuição médica da empresa. | Documentadas todas as operações-chave: hospitais, licitações, consignações e regras fiscais. | [01 - Perfil e Regras de Negócio](01_perfil_e_regras_de_negocio.md) |
| **02** | **Dicionário de Dados** — Campos Customizados | Dificuldade em rastrear lotes cirúrgicos, validades curtas e dados hospitalares específicos. | Mapeados e organizados todos os campos personalizados (`AD_`) criados nas tabelas do sistema. | [02 - Campos Customizados AD](02_campos_customizados_ad.md) |
| **03** | **Relatórios Gráficos** — Modelos 14 e 67 | Travamento e erros de compilação ao carregar layouts de pedidos de venda no Sankhya. | Corrigidas as tags de incompatibilidade da biblioteca JasperReports para a versão do servidor. | [03 - Relatórios Jasper](03_relatorios_jasper_modelo14_relatorio67.md) |
| **04** | **Faturamento / Vendas** — Central de Vendas | Erros de confirmação ao faturar pedidos da UNIMED e erros de impressão de pedidos. | Tratadas inconsistências de CRM de médicos e divisão por zero na unidade do produto. | [04 - Troubleshooting de Erros](04_troubleshooting_erros_conhecidos.md) |
| **05** | **Licitações** — Dashboards 2301 e 2302 | O painel gerencial de contratos não exibia a coluna Modalidade (Pregão, Dispensa, etc.). | Criado cruzamento inteligente entre editais e contratos, adicionando a modalidade no painel. | [05 - Dashboards Licitações](05_dashboards_licitacoes_2301_2302.md) |
| **06** | **Licitações** — Portal de Licitações | Opção **"REVOGADO"** sumiu da caixinha de resultado do item após atualização do sistema. | Reensinado o dicionário do Sankhya com as opções *Revogado*, *Desclassificado* e *Suspenso*. | [06 - Incidente Dicionário Licitações](06_incidente_dicionario_licitacoes_opcoes_perdidas.md) |
| **07** | **Financeiro / Contabilidade** — Plano de Contas | Amarração e conciliação contábil dos 3 fundos de investimento do Banco Safra. | Criadas as contas contábeis 7325, 7327 e 7329 no grupo 1.1.1.03 e vinculadas ao banco. | [07 - Contas Contábeis Safra](07_configuracao_contas_contabeis_banco_safra.md) |
| **08** | **Fiscal / Faturamento** — Reforma Tributária | SEFAZ rejeitando notas de teste de IBS e CBS (Erros 1033, 1026 e 1036) para hospitais. | Configurado o Grupo 4 com redução de 60% (CST 200 / cClassTrib 200030) para materiais médicos. | [08 - Reforma Tributária IBS/CBS](08_reforma_tributaria_ibs_cbs_configuracao_sankhya.md) |
| **09** | **Fiscal / Tributário** — Retenções Federais | Órgãos públicos federais retendo PIS/COFINS indevidamente e devoluções com cálculo incorreto. | Criada a Trigger do Anexo III da IN 1234/2012, blindando notas de devolução de interferência. | [09 - Automação Retenções Trigger](09_automacao_retencoes_orgaos_publicos_trigger_anexo3.md) |
| **10** | **Fiscal / Compras** — ICMS-ST Interestadual | GNRE de compras de SP com valor a menor, gerando risco de apreensão de cargas no posto fiscal. | Corrigida a MVA para 91,53% no Grupo 60 para produtos importados faturados a 4%. | [10 - ICMS-ST Compras Importados](10_correcao_calculo_icms_st_gnre_compras_importados.md) |
| **11** | **Financeiro / Cobrança** — Banco Safra (422) | Impossibilidade de emitir boletos registrados e transmitir remessas CNAB pelo Banco Safra. | Customizado layout Jasper do boleto e homologado layout CNAB 400 (Layout 27) junto ao Safra. | [11 - Cobrança Registrada Safra](11_implantacao_cobranca_banco_safra_boleto_cnab400.md) |
| **12** | **Compras / Estoque** — MD-e e SEFAZ | Notas de fornecedores paravam de chegar com erro de "Consumo Indevido (Rejeição 656)". | Descompassados os robôs de busca para intervalos seguros e recuado o NSU na SEFAZ. | [12 - Resolução Bloqueio SEFAZ 656](12_resolucao_bloqueios_sefaz_mde_consumo_indevido_656.md) |
| **13** | **Gestão Comercial** — Dashboards Avançados | Dashboard 4106 de Sell Out travando com erro de divisão por zero e falta de visão de pedidos pendentes. | Blindada fórmula SQL com NULLIF e criada consulta gerencial de saldo de pedidos de compra. | [13 - Dashboards Sell Out e Compras](13_dashboards_gerenciais_sellout_4106_compras_pendentes.md) |
| **14** | **Infraestrutura / TI** — Acesso e Segurança | Usuários com múltiplas senhas despadronizadas e sem segurança centralizada nos notebooks. | Implantado o Google Credential Provider (GCPW) com login único e 2FA corporativo nos PCs Dell. | [14 - Login Windows com GCPW](14_gcpw_login_windows_google_workspace_implantacao.md) |
| **15** | **Suprimentos / Compras** — Gadget 1318 (BI) | Gadget 1318 travava com erro CORE_E05294 (subconsulta retornou mais de 1 valor) ao analisar marcas BD. | Blindada subconsulta de metas (SELLIN_MES) com filtro de ano e SUM, além de ajuste de ano em pedidos de compra. | [15 - Correção Gadget 1318](15_correcao_gadget_1318_analise_compras_subconsulta_retornou_mais_de_1_valor.md) |


---

## 📌 Padrão Adotado para Todos os Registros

Cada documento desta base foi estruturado pensando no entendimento imediato de qualquer colaborador:

1. **O Problema (O que o usuário viu):** O sintoma operacional no dia a dia, mensagens de erro na tela e impacto nas rotinas.
2. **Por que aconteceu? (Explicação Simples):** A explicação didática e sem jargões complexos do motivo da falha.
3. **O que fizemos para arrumar:** A solução prática adotada no sistema para sanar o problema definitivamente.
4. **Como o usuário valida no dia a dia:** Instruções passo a passo para conferência rápida pelo colaborador.
5. **Detalhes Técnicos:** O registro completo de tabelas, scripts SQL, triggers e parâmetros para histórico e auditoria da TI.

---

## 📂 Formato e Localização dos Arquivos

* **Versão em Texto Técnico (Markdown):** Mantida localmente no repositório de agentes em `base_conhecimento/ambiente_saavedra/`.
* **Versão para Leitura Geral (Microsoft Word / Google Docs):** Convertida automaticamente e sincronizada no Google Drive corporativo na pasta:  
  📁 `G:\Drives compartilhados\Informatica\Documentacoes Sankhya - Melhorias e Consertos\`
