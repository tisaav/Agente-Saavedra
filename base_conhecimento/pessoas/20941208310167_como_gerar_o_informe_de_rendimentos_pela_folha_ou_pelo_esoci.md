# Como gerar o Informe de Rendimentos pela folha ou pelo eSocial?

> **Módulo:** Pessoas+ | **Subseção:** Conferência do IRRF no eSocial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial)  
> **ID:** `20941208310167` | **Última Atualização:** 2026-09-27T18:54:55Z

---

**Módulo: **Pessoal+
**Versão Mínima: **5.76.0 
**SAN eSocial:** 3.41 
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela: **br.com.sankhya.rh.GeracaoGuias

### **Sumário**

[Descrição e Usabilidade](#h_01KEJHKYYGM5YWS98TP86S0AF8)

[1. Pré-requisitos](#h_01KEHHEN852B34DK3P1A507270)
[2. Jornada de Uso](#h_01KEHHGHRW2B5R424TB1D8269E)

[Gerar Informe](#h_01KR3VH745TNHTQQRQQH0S19ZK)
[Consolidar Informe](#h_01KR3VJDMFYNCC5M47Q0ZGNZVN)
[Informações apresentadas no relatório](#h_01KEHNMN5TED5A8PYNM385542V)

[3. Pontos de Atenção](#h_01KEHNMN6QYYQCG0TZ0MPH1EF2)
[4. Dicas de Usabilidade](#h_01KEHNMN6WDR35643HV50GGNQK)

[Artigos Relacionados](#h_01KEHNMN6Z0WGXED0EBMY26XGP)

 

### **Descrição e Usabilidade**

**O Informe de Rendimentos** é um documento anual obrigatório que reúne todas as informações sobre os rendimentos pagos a trabalhadores ao longo de um ano-calendário, assim como os valores de tributos retidos na fonte. Ele é utilizado para fins de **declaração do Imposto de Renda da Pessoa Física (IRPF)** e deve atender ao modelo e aos requisitos definidos pelo governo federal.

A geração do Informe de Rendimentos no sistema Pessoal+ segue as **determinações legais vigentes**, especialmente o **leiaute previsto na ******[Instrução Normativa RFB n.º 2.060/2021](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/122177), que padroniza os campos, a natureza dos rendimentos e as informações obrigatórias a serem apresentados no documento.

Este comprovante deve ser entregue ao trabalhador até o **último dia útil do mês de fevereiro** do ano seguinte ao pagamento dos rendimentos, ou no momento da **rescisão de contrato de trabalho**, caso esta ocorra antes dessa data.

O novo processo de geração considera duas formas distintas, conforme as regras do governo:

- 

**Folha de pagamento (cálculo)**

O Informe é gerado a partir dos valores efetivamente pagos pela empresa, com base na **data de pagamento** registrada na folha. Todos os rendimentos tributáveis, deduções e tributos retidos são consolidados diretamente dos resultados de cálculo da folha de pagamento.

- 

**eSocial (S-5002)**

O Informe é gerado a partir dos **retornos de dados oficiais enviados ao eSocial**, do envio do evento **S-1210** (informações de pagamento) e do retorno do evento **S-5002** (informações de rendimentos e tributos). Esta forma de geração entrega um documento alinhado às informações homologadas pelo governo, seguindo integralmente o leiaute legal para fins fiscais.

### **1. Pré-requisitos**

#### **Permissões necessárias**

- 

Acesso liberado para a tela **Geração de Guias**.

Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

#### **Configurações prévias**

Antes de gerar o Informe de Rendimentos, verifique as seguintes configurações:

**1. Empresa Matriz:**

No cadastro da ****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913) (Configurações > Cadastros), aba ****[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abageral), a **Empresa Matriz** deve ser indicada, pois ela tem a função de gerar também os dados das filiais.

![Empresa-matriz-dirf.png](https://ajuda.sankhya.com.br/hc/article_attachments/20941858728087)

**2. Dados do declarante**

As informações do declarante devem estar preenchidas na aba ****[Informações para DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas#abainforma%C3%A7%C3%B5esparadirf) da tela **Empresas** (Pessoal+ > Cadastros).

![Responsavel-dirf-empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/20942148113687)

 

### **2. Jornada de Uso**

 

********

************[Instrução Normativa RFB n.º 2.060/2021](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/122177)****

| ⚠️ Atenção O Informe de Rendimentos referente ao ano-calendário 2025 é gerado conforme o novo procedimento de envio das informações da DIRF pelo eSocial e mantendo o que determina o leiaute definido na . Para os anos-calendários anteriores, o sistema utiliza o leiaute DIRF disponibilizado para o envio das informações até o ano base 2024. |
| --- |

 

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315263843863)

 **Gerar Informe**

Com as configurações realizadas, acesse a tela **Geração de Guias** e, primeiramente, clique sobre o card **DIRF **e, depois, em** Demonstrativo e Rendimentos **e siga as etapas abaixo:

![geracaoinfrenddirfnova.gif](https://ajuda.sankhya.com.br/hc/article_attachments/41345947990295)

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20948448029463)

** Informações Gerais**

1. 

Preencha o campo **Ano base (Ano calendário)** com o ano em que os rendimentos foram pagos.

O sistema apresentará para seleção apenas os trabalhadores que possuam **rendimentos pagos dentro desse período**, considerando a **data de pagamento da folha**. Colaboradores sem pagamentos no ano-base não serão exibidos, mesmo que estejam ativos. Trabalhadores desligados serão apresentados normalmente, desde que tenham recebido algum pagamento no período.

1. Selecione a **Forma de Geração** do relatório:

  - 
**Folha de pagamento (cálculo):** utiliza os valores calculados na folha, considerando a data de pagamento no ano-base, como: salários, férias, 13º, pensões, previdência, plano de saúde e IRRF;

  - 
**eSocial (S-5002): **utiliza exclusivamente os retornos do eSocial, considerando apenas trabalhadores com pagamento enviado no evento S-1210 e retorno disponível do S-5002 dentro do ano-base informado.

1. Marque **Liberar informes para os funcionários** para disponibilizar os informes no **Portal RH**, bem como o envio dos documentos para o e-mail cadastrado.

1. Clique na etapa **2 Empresas** ou no botão **Próximo** para avançar para a próxima etapa.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20952136026135)

  **Empresas**

1. Selecione a(s) **Empresa(s)** responsável(eis) pelo Informe, clicando em seus respectivos card.

1. Avance para a próxima etapa.

![etapaempresadirf.png](https://ajuda.sankhya.com.br/hc/article_attachments/37564073129751)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20954214832919)

 **Funcionários** 

1. 

Selecione os colaboradores que irão compor o Informe:

  - 

individualmente, clicando nos respectivos cards ou

  - 

utilizando a opção **Marcar todos**.

1. Para facilitar essa seleção, utilize os 

![botão Filtrar-P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20954231167511)

 **Filtros** padrões ou personalizados (por meio da opção **Gerenciar filtros**).

1. Avance para a etapa final.

![funcdirf-2025.gif](https://ajuda.sankhya.com.br/hc/article_attachments/37564096952343)

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20952361176727)

 Gerar**

1. 

Clique no botão **Gerar.**

Os Informes estarão disponíveis para:

  - 

salvar no computador;

  - 

imprimir;

  - 

enviar por e-mail.

![informedirf2025.png](https://ajuda.sankhya.com.br/hc/article_attachments/37564096955287)

- 

Para envio por e-mail, clique em **Enviar comprovantes por e-mail** e confirme a ação.

********

****

| ⚠️ Atenção O ícone de envio dos informes por e-mail (envelope) só será apresentado se a marcação Liberar informes para os funcionários tiver sido habilitada na etapa 1 da geração. |
| --- |

![gerardirf2025.png](https://ajuda.sankhya.com.br/hc/article_attachments/37564073132567)

 

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315263843863)

 **Consolidar Informe**

Após informar o ano-base na rotina, o sistema disponibiliza o botão **Consolidar Informe** no canto inferior direito da tela.

Essa opção deve ser utilizada quando houver necessidade de atualizar os dados do Informe de Rendimentos após:

- recálculo de folhas;

- ajustes de IRRF;

- alterações em eventos;

- reabertura de competências;

- novas informações inseridas na folha de pagamento.

Ao clicar em **Consolidar Informe**, o sistema reprocessa as informações utilizadas na geração do demonstrativo para o ano informado.

****

| 💡 Dica Recomenda-se executar essa ação antes da emissão final do informe sempre que houver alterações na folha após uma geração anterior. |
| --- |

 

### **Informações apresentadas no relatório**

As informações exibidas no Informe de Rendimentos variam conforme a **Forma de Geração** selecionada.

Observe abaixo de onde o sistema busca cada dado em cada cenário.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450443875991)

 Geração pela **Folha de Pagamento (cálculo):**

Nesta forma de geração, o sistema utiliza **os valores calculados e pagos na folha**, considerando a **data de pagamento dentro do ano-base**.

****

****

************

****

****

****

****

****

****

| Seção do Informe | Informação apresentada | Origem da informação |
| --- | --- | --- |
| 1 Fonte pagadora | Razão social | Cadastro da Empresa - aba Geral |
| CNPJ / CPF |  |  |
| 2 Pessoa Física Beneficiária dos Rendimentos | Nome Completo | Cadastro do Funcionário - Painel principal ⚠️A partir da versão 5.100, para preencher o Nome Completo, o sistema verifica se o trabalhador tem um Nome Social cadastrado. Se essa informação estiver disponível, o campo Nome Completo será preenchido com o Nome Social. Caso contrário, será usado o nome civil cadastrado do trabalhador. Essa regra vale tanto para informes gerados pela Folha de Pagamento quanto para os gerados a partir das informações do eSocial. |
| CPF |  |  |
| Natureza do rendimento | Código de categoria para o eSocial + vínculo (cadastro do funcionário) |  |
| 3 Rendimentos Tributáveis, Deduções e Imposto sobre a Renda Retina na Fonte | Rendimentos pagos (inclusive férias) | Eventos de pagamentos do ano-base |
| Contribuição previdenciária oficial | Eventos de INSS |  |
| Previdência complementar / FAPI | Cadastro de Previdência complementar + eventos configurados para desconto no cálculo. |  |
| Pensão alimentícia | Cadastro de Dependentes de Pensão + eventos para desconto no cálculo |  |
| IRRF retido | Cadastro de funcionários + eventos de retenção |  |
| 4 Rendimentos Isentos e Não Tributáveis | Parcela isenta (65 anos ou mais), exceto a parcela isenta do 13º salário | Cadastro do funcionário + eventos de isenção. |
| Pensão e proventos de aposentadoria ou reforma por moléstia grave, ou por acidente em serviço | Cadastro do Funcionário |  |
| Diárias e ajuda de custo | Eventos de ajuda de custo |  |
| Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV e por acidente de trabalho | Eventos de rescisão por acidente de trabalho |  |
| Juros de mora | Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função |  |
| Lucros e dividendos, apurados a partir de 1996, pagos por pessoa jurídica | Eventos de pagamentos do ano-base |  |
| Outros rendimentos isentos | Eventos de pagamentos do ano-base |  |
| 5 Rendimentos Sujeitos à Tributação Exclusiva (rendimento líquido) | 13º salário | Eventos de pagamentos do ano-base |
| IRRF sobre 13º |  |  |
| Outros rendimentos de tributação exclusiva. |  |  |
| 6 Rendimentos Recebidos Acumuladamente - Art. 12-A da Lei n.º 7.713, de 1988 (sujeitos à tributação exclusiva) | Número do processo | Cadastro de Processos Trabalhistas |
| Quantidade de meses |  |  |
| Valores tributáveis, deduções e IRRF | Eventos vinculados ao processo |  |
| 7 Informações Complementares | Pensionistas | Cadastro de Dependentes de Pensão + eventos |
| Previdência privada | Cadastro da Previdência + eventos para desconto no cálculo |  |
| Plano de saúde | Cadastro do Plano + dependentes + eventos para desconto no cálculo |  |
| 8 Responsável pelas informações | Nome do responsável | Cadastro da Empresa – Informações para DIRF |
| Data de emissão | Data de geração do relatório |  |

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450443875991)

 Geração pelo **eSocial (S-5002)**

Nesta forma de geração, o sistema utiliza **exclusivamente os retornos do eSocial**, considerando apenas os trabalhadores que tiveram **envio do evento S-1210** e **retorno do evento S-5002** dentro do **ano-base informado**.

Os valores apresentados correspondem à **soma das tags dos grupos do evento S-5002**, apuradas por **cpfBenef**, abrangendo os períodos de apuração de **janeiro a dezembro** do ano-base.

****

****

************

******

**

**

**

**

******

****

******

**

**

****

****

******

******

**

********
**

**********
******
******
********
********
********
******
********
************

**********

******
********

****

| Seção do Informe | Informação apresentada | Origem da informação |
| --- | --- | --- |
| 1 Fonte pagadora | Razão social | Cadastro da Empresa - aba Geral |
| CNPJ / CPF |  |  |
| 2 Pessoa Física Beneficiária dos Rendimentos | Nome Completo | Cadastro do Funcionário - Painel principal ⚠️A partir da versão 5.100, para preencher o Nome Completo, o sistema verifica se o trabalhador tem um Nome Social cadastrado. Se essa informação estiver disponível, o campo Nome Completo será preenchido com o Nome Social. Caso contrário, será usado o nome civil cadastrado do trabalhador. Essa regra vale tanto para informes gerados pela Folha de Pagamento quanto para os gerados a partir das informações do eSocial. |
| CPF |  |  |
| Natureza do rendimento | Código de categoria para o eSocial + vínculo (cadastro do funcionário) |  |
| 3 Rendimentos Tributáveis, Deduções e Imposto sobre a Renda Retina na Fonte | Rendimentos pagos (inclusive férias) | Soma dos valores informados na tag vlrRendTrib do grupo consolidApurMen do evento S-5002, considerando especificamente cpfBene. |
| Contribuição previdenciária oficial | Soma dos valores informados na tag vlrPrevOficial do grupo consolidaApurMen do evento S-5002. |  |
| Previdência complementar / FAPI | Soma dos valores informados na tag vlrDedPC do grupo previdCompl do evento S-5002. |  |
| Pensão alimentícia | Valores informados na tag vlrDedPenAlim do subgrupo penAlim, do grupo infoIRComplem do evento S-5002. |  |
| IRRF retido | Soma dos valores informados na tag vlrCRMen do grupo consolidaApurMen do evento S-5002. |  |
| 4 Rendimentos Isentos e Não Tributáveis | Parcela isenta (65 anos ou mais), exceto a parcela isenta do 13º salário | Soma dos valores mensais informados na tag vlrParcIsenta65, do grupo consolidApurMen do evento S-5002. |
| Pensão e proventos de aposentadoria ou reforma por moléstia grave, ou por acidente em serviço | Soma dos valores mensais informados nas tags vlrRendMoleGrave e vlrRendMoleGrave13, do grupo consolidApurMen do evento S-5002. |  |
| Diárias e ajuda de custo | Soma dos valores informados nas tags vlrDiarias, vlrAuxMoradia e vlrAjudaCusto, conforme o caso, do grupo consolidApurMen do evento S-5002. |  |
| Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV e por acidente de trabalho | Soma dos valores informados na tag vlrIndResContrato do grupo consolidApurMen do evento S-5002. |  |
| Lucros e dividendos, apurados a partir de 1996, pagos por pessoa jurídica | Valor zerado, informações não estão presentes no S-5002. |  |
| Juros de mora | Soma dos valores informados na tag vlrJurosMora do grupo consolidApurMen do evento S-5002. |  |
| Outros rendimentos isentos | Soma dos valores informados nas tags vlrIsenOutros e vlrAbonoPec do grupo consolidApurMen do evento S-5002. |  |
| 5 Rendimentos Sujeitos à Tributação Exclusiva (rendimento líquido) | 13º salário | Soma dos valores informados na tag vlrRendTrib13 e deduzindo os valores correspondentes das tags vlrPrevOficial13 e vlrCR13Men, todos pertencentes ao grupo consolidApurMen do evento S-5002. Soma dos valores pagos a título de pensão alimentícia e dedução de dependentes, conforme as tags vlrDedPenAlim e dedDepen, para cada dependente cpfDep de janeiro à dezembro do ano base informado. |
| IRRF sobre 13º | Soma dos valores informados na tag vlrCR13Men do grupo consolidApurMen do evento S-5002. |  |
| Outros rendimentos de tributação exclusiva. | Soma dos valores mensais da tag vlrRendTrib, com a dedução das tags vlrPrevOficial, vlrCRMen e vlrDedPenAlim.A tag vlrDedPenAlim é considerada na dedução somente quando: tpRend = 14 e registrada no grupo penAlim para o tpCR 356201. |  |
| 6 Rendimentos Recebidos Acumuladamente - Art. 12-A da Lei n.º 7.713, de 1988 (sujeitos à tributação exclusiva) | Processo, meses, valores e IRRF | Número do processo: tag nrProcRRAdo grupo infoRRA.Natureza do rendimento: tag descRRA.Quantidade de meses: tag qtdMesesRRA.Total dos rendimentos tributáveis (inclusive férias e décimo terceiro salário): tags vlrRendTrib e vlrRendTrib13 do grupo consolidApurMen.Exclusão: Despesas com a ação judicial: grupo despProcJud, nas tags vlrDespCustas e vlrDespAdvogados.Dedução: Contribuição previdenciária oficial: soma dos valores das tags vlrPrevOficial e vlrPrevOficial13 do grupo consolidApurMen.Dedução: Pensão alimentícia: tag vlrDedPenAlim do subgrupo penAlim do grupo infoIRComplem.Imposto sobre a Renda Retido na Fonte (IRRF): soma das tag vlrCRMen e vlrCR13Men do grupo consolidApurMen.Rendimentos isentos de pensão, proventos de aposentadoria ou reforma por moléstia grave ou aposentadoria ou reforma por acidente em serviço: soma das tags vlrParcIsenta65, vlrParcIsenta65Dec, vlrRendMoleGrave, vlrRendMoleGrave13 do grupo consolidApurMen. |
| 7 Informações Complementares | Pensionistas | Exibe o nome e o CPF do dependente pensionista, conforme indicados no grupo infoIRComplem, subgrupo ideDep (tags nome, dtNascto e cpfDep), bem como, o valor pago a título de pensão alimentícia, informado na tag vlrDedPenAlim para cada cpfDep. |
| Previdência privada | Exibe o nome e o CNPJ da entidade de previdência complementar ou do FAPI, o valor total das contribuições, incluindo os descontos do 13º salário, e o tipo de previdência, conforme abaixo:1 – Previdência privada2 – FAPI3 – Funpresp |  |
| Plano de saúde (titular e dependentes) | Exibe o CNPJ e o nome da operadora (verificado na tabela de plano de saúde), além do total anual descontado, conforme o evento S-5002: Titular: valores do grupo PlanSaude (tag vlrSaudeTit).Dependentes: valores do grupo infoDepSau (tags cpfDep e vlrSaudeDep), detalhando o total anual de cada dependente. |  |
| 8 Responsável pelas informações | Nome do responsável | Cadastro da Empresa – Informações para DIRF |
| Data de emissão | Data de geração do relatório |  |

 

### **3. Pontos de Atenção**

- 

O Informe considera **a data de pagamento**, não a competência.

- 

É gerado **um Informe por empregador**.

- 

Quando o trabalhador possui mais de um contrato com o mesmo empregador, os valores são **agrupados**.

- 

Rendimentos com **exigibilidade suspensa** são apresentados separadamente, conforme a legislação.

### **4. Dicas de Usabilidade**

- 

Gere o Informe após o fechamento da folha ou após a consolidação dos eventos do eSocial.

- 

Utilize a mesma forma de geração para todos os trabalhadores do ano-base.

- 

Em caso de divergência, revise os valores de pagamento e o retorno do eSocial.

### **Artigos Relacionados**

[Nova DIRF/eSocial 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361211258647)

[Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071)

[Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abageral)
- [Informações para DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas#abainforma%C3%A7%C3%B5esparadirf)
- [Nova DIRF/eSocial 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361211258647)
- [Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071)
- [Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)