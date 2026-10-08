# Rejeição 865: Total dos pagamentos menor que o total da nota

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32618855110423-Rejei%C3%A7%C3%A3o-865-Total-dos-pagamentos-menor-que-o-total-da-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/32618855110423-Rejei%C3%A7%C3%A3o-865-Total-dos-pagamentos-menor-que-o-total-da-nota)  
> **ID:** `32618855110423` | **Última Atualização:** 2026-07-22T14:30:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32618825090711)

 **MENSAGEM:**

Rejeição 865: Total dos pagamentos menor que o total da nota

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32618825091223)

SOLUÇÃO:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33157417768599)

 Verifique o total da nota (**`**vNF**`**), analisando o XML  da nota.**

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33157441504919)

 ****Revise os campos de pagamento no XML**:

- A tag `<pag>` deve conter todas as formas de pagamento usadas.

- A **soma dos valores de **`**<vPag>**` precisa ser **igual **o valor total da nota.

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33157441506967)

 Ajuste o(s) valor(es) de pagamento**:

Se precisar ajustar, necessário refazer o financeiro da nota. 

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33157417776151)

 **Se houver troco, ele deve estar especificado corretamente na tag `<vTroco>`.

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33157441508759)

 **Observações importantes:**

- A rejeição pode ocorrer por **erro de digitação**, **cálculo incorreto** ou **valor trocado em centavos;**

- Para **NFC-e**, isso é especialmente sensível por causa do pagamento no ato da venda;

- Em alguns casos, o valor dos produtos foi alterado, mas os pagamentos não foram atualizados no XML;

- Existem** duas exceções a Regra de Validação 865**. Veja a seguir, cada uma delas:

  - Esta regra **não se aplica para nota fiscal de Ajuste,** campo finNFe=3 (id:B25) e **para nota fiscal de Devolução finNFe=4 (id:B25)**

  - Esta regra n**ão se aplica quando o campo Meio de Pagamento** (id:YA02, tag:tPag) for igual a 90 (sem pagamento).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32618855105047)

CAUSA:**

Essa rejeição ocorre quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o total do pagamento (Campo: pag / vPag – ID: YA03) for menor que o total da NF-e.

###  

**Exemplo: **

Se o total da nota fiscal (`vNF`) for R$ 12,00 e no XML a soma dos pagamentos é R$ 10,00 (menor que R$ 12,00) gera a rejeição 865:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32618855104279)