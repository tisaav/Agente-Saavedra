# Frete FOB exige que a transportadora seja informada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133154-Frete-FOB-exige-que-a-transportadora-seja-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133154-Frete-FOB-exige-que-a-transportadora-seja-informada)  
> **ID:** `360043133154` | **Última Atualização:** 2026-08-11T19:55:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137126521495)

 MENSAGEM:**

[CORE_E02065] Frete FOB exige que a transportadora seja informada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137106442519)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137126524311)

 Quando definido na aba **"Transporte"** do respectivo lançamento o frete: **FOB** [Campo "**CIF/FOB"**] e informar **"Vlr do Frete"** é necessário que o campo** "Parceiro Transportadora"** seja devidamente preenchido.

 

![Frete_FOB_exige_que_a_transportadora_seja_informada.png](https://ajuda.sankhya.com.br/hc/article_attachments/14663590357655)

 

Caso não localize esse campo no lançamento, será necessário inseri-lo através do 'Configurador de layout da nota', para mais detalhes: [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137106446103)

 IMPORTANTE: ** 

Se informar frete **"FOB"**, **"Vlr do Frete"** e **"Parceiro Transportadora"** é necessário informar também data de vencimento para o frete, caso não informe o sistema irá apresentar a mensagem: 

 

Vencimento do frete deve ser maior que a data da negociação menos 30 dias (DD/MM/AAAA).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137106447895)

 CAUSA:**

Quando definido na aba **"Transporte"** do respectivo lançamento o frete: **FOB** [Campo 'CIF/FOB'], o **"Vlr do Frete"** for diferente de zero e o parceiro transportador não for informado, será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)