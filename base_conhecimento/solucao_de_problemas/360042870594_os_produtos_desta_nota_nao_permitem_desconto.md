# Os produtos desta nota não permitem desconto

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870594-Os-produtos-desta-nota-n%C3%A3o-permitem-desconto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870594-Os-produtos-desta-nota-n%C3%A3o-permitem-desconto)  
> **ID:** `360042870594` | **Última Atualização:** 2026-07-22T16:05:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114018040215)

 MENSAGEM:**

[CORE_E02700] Os produtos desta nota não permitem desconto.

[COM_E00223]  Os produtos desta nota não permitem desconto

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114018044695)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986801815)

 Acesse: Configurações » Avançado » Preferências

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114018058903)

 **Analise a configuração atual dos 3 parâmetros abaixo:

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986810007)

"DISTJDCONF - Distribuir desc. na confirmação da nota?"**

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986810007)

"DISTDESCNFE - Distribuir desc.na confirmação da NFE?"**

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986810007)

"VALDESCMAX - Valida desconto máximo."**

Com os parâmetros "**DISTJDCONF ou DISTDESCNFE" **ligados, o sistema tentará distribuir o desconto do rodapé da nota entre os itens, obedecendo o % de desconto máximo do cadastro de produtos.

Caso exceda e o parâmetro VALDESCMAX esteja **desligado, **a mensagem será apresentada, sendo necessário aplicar as duas soluções listadas nos itens 3 e 4 abaixo:

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986812823)

 Ajuste o parâmetro VALDESCMAX para **diferente** de** "Não Valida"**.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114018075031)

 **No cadastro de** "[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** *(Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)* para todos os itens da nota, ajuste a informação contida no campo **"%Desconto Máximo", **aba **"Venda" **para um percentual que atenda a necessidade de aplicação de desconto atual.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14557321385879)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114018079511)

 Por fim, proceda com uma nova tentativa de confirmação da respectiva NF-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113986824599)

 CAUSA:**

Ocorre quando o(s) produto(s) não estão devidamente configurados para receber desconto, distribuídos pela confirmação da nota.


---

### 🔗 Links e Referências Internas:

- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)