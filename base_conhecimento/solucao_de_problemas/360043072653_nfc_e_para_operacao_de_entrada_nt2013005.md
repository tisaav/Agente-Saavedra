# NFC-e para operação de entrada (NT2013/005)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043072653-NFC-e-para-opera%C3%A7%C3%A3o-de-entrada-NT2013-005](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043072653-NFC-e-para-opera%C3%A7%C3%A3o-de-entrada-NT2013-005)  
> **ID:** `360043072653` | **Última Atualização:** 2026-08-08T17:40:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309491533079)

 **MENSAGEM:**

[706 - Rejeição]: NFC-e para operação de entrada (NT2013/005).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309543555095)

 **SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309543556759)

 Acesse a tela ****[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (*Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), *aba: **"Livro Fiscal". **Verifique as CFOPs inseridas para **"Dentro/Fora do Estado":**

- CFOPs de Saída, iniciada por 5, 6, 7, para operações de Venda

- CFOPs de Entrada, iniciada por 1, 2, 3, para operações de Entrada

![CFOPs.png](https://ajuda.sankhya.com.br/hc/article_attachments/14337825968151)

 

Em operações acobertadas por NFC-e é permitido apenas que sejam de saída (Venda). 
Para operações de entrada, opte pela emissão de uma NF-e de Terceiro (modelo 55).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309491542551)

 Acesse a nota novamente, inutilize a numeração e fature novamente a NFC-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309576618007)

 **CAUSA:**

Quando for emitida uma NFC-e e o Tipo da Operação de Entrada (TpNF = 0) será retornado a rejeição.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16309543572247)

 **OBSERVAÇÃO:**

(****[NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)