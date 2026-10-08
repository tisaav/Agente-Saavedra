# Quantidade de Casas Decimais no Valor do Contrato 

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109713-Quantidade-de-Casas-Decimais-no-Valor-do-Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109713-Quantidade-de-Casas-Decimais-no-Valor-do-Contrato)  
> **ID:** `360045109713` | **Última Atualização:** 2026-07-29T13:55:53Z

---

Para que os [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) apresentem os valores na quantidade de casas decimais desejada, realize as seguintes configurações:

**1)** Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#top), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), preencha no campo **"Decimais para o valor" **o número de casas decimais que o sistema aceitará para a quantidade do produto.

![Imagens_ksnip_97_.png](https://ajuda.sankhya.com.br/hc/article_attachments/6606970012823)

**2)** Informe também o campo **"Valor"**, localizado na tela Contratos, aba [Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprodutosservios).

![Imagens_ksnip_98_.png](https://ajuda.sankhya.com.br/hc/article_attachments/6607366283799)

#### ** 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310909598871)

Regras Importantes**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745336291223)

 Nas telas [Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573) e [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654) não serão consideradas as casas decimais em suas respectivas grades. No caso do Faturamento de Contratos, como na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) é levada em consideração a quantidade de casas decimais para valor, na nota virá com a quantidade conforme configurado no campo **"Vlr. Unitário"**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745336291223)

 No Banco de Dados Sql Server tem a limitação do campo para 4 casas decimais, por isso, pode ocorrer a mensagem que o campo não suporta mais do que isso. Trata-se de comportamento do BD.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745336291223)

 Se o produto\serviço estiver configurado com o campo **"Decimal para Valor"** igual a vazio (em branco) o sistema levará em consideração que se trata de duas casas decimais como padrão. Se o campo estiver igual à zero, então será considerado que para este produto\serviço não podem ser aplicadas casas decimais, tornando o valor como inteiro.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745336291223)

 O parâmetro **"Habilitar preço por faixa? - BILFAIXA"** se habilitado será apresentada a aba **"Preços por Faixa"**, na aba de Produtos\Serviços do cadastro de Contratos. Além disso, será considerada duas casas decimais como padrão.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#top)
- [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)
- [Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprodutosservios)
- [Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573)
- [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)