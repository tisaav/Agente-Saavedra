# Aviso: Already connected - Servidor SMTP e/ou Contas SMTP

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30366383112727-Aviso-Already-connected-Servidor-SMTP-e-ou-Contas-SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/30366383112727-Aviso-Already-connected-Servidor-SMTP-e-ou-Contas-SMTP)  
> **ID:** `30366383112727` | **Última Atualização:** 2026-07-22T14:35:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366383077143)

 MENSAGEM: **

Aviso: Already connected.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366383081367)

 **SITUAÇÃO: **

Ao realizar um cadastro de e-mail na tela "Conta SMTP" ou "Servidor SMTP" e realizar o envio de e-mail teste retorna o aviso a cima.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366413170967)

SOLUÇÃO: **

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366413173527)

 Acesse o e-mail que está sendo configurado fora do Sankhya. Por exemplo, se o provedor for o Gmail, acesse gmail.com e faça login com seu e-mail.**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366413176727)

 Verifique em "enviadas" ou "caixa de entrada" do email se há algum e-mail informando que não foi possível fazer o envio, no próprio e-mail terá o motivo, que pode ser quantidade de envio ultrapassada, destinatário bloqueado ou até mesmo algum bloqueio de "blacklist".

**Observação:** normalmente a mensagem estará em inglês, caso necessário faça a tradução para conhecer o real motivo.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366383097751)

 Envie um e-mail diretamente do provedor para verificar se a questão está relacionada à configuração do provedor e não ao Sankhya. Ao enviar, na maioria dos casos, ocorrerá um erro. Caso seja possível enviar o e-mail fora do Sankhya, mas ocorra o erro "Already Connected" dentro do Sankhya, pode se tratar de um bloqueio de envio por meio da API.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366383099543)

 Neste caso, verifique diretamente com o setor de TI da empresa ou com o responsável pelo provedor. Se necessário, cadastre um e-mail de teste que esteja liberado e realize um envio de teste para certificar que não há restrições por parte da Sankhya.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30366383085719)

 CAUSA: **

O aviso é retornado devido o Sankhya ter solicitado a conexão com a API do provedor do email configurado e ter enviado a requisição para o provedor realizar o envio normalmente, porém por algum motivo o provedor não conseguiu enviar o e-mail. Retornando que "já está conectado".