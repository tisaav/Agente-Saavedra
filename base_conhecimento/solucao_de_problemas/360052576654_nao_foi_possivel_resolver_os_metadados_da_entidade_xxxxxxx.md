# Não foi possível resolver os metadados da entidade 'XXXXXXX'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052576654-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-XXXXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052576654-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-XXXXXXX)  
> **ID:** `360052576654` | **Última Atualização:** 2026-09-23T11:32:47Z

---

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43697899767703)

**SITUAÇÃO**

Este erro pode ocorrer ao tentar acessar diferentes telas do sistema após atualização, replicação de base ou instabilidade.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/20951904484887)

**CAUSA**

Este erro ocorre devido a inconsistências nos metadados das tabelas do sistema, causadas por:

- 

**"Falhas no carregamento de metadados de add-ons"**: Comum após atualizações de addons como o **"IMPEX"**, onde entidades específicas não são sincronizadas automaticamente.
 

1. 

**"Campos não inicializados ou customizados"**: O sistema não consegue processar corretamente campos que não foram declarados corretamente ou que foram removidos ou renomeados em atualizações.
 

1. 

**"Campo ausente no banco"**: O campo existe no dicionário, mas não existe na estrutura física da tabela.
 

1. 

**"Módulos desatualizados"**: Versões incompatíveis ou falhas na sincronização de metadados após atualizações de versão.
 

1. 

**"Cache desatualizado"**: Cache de metadados que não foi recarregado após alterações no banco de dados.
 

1. 

**"Sincronização"**: Falhas na sincronização entre o dicionário de dados e as estruturas do banco.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/20951904426775)

**POSSÍVEIS SOLUÇÕES**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/20951904433047)

 Alternativa 1:

- 

Acesse a tela **"Dicionário de Dados"** (Configurações >> Avançado >> Dicionário de Dados).

- 

Identifique na mensagem de erro a instância ou tabela relacionada. No campo de pesquisa, digite o nome da tabela ou o nome da instância.

- 

Selecione o registro na lista, clique nos **"três pontinhos"** e selecione a opção **"Reiniciar esta Unidade de Dados"**.

- 

Aguarde a conclusão do processo de reinicialização dos metadados.

- 

Caso o erro persista, siga para a próxima alternativa.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/20951904460311)

 Alternativa 2:

- 

Se na mensagem de erro apresenta o nome de um campo da tabela, verifique no "modo formulário" se o campo existe no "Dicionário de Dados".

- 

Abra a tela "DBExplorer", busque pela mesma tabela e verifique se o campo existe também.

- 

Se o campo existir no dicionário de dados, mas não no DBExplorer, será necessário criar o campo no banco de dados e depois reiniciar a unidade de dados (passos detalhados na alternativa 1).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43697890574871)

 Alternativa 3:

- 

Se o erro passou a ocorrer, na base de teste, após replicar a base de produção na base de teste, provavelmente ocorre por um dos dois motivos a seguir:
- A base de produção tem addons e a base de teste não tem os mesmos addons
- A versão das bases está muito diferente

1. 

Se for pela falta dos addons, basta instalar na base de teste para que os erros parem de ocorrer. Isso ocorre, pois a replicação da base copia todas as informações do banco de dados, inclusive dos addons, mas a instalação de addons não é feita automaticamente nesse processo.
Se o addon já existe na base de teste, abra a tela "Minhas Soluções" e tente reiniciar o dicionário de dados do addon.

1. 

Se for a versão muito diferente (geralmente a base de teste está atualizada para uma versão mais recente que a produção), pelo WPM, rode a mesma versão da base de teste novamente.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43697899769111)

 Alternativa 4:

Se nenhum dos passos anteriores funcionar, tente limpar cache e reiniciar o sistema. E, caso, mesmo assim, o erro persistir, abra um chamado para seguir para análise técnica.