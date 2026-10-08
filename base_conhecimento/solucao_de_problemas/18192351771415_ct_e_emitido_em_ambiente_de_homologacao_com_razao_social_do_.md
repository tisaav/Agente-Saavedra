# CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18192351771415-CT-e-emitido-em-ambiente-de-homologa%C3%A7%C3%A3o-com-Raz%C3%A3o-Social-do-remetente-diferente-de-CT-E-EMITIDO-EM-AMBIENTE-DE-HOMOLOGACAO-SEM-VALOR-FISCAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/18192351771415-CT-e-emitido-em-ambiente-de-homologa%C3%A7%C3%A3o-com-Raz%C3%A3o-Social-do-remetente-diferente-de-CT-E-EMITIDO-EM-AMBIENTE-DE-HOMOLOGACAO-SEM-VALOR-FISCAL)  
> **ID:** `18192351771415` | **Última Atualização:** 2026-07-22T14:52:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18192351755287)

 **MENSAGEM:**

Rejeição 646: CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18192336709911)

SOLUÇÃO:**

Deve-se alterar o Nome ou Razão Social do Remetente do CT-e e informar o trecho literal: " **CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL **". Veja a seguir o exemplo corrigido:

-  No XML:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18192229737367)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18192290514711)

CAUSA:**

Quando for emitido um CT-e em Homologação (tpAmb = 2) e o Remetente for informado com a Razão Social (xNome) diferente do trecho literal: “CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL”, será retornado a rejeição "646 - CT-e emitido em ambiente de homologação com Razão Social do remetente diferente de CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL".

 

Exemplo:

Foi emitido um CT-e em Homologação e o Remetente foi informado com a Razão Social "Oobj Tecnologia da Informação Ltda." Nessa situação, o CT-e será rejeitado pelo motivo 646.

-  No XML:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18192333155735)

Veja validação da Sefaz:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18192335745175)