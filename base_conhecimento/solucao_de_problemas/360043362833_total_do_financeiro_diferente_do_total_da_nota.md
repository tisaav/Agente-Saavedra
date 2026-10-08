# Total do financeiro diferente do total da nota

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362833-Total-do-financeiro-diferente-do-total-da-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362833-Total-do-financeiro-diferente-do-total-da-nota)  
> **ID:** `360043362833` | **Última Atualização:** 2026-07-22T16:05:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031020439)

 MENSAGEM:**

[CORE_E02783] Total do financeiro diferente do total da nota.

[CORE_E02782] Total do financeiro diferente do total da nota.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016367639)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016369687)

 Certifique-se que o valor gerado no **financeiro da nota** (soma das parcelas da aba **"Financeiro"**) está igual ao **Valor total da nota**. 

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14601414346391)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016371991)

 Acesse Comercial » Arquivo » Cadastros »** "[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)"** e verifique no tipo de negociação, aba **"Parcelas"**, se os percentuais, caso haja parcelas, somados resultará em 100%.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14601430094999)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016373271)

 Verifique se existem parcelas por Empresa, na aba** "Parcelas"**, caso exista mais de uma parcela e cada parcela tenha um código de empresa, deverá criar uma parcela específica para empresa da nota.

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14601430243735)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016374551)

 Em caso positivo, Botão **"Outras opções (...)"** » **"Refazer Financeiro"**, certificando-se que o valor das parcelas condiz com o total da nota

 

![mceclip2__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14601430208791)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031031447)

 Caso a divergência não esteja relacionada com os tópicos anteriores (cálculo incorreto do financeiro, fórmulas do tipo de negociação), avalie se essa divergência está relacionada a incoerência de impostos. Exemplo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031033111)

 A diferença entre o total da nota e o valor do financeiro está relacionado ao Vlr.do IPI : nesse caso o IPI deveria somar ao total da nota, sendo necessário marcar na TOP a opção **"Somar IPI ao total da nota"**;

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031034519)

 OBSERVAÇÕES:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458195844119)

 Se o processo da sua empresa permite essa situação de divergência de valores, valide com o implantador da empresa a necessidade de ajustar os parâmetros abaixo, que permitem esse cenário:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031033111)

 Validação por TOP:**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031036823)

Parâmetro "**HABOPCFINMENNOT": **ativado

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031036823)

Realizada marcação** "Permite financeiro menor que o valor total da nota" **(Tela 'Tipos de Operação-TOP', aba 'Financeiro')

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031033111)

 Validação Geral:**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116031036823)

Parâmetro **"VALTOTFINNOT- Valida total dos financeiros da nota"**: desativado

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801989316503)

 IMPORTANTE: **

- Nesse caso, é importante avaliar também as configurações atuais do parâmetro **NFEFINDIFNOTA**, de forma que a diferença dos valores seja devidamente gerada.

- Os parâmetros acima afetam a divergência de valor: financeiro **menor** que o total da nota. Se financeiro **maior** que o total da nota, a validação continuará acontecendo, visto não tratar-se de um cenário válido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16116016396567)

 CAUSA:**

Ocorre, quando o financeiro da nota está diferente do total da nota, devido configurações inadequadas no tipo de operação ou fórmulas personalizadas no tipo de negociação.


---

### 🔗 Links e Referências Internas:

- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)