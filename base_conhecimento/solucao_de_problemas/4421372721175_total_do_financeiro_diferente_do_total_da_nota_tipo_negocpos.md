# Total do financeiro diferente do total da nota (Tipo Negoc.possui Nro de Parcelas)

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4421372721175-Total-do-financeiro-diferente-do-total-da-nota-Tipo-Negoc-possui-Nro-de-Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4421372721175-Total-do-financeiro-diferente-do-total-da-nota-Tipo-Negoc-possui-Nro-de-Parcelas)  
> **ID:** `4421372721175` | **Última Atualização:** 2026-07-22T15:19:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287126709143)

 MENSAGEM: **

[CORE_E02784] - Total do financeiro diferente do total da nota (Tipo Negoc.possui Nro de Parcelas).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287126713495)

 CAUSA:**

Essa mensagem será apresentada quando o tipo de negociação utilizado possui 'Nro de Parcelas' informado (aba **"Característica",** da tela **"Tipo de Negociação"**) e o total do financeiro gerado difere do total da nota. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287158058903)

 SOLUÇÃO:**

Para correção, siga os passos abaixo: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287126718487)

 Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba **"Financeiro"**) está igual ao 'Valor total da nota'. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15500597353367)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287126719767)

 Selecione a opção **"Refazer Financeiro"** e valide se as parcelas geradas foram ajustadas, de forma que essa divergência sejam sanadas.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15500673593751)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287158062231)

 OBSERVAÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451013877655)

 Se o processo da sua empresa permite essa situação, valide com o implantador da empresa a necessidade de ajustar os parâmetros abaixo, que permitem esse cenário:

**Validação por TOP:**

- Parâmetro "**HABOPCFINMENNOT" : **ativado

- Realizada marcação** 'Permite financeiro menor que o valor total da nota '** (Tela 'Tipos de Operação-TOP' >> aba 'X')

**Validação Geral:**

- Parâmetro **"VALTOTFINNOT- Valida total dos financeiros da nota":** desativado

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287158066583)

 IMPORTANTE: **

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451013877655)

 **Nesse caso, é importante avaliar também as configurações atuais do parâmetro NFEFINDIFNOTA, de forma que a diferença dos valores seja devidamente gerada.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451013877655)

 Os parâmetros acima afetam a divergência de valor: financeiro **menor **que o total da nota. Se financeiro maior que o total da nota, a validação continuará acontecendo, visto não tratar-se de um cenário válido.