# Solicitação de liberação de orçamento está pendente

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9299196084119-Solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-de-or%C3%A7amento-est%C3%A1-pendente](https://ajuda.sankhya.com.br/hc/pt-br/articles/9299196084119-Solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-de-or%C3%A7amento-est%C3%A1-pendente)  
> **ID:** `9299196084119` | **Última Atualização:** 2026-07-22T15:08:59Z

---

**

![1__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/23724725178775)

Mensagem:**

[CORE_E05411]  Solicitação de liberação de orçamento está pendente.

**

![2__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/23724725192599)

Causa:**

Ocorre quando o orçamento não é aprovado.

**

![3__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/23724767000727)

Solução:**

Na estrutura de metas e orçamentos temos a seguinte configuração:

- Ignora orçamento não previsto = marcado

- Quando exceder a Despesa Prevista = Avisar e Não aceitar o lançamento

- No Planejamento de Metas e Orçamentos, se a coluna de Previstos estiver zerada e a coluna de realizados estiver preenchida, ao fazer um lançamento com esse projeto, o sistema solicita a liberação dessa meta.

- Para não solicitar essa liberação, o cliente tira o 'zero - 0,00' da coluna de previstos, logo a coluna de realizado também fica sem registros, aí dessa forma o sistema não solicita a liberação.

Verificar a configuração na tela **Preferências** *(Configurações » Avançado » Preferências)* do parâmetro **'METZERONAOPREV - Considera orçamento zerado como não previsto?' **caso esteja desligado basta ligá-lo e realizar o teste novamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14367412079767)