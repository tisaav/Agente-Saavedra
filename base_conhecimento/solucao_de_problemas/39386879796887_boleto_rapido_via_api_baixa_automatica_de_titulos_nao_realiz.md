# Boleto Rápido via API: Baixa automática de títulos não realizada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39386879796887-Boleto-R%C3%A1pido-via-API-Baixa-autom%C3%A1tica-de-t%C3%ADtulos-n%C3%A3o-realizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/39386879796887-Boleto-R%C3%A1pido-via-API-Baixa-autom%C3%A1tica-de-t%C3%ADtulos-n%C3%A3o-realizada)  
> **ID:** `39386879796887` | **Última Atualização:** 2026-07-24T15:36:40Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39386879780631)

 MENSAGEM**

Os títulos não estão sendo baixados automaticamente via API, mesmo com a liquidação sendo exibida na tela **"Acompanhamento de Boletos - API"** (Financeiro »   Consultas Acompanhamento de Boletos - API).

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39386884160791)

 SITUAÇÃO**

Este problema ocorre quando os boletos são enviados e recebidos corretamente pela API, porém a baixa automática não é executada na tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira). A liquidação aparece registrada no acompanhamento de boletos, mas o status do título não é atualizado no sistema.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39386884161303)

 SOLUÇÃO**

A solução para este problema varia conforme a causa identificada. Siga as orientações abaixo:

 

**Atualização do sistema**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39386884167063)

 Verifique a versão atual do sistema Sankhya Om.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169111)

 Caso esteja em versão anterior à 4.35b439, realize a atualização para a versão igual ou superior.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169879)

 Monitore as próximas baixas automáticas para confirmar o comportamento esperado.
 

**Verificação do credenciamento da API**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39386884167063)

 Acesse a tela **"Acompanhamento de Boletos - API"** (Financeiro »  Consultas Acompanhamento de Boletos - API).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169111)

  Verifique se o credenciamento da conta bancária está ativo.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169879)

 Caso o credenciamento esteja inativo ou descredenciado, realize um novo credenciamento da conta bancária.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39386884171031)

 Após o novo credenciamento, o banco identificará automaticamente os títulos pendentes e efetuará as baixas, sem necessidade de processamento manual.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39628385548055)

 Ainda nesta tela, verifique as ações automáticas configuradas para o retorno da API. Na opção "Baixa Automática", é necessário que esteja definida a execução da baixa com base na "data de pagamento" ou na "data de crédito em conta", garantindo assim que o processo seja realizado automaticamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39628385549975)

 

**Verifique o campo Baixa via API**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39386884167063)

 Acessa a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169111)

 Verifique o campo "**Baixa via API**" se o mesmo consta com alguma mensagem de erro, realize a devida correção e proceda com a baixa manual do titulo.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39386884169879)

 Monitore as próximas baixas automáticas para confirmar o ajuste realizado.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39627854425495)

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39386884172183)

 CAUSA**

Esse incidente ocorre porque a liquidação dos boletos é recebida corretamente pela API, porém a baixa automática não é realizada no financeiro devido a inconsistências de configuração, como versão do sistema desatualizada, problemas no credenciamento da API ou ausência/erro nos parâmetros de baixa automática.