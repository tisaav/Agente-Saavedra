# Como importar XML'S contendo itens com "unidades" com mais de 2 caracteres

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052498373-Como-importar-XML-S-contendo-itens-com-unidades-com-mais-de-2-caracteres](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052498373-Como-importar-XML-S-contendo-itens-com-unidades-com-mais-de-2-caracteres)  
> **ID:** `360052498373` | **Última Atualização:** 2026-07-22T15:29:48Z

---

Considere o xml do fornecedor contendo itens com mais de 2(dois) caracteres na sigla de sua unidade, conforme exemplo abaixo:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083297413)

Nesse caso, o XML poderá ser importado normalmente. Visto que, conforme vínculo realizado entre o item do XML com o item correspondente no sistema, a conversão de "Unidade" será realizada. 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18942151806743)

 Como esse vínculo é realizado na Central de Compras?**

- 

![426.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084348514)

- 

![427.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085512813)

- 
- ****

![428.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085512873)

![429.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084348614)

| Ao tentar importar xml com unidade não cadastrada no sistema é apresentada a mensagem:    O quadro 'Cadastre os produtos equivalentes' é apresentado. Neste momento é possível vincular o produto cadastrado no sistema e a unidade correspondente à unidade utilizada no xml, exemplo:    No exemplo será vinculado o produto 'GAI000011' do xml ao produto 'PRODUTO TESTE LU' no sistema, e a unidade PCE do XML para a unidade UN no sistema. Após informar produtos equivalentes no sistema para todos os produtos sem vínculo, deverá clicar em 'Registrar Cód.Prod.do Fornec.'.    Dessa forma ficará registrado como produto equivalente, o registro poderá ser visto no cadastro do produto, aba 'Produtos Equivalentes':  E também no cadastro do parceiro, aba 'Produtos Equivalentes': |
| --- |

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18942158785431)

 **Como esse vínculo é realizado no Portal de Importação de XML?**

 

- 

**

- ****

![430.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084348734)

| No Portal de Importação de xml, ao importar xml com produtos não cadastrados no sistema e ainda não vinculados, é apresentada a mensagem:  Divergências de produtos não encontrados.  Neste caso o vínculo deve ser realizado na aba 'Produtos por Parceiro' (mesmo nos casos onde a unidade do produto no xml contenha mais caracteres do que o cadastrado no sistema para o mesmo produto):     Da mesma forma o vínculo pode ser visto no cadastro do produto e também no cadastro do parceiro aba 'Produtos Equivalentes'. |
| --- |