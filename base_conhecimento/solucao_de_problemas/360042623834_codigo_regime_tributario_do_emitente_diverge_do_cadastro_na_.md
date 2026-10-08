# Código Regime Tributário do emitente diverge do cadastro na SEFAZ (NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042623834-C%C3%B3digo-Regime-Tribut%C3%A1rio-do-emitente-diverge-do-cadastro-na-SEFAZ-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042623834-C%C3%B3digo-Regime-Tribut%C3%A1rio-do-emitente-diverge-do-cadastro-na-SEFAZ-NT2015-002)  
> **ID:** `360042623834` | **Última Atualização:** 2026-07-22T16:08:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082073084183)

 MENSAGEM:**

481-Rejeição: Código Regime Tributário do emitente diverge do cadastro na SEFAZ (NT2015/002)

[CORE_E04171] Empresa optante pelo simples deve usar regime tributário 'Simples Nacional' ou 'Simples Nacional - Sublimite'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082051196055)

 SOLUÇÃO:**

Para correção, siga os passos abaixo.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082051199895)

 Acesse: Configurações » Cadastros » Empresas

Aba: **"Naturezas"**

- Campo: **"Cód. Regime Tribut."**

Sintonize junto ao Contador da Empresa e/ou através do site do SINTEGRA o “Cód.Regime Tribut.” referente CNPJ da Empresa emissora da NF-e e efetue o ajuste no campo mencionado.

Importante:

- Se a opção "**Cód. Regime Tribut."** for alterada para 'Regime Normal', ajuste o campo "**Tipo de Partilha SN" para "vazio". **Caso contrário, a seguinte rejeição será apresentada: *"Empresa optante pelo simples deve usar regime tributário 'Simples Nacional' ou 'Simples Nacional - excesso de sublimite de receita bruta'"*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082051204631)

 Gere o lote da NF-e novamente e valide no XML se a correção foi atualizada (Tag CRT).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082073098135)

 CAUSA:**

Quando for emitida uma NF-e e o Código do Regime Tributário (CRT) do Emitente informado for divergente do Cadastrado na Sefaz, será retornado a rejeição "481 - Código Regime Tributário do emitente diverge do cadastro na SEFAZ".

Os códigos de regime tributário são:

- 1 = Simples Nacional;

- 3 = Regime Normal.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16082051211671)

 OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota Técnica.