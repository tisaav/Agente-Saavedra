# The value '' of element 'MunicipioIncidencia' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043649113-The-value-of-element-MunicipioIncidencia-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043649113-The-value-of-element-MunicipioIncidencia-is-not-valid)  
> **ID:** `360043649113` | **Última Atualização:** 2026-07-22T16:04:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118610904343)

MENSAGEM:**

cvc-type.3.1.3: The value '' of element 'MunicipioIncidencia' is not valid.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118636583575)

 SITUAÇÃO:**

Mensagem apresentada na emissão de nota fiscal de serviço eletrônica (NFS-e).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118636586135)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

Para gerar a tag MunicipioIncidencia é necessário que o Código de Tributação do Município esteja preenchido. A regra para o sistema buscar esse valor é a seguinte:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118636597399)

 Primeiro o sistema tenta buscar o valor da tabela de impostos (TGFDIN), considerando o tipo de imposto igual a 4 (ISS), dessa forma será necessário verificar:

- Tela** "Serviços"** (Caminho de acesso: Configurações » Cadastros » Produtos » Serviços)

- Aba **Alíquotas de ISS**, para a respectiva **Cidade** certifique-se que o campo "**Cód.Trib.Municipio"** foi configurado:

 

![servicos5.png](https://ajuda.sankhya.com.br/hc/article_attachments/14640128458135)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118610923415)

 Caso não existam informações para o item 1, o sistema tenta buscar o valor através das 'Configurações de Serviço por Empresa'.

- Tela Serviços (Caminho de acesso: Configurações » Cadastros » Produtos » Serviços)

- Aba **Configurações por Empresa**, campo "**Cód.Trib.Municipio NFS-e":**

 

![servicos6.png](https://ajuda.sankhya.com.br/hc/article_attachments/14640138200215)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118636605079)

 Por fim, caso não esteja configurado em nenhum dos cenários acima, o sistema verifica o campo da aba **Impostos:**

- Tela Serviços (Caminho de acesso: Configurações » Cadastros » Produtos » Serviços)

- Aba Impostos, campo "**Cód.Trib.Municipio NFS-e".**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118636612119)

 CAUSA:**

Mensagem será apresentada quando não informado ou informado valor indevido para a TAG MunicipioIncidencia no XML.