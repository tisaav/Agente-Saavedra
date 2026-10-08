# Valor informado no financeiro para compensação maior que o crédito do cliente

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6427511395735-Valor-informado-no-financeiro-para-compensa%C3%A7%C3%A3o-maior-que-o-cr%C3%A9dito-do-cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/6427511395735-Valor-informado-no-financeiro-para-compensa%C3%A7%C3%A3o-maior-que-o-cr%C3%A9dito-do-cliente)  
> **ID:** `6427511395735` | **Última Atualização:** 2026-07-30T19:37:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461380501015)

  MENSAGEM: **

[CORE_E03745]  Valor informado no financeiro para compensação maior que o crédito do cliente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461380503063)

 SOLUÇÃO: **

Para a resolução do erro, o tipo de título informado no parâmetro **"****TIPTITCREDCLI"** não pode ser o mesmo da nota e ele é padrão zero. Informando um tipo de título dentro do financeiro da nota ao confirmar o lançamento, o sistema apresenta a mensagem de compensação de crédito, sendo possível realizar a compensação corretamente. 
**Dica:** o ideal é que seja configurado um tipo de titulo no parâmetro TIPTITCREDCLI pra evitar que o erro ocorra novamente. 

Segue mais detalhes das configurações e do funcionamento da rotina no seguinte artigo:
[Compensação de Crédito ou Débito em Compra ou Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461380505111)

CAUSA: **

Quando o parâmetro TIPTITCREDCLI  = 0 e no financeiro da nota também estiver com o tipo de título = 0, o sistema não executa a compensação de crédito no lançamento.


---

### 🔗 Links e Referências Internas:

- [Compensação de Crédito ou Débito em Compra ou Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda)