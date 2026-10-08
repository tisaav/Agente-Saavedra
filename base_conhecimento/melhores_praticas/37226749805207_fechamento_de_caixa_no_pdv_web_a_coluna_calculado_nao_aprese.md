# Fechamento de Caixa no PDV Web: A coluna “Calculado” não apresenta os valores esperados

> **Módulo:** Melhores Praticas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226749805207-Fechamento-de-Caixa-no-PDV-Web-A-coluna-Calculado-n%C3%A3o-apresenta-os-valores-esperados](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226749805207-Fechamento-de-Caixa-no-PDV-Web-A-coluna-Calculado-n%C3%A3o-apresenta-os-valores-esperados)  
> **ID:** `37226749805207` | **Última Atualização:** 2026-07-22T14:14:40Z

---

Durante o fechamento de caixa no PDV Web, alguns usuários podem notar que a coluna **“Calculado”** não apresenta os valores esperados para determinadas formas de pagamento, especialmente **Cartão de Crédito** e **Cartão de Débito**.

Esse comportamento é normal e está relacionado à maneira como o sistema realiza a apuração automática dos valores do caixa.

No fechamento, cada forma de pagamento exibe duas colunas:

- 

**Informado**: Valor inserido manualmente pelo usuário no momento do fechamento do caixa.

- 

**Calculado**: Valor apurado automaticamente pelo sistema com base nos lançamentos realizados durante o período do caixa.

 

![image - 2025-12-24T084536.176.png](https://ajuda.sankhya.com.br/hc/article_attachments/37242834836631)

 

#### **Por que os valores de pagamento em cartão não aparecem na coluna “Calculado”?**

Esse comportamento é esperado. Os valores de **Cartão de Crédito** e **Cartão de Débito** só são exibidos automaticamente na coluna **“Calculado”** quando:

- 

As vendas foram **baixadas corretamente**

- 

A baixa foi realizada pelo mesmo usuário do caixa.

Quando essas condições não são atendidas, o sistema não consegue associar os valores ao caixa, mantendo os campos de cartão zerados na coluna **Calculado**.

Nesses casos, apenas a coluna **Informado** deve ser utilizada para o preenchimento manual dos valores.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229768287255)

 OBSERVAÇÃO: **Para que a baixa seja considerada no momento da confirmação, o **Tipo de Título / Tipo de Negociação** deve estar configurado corretamente para esse processo.