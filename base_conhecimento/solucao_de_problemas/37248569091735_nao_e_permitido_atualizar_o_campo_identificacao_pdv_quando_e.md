# Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37248569091735-N%C3%A3o-%C3%A9-permitido-atualizar-o-campo-Identifica%C3%A7%C3%A3o-PDV-quando-ele-j%C3%A1-possui-valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/37248569091735-N%C3%A3o-%C3%A9-permitido-atualizar-o-campo-Identifica%C3%A7%C3%A3o-PDV-quando-ele-j%C3%A1-possui-valor)  
> **ID:** `37248569091735` | **Última Atualização:** 2026-07-22T14:13:36Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37248569087639)

 **MENSAGEM:**

ORA-20002: Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.
ORA-06512: em "SANKHYA.TRG_INC_UPD_TGFPDV_BEFORE", line 6
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TGFPDV_BEFORE'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37345349491991)

 SITUAÇÃO:**

Ao tentar alterar o cadastro do PDV, o sistema pode impedir a gravação das alterações e exibir uma das seguintes mensagens:

- 

“Não é permitido atualizar o campo Identificação PDV quando ele já possui valor.”

- 

“O campo Identificação PDV não pode ser alterado para vazio.”

- 

“Já existe um registro com a Identificação PDV informada.”

Esse comportamento é esperado e faz parte das regras de segurança do sistema, que não permitem alterar a Identificação do PDV após o cadastro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37248569088407)

SOLUÇÃO:**

Caso seja necessário utilizar o PDV em **outro equipamento**, o procedimento correto é:

- 

**Criar um novo cadastro de PDV** para a nova máquina

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37345349494295)

 OBSERVAÇÃO: **A alteração direta da Identificação do PDV **não é suportada**, nem via tela nem por comandos no banco de dados, pois pode causar inconsistências no sistema.

 

##### **Posso usar o mesmo PDV para mais de um usuário?**

É possível cadastrar mais de um usuário para o mesmo PDV, desde que a utilização ocorra em momentos distintos. O sistema não permite que dois usuários utilizem o mesmo PDV simultaneamente. Caso seja necessário o uso simultâneo de usuários caixa, cada usuário deverá possuir seu próprio cadastro de PDV e sua própria máquina.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37248552207255)

CAUSA:**

Esse erro ocorre porque o campo **''Identificação do PDV''** possui validações internas de segurança que impedem sua alteração após o cadastro inicial.

A Identificação do PDV é utilizada pelo sistema como um **identificador único do equipamento**, garantindo integridade, rastreabilidade e controle das operações do ponto de venda.

Por esse motivo, o sistema bloqueia alterações do valor já informado, limpeza do campo e reutilização da mesma identificação em outro PDV.