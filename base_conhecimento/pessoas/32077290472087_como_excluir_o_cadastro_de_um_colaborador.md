# Como excluir o cadastro de um colaborador?

> **Módulo:** Pessoas+ | **Subseção:** Histórico, Reintegração e Exclusão de Colaboradores  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32077290472087-Como-excluir-o-cadastro-de-um-colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/32077290472087-Como-excluir-o-cadastro-de-um-colaborador)  
> **ID:** `32077290472087` | **Última Atualização:** 2026-09-27T14:37:31Z

---

**Módulo:** Pessoal+
**Caminho de acesso: **Pessoal+ > Cadastros > Configuração Funcionários 
**ID da Tela: **br.com.sankhya.cadastro.funcionarios

 

O sistema **só permite excluir o cadastro** se o colaborador **não tiver nenhum movimento ou vínculo ativo**.

Observe o que é necessário para conseguir excluir:

- 

o colaborador **não pode ter nenhuma folha calculada**;

- 

**não pode ter ocorrências lançadas**, como afastamentos. Se existir apenas uma ocorrência cadastrada no parâmetro **Cód. Hist. Ocorr. p/ Mudança de Cargo (LOTACAO) - ****FPHISTLOTACAO**, a exclusão será permitida;

- 

**não pode ter convocações** de trabalhador intermitente;

- 

**não pode ter lançamentos de movimento** (valores, verbas);

- 

**não pode ter registros de ponto**;

- 

**não pode ter CAT registrada** (Comunicação de Acidente de Trabalho);

- 

**não pode ter ambiente de trabalho vinculado** ao cadastro;

- 

**não pode ter ASO **(Atestado de Saúde Ocupacional) cadastrado.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445001836695)

 Se os eventos de admissão (S-2190 ou S-2200) já tiverem sido enviados ao eSocial, o sistema **exclui esses eventos automaticamente** ao excluir o cadastro do funcionário.

Para excluir o cadastro, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445001839767)

  Verifique a referência da empresa na tela **Empresa da Folha de Pagamento** (Pessoal+ > Preferências) > aba **Informações Gerais** > campo **Data Referência**. 

A exclusão só funciona se a empresa estiver na **referência correta (mês da admissão)**.

![data-referencia-exclusao-admissao.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445015445143)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445015446551)

 Após ajustar a data de referência conforme o mês da admissão, acesse a tela **Configuração Funcionários **(Pessoal+ > Cadastros) para excluir tudo o que estiver vinculado ao colaborador:

- aba **Ambientes de Trabalho:** caso tenha algum ambiente cadastrado, deverá excluí-lo por meio do botão **Excluir**.

![excluir-ambtrab-exclusao-funcionario.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445001853719)

- aba **Dependentes**: exclua todos os dependentes cadastrados clicando no botão **Excluir**.

![excluirdep-exclusaofuncionario.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445213802775)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445764522391)

  Em seguida, acesse a tela **Atestado de Saúde Ocupacional (ASO) **(Pessoal+ > Cadastros)** **e, caso tenha algum exame cadastrado para o funcionário, deverá excluí-lo por meio do botão **Excluir ASO**.

![excluirASO-exclusaofuncionario.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445777811991)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445881363863)

 Agora, retorne à tela **Configuração Funcionários **e** **acione o botão **Excluir**.

![excluir-funcionario.png](https://ajuda.sankhya.com.br/hc/article_attachments/32077597523863)

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37445001836695)

 Caso apareça a mensagem: ***"Não será possível excluir o cadastro. Motivo: há eventos periódicos enviados"***

Significa que a referência está divergente da Central do eSocial. Dessa forma, para conseguir excluir a admissão, acesse a tela **Central do eSocial** e reabra a referência através do menu **Finalização**.

![reabrireventos-exclusaofuncionarios.png](https://ajuda.sankhya.com.br/hc/article_attachments/37447042226199)