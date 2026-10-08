# Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/5742198491287-Transporte-n%C3%A3o-%C3%A9-pr%C3%B3prio-por-conta-do-Remetente-e-CNPJ-Base-ou-CPF-do-Transportador-igual-ao-CNPJ-Base-ou-CPF-do-Remetente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742198491287-Transporte-n%C3%A3o-%C3%A9-pr%C3%B3prio-por-conta-do-Remetente-e-CNPJ-Base-ou-CPF-do-Transportador-igual-ao-CNPJ-Base-ou-CPF-do-Remetente)  
> **ID:** `5742198491287` | **Última Atualização:** 2026-07-22T15:17:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16368152052759)

  MENSAGEM**:

847 - Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16368173008279)

 CAUSA:**

Quando a modalidade do frete for diferente de 3 o CNPJ ou CPF do transportador deve ser diferente do CNPJ ou CPF do transportador. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16368173010071)

 SOLUÇÃO:**

Para a resolução dessa rejeição, siga os passos abaixo.

1. Se for NF-e de saída e Modalidade do Frete <> 3, o CNPJ Base ou CPF do transportador deve ser DIFERENTE do CNPJ Base ou CPF do Remetente.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16368152060951)

 OBSERVAÇÃO:**

Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.

| Se o campo CIF_FOB da TGFCAB estiver igual a C (CIF - Contratação do Frete por conta do Remetente) a tag será modFrete será gerado igual a:modFrete = 0   Se o campo CIF_FOB da TGFCAB estiver igual a T (Terceiros) a tag será modFrete será gerado igual a:modFrete = 2   Se o campo CIF_FOB da TGFCAB estiver igual a S (Sem frete) a tag será modFrete será gerado igual a: modFrete =9   Se o campo CIF_FOB da TGFCAB estiver igual a R (Transp. Próprio Remetente) a tag será modFrete será gerado igual a: modFrete =3   Se o campo CIF_FOB da TGFCAB estiver igual a D (Transp. Próprio Destinatário) a tag será modFrete será gerado igual a:modFrete = 4   Com o campo CIF_FOB diferente das opções acima o sistema gera a tag modFrete igual a 1. Como por exemplo, se o campo CIF_FOB estiver vazio. |
| --- |

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16368152060951)

 OBSERVAÇÃO: **

No faturamento, o sistema copiará a informação constante no campo CIF/FOB do pedido.