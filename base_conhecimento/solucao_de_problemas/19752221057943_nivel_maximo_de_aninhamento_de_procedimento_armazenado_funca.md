# Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32)

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/19752221057943-N%C3%ADvel-m%C3%A1ximo-de-aninhamento-de-procedimento-armazenado-fun%C3%A7%C3%A3o-gatilho-ou-exibi%C3%A7%C3%A3o-excedido-o-limite-%C3%A9-32](https://ajuda.sankhya.com.br/hc/pt-br/articles/19752221057943-N%C3%ADvel-m%C3%A1ximo-de-aninhamento-de-procedimento-armazenado-fun%C3%A7%C3%A3o-gatilho-ou-exibi%C3%A7%C3%A3o-excedido-o-limite-%C3%A9-32)  
> **ID:** `19752221057943` | **Última Atualização:** 2026-07-22T14:51:32Z

---

####                    **'Artigo criado para apoio ao usuário técnico da empresa'**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19752221042327)

 **MENSAGEM:**

Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19752176534935)

SOLUÇÃO:**

Ajustar objetos de banco de dados personalizados a fim de evitar a recursividade nestes

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19752231652375)

CAUSA:**
No SQL Server, devemos nos atentar durante o desenvolvimento de objetos quanto a possibilidade de recursividade (loop).
É comum em criação de triggers de UPDATE (exemplo mais clássico), a ocorrência de um comando de UPDATE que irá disparar novamente esta trigger, até que surja uma mensagem de erro:
 
Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).
 
Isto ocorre caso o banco de dados esteja com o parâmetro RECURSIVE_TRIGGERS ativado. Para verificar esta condição, execute o comando:
 
select name, is_recursive_triggers_on from sys.databases where name = db_name()
 
Caso a segunda coluna retorne 1, este parâmetro está ligado. Caso esteja 0, é provável que mais objetos dentro do processo no banco de dados gerem o loop. Neste caso, é recomendado adicionar, então, um teste para verificar qual é o nível de recursão daquela entrada no objeto. Eis a expressão que pode fazer este controle:
 
  IF @@NESTLEVEL > 1
    RETURN
 
Para desativar o parâmetro RECURSIVE_TRIGGERS, é preciso executar o seguinte comando:
 
ALTER DATABASE <dbname> SET RECURSIVE_TRIGGERS OFF
 
Abaixo um exemplo de loop. Basta retirar o comentário do trecho do @@NESTLEVEL citado acima para ver o comportamento.
 
 
ALTER DATABASE <dbname> SET RECURSIVE_TRIGGERS ON
 
CREATE TABLE TESTE_LOOP
(
  ID INT IDENTITY(1,1) PRIMARY KEY,
  VALOR INT NOT NULL
)
GO
 
CREATE TRIGGER TRG_TESTE_LOOP ON TESTE_LOOP
FOR UPDATE
AS
BEGIN
 
/*  IF @@NESTLEVEL > 1
    RETURN*/
 
  UPDATE TESTE_LOOP SET TESTE_LOOP.VALOR = TESTE_LOOP.VALOR + 1 FROM INSERTED INS WHERE TESTE_LOOP.ID = INS.ID
END
GO
 
INSERT INTO TESTE_LOOP VALUES (1)
GO
 

UPDATE TESTE_LOOP SET VALOR = 5 WHERE ID = 3
GO
 
Mensagem apresentada:
Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).
 
Não se esqueça de desativar o parâmetro ao final do teste:
 
ALTER DATABASE <dbname> SET RECURSIVE_TRIGGERS OFF