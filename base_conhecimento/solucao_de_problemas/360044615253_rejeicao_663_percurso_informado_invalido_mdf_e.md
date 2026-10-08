# Rejeição 663: Percurso informado inválido - MDF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615253-Rejei%C3%A7%C3%A3o-663-Percurso-informado-inv%C3%A1lido-MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615253-Rejei%C3%A7%C3%A3o-663-Percurso-informado-inv%C3%A1lido-MDF-e)  
> **ID:** `360044615253` | **Última Atualização:** 2026-07-22T15:55:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813411557783)

 **MENSAGEM:**

Rejeição 663: Percurso informado inválido - Como resolver?

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32394664745495)

 **SITUAÇÃO 1:**

Foi emitido um MDFe onde o transporte será iniciado no Estado Brasília (DF) e será concluído no Estado do Mato Grosso  (MT). **Os Estados não fazem fronteira e o percurso não foi informado.**

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32394664745495)

 **SITUAÇÃO 2:**

Foi emitido MDFe onde o transporte será iniciado em Minas Gerais e finalizado em São Paulo. **Os Estados são fronteiriços, no entanto foi informado o percurso. **

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813427758103)

SOLUÇÃO:**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/32394666901783)

 Para a **situação 1, **vá até a tela **"Viagens" ***(Comercial » Rotinas » Viagens de Transporte (MDF-e), *selecione a viagem em questão, acesse a aba **"MDF-e", **em seguida, sub aba **"UFs do percurso"** e preencha corretamente o percurso no qual o transporte da mercadoria irá transitar, considerando todos os Estados que estão entre as fronteiras dos Estados início e fim da viagem. No caso da **situação 1**, coloque a UF do Estado de Goiás. 

 

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/32394666901783)

 Para a **situação 2,** vá até a tela Viagens, selecione a viagem em questão, acesse a aba MDF-e, em seguida, sub aba UFs do percurso e remova as UF's que estiverem cadastradas. Pois, os Estados são fronteiriços e suas UF's já foram informadas anteriormente. 

 

![Percurso informado inválido - MDF-e.png](https://ajuda.sankhya.com.br/hc/article_attachments/32405908998551)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813411580183)

CAUSA:**

A rejeição é apresentada quando os **Estados início e fim não fazem fronteira e não foi informado o percurso**. Também, quando os **Estados são fronteiriços e foi informado um percurso. **