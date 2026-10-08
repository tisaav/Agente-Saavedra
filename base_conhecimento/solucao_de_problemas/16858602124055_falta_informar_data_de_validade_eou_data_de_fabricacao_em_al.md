# Falta informar Data de Validade e/ou Data de Fabricação em alguns produtos

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16858602124055-Falta-informar-Data-de-Validade-e-ou-Data-de-Fabrica%C3%A7%C3%A3o-em-alguns-produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/16858602124055-Falta-informar-Data-de-Validade-e-ou-Data-de-Fabrica%C3%A7%C3%A3o-em-alguns-produtos)  
> **ID:** `16858602124055` | **Última Atualização:** 2026-07-22T14:54:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16858638135319)

  MENSAGEM:**

[CORE_E04788] Falta informar Data de Validade e/ou Data de Fabricação em alguns produtos.
[ { Produto: xx, Lote: xxx} ].

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16858646476055)

 CAUSA:**

A solicitação de 'Data de Fabricação' e 'Data de Validade' acontecerá nas seguintes condições:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16858602118167)

 Tela **Preferência** *(Configurações » Avançado)*, parâmetros:

- 
**Usar data de Fabricação junto com Lote? - LOTEDTFAB** 

- 
**Usar data de validade junto com Lote? - LOTEDTVAL** 

- 
** Informações adicionais para** **Lotes? - LOTEINFO**

Se LIGADOS, para cada produto, as marcações detalhadas abaixo (*Utiliza data de Fabricação  e Utiliza data de Validade***) **serão consideradas, e as datas de fabricação/validade exigidas:

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16858618262423)

 Tela 'Produtos' *(Configurações » Cadastros » Produtos):*

- **Utiliza data de Fabricação**

- **Utiliza data de Validade**

Os campos "Utiliza data de Fabricação" e "Utiliza data de Validade" estão relacionados ao controle de estoque de produtos; posto isto, se aplicam à produtos que utilizam controle adicional por número de lote e/ou data de validade (aba Medidas e Estoque, sub-aba Controle Adicional).

**

![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/16858625048087)

 IMPORTANTE:**

Quando o parâmetro **"Usar data val. fab. junto com Lote, por produto? - LOTEDTVALFABPRO"** estiver ligado, o sistema exigirá as validações das marcações Utiliza data de Fabricação e Utiliza data de Validade.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16866260273431)

 Tela **Produtos** (*Configurações » Cadastros » Produtos)

*Na aba **Estoque**, pode existir linhas de estoque sem Data de Validade e Data de Fabricação para o Lote apresentado na mensagem de erro. Deve ser avaliado o motivo de controlar data de validade e fabricação e não ter essa informação para o determinado Lote, assim tomando a melhor decisão naquele caso (exclusão, edição,...).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16858602119447)

 SOLUÇÃO:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16858618263959)

 Verifique para o produto apresentado na mensagem da nota, o preenchimento das informações 'Data de validade' e 'Data de fabricação':

- Central de Notas  >> Itens >> Outras Opções >> **Informações de Controle Adicional**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16858625049495)