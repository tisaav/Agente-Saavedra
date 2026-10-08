# 1135 Rejeição: CST do IBS/CBS informado exige a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097224314647-1135-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-exige-a-informa%C3%A7%C3%A3o-do-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097224314647-1135-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-exige-a-informa%C3%A7%C3%A3o-do-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999)  
> **ID:** `37097224314647` | **Última Atualização:** 2026-07-22T14:20:49Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097224305303)

 **MENSAGEM**

1135 Rejeição: CST do IBS/CBS informado exige a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097224306327)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) modelo 55 a partir da Zona Franca de Manaus (ZFM), utilizando um CST do IBS/CBS que exige a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM, o documento foi rejeitado porque o grupo **gCredPresIBSZFM** não foi informado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097249221399)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097249222295)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP utilizado na operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097249223447)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097224310039)

 Acesse a tela **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097224310807)

 Verifique se o CST utilizado possui o indicador que exige a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (ind_gCredPresIBSZFM = 1).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097249227543)

 Ao emitir a NF-e, certifique-se de que o grupo **gCredPresIBSZFM** esteja devidamente preenchido com:

- 

O **"Tipo de Classificação para o cálculo do crédito presumido na ZFM"** (tpCredPresIBSZFM)

- 

O **"Valor do crédito presumido calculado sobre o saldo devedor apurado"** (vCredPresIBSZFM).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38387132075543)

 Verifique se o emitente está localizado na UF Amazonas (código 13) e possui inscrição de indústria incentivada, pois somente emitentes com essas características podem utilizar o grupo de crédito presumido da ZFM.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38795258568855)

 Acesse as telas **''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e/ou** ''Central de Compras'' **(Comercial » Rotinas » Central de Compras).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38795258571159)

 Na grade** ''Itens''**, selecione o produto e clique em **''Outras opções'' (ícone com três pontos)**.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38795254787735)

 Selecione a opção **''Consultar/Alterar Dados do Imposto do Item''** confira e preencha (se necessário) as bases, alíquotas e o valor do crédito presumi calculados para o IBS e a CBS.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38795451593495)

 **OBSERVAÇÃO**: O IBS/CBS segue as regras da NT 2025.002 (v1.33). Certifique-se de que o módulo Fiscal está atualizado e com os layouts de NF-e mais recentes aplicados para garantir a comunicação correta com a SEFAZ.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097249228823)

 **CAUSA**

A rejeição ocorre porque o CST do IBS/CBS utilizado na operação possui um indicador (ind_gCredPresIBSZFM = 1) que **exige** a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM, mas este grupo não foi informado no documento fiscal.

Esta validação é aplicada especificamente para emitentes localizados na Zona Franca de Manaus (UF Amazonas) que possuem inscrição de indústria incentivada e estão utilizando o **"Tipo de Nota Fiscal de Crédito"** configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**. O grupo gCredPresIBSZFM é obrigatório neste cenário, conforme estabelecido na Lei Complementar 214/2025, que regulamenta os benefícios fiscais para a Zona Franca de Manaus no contexto da Reforma Tributária.