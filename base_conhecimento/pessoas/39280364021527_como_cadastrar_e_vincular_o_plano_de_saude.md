# Como cadastrar e vincular o plano de saúde?

> **Módulo:** Pessoas+ | **Subseção:** Plano de Saúde  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Como-cadastrar-e-vincular-o-plano-de-sa%C3%BAde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Como-cadastrar-e-vincular-o-plano-de-sa%C3%BAde)  
> **ID:** `39280364021527` | **Última Atualização:** 2026-09-27T18:35:37Z

---

**Módulo: **Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela: **br.com.sankhya.rh.PlanoSaude

## **Sumário**

[Descrição e Usabilidade](#h_01KMJC83K6BP6H94TT8Z7WBAGT)

1. [Descrição da Funcionalidade](#h_01KMJC5K8C883Z1YXATRCC3A7H)

1. [Pré-requisitos](#h_01KMJC5K8G983B3M7HWNS9GKQ6)

1. 
[Jornada de Uso](#h_01KMJC5K8KA22CXV6V6NPAZJY7)

  - [Cadastrar Operadora de Plano de Saúde](#h_01KMJR7YQ3R89C7A962WQHRT5R)

  - [Vincular Plano ao Funcionário (Titular)](#h_01KMJR83VVCEQSYYCEXCWH6PDB)

  - [Vincular Plano aos Dependentes](#h_01KMJR896VGGX9V81M6AGV6R1G)

1. [Pontos de Atenção](#h_01KMJC5K9PCT785VCH5VPXRQ0N)

1. [Dicas de Usabilidade](#h_01KMJC5K9SRAM6ZDSE3J86Y36F)

[Perguntas Frequentes (FAQ)](#h_01KMJC5K9VRNFM91E0NDCEWX3N)

[Artigos Relacionados](#h_01KMJC5KA5XQ78W64J9VCQ5350)

 

## **Descrição e Usabilidade**

O cadastro de **Plano de Saúde** é responsável por registrar os convênios médicos e odontológicos disponibilizados pela empresa aos colaboradores, garantindo que os valores sejam corretamente considerados nos cálculos da folha de pagamento.

Por meio desse cadastro, o sistema consegue:

- Aplicar descontos de plano de saúde em folha;

- Controlar participação da empresa e do colaborador;

- Gerenciar reembolsos;

- Vincular planos a titulares e dependentes;

- Garantir consistência das informações para encargos e relatórios.

Esse processo é essencial para evitar divergências nos descontos, garantir transparência ao colaborador e manter a conformidade com regras trabalhistas e acordos coletivos.

### **1. Descrição da Funcionalidade**

Utilize esta rotina para cadastrar os convênios médicos e odontológicos oferecidos pela empresa e realizar o vínculo com colaboradores e dependentes.

Esse cadastro é utilizado para:

- gerar descontos automáticos na folha;

- controlar participação da empresa;

- calcular valores por faixa;

- considerar dependentes no benefício;

- garantir valores corretos em relatórios e DIRF. 

**⚠️**O cadastro do plano deve ser realizado antes do vínculo no colaborador.

### **2. Pré-requisitos**

Antes de realizar o cadastro, verifique:

- Acesso liberado à tela **Plano de Saúde**, concedido pelo usuário administrador do sistema por meio da rotina **Acessos** (Configurações > Controle de Acessos);

- Eventos de desconto e reembolso de plano de saúde previamente cadastrados:

  - 

os eventos utilizados para desconto do plano de saúde devem possuir configuração válida para o eSocial:

    - Natureza da Rubrica: **9219**, **1405** ou **9299**;

    - Incidência de IRRF (codIncIRRF): **09**, **67** ou **9067**.

- Dados do plano em mãos (CNPJ, registro ANS, tipo de plano);

- Se a opção **Possui Plano de Saúde** está marcada na aba **Contrato** do **cadastro do colaborador**. Sem essa marcação, o sistema bloqueia a inclusão do plano.

- 
[Tabela de Faixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519) criada, quando o plano utilizar valor por idade ou salário.

### **3. Jornada de Uso**

#### 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315081157527)

 **Cadastrar Operadora de Plano de Saúde**

![planosaude-unimed.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280869784471)

1. Acesse a tela **Plano de Saúde** (Pessoal+ > Cadastros).

1. Clique em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280444745367)

 **Cadastrar Plano de Saúde****.**

1. Preencha:

  - 
**Código** (controle interno);

  - 
**Razão Social** (nome do plano).

1. Na aba **Geral**, informe:

  - 
**CNPJ**;

  - 
**Registro na ANS**;

  - 
**Tipo** de plano;

  - 

**Eventos de desconto**;

⚠️ Somente eventos de desconto para o colaborador.

  - 
**Eventos de reembolso** (se houver);

  - 
**Eventos de reembolso anterior** (se aplicável);

  - 
**Evento de reembolso anterior**.

⚠️ Informe apenas o **código numérico dos eventos**, sem descrição ou caractere especial.

1. Clique em 

![botão Salvar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/39280444747159)

 **Salvar [F7]**.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39290089307415)

 **Validações realizadas pelo sistema**

Ao informar os eventos de desconto do plano de saúde, o sistema valida automaticamente se o evento possui configuração compatível com o eSocial.

São aceitos apenas eventos que possuam:

- Natureza da Rubrica: **9219**, **1405** ou **9299**;

- Incidência de IRRF (codIncIRRF): **09**, **67** ou **9067**.

Caso o evento não atenda a essas configurações, será exibida a mensagem:

***"Não foi possível vincular o evento ao Plano de Saúde.***

***O evento [Código do Evento] não possui configuração válida para o eSocial.***

***Para ser utilizado, o evento deve ter:***

- ***Natureza da rubrica: 9219, 1405 ou 9299;***

- ***Incidência de IRRF (codIncIRRF): 09, 67 ou 9067.***

***Revise a configuração do evento ou informe outro evento compatível."***

 

O sistema também valida a unicidade dos eventos de desconto entre os planos cadastrados.

Se o evento já estiver vinculado a outro plano de saúde com CNPJ e/ou registro ANS diferentes, o cadastro será bloqueado para evitar inconsistências no eSocial e no Informe de Rendimentos.

Mensagem apresentada:

***"O evento [Código do Evento] já está vinculado ao Plano de Saúde [Código/Nome do Plano], CNPJ [CNPJ].***

***Para este plano, utilize um evento de desconto diferente."***

 

O registro ANS também deve ser exclusivo para cada operadora.

Caso o código ANS informado já esteja vinculado a outro plano de saúde com CNPJ diferente, a gravação será impedida.

Mensagem apresentada:

***"O código de ANS [XXX] já está vinculado ao Plano de Saúde [Código/Nome do Plano], CNPJ [XXX].***

***Para continuar, informe um código de ANS diferente."***

 

#### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315084293783)

 **Vincular Plano ao Funcionário (Titular)**

O vínculo de Plano de Saúde nessa tela permite associar o colaborador a um plano de saúde com suas respectivas faixas etárias, percentuais de contribuição e valores. 

O sistema utiliza as Tabelas de Faixas para calcular automaticamente o valor do plano baseado na idade e na faixa de rendimento do funcionário.

1. Acesse o cadastro do colaborador na tela **Configuração Funcionários** (Pessoal+ > Cadastros).

1. 

Na aba **Contrato**, marque a opção **Possui Plano de Saúde**.

![planodesaude-contrato.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280681672727)

1. 

Acesse a aba **Plano de Saúde**.

![planosaude-funcionario.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280980228375)

1. Clique em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280444745367)

 **Cadastrar Plano de Saúde**.

1. O campo **Sequência** será preenchido automaticamente com o valor **"0"**, que significa que esse plano é do colaborador/titular.

1. Preencha:

  - 
**Código do Convênio**: cadastrado previamente na tela **Plano de Saúde**.

  - 
**Referência Inicial: **início de vigência do vínculo do colaborador com o plano de saúde.

  - 

**Referência Final** (opcional): define até quando o plano será descontado (ex: rescisão, mudança de plano).

Se deixado em branco, assume que plano é vigente indefinidamente.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39290089307415)

Ao incluir **um novo plano de saúde** com o **mesmo código do convênio** para o colaborador, sem informar a **Referência Final** no registro anterior, o sistema realizará o **encerramento automático** do plano anterior.

****

********[lançamento de eventos de plano de saúde na folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/38299661897239)

| ℹ️ Nota As datas de Referência Inicial e Referência Final são usadas também para validar o . Um lançamento com referência anterior à Referência Inicial ou posterior à Referência Final será bloqueado pelo sistema. Por isso, mantenha essas datas sempre atualizadas para evitar bloqueios indevidos. |
| --- |

⚠️ Os campos **Tabela de Faixa**,** ****Código da Faixa **e** ****Faixa do Provento** são preenchidos em planos de saúde que utiliza ****[Tabela de Faixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)**.**

  1. 
**Tabela de Faixa**: referencia a tabela de faixas etárias/rendimento configurada para o plano.

  1. 
**Código da Faixa**: identifica a faixa específica dentro da tabela de faixas e determina o valor/percentual a ser aplicado na folha.

  1. 

**Percentual da Empresa**: valor percentual da contribuição que a empresa arcará.

Se deixar vazio, assume padrão configurado no plano.

  1. 

**Faixa do Provento**: define a faixa de rendimento mensal do colaborador.

Utilizada para planos com precificação diferenciada por salário.

    - Se o plano é variável por salário, campo é obrigatório;

    - Se o plano é fixo por idade, campo fica desabilitado.

1. A seção **Valor Plano Saúde** é preenchida automaticamente com a **Referência**, **Valor do Plano **e **Tipo de Folha**.

1. Salve o cadastro.

#### 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315081158807)

 **Vincular Plano aos Dependentes**

1. 

Na aba **Dependentes**, acesse a sub-aba **Plano de Saúde**.

![planodesaude-dependentes.png](https://ajuda.sankhya.com.br/hc/article_attachments/39283668015127)

1. Certifique-se de que a opção **Dependente de Convênio Médico** está ativada na sub-aba **Geral **da aba **Dependentes**.

1. Com o dependente já cadastrado, clique em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39280444745367)

 **Cadastrar Plano de Saúde**.

1. Preencha:

  - 
**Código do Convênio**;

  - 
**Referência Inicial**;

  - 
**Referência Final** (opcional);

  - 
**Tabela de Faixa**;

  - 
**Código da Faixa**;

  - 
**Percentual da Empresa**;

  - 
**Faixa do Provento**.

1. 

Salve o cadastro.

⚠️ Os campos **Tabela de Faixa**,** ****Código da Faixa **e** ****Faixa do Provento** são preenchidos em planos de saúde que utiliza ****[Tabela de Faixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)**.**

### **4. Pontos de Atenção**

- A opção **Possui Plano de Saúde** é obrigatória para vincular o plano.

- Os eventos devem ser informados **apenas com código numérico**.

- O desconto inicia a partir da **Referência Inicial** informada no vínculo.

- 

Se um evento de plano de saúde for lançado para um colaborador ou dependente que ainda não tem cadastro para aquele convênio, o sistema cria esse cadastro automaticamente, usando a referência do lançamento como data de início de vigência. 

Isso só acontece quando o evento está vinculado a um único convênio. Se o evento estiver vinculado a mais de um convênio, o cadastro automático não é feito, e as demais validações de lançamento seguem normalmente.

- Um mesmo evento de desconto **não** pode ser utilizado em planos de saúde distintos. 

- O registro **ANS** deve ser **exclusivo** para cada operadora de plano de saúde. 

- O sistema realiza validações preventivas para evitar rejeições no eSocial e inconsistências no Informe de Rendimentos. 

- Caso uma validação seja acionada, a alteração não será salva e o cadastro permanecerá com os dados originais.

- 

**Em caso de desconto de plano de saúde zerado ou não aplicado ao colaborador**, confira o campo **Percentual da Empresa** no cadastro do dependente (ou do titular). Se esse campo estiver preenchido com **100%**, o sistema entende que a empresa custeia integralmente o plano, e por isso não desconta nenhum valor do colaborador. Esse é o motivo mais comum quando o desconto do plano de saúde aparece zerado na folha.

- 

**Se um desconto indevido já foi calculado** e precisa ser estornado, siga esta ordem:

- Exclua o cálculo da folha em que o desconto indevido ocorreu.

- Corrija o campo Percentual Empresa no cadastro do dependente (ou do titular).

- Recalcule a folha.

- 

Corrigir o percentual sem excluir o cálculo anterior não resolve o desconto já processado — a ordem dos passos importa.

- Ao cadastrar o mesmo convênio novamente para o colaborador, o sistema pode encerrar automaticamente o vínculo anterior quando ele estiver sem referência final.

- Para realizar a exclusão ou alteração do plano de saúde, **não pode existir folha calculada na referência**.

### **5. Dicas de Usabilidade**

- Utilize descrições claras para facilitar a identificação dos planos.

- Valide os eventos com o time de folha antes de vincular.

- Revise percentuais de participação da empresa e colaborador.

- Utilize corretamente as faixas para automatizar cálculos.

- Sempre confira os valores antes do fechamento da folha.

## **Perguntas Frequentes (FAQ)**

 

**1. O plano não apareceu para o colaborador. O que verificar?**

Confirme se a opção **Possui Plano de Saúde** não está marcada na aba **Contrato** da tela **Configuração Funcionários**.

Sem essa marcação, o sistema bloqueia a inclusão e exibe mensagem de orientação.

**2. Posso informar o nome do evento no cadastro do plano?**

Não. O sistema aceita apenas o **código numérico do evento**, sem descrição ou caracteres especiais.

**3. O desconto não saiu na folha. O que pode ser?**

Verifique se:

- A **referência inicial** está correta;

- Faixa configurada;

- O **tipo de folha** foi informado;

- O plano está vinculado corretamente ao colaborador;

- Os **eventos de desconto** foram configurados.

- Se necessário, utilize o processo de **reprocessamento de plano de saúde** no **Gerenciador de Folhas**.

**4. Qual a diferença entre plano do titular e do dependente?**

- 
**Titular:** sequência automática = 0

- 
**Dependente:** cadastrado na sub-aba específica

Isso garante que os valores sejam tratados corretamente no cálculo.

**5. Posso alterar o valor do plano após já ter sido utilizado?**

Sim, mas o novo valor só será considerado nas próximas competências.

Se a folha já estiver calculada, será necessário recalcular.

**6. O que acontece se eu configurar a faixa ou percentual incorretamente?**

Pode gerar:

- Descontos incorretos;

- Diferenças na folha;

- Retrabalho no fechamento.

Sempre valide essas informações antes de salvar.

**7. É obrigatório informar reembolso?**

Não. Os eventos de reembolso são opcionais e devem ser preenchidos apenas quando a empresa utilizar esse processo.

**8. O dependente não recebeu desconto.**

Verifique se a marcação **Dependente de Convênio Médico** foi ativada na sub-aba **Geral **da aba **Dependentes **no cadastro.

9. **Quando usar tabela de faixa?**

Use quando o plano variar por:

- idade;

- salário;

- categoria;

- coparticipação.

**10. ****Posso utilizar o mesmo evento de desconto em dois planos de saúde diferentes?**

Não. O sistema exige que cada plano de saúde possua seu próprio evento de desconto quando os planos possuírem CNPJ e/ou registro ANS diferentes.

**11. Por que o sistema não permite salvar o evento informado no plano de saúde?**

Verifique se o evento possui configuração válida para o eSocial.

São aceitos apenas eventos com:

- Natureza da Rubrica: 9219, 1405 ou 9299;

- Incidência de IRRF (codIncIRRF): 09, 67 ou 9067.

**12. Posso utilizar o mesmo código ANS em operadoras diferentes?**

Não. O código ANS deve estar vinculado a apenas uma operadora de plano de saúde. Caso o mesmo código esteja associado a outro CNPJ, o sistema bloqueará o cadastro.

 

## **Artigos Relacionados**

- [Configuração de Tabelas de Faixas para Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Lançamento de movimento por Evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38299661897239)

- [Reprocessamento de Plano de Saúde para Funcionários e Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079)

- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)

- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)


---

### 🔗 Links e Referências Internas:

- [Tabela de Faixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)
- [lançamento de eventos de plano de saúde na folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/38299661897239)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Reprocessamento de Plano de Saúde para Funcionários e Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079)
- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)
- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)