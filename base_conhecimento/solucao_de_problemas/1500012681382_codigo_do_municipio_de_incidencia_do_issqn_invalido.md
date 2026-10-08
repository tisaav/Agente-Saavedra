# Código do município de incidência do ISSQN inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012681382-C%C3%B3digo-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012681382-C%C3%B3digo-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-inv%C3%A1lido)  
> **ID:** `1500012681382` | **Última Atualização:** 2026-07-22T15:24:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337229304087)

 MENSAGEM**:

Ao gerar lote NFS-e para Vitória - ES apresenta erro, E309: Código do município de incidência do ISSQN inválido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337207881495)

 SOLUÇÃO:**

Informe o código do município de incidência do ISSQN com sete caracteres, conforme a tabela de municípios do IBGE.

Para o município de Vitória-ES a tag 'MunicipioIncidencia' deve constar com as mesmas informações da tag 'CodigoMunicipio'.

- A tag 'CodigoMunicipio' é configurado no cadastro de cidade em "Mun. Domicílio fiscal".

- A tag 'MunicipioIncidencia' é obtida no sistema pela seguinte regra:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337207885079)

 Primeiro o sistema tenta buscar o valor da tabela de impostos (TGFDIN), considerando o tipo de imposto igual a 4 (ISS), dessa forma verifique:

- Tela 'Serviços' (Configurações » Cadastros » Serviços)

- Aba **"Alíquotas de ISS"**, para a respectiva 'Cidade' certifique-se que o campo **'Cód.Trib.Municipio'** foi configurado:

-  

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15071554463255)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337207888407)

 Caso não existam informações para o item 1, o sistema tentar buscar o valor através das 'Configurações de Serviço por Empresa'.

- Tela **"Serviços"** *(Caminho de acesso: Configurações » Cadastros » Serviços)*

- Aba **"Configurações por Empresa"**, campo **"Cód.Trib.Municipio NFS-e":**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15071616279447)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337229331223)

 Por fim, caso não esteja configurado em nenhum dos cenários acima, o sistema verifica o campo da aba **"Impostos"**:

- Tela **"Serviços"** *(Caminho de acesso: Configurações » Cadastros » Serviços)*

- Aba **"Impostos"**, campo **'Cód.Trib.Municipio NFS-e'.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16337229334295)

 CAUSA:**

Ocorre normalmente para notas enviadas a prefeitura de Vitória/ES, Porém, pode ocorrer para outras prefeituras que exijam a TAG, 'MunicipioIncidencia' no XML.