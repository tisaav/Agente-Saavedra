# Cadastro de Ocorrências da Folha

> **Módulo:** Pessoas+ | **Subseção:** Configurações de Tipos de Ocorrências  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Cadastro-de-Ocorr%C3%AAncias-da-Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Cadastro-de-Ocorr%C3%AAncias-da-Folha)  
> **ID:** `360044610494` | **Última Atualização:** 2026-09-27T14:45:56Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências > Cadastro
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

 

## 
**Descrição e Usabilidade**

### **1. Descrição da Funcionalidade**

A aba **Cadastro** da tela **Ocorrências** é utilizada para configurar e manter os tipos de ocorrência (também chamados de "históricos de ocorrência") que poderão ser lançados para os colaboradores.

São exemplos de ocorrências:

- faltas;

- atestados médicos;

- compensações de horas ou dias;

- licenças (maternidade, paternidade, casamento, cárcere, alistamento militar, doação de sangue, vestibular, entre outras);

- demais afastamentos previstos pela legislação ou definidos pela empresa.

Cada tipo de ocorrência cadastrado aqui determina, através das **Propriedades da Ocorrência**, como o sistema vai se comportar no controle de ponto, no cálculo da folha de pagamento, no eSocial e no Portal RH/App Pessoas+ sempre que aquele tipo for lançado para um colaborador.

****

| ℹ️ Nota Este artigo trata apenas do cadastro dos tipos de ocorrência. O lançamento, consulta, edição e exclusão de ocorrências para colaboradores possuem artigos específicos. |
| --- |

 

### 
**2. Pré-requisitos**

- Permissão de acesso à tela **Ocorrências **(Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

- Para ocorrências  que geram evento no eSocial, ter em mãos o **motivo de afastamento** oficial do eSocial a associar — motivos descontinuados pela **NT 01/2023 (versão S-1.2)** não podem ser usados (o sistema bloqueia o salvamento).

- Quando a ocorrência controlar estabilidade, configurar posteriormente o seu código no parâmetro **Cód. Hist. Ocorr. para Estabilidade - FPCODHISESTABIL**.

### **3. Jornada de Uso**

**

![cadastro-ocorrencias.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42548687508247)

**

1. Acesse a tela **Ocorrências **(Pessoal+ > Rotinas Folha);

1. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Pesquisar**;

1. Selecione a aba **Cadastro**;

1. Clique em **Adicionar novo tipo de ocorrência**;

1. Na seção **Geral**, selecione o **Tipo de afastamento**, que determina o comportamento da ocorrência nas rotinas do sistema;

1. Informe uma **Descrição** para identificar a ocorrência;

1. Quando se tratar de um afastamento ou ausência legalmente prevista, preencha as informações utilizadas pelo eSocial, FGTS, RAIS e descrição da causa;

1. Marque **Aparece no Portal RH** caso a ocorrência possa ser solicitada pelos colaboradores via Portal RH/App Pessoas+;

1. 

Configure as **Propriedades da Ocorrência**, conforme a finalidade desejada;

📚Para mais detalhes, acesse [Configurações das Propriedades da Ocorrência para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479).

1. 

Clique em **Confirmar alterações**.

Para alterar um cadastro existente, selecione a ocorrência na lista, realize as alterações necessárias e confirme novamente.

### 
**4. Pontos de Atenção**

- O **Tipo de afastamento** influencia diversas validações realizadas pelo sistema, como estabilidade, cálculos e regras específicas de afastamento.

- Para ocorrências enviadas ao eSocial, utilize apenas motivos de afastamento vigentes. Motivos descontinuados impedem o salvamento do cadastro.

- 
**Sobreposição de datas é bloqueada.** Não é possível lançar/editar um afastamento cujo período conflite com outro afastamento do mesmo colaborador — nem com um já **em aberto** (sem data fim), nem com um já **encerrado** cujas datas se sobreponham — quando o tipo pertence à lista de afastamentos "não concomitantes". Essa validação **não vale** para Férias e Licença Gestante.

- Algumas propriedades exigem configurações complementares para produzir efeito.

- Alterações em ocorrências já utilizadas podem impactar cálculos futuros.

- Para que o evento **S-2230 (Afastamento Temporário)** seja gerado a partir de uma ocorrência, é necessário que já exista um evento **S-2200 (Admissão)** ou **S-2300 (TSVE)** finalizado para o colaborador no eSocial. Sem esse evento anterior, o sistema não permite a geração do S-2230.

### **5. Dicas de Usabilidade**

- Padronize a **Descrição **dos tipos de ocorrência para facilitar a busca do Líder/RH tanto na tela de Cadastro quanto no Portal RH/App Pessoas+.

- Revise as propriedades antes de disponibilizar a ocorrência no Portal RH.

- Sempre valide novas configurações em ambiente de testes.

## **Perguntas Frequentes (FAQ)**

**1. Posso alterar uma ocorrência já cadastrada?**

Sim. Basta selecionar o cadastro, realizar as alterações e confirmar novamente.

**2. Como habilito um tipo de ocorrência para aparecer como opção de solicitação no Portal RH/App?** 

Marque **Aparece no Portal RH** no cadastro do tipo de ocorrência.

**3. Por que não consigo salvar uma ocorrência de afastamento?**

Verifique se o motivo de afastamento utilizado está vigente no eSocial e se todos os campos obrigatórios foram preenchidos.

**4. A folha está calculando 1 dia a mais de atestado — por que?** 

Consulte o artigo [Folha de Pagamento Calculando 1 Dia a Mais de Atestado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340522954263).

**5. Deu erro no cálculo do 13º para contrato suspenso — o que fazer?** 

Consulte o artigo [Erro no Cálculo de Décimo Terceiro para Contrato Suspenso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340252616855).

**6.** **Por que não consigo editar ou excluir uma ocorrência já lançada?** 

Ocorrências de férias ou já processadas em folha fechada não podem ser editadas/excluídas.

## **Artigos Relacionados**

- [Configurações das Propriedades da Ocorrência para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479)

- [Cadastro de Ocorrências com Estabilidade para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)

- [Lançamento de Ocorrências para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/42603052607255)

##


---

### 🔗 Links e Referências Internas:

- [Configurações das Propriedades da Ocorrência para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479)
- [Folha de Pagamento Calculando 1 Dia a Mais de Atestado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340522954263)
- [Erro no Cálculo de Décimo Terceiro para Contrato Suspenso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340252616855)
- [Cadastro de Ocorrências com Estabilidade para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)
- [Lançamento de Ocorrências para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/42603052607255)