# 303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35298216515863-303-Rejei%C3%A7%C3%A3o-Dados-banc%C3%A1rios-e-de-pagamento-devem-ser-informados-para-TAC-e-equiparado-a-TAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/35298216515863-303-Rejei%C3%A7%C3%A3o-Dados-banc%C3%A1rios-e-de-pagamento-devem-ser-informados-para-TAC-e-equiparado-a-TAC)  
> **ID:** `35298216515863` | **Última Atualização:** 2026-07-22T14:25:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35298170772247)

 **MENSAGEM:**

303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35298216502679)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304943365911)

 Acesse a tela de **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), em seguida, abra a viagem que está sendo apresentada a rejeição.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304943366807)

 Depois, na viagem em questão, vá até a aba** "MDF-e"**, sub aba **"Pagamento de Frete", **em seguida, sub aba **"Geral" e** preencha as informações referente ao pagamento do frete, conforme exemplo abaixo: 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35298216505623)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304943368983)

 Importante**: caso seja** informado a forma de pagamento "A prazo", preencha os dados da aba "Informações do Pagamento a Prazo".**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35298170777239)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35298170778391)

 

**Após o preencimento dessas informações, no arquivo XML do MDF-e  será gerado o grupo de Tags <infPag> e <infBanc>.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35298216508439)

CAUSA:**

A rejeição acontece se o grupo de** informações de pagamento (infPag) e informações bancárias (infBanc) não tiverem sido informados** nos casos em que:

- O **modal for rodoviário**;

- E for **informado **o RNTRC (registro da ANTT), do **emitente **ou do **proprietário **do **veículo**;

- E essa pessoa for um **TAC ou Equiparado a TAC** (segundo o cadastro na ANTT),

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35333279531287)

 Para **mais informações sobre os ajustes necessários para adequação à Nota Técnica 2025.001 v1.02** acesse o artigo: ****[Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)


---

### 🔗 Links e Referências Internas:

- [Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)