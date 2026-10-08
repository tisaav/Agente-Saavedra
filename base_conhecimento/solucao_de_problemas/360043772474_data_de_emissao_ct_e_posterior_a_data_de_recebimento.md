# Data de emissão CT-e posterior a data de recebimento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772474-Data-de-emiss%C3%A3o-CT-e-posterior-a-data-de-recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772474-Data-de-emiss%C3%A3o-CT-e-posterior-a-data-de-recebimento)  
> **ID:** `360043772474` | **Última Atualização:** 2026-07-22T15:59:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863455511)

 MENSAGEM:**

[212 - Rejeição]: Data de emissão CT-e posterior a data de recebimento.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863458711)

 SOLUÇÃO:**

Existem duas situações que podem ocorrer esta mensagem:

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863462167)

 Suponhamos a emissão de um CT-e no dia 15/01/2020 com horário de emissão igual à 15:00:00 (GMT -03:00). Na SEFAZ Estadual, considere o horário local 14:50:00 (GMT -03:00). Como o horário de emissão do respectivo conhecimento de transporte é maior que o horário da SEFAZ, no momento de recebimento do documento, este será rejeitado.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863462167)

 A segunda situação recorrente para essa validação são os períodos de início/fim do horário de verão. Em alguns Estados o fuso horário da SEFAZ é alterado  para o 'GMT -02:00', mas no sistema emissor não é realizada essa alteração e continua sendo usado o 'GMT -03:00'. Quando a CT-e chega no ambiente autorizador da SEFAZ, a rejeição ocorre.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458125925399)

 Dessa forma, aplique as soluções abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863466519)

 Verifique a data/Hora de emissão do CT-e e informe uma data/hora de emissão menor ou igual ao horário local da SEFAZ autorizadora.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454879061911)

 Verifique se o horário do servidor está sincronizado com o horário da SEFAZ do seu Estado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454863470359)

 Feito o ajuste, reenvie o CT-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16454879066775)

 CAUSA:**

Quando for emitido um CT-e com Data/Hora de Emissão maior que a Data/Hora da Sefaz, no momento da recepção do documento será retornado a rejeição.