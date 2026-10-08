# Liberação de Ocorrências

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613294-Libera%C3%A7%C3%A3o-de-Ocorr%C3%AAncias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613294-Libera%C3%A7%C3%A3o-de-Ocorr%C3%AAncias)  
> **ID:** `360044613294` | **Última Atualização:** 2026-07-29T14:14:41Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311516353687)

 Módulo: **WMS > Rotinas
```

A rotina de Liberação de Ocorrências tem a finalidade de permitir a liberação ou o cancelamento de uma solicitação de liberação de ocorrência.

![LO01.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085273174)

Assim, na grade são apresentadas as solicitações de acordo com o filtro.

**Observação:** é obrigatório o uso de pelo menos um dos filtros; o uso desse filtro será necessário para evitar o carregamento de um número muito grande de solicitações.

Para realizar a Liberação da Ocorrências, acione o botão **"Liberar"** (localizado no alto da tela) ou executar um duplo clique no registro.

**Importante:** o parâmetro **"Configuração de registro de ocorrências do WMS - WMSREGOCOR"** do tipo lista com as opções: **"Nunca"**, **"Sempre"** e **"Em caso de Corte"**, influencia nesta rotina da seguinte forma:

- 
**Nunca:** Com esta opção selecionada, o comportamento será da mesma forma que hoje, permitindo lançar ocorrência de estoque durante as tarefas sem restrições não gerando liberação de ocorrência.

- 
**Sempre:** Selecionando esta opção, antes de processar a ocorrência de estoque, será gerada uma solicitação de ocorrência em estado **"Pendente"**, que deverá ser liberada antes de continuar com a execução da tarefa. Quando uma tarefa estiver com uma solicitação de liberação em estado Pendente, ela não será mais procurada pelo Coletor de Dados enquanto não for liberada.

- 
**Em caso de Corte:** Por meio desta, apenas será gerada a solicitação de liberação caso a ocorrência lançada for de gerar corte na nota.

**Nota:** estas solicitações somente serão geradas quando relacionadas à uma tarefa, ou seja, não será possível lançá-las como uma ocorrência de avaria pela função **"Avaria"** do menu principal do Coletor do WMS.

Nesta tela, será possível também visualizar na grade os dados referentes ao endereço no qual foram lançadas as ocorrências no coletor, através das colunas **"Descrição (Endereço de Origem)"**, **"End. Reduzido"** e **"Endereço"**.

Quando a marcação **"Mostrar solicitações concluídas" **for habilitada,** **possibilitará a consulta de liberações já realizadas. Assim, a marcação **"Pendentes"** localizada logo abaixo, será desabilitada. Você também poderá pesquisar por liberações pendentes ou negadas de tarefas que já estão concluídas.