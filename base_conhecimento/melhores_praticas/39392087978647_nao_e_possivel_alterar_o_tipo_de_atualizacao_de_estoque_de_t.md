# Não é possível alterar o Tipo de atualização de estoque de terceiros

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39392087978647-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-Tipo-de-atualiza%C3%A7%C3%A3o-de-estoque-de-terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/39392087978647-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-Tipo-de-atualiza%C3%A7%C3%A3o-de-estoque-de-terceiros)  
> **ID:** `39392087978647` | **Última Atualização:** 2026-07-22T13:29:31Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39392087965719)

 **Mensagem**

**ORA-20101:** Não é possível alterar o Tipo de atualização de estoque de terceiros

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39392087965847)

 **Situação**

O erro ocorre ao tentar alterar a **Tipo de Operação (TOP)** de um documento já registrado no sistema, quando a TOP de origem possui configuração diferente da TOP de destino em relação a **"Atualiza Estoque de Terceiros"**. 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39392117105943)

 **Solução**

Não existe um procedimento que permita alterar um documento já lançado de uma TOP que **atualiza Estoque de Terceiros** para outra que **não atualiza**, ou vice-versa.

Nesses casos, a única forma de correção é:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39392117106839)

 Acesse o Portal correspondente (Compras ou Vendas) e encontre o documento que foi registrado com a TOP incorreta.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39392117107479)

 Realize a exclusão do documento incorreto.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39392087968151)

 Antes de refazer o processo, acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros) e, na aba **"Estoque de Terceiros"**, confirme se a TOP que você deseja utilizar está configurada corretamente.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39392087969687)

 Realize uma nova importação do XML ou digitação do documento manual utilizando a TOP correta desde o início.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39392087971991)

 Valide se o documento foi registrado corretamente e se o estoque foi atualizado conforme esperado.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39392087972503)

 **Causa**

Este é um comportamento padrão do sistema para garantir a **segurança e integridade dos dados**.

Quando um documento é lançado, o sistema realiza registros físicos na tabela de controle de estoque (`TGFEST`) com base nas regras de terceiros da TOP utilizada. Permitir a alteração posterior para uma TOP com comportamento de estoque diferente geraria inconsistências graves nos saldos de estoque da empresa e de terceiros, pois o histórico gravado não bateria com a nova regra.