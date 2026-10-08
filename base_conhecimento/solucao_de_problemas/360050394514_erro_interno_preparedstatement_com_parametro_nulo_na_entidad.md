# Erro interno: PreparedStatement com parâmetro nulo na entidade 'HistoricoBancario': param[0] = nullde

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360050394514-Erro-interno-PreparedStatement-com-par%C3%A2metro-nulo-na-entidade-HistoricoBancario-param-0-nullde](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050394514-Erro-interno-PreparedStatement-com-par%C3%A2metro-nulo-na-entidade-HistoricoBancario-param-0-nullde)  
> **ID:** `360050394514` | **Última Atualização:** 2026-08-19T14:24:19Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611284513943)

 MENSAGEM**:

Erro interno: PreparedStatement com parâmetro nulo na entidade 'HistoricoBancario':
param[0] = nullde.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611310494359)

 CAUSA:**

Erro ao processar venda na Administração do Checkout, causada pela ausência de configurações de lançamento bancário.

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611310501015)

 **SOLUÇÃO:**

- Tela **'Empresa'** (Comercial » Preferências)
Aba: Propriedades
Campos **"Lançamento bancário receitas:"** e **"Lançamento bancário despesas:"** devem estar preenchidos.

![empresa propriedades.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611310515223)

 **No Checkout :**

- Preferencias > Integração

- Os campos **'Código de lançamento Bancário para Sangria' **e** 'Código de lançamento para Suprimento'** devem estar preenchidos:

![pref.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611310518039)