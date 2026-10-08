# 1167 Rejeição: Classificação para subapuração do IBS na ZFM não informada [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095416098327-1167-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-n%C3%A3o-informada-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095416098327-1167-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-n%C3%A3o-informada-nItem-999)  
> **ID:** `37095416098327` | **Última Atualização:** 2026-07-22T14:21:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095416080919)

 **MENSAGEM**

1167 Rejeição: Classificação para subapuração do IBS na ZFM não informada [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095416082583)

 **SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) modelo 55 com o tipo de Nota Fiscal de Crédito configurado como "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM", o documento foi rejeitado pela SEFAZ porque não foi informada a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397396375)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397397271)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o tipo de operação utilizado para emissão da nota fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095416087319)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397399191)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397400215)

 Verifique se o CST do IBS e CBS utilizado na operação permite a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095416090135)

 Na seção **''Tributação''** do item, localize o grupo do IBS e CBS, e verifique o campo **''Código de Class. do Crédito Presumido''**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397408791)

 Preencha o campo com um dos valores válidos para a classificação de subapuração do IBS na ZFM.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095397409559)

 Salve as alterações e tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095416091415)

 **CAUSA**

A rejeição ocorre porque, de acordo com as regras de validação da SEFAZ, quando uma nota fiscal é emitida com o **Tipo de Nota Fiscal de Crédito** configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, é obrigatório informar a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM) para cada item da nota. Esta validação está relacionada às regras específicas para operações na Zona Franca de Manaus, conforme estabelecido na Lei Complementar 214/2025, que implementa a Reforma Tributária.

A classificação para subapuração do IBS na ZFM é necessária para o correto cálculo e apropriação do crédito presumido de IBS sobre o saldo devedor nas operações realizadas na Zona Franca de Manaus. Além disso, conforme a regra de validação UB110-10, não é possível repetir o mesmo Tipo de Classificação para o cálculo do crédito presumido na ZFM em mais de um item do documento fiscal quando o Tipo de Nota de Crédito for "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM".