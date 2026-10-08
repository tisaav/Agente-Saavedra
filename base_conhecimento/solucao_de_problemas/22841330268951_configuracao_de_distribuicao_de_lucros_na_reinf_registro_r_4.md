# Configuração de "Distribuição de Lucros" na REINF registro R-4010

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/22841330268951-Configura%C3%A7%C3%A3o-de-Distribui%C3%A7%C3%A3o-de-Lucros-na-REINF-registro-R-4010](https://ajuda.sankhya.com.br/hc/pt-br/articles/22841330268951-Configura%C3%A7%C3%A3o-de-Distribui%C3%A7%C3%A3o-de-Lucros-na-REINF-registro-R-4010)  
> **ID:** `22841330268951` | **Última Atualização:** 2026-07-22T14:48:44Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22841346850967)

SOLUÇÃO:**

Para a geração desse evento, deverá existir pelo menos uma Movimentação Financeira de origem Financeira para um Parceiro Pessoa Física, com o "Código Natureza Rendimento - 12001” informado na aba EFD - REINF da **Movimentação Financeira** *(Financeiro » Rotinas » Movimentação Financeira)*.

 

![Movimentação financeira 18-04.png](https://ajuda.sankhya.com.br/hc/article_attachments/22894255610135)

Necessário que no cadastro do **Tipo de Operação - TOP** *(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)* usado esteja com a marcação "Gerar informações do EFD REINF Grupo 4000?" da aba Impostos habilitada.

 

![Tipos de operação 18-04.png](https://ajuda.sankhya.com.br/hc/article_attachments/22894259767063)

 

Na tela **Códigos de Naturezas de Rendimentos** *(Livros Fiscais » Arquivos » Códigos de Naturezas de Rendimentos) * Efetue a marcação "Gera sem tributação?"

 

![códigos de natureza 18-04.png](https://ajuda.sankhya.com.br/hc/article_attachments/22894255645335)

 

Caso e empresa opte por geração trimestral se atentar a configuração abaixo:
 
Na tela **Empresa** *(Comercial » Preferências » Empresa)* aba EFD - REINF por meio da marcação "Gerar Lucros e Dividendos com periodicidade trimestral", os rendimentos classificados com o código de  natureza de rendimento 12001 serão gerados na referência subsequente ao trimestre no qual os documentos foram lançados.
Desse modo, considere o exemplo:
Na referência 01/2024 irá contemplar o 4° trimestre/2023, desde que tenham sido registrados com o código de natureza de rendimento 12001 e a data de negociação esteja compreendida entre 01/10/2023 e 31/12/2023.
 
Porém, lembre-se que, para habilitar essa marcação, o parâmetro **"GERREINFJAVA - Habilita geração do REINF através do Java?" **deve ser ligado.

 

**Importante:** 

As versões que contemplam a implementação do parâmetro **"GERREINFJAVA - Habilita geração do REINF através do Java?"** e do campo Gerar Lucros e Dividendos com periodicidade trimestral são as seguintes:
 

**4.24b95 e superiores**

**4.25b44 e superiores**

 

Com a marcação Gerar Lucros e Dividendos com periodicidade trimestral desabilitada e/ou com o parâmetro **"GERREINFJAVA - Habilita geração do REINF através do Java?" **desligado, a geração será realizada de forma mensal.