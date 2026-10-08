# Falha ao executar a procedure Stp_Set_Session2. Erro: ORA-04068: estado atual dos pacotes foi descartado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31872306056599-Falha-ao-executar-a-procedure-Stp-Set-Session2-Erro-ORA-04068-estado-atual-dos-pacotes-foi-descartado](https://ajuda.sankhya.com.br/hc/pt-br/articles/31872306056599-Falha-ao-executar-a-procedure-Stp-Set-Session2-Erro-ORA-04068-estado-atual-dos-pacotes-foi-descartado)  
> **ID:** `31872306056599` | **Última Atualização:** 2026-07-22T14:32:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31999153052183)

 MENSAGEM:**

[CORE_E01003] Falha ao executar a procedure Stp_Set_Session2. Erro: ORA-04068: estado atual dos pacotes foi descartado.
ORA-04061: estado existente de package "SANKHYA.VARIAVEIS_PKG" foi invalidado
ORA-04065: package "SANKHYA.VARIAVEIS_PKG" não executado, alterado ou eliminado
ORA-06508: PL/SQL: não foi localizada a unidade de programa que está sendo chamada: "SANKHYA.VARIAVEIS_PKG"
ORA-06512: em "SANKHYA.STP_SET_SESSION", line 9
ORA-06512: em "SANKHYA.STP_SET_SESSION2", line 3
ORA-06512: em line 1

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31999126768663)

 SITUAÇÃO:**

Ao realizar qualquer processo nos portais (venda ou compra).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31888056124823)

SOLUÇÃO:**

Este erro ocorre pois o Package "**VARIAVEIS_PKG**" que é um objeto nativo da Sankhya, foi excluído, alterado ou até mesmo compilado utilizando o Owner incorreto.

Então, para solução, entre em **contato com a equipe de Service Desk** para obter o Script atualizado do objeto para uma nova compilação. 

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31872499888279)

 Esse pacote atua como um **repositório de variáveis e estruturas de apoio,** que podem ser usadas por diversos procedimentos e funções do sistema, ajudando a manter **consistência, desempenho e organização** em ambientes com lógica de negócio complexa.