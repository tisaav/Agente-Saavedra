# Empresa XXX é optante do 'Simples Nacional - excesso de sublimite de receita bruta' e o campo 'Tipo de Partilha SN' não pode estar preenchido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659173-Empresa-XXX-%C3%A9-optante-do-Simples-Nacional-excesso-de-sublimite-de-receita-bruta-e-o-campo-Tipo-de-Partilha-SN-n%C3%A3o-pode-estar-preenchido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043659173-Empresa-XXX-%C3%A9-optante-do-Simples-Nacional-excesso-de-sublimite-de-receita-bruta-e-o-campo-Tipo-de-Partilha-SN-n%C3%A3o-pode-estar-preenchido)  
> **ID:** `360043659173` | **Última Atualização:** 2026-07-22T16:04:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134803993879)

 MENSAGEM:**

[CORE_E04172] Empresa XXX é optante do 'Simples Nacional - excesso de sublimite de receita bruta' e o campo

'Tipo de Partilha SN' não pode estar preenchido!

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134803996951)

 SITUAÇÃO:**

Ao tentar alterar tipo de partilha da empresa, ocorre a mensagem.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134817190295)

 CAUSA:**

A partir do momento que a empresa excedeu o limite do faturamento do Simples Nacional a marcação do Código do Regime Tributário será 'Simples Nacional - Excesso de Sublimite de Receita Bruta' e o campo Tipo de Partilha SN deve ficar em branco'.

O sistema não irá considerar mais a partilha e nesta faixa o cliente também não terá partilha, será necessário a configuração de regras de alíquotas tanto de ICMS quanto de PIS/COFINS. Desta forma não será utilizado o campo CSOSN e sim o campo CST do cadastro de alíquotas.

Para detalhes de como configurar Alíquotas de ICMS acesse o artigo: **"****[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"**

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134817186327)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134803998231)

 Acesse: Configurações » Cadastros » Empresas, aba **"Naturezas"**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134817189015)

 Optante pelo SIMPLES: marcado

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134817189015)

 Cód. Regime Tribut: Simples Nacional - excesso de sublimite de receita bruta

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134817189015)

 Tipo de Partilha SN: Deixar em branco

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14633792080535)


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)