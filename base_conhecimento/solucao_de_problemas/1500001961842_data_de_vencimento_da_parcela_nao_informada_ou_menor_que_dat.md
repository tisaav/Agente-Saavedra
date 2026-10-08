# Data de vencimento da parcela não informada ou menor que Data de Emissão [Ocorr:1]-NT(2016/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001961842-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Emiss%C3%A3o-Ocorr-1-NT-2016-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001961842-Data-de-vencimento-da-parcela-n%C3%A3o-informada-ou-menor-que-Data-de-Emiss%C3%A3o-Ocorr-1-NT-2016-002)  
> **ID:** `1500001961842` | **Última Atualização:** 2026-07-22T15:25:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287431639959)

 MENSAGEM**:

[900 - Rejeição]: Data de vencimento da parcela não informada ou menor que Data de Emissão [Ocorr:1].

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287407062039)

 SOLUÇÃO:**

Para essa Regra de Validação não há exceções. Sempre que informado o grupo de Parcelas de cobrança, a data de vencimento da parcela deve ser preenchida com uma data maior que a data de emissão do documento.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453262487703)

 Exemplo:**
Foi emitida uma NF-e com uma parcela de duplicata e a data de vencimento (**17**/06/2020) foi informada com a data menor que a data de emissão do documento  (**06**/07/2020). Nessas condições, a NF-e foi rejeitada pelo motivo 900. 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287431651351)

 Acesse: Portal de Vendas>>Central de Notas
Acesse a NF-e e identifique a data de emissão da nota, depois verifique na aba: **"Financeiro"** a Data de Vencimento dos títulos. Caso esteja menor que a data de emissão do documento considere ajustar:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453262487703)

 Se as Parcelas do Tipo de Negociação estiverem configuradas com a opção de digitação (**Digitar somente Data ou Digita Data e valor**), será possível ajustar manualmente os vencimentos dos títulos, acessando a nota.
**
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453262487703)

 Se as Parcelas do Tipo de Negociação estiverem configuradas com a opção de digitação (**Não Digita**), acesse a opção Refazer Financeiro da Nota em: Outras Opções>>Refazer Financeiro. Esta ação considerará os prazos estipulados pelas parcelas do tipo de negociação e efetuará o cálculo automático  dos vencimentos, considerando a base do prazo.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287431654679)

 Após os ajustes, gere lote da NF-e novamente.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287431658135)

 OBSERVAÇÃO:**

altere o parâmetro **"USADTVINCOMPFIN"** para a opção **"Data Baixa". **Deste modo, no momento da compensação do crédito o título compensado (receita) ficará com a data de vencimento igual a data em que está sendo baixado. 

 

![Data_de_vencimento_da_parcela_n_o_informada_ou_menor_que_Data_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/15022114935319)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287407087127)

 CAUSA:**

Quando for emitida uma NF-e (modelo 55) e informado o grupo de Parcelas de cobrança e a Data de vencimento da parcela não for informada ou for menor que a data de emissão do documento, haverá a rejeição pelo motivo.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287431658135)

 OBSERVAÇÃO:**

**1-** (**NT2016/002**)

Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)