# Veja como localizar TRIGGER  desabilitadas em banco  ORACLE  ou SQL

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26556536785303-Veja-como-localizar-TRIGGER-desabilitadas-em-banco-ORACLE-ou-SQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/26556536785303-Veja-como-localizar-TRIGGER-desabilitadas-em-banco-ORACLE-ou-SQL)  
> **ID:** `26556536785303` | **Última Atualização:** 2026-07-22T14:41:26Z

---

Durante a atualização do sistema ou atuações diretamente no **Banco de dados**, podem  ocorrer situações em que triggers (nativas ou personalizadas) fiquem desabilitadas, impedindo o correto fluxo de atualização dos dados no sistema.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26556536782487)

SOLUÇÃO:**

Para localizar essas situações, pode-se utilizar os comandos abaixo para cada **Banco de dados,** através do **DBEXPLORER**: 

 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450197889687)

 COMANDO ORACLE: **

*SELECT trigger_name,*
*table_owner,*
*table_name,*
*status *
*FROM all_triggers*
*WHERE status = 'DISABLED'***
**

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450197889687)

 COMANDO SQL: **

*SELECT 
TAB.name as Table_Name 
, TRIG.name as Trigger_Name
, TRIG.is_disabled --or objectproperty(object_id('TriggerName'), 'ExecIsTriggerEnabled')
FROM [sys].[triggers] as TRIG 
inner join sys.tables as TAB 
on TRIG.parent_id = TAB.object_id
where TRIG.is_disabled = 1*