# Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084873-N%C3%A3o-foram-encontrados-documentos-de-venda-devolu%C3%A7%C3%A3o-de-compra-devolu%C3%A7%C3%A3o-de-venda-transfer%C3%AAncia-ou-conhecimento-de-transporte-na-s-ordem-ns-de-carga-o-modelo-de-documento-1-1B-4-8-55-ou-57](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084873-N%C3%A3o-foram-encontrados-documentos-de-venda-devolu%C3%A7%C3%A3o-de-compra-devolu%C3%A7%C3%A3o-de-venda-transfer%C3%AAncia-ou-conhecimento-de-transporte-na-s-ordem-ns-de-carga-o-modelo-de-documento-1-1B-4-8-55-ou-57)  
> **ID:** `360044084873` | **Última Atualização:** 2026-08-10T16:22:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725678103)

 MENSAGEM:**

[COM_E00041] Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57.

[COM_E00043] Não foram encontrados documentos de venda, compra, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725678743)

 SOLUÇÃO:**

Quando se tratar de Nota de Compra, a melhor prática pra gerar a MDF-e é a seguinte:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725681943)

 Efetue o lançamento da nota de Compra, inserindo as informações de Chave e Número da nota - NÃO CONFIRMAR.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725682839)

 Não vincule a Nota de Compra a uma OC (Ordem de Carga).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106741226519)

 Acesse a Rotina: Comercial » Rotinas » Viagens de Transporte (MDF-e) e crie a Viagem.
Na aba: **Geral**, marque o campo: **"Contem documentos de Terceiros [X]**".

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725685143)

 Aba:** MDF-e** » Sub-aba: **Documentos MDF-e**
Pesquise pela Nota de Compra, anteriormente lançado.

Preencha os principais campos da Viagem, necessários e obrigatórios para geração da MDF-e.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725686039)

 Transmita a MDF-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106725690647)

 CAUSA:**

Ocorre quando no Lançamento de uma MDF-e, para uma nota de Compra, não foi marcado a opção que a MDF-e é para Documentos de Terceiros.