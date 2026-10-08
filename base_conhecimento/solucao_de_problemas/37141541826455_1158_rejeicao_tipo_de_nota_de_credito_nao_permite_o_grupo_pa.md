# 1158 Rejeição: Tipo de Nota de Crédito não permite o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141541826455-1158-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-Cr%C3%A9dito-n%C3%A3o-permite-o-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141541826455-1158-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-Cr%C3%A9dito-n%C3%A3o-permite-o-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999)  
> **ID:** `37141541826455` | **Última Atualização:** 2026-07-22T14:19:04Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141541822359)

 **MENSAGEM**

1158 Rejeição: Tipo de Nota de Crédito não permite o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141541822743)

 **SITUAÇÃO**

A NF-e foi emitida com a informação de apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus, utilizando o grupo gCredPresIBSZFM, associada a um tipo de nota de crédito diferente do previsto para esse enquadramento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141558106007)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38157482193303)

 Verifique o tipo de nota de crédito que está sendo utilizado na NF-e através da tela de **"Notas Fiscais"** (Gestão Fiscal » Movimentação » Notas Fiscais).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141541823383)

 Altere o tipo de nota de crédito para **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)"** ou remova o grupo de apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141558108823)

 Caso opte por alterar o tipo de nota de crédito, certifique-se de que a finalidade da NF-e esteja configurada como **"5 - Nota de crédito"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141558109335)

 Verifique se a empresa emitente está localizada no **Amazonas (UF 13)** e possui inscrição de indústria incentivada, pois apenas empresas com estas características podem utilizar este tipo de nota de crédito.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141558109591)

 Certifique-se de que a data de emissão da nota seja a partir de **janeiro de 2029**, pois este tipo de nota de crédito só poderá ser utilizado a partir desta data, conforme a regra de validação B25.2-30.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141541825559)

 Verifique se o CST utilizado permite o uso do grupo de crédito presumido para a ZFM (indicador ind_gCredPresIBSZFM = 1).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141558110615)

 **CAUSA**

Esta rejeição ocorre devido à incompatibilidade entre o tipo de nota de crédito selecionado e a tentativa de informar o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM. De acordo com a regra de validação UB131-40, o grupo gCredPresIBSZFM só pode ser informado quando o tipo de nota de crédito for **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

A Lei Complementar 214/25, em seu artigo 450, § 1º, estabelece condições específicas para a apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus, e a SEFAZ implementou validações rigorosas para garantir que este benefício fiscal seja utilizado apenas nas situações previstas em lei.