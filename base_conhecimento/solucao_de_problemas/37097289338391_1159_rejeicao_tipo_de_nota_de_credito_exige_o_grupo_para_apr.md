# 1159 Rejeição: Tipo de Nota de Crédito exige o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097289338391-1159-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-Cr%C3%A9dito-exige-o-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097289338391-1159-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-Cr%C3%A9dito-exige-o-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999)  
> **ID:** `37097289338391` | **Última Atualização:** 2026-07-22T14:20:48Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097289320471)

 **MENSAGEM**

1159 Rejeição: Tipo de Nota de Crédito exige o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097281214871)

 **SITUAÇÃO**

Rejeição na validação da **NF-e** com finalidade de **Nota de Crédito – 02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM**, em razão de inconsistência relacionada às informações exigidas para esse tipo de operação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097289323799)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097281218071)

 Acesse a tela ''Tipos de Operação - TOP'' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097281220119)

 Na aba ''NF-e/NFC-e/CF-e'', verifique se o campo ''NF-e'' está configurado corretamente como a finalidade **"Nota de Crédito"** e o campo ''Tipo de Nota Fiscal de Crédito'' como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097281220503)

 Verifique se a empresa emitente está localizada no **Amazonas (AM)** e possui inscrição de indústria incentivada, pois apenas empresas com estas características podem utilizar este tipo de nota de crédito.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097289333399)

 Ao emitir a nota fiscal, certifique-se de que o **grupo de dados para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM** (grupo: gCredPresIBSZFM) esteja devidamente preenchido com:

- 

Tipo de Classificação para o cálculo do crédito presumido na ZFM (tpCredPresIBSZFM);

- 

Ano e mês referência do período de apuração (competApur);

- 

Valor do crédito presumido calculado sobre o saldo devedor apurado (vCredPresIBSZFM).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097281222295)

 Certifique-se de que o **Código de Situação Tributária CST **utilizado na nota fiscal seja compatível com a apropriação de crédito presumido para a ZFM, ou seja, que possua o indicador que permite o uso deste tipo de crédito (ind_gCredPresIBSZFM = 1).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38386935294359)

 Verifique se a data de emissão da nota fiscal é **igual ou posterior a janeiro de 2029**, pois este tipo de nota de crédito só pode ser utilizado a partir desta data, conforme regra B25.2-30.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097289335063)

 **CAUSA**

Esta rejeição ocorre devido à regra de validação UB131-50 da Sefaz, que exige que quando o **Tipo de Nota de Crédito** (tag: tpNFCredito) for igual a **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, o grupo de dados específico para esta apropriação (grupo: gCredPresIBSZFM) deve ser obrigatoriamente informado.

Esta regra está alinhada com o artigo 450, § 1º da Lei Complementar 214/25, que estabelece o mecanismo de crédito presumido de IBS sobre o saldo devedor para empresas localizadas na Zona Franca de Manaus. A ausência deste grupo de dados impede que a Sefaz processe corretamente as informações necessárias para a apropriação do crédito presumido, resultando na rejeição do documento fiscal.