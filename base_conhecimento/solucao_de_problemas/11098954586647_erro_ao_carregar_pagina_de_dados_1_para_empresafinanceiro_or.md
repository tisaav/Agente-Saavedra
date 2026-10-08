# Erro ao carregar página de dados 1 para EmpresaFinanceiro. ORA-06502: PL/SQL: erro numérico ou de valor ORA-06512: em line 1 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/11098954586647-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-EmpresaFinanceiro-ORA-06502-PL-SQL-erro-num%C3%A9rico-ou-de-valor-ORA-06512-em-line-1](https://ajuda.sankhya.com.br/hc/pt-br/articles/11098954586647-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-EmpresaFinanceiro-ORA-06502-PL-SQL-erro-num%C3%A9rico-ou-de-valor-ORA-06512-em-line-1)  
> **ID:** `11098954586647` | **Última Atualização:** 2026-07-22T15:02:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033033152279)

 MENSAGEM**:

[CORE_E00358] Erro ao carregar página de dados 1 para EmpresaFinanceiro.
ORA-06502: PL/SQL: erro numérico ou de valor
ORA-06512: em line 1

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033033166999)

 CAUSA:**

Erro de leitura da query via procedure.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033033177751)

 SOLUÇÃO:**

Para que o erro não seja mais apresentado e necessário realizar as configurações abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611018895255)

 Desative o parâmetro **Usar Stored Procedure ao exec. queries do sistema - USESTPQUERY** na tela **Preferências** *(Configurações » Avançado » Preferências)*, conforme imagem abaixo:

![Imagem](/attachments/token/tkVGgJyvKpPNxF2sgYvTqPfl2/?name=image.png)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611018901015)

 Reinicie o servidor do sistema na tela **Administração do Servidor** *(Configurações » Avançado » Administração do Servidor)*

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18611018906647)

 

Assim ele mudará a forma de ler os dados, onde a query que traz o erro pare de ser executada via procedure e a tela consiga carregar corretamente.