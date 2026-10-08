# Não é possível estender o segmento / não é possível estender o índice 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616193-N%C3%A3o-%C3%A9-poss%C3%ADvel-estender-o-segmento-n%C3%A3o-%C3%A9-poss%C3%ADvel-estender-o-%C3%ADndice](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616193-N%C3%A3o-%C3%A9-poss%C3%ADvel-estender-o-segmento-n%C3%A3o-%C3%A9-poss%C3%ADvel-estender-o-%C3%ADndice)  
> **ID:** `360044616193` | **Última Atualização:** 2026-08-20T12:10:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16783035296919)

 MENSAGEM:**

[ORA-01691]: Não é possível estender o segmento lob.
[ORA-01652]: Não é possível estender o segmento temp. em 999 no tablespace TEMP."
[ORA-01654]: não é possível estender o índice BANCO.TABELA em 8 no tablespace XXXXXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16783040852119)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Neste caso, crie ou aumente a tablespace/índice: este processo é um processo efetuado direto no banco de dados e feito pela Equipe de TI (DBA - Administrador de Banco de Dados) da empresa ou terceiro, caso a empresa não tenha uma Equipe de TI própria ou pode alocar o serviço de um consultor DBA da Unidade para realizar o procedimento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16783040858903)

 CAUSA:**

Esta mensagem é apresentada, pois a tablespace/índice do banco de dados atingiu o limite de espaço.