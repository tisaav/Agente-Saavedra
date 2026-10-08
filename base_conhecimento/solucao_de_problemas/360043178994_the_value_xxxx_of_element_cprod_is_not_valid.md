# The value 'XXXX 'of element 'cProd' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178994-The-value-XXXX-of-element-cProd-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178994-The-value-XXXX-of-element-cProd-is-not-valid)  
> **ID:** `360043178994` | **Última Atualização:** 2026-07-22T16:02:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148080083735)

 MENSAGEM:**

cvc-pattern-valid: Value 'XXXX ' is not facet-valid with respect to pattern '[!-y]{1}[ -y]{0,}[!-y]{1}|[!-y]{1}' for type '#AnonType_cProdproddetinfNFeTNFe. cvc-type.3.1.3: The value 'XXXX 'of element 'cProd' is not valid.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148066056343)

 SITUAÇÃO:**

Ao realizar  emissão de NF-e pela tela Central de Vendas no SankhyaW, a nota ficará com Status: 'Aguardando Correção'. Acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da rejeição a seguir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148080091543)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148080092567)

 Acesse: tela** "Produtos"** (*Caminho de acesso: Configurações » Cadastros » Produtos*)

- Aba **Impostos** » Campo** "Cód. Produto p/ NF-e/NFC-e/CF-e":**

 

![produtos4.png](https://ajuda.sankhya.com.br/hc/article_attachments/14633770550935)

 

Caso esse esteja definido como "Referência", busque pelo campo** "Referência"** na aba **Geral** e certifique-se que essa informação foi inserida corretamente. Verifique possíveis espaços em branco antes ou após a informação inserida, e existindo apague os mesmos e salve as alterações.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148080097687)

 Realizado ajuste, conforme item anterior, redigite o cabeçalho da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148066075031)

 CAUSA:**

Mensagem apresentada quando enviado na tag <cProd> informações incoerentes com o esperado pela SEFAZ.