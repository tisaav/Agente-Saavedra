# Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41835339582871-Doca-n%C3%A3o-pode-ser-liberada-devido-a-restri%C3%A7%C3%A3o-de-configura%C3%A7%C3%A3o-Existem-os-seguintes-pedidos-pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41835339582871-Doca-n%C3%A3o-pode-ser-liberada-devido-a-restri%C3%A7%C3%A3o-de-configura%C3%A7%C3%A3o-Existem-os-seguintes-pedidos-pendentes)  
> **ID:** `41835339582871` | **Última Atualização:** 2026-09-14T14:55:10Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835355824663)

 MENSAGEM**

Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835339569431)

 **SITUAÇÃO**

Ao tentar liberar a Doca pelo outras opções da tela expedição de mercadorias, o sistema apresenta a seguinte mensagem

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835339570839)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835355828119)

 Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835339572631)

 Altere o parâmetro **''VALFATLIBDOCA''** - **''Regra para validar faturamento na liberação de doc''** para não valida.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41835339574423)

 **CAUSA**

É um comportamento sistêmico, pois, quando o parâmetro **''Regra para validar faturamento na liberação de doc''** - **''VALFATLIBDOCA"** que tem o objetivo de validar os pedidos de venda não faturados, está com a situação **Valida e Bloqueia**, o sistema não permite a liberação da doca até que o pedido de venda seja faturado.