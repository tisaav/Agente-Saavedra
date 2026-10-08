# 1136 Rejeição: Não é possível repetir o Tipo de Classificação para o cálculo do crédito presumido na ZFM neste DFe

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099211102487-1136-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-repetir-o-Tipo-de-Classifica%C3%A7%C3%A3o-para-o-c%C3%A1lculo-do-cr%C3%A9dito-presumido-na-ZFM-neste-DFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099211102487-1136-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-repetir-o-Tipo-de-Classifica%C3%A7%C3%A3o-para-o-c%C3%A1lculo-do-cr%C3%A9dito-presumido-na-ZFM-neste-DFe)  
> **ID:** `37099211102487` | **Última Atualização:** 2026-07-22T14:19:55Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099241680279)

 **MENSAGEM**

1136 Rejeição: Não é possível repetir o Tipo de Classificação para o cálculo do crédito presumido na ZFM neste DFe

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099211084439)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) com apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus (ZFM), o documento foi rejeitado porque foram informados dois ou mais itens com o mesmo **Tipo de Classificação para o cálculo do crédito presumido na ZFM** (mesmo valor na tag tpCredPresIBSZFM).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099241692183)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099211086231)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099241693975)

 Na aba **''NF-e/NFC-e/CF-e''**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099241699735)

 Acesse a nota fiscal que está sendo rejeitada e verifique os itens que possuem o grupo de crédito presumido da ZFM.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099211088535)

 Para cada item da nota, certifique-se de que o **tipo de classificação para o cálculo do crédito presumido na ZFM **seja único, não podendo haver repetição do mesmo tipo em diferentes itens da nota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38365261622167)

 Altere os tipos de classificação repetidos, atribuindo um tipo diferente para cada item, conforme a natureza da operação e as regras específicas da Zona Franca de Manaus. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099241702551)

 **CAUSA**

Esta rejeição ocorre porque, de acordo com as regras de validação da Sefaz, quando o **Tipo de Nota de Crédito** é igual a **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, não é permitido que haja dois ou mais itens com o mesmo **Tipo de Classificação para o cálculo do crédito presumido na ZFM** (mesmo valor na tag tpCredPresIBSZFM).

A validação UB110-10 especifica que, para notas fiscais com finalidade de apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM, cada tipo de classificação deve ser único dentro do documento fiscal, garantindo assim a correta aplicação dos benefícios fiscais previstos para a Zona Franca de Manaus, conforme estabelecido na Lei Complementar 214/2025.