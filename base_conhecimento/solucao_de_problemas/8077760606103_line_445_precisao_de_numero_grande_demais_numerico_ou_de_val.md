# LINE 445 - Precisão de número grande demais numérico ou de valor ORA-06512: em "SDETESTE01.SNK_MATGIRCALCSUG"

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8077760606103-LINE-445-Precis%C3%A3o-de-n%C3%BAmero-grande-demais-num%C3%A9rico-ou-de-valor-ORA-06512-em-SDETESTE01-SNK-MATGIRCALCSUG](https://ajuda.sankhya.com.br/hc/pt-br/articles/8077760606103-LINE-445-Precis%C3%A3o-de-n%C3%BAmero-grande-demais-num%C3%A9rico-ou-de-valor-ORA-06512-em-SDETESTE01-SNK-MATGIRCALCSUG)  
> **ID:** `8077760606103` | **Última Atualização:** 2026-07-22T15:12:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585513884311)

 MENSAGEM**:

- "ERRO: ORA-06502: PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em "SDETESTE01.SNK_MATGIRCALCSUG", line 445 ORA-06512: em line 1".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585513889687)

 **SITUAÇÃO:**

Mensagem de erro apresentada ao processar matriz da analise de giro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585529427095)

 SOLUÇÃO:**

Execute o seguinte SELECT, a fim de validar se há algum produto com estoque que ultrapasse a quantidade limite de casas decimais para a analise de giro;

SELECT * FROM TGFGIR WHERE ABS(ESTOQUE) > 10000000000

Valide se a quantidade em estoque está correta.

O produto pode ser retirado do processamento da matriz por meio da criação de filtros.  

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585513898263)

CAUSA:**

O erro ocorre devido a alguns produtos estarem com estoque com mais de 30 dígitos e, ao calcular o giro diário, encontra um número com mais de 10 dígitos, que excede o tamanho do campo do giro diário.