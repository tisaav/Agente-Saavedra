# [CORE_01856] Número da nota não pode ser informado

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39311485541143--CORE-01856-N%C3%BAmero-da-nota-n%C3%A3o-pode-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39311485541143--CORE-01856-N%C3%BAmero-da-nota-n%C3%A3o-pode-ser-informado)  
> **ID:** `39311485541143` | **Última Atualização:** 2026-07-24T19:02:11Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39311475055767)

 **Mensagem**

[CORE_01856] Número da nota não pode ser informado

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39311485534615)

 **Situação**

Ao realizar o apontamento de ordem de produção na tela **"Operações de Produção"** (Produção » Rotinas » Operações de Produção), o sistema apresenta a mensagem de erro impedindo a conclusão do processo.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39311485534999)

 **Solução**

Para resolver o erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39311485535511)

 Acesse a tela **"Modelos de Notas e Pedidos"** (Comercial » Consulta » Modelo de Notas e Pedidos) e localize o modelo de nota utilizado na geração da nota de produção.

Obs.: Essa informação pode ser verificada nas Operações de Estoque do Processo Produtivo que está utilizando para a OP.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39311475057815)

 Verifique se o campo **"Nro. Nota"** está preenchido no modelo. Caso esteja, apague o número da nota informado e coloque o número 0.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39311475058199)

 Retorne à tela **"Operações de Produção "** e realize novamente o apontamento da ordem de produção.
 

Após a realização desse procedimento, o sistema gerará corretamente a nota de produção e sua respectiva numeração, não apresentando mais o erro identificado nesse cenário.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39311475060119)

 **Causa**

O erro ocorre devido a um conflito de configuração entre o modelo de nota e a TOP. Quando o campo **"Nro. Nota"** está preenchido manualmente no modelo de nota, mas a TOP está configurada para gerar o número automaticamente, o sistema identifica uma inconsistência e bloqueia o apontamento da ordem de produção.