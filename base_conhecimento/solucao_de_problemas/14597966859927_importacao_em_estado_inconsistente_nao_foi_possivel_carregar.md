# Importação em estado inconsistente. Não foi possível carregar os produtos vinculados para o produto "xxxxxxx", unidade "MIL", referência "SEM GTIN" da empresa "xxx". Por favor, tente reimportar novamente o XML

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14597966859927-Importa%C3%A7%C3%A3o-em-estado-inconsistente-N%C3%A3o-foi-poss%C3%ADvel-carregar-os-produtos-vinculados-para-o-produto-xxxxxxx-unidade-MIL-refer%C3%AAncia-SEM-GTIN-da-empresa-xxx-Por-favor-tente-reimportar-novamente-o-XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/14597966859927-Importa%C3%A7%C3%A3o-em-estado-inconsistente-N%C3%A3o-foi-poss%C3%ADvel-carregar-os-produtos-vinculados-para-o-produto-xxxxxxx-unidade-MIL-refer%C3%AAncia-SEM-GTIN-da-empresa-xxx-Por-favor-tente-reimportar-novamente-o-XML)  
> **ID:** `14597966859927` | **Última Atualização:** 2026-07-22T14:58:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16842157367959)

 MENSAGEM:**

"Erro interno: importação em estado inconsistente. Não foi possível carregar os produtos vinculados para o produto "xxxxxxx", unidade "MIL", referência "SEM GTIN" da empresa "xxx". Por favor, tente reimportar novamente o XML."

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16842199534871)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16842157375895)

 Acesse a tela **Parceiros** -*Configurações » Cadastros » Parceiros*

Aba: "**Fiscal**"

Campo: **"Unidade para considerar na importação"**

- 

Unidade Comercial

- 

Unidade Tributável 

 

Caso o campo esteja diferente de **"Unidade Comercial",** o sistema não consegue identificar o produto.

Para o uso da rotina no sistema, configure o campo **"Unidade"** para considerar na importação:" Flegado para trabalhar com **"Unidade Comercial"** no cadastro do Parceiro, dessa forma, o sistema realiza a validação da importação sem apresentar a mensagem de erro. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14605483800087)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16842157378711)

CAUSA:**

Ao clicar em **"Validar Importação"** após ter atribuídos os produtos na aba **"Produtos Por Parceiro"** na tela **"Portal de Importação de XML"** com a configuração do cadastro do Parceiro diferente de  Unidade Comercial.