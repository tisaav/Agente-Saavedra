# Esta nota não tem produtos que estejam fora da promoção para poder dar desconto

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042872414-Esta-nota-n%C3%A3o-tem-produtos-que-estejam-fora-da-promo%C3%A7%C3%A3o-para-poder-dar-desconto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042872414-Esta-nota-n%C3%A3o-tem-produtos-que-estejam-fora-da-promo%C3%A7%C3%A3o-para-poder-dar-desconto)  
> **ID:** `360042872414` | **Última Atualização:** 2026-07-22T16:05:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108779284631)

 MENSAGEM:**

[CORE_E02362] Esta nota não tem produtos que estejam fora da promoção para poder dar desconto.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108779287063)

 SOLUÇÃO:**

Quando o parâmetro **"VALDESCMAX - Valida desconto máximo"** estiver definido com a opção "**VALIDA E NÃO ACEITA (EXCETO PROD. PROMOÇÃO)"** e o produto inserido no lançamento fizer parte de uma regra de **Desconto Promocional**, ao aplicar um desconto no rodapé da nota, esse não será permitido. Visto que não existirá no lançamento produtos para rateio deste desconto.

Dessa forma, avalie junto ao responsável pela definição/parametrização de desconto promocional em sua empresa, se a configuração do parâmetro encontra-se coerente com o processo. Em caso negativo, realize os devidos ajustes.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108733542167)

** Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** *(Caminho de acesso: Configurações » Avançado), *Chave VALDESCMAX:

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14532763472407)

 

Caso o parâmetro esteja adequado, o desconto aplicado no rodapé não será permitido, sendo necessário retirar esse valor de seu lançamento. Após esse ajuste, teste a confirmação da nota.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108733547799)

 OBSERVAÇÃO:**

No cenário acima, o desconto no rodapé será permitido apenas se houver outros itens na nota, não vinculados a descontos promocionais, que permitam o rateio do desconto.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108779297559)

 CAUSA:**

Quando o parâmetro VALDESCMAX estiver definido com a opção VALIDA E NÃO ACEITA (EXCETO PROD. PROMOÇÃO) e o produto inserido no lançamento fizer parte de uma regra de Desconto Promocional, ao aplicar um desconto no rodapé da nota, esse não será permitido.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)