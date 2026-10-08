# Cadastro do Registro Fiscal

> **Módulo:** Pessoas+ | **Subseção:** Estrutura da Empresa  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal)  
> **ID:** `39123464898199` | **Última Atualização:** 2026-08-27T13:09:02Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.RegistroFiscal

## **Sumário**

[Descrição e Usabilidade](#h_01KM124MP4Q4T9TMEGACAJBVSD)

1. [Descrição da Funcionalidade](#h_01KM0EQ52PE16ZSX0VKKNNSXEK)

1. [Pré-requisitos](#h_01KM0EQ5310Q847NKFJ9V6W2HT)

1. [Jornada de Uso](#h_01KM0EQ537EZHS2GM7W97GH58K)

1. [Pontos de Atenção](#h_01KM0EQ54TZM9GZ10G80D9D09R)

1. [Dicas de Usabilidade](#h_01KM0EQ550ZC0KENFNHH3D9RQH)

[Perguntas Frequentes (FAQ)](#h_01JXZD26WS16MD2RV6DQZ3KG9X)

[Artigos Relacionados](#h_01KM0EQ552PB6F72T5Z2K7MMJ6)

 

## **Descrição e Usabilidade**

O **Registro Fiscal** é o cadastro responsável por definir as regras tributárias e previdenciárias da empresa dentro do sistema. Ele é essencial para garantir o cálculo correto da folha de pagamento e a geração das obrigações legais.

Por meio desse cadastro, são configuradas informações como:

- 

Alíquotas de **INSS**, **FGTS** e **IRRF**;

- 

Enquadramento tributário da empresa;

- 

Códigos de recolhimento (GPS, FPAS, CNAE, entre outros);

- 

Regras de **desoneração da folha**;

- 

Incidência de **PIS sobre a folha de pagamento**.

Essas informações atendem às exigências legais previstas na legislação, como:

- 

**Lei nº 8.212/1991** (Custeio da Previdência Social);

- 

**Lei nº 8.036/1990** (FGTS);

- 

**Lei nº 12.546/2011** (Desoneração da folha);

- 

Regras do **eSocial**, especialmente os eventos cadastrais e periódicos (como S-1000 e S-1280).

A correta configuração do **Registro Fiscal** garante que:

- 

Os encargos sejam calculados conforme a legislação vigente;

- 

As guias de recolhimento sejam geradas corretamente;

- 

As informações enviadas ao governo estejam consistentes;

- 

A empresa evite divergências fiscais, multas e autuações.

### **1. Descrição da Funcionalidade**

A tela **Registro Fiscal **centraliza as configurações utilizadas no cálculo da folha e envio ao eSocial, como:

- 

Percentuais de encargos (INSS, FGTS, RAT, FAP)

- 

Enquadramento tributário

- 

Códigos fiscais

- 

Regras de desoneração e PIS sobre a folha

********

********

| ⚠️ Atenção É obrigatório possuir um Registro Fiscal cadastrado para cada empresa. |
| --- |

 

### **2. Pré-requisitos**

Antes de realizar o cadastro, verifique:

- O** acesso liberado para a tela Registro Fiscal**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

- No cadastro da **Empresa** (Pessoal+ > Cadastros) previamente configurado:

  - 

CNPJ, CNAE e FPAS;

  - 

Enquadramento tributário;

  - 

Incidência de PIS sobre a folha;

  - 

Informações de desoneração (se aplicável).

- 

Percentuais de encargos validados com a contabilidade.

#### **Configurações relacionadas**

- 

Utilize o botão **Configuração da Tela **para ajustar a ordem e a exibição dos campos mais utilizados pela empresa, ocultando aqueles que não se aplicam ao seu negócio.

- 

Ao acioná-lo:

- 

Observe os campos no painel **Campos disponíveis**.

- 

Clique na aba desejada.

- 

Mova os campos para a aba selecionada.

- 

Clique em **Salvar** para aplicar as alterações.

- 

Caso queira ocultar algum campo ou opção da tela, basta fazer a operação reversa.

![config-registrofiscal.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39148872700951)

 

### **3. Jornada de Uso**

Utilize a tabela abaixo como **exemplo de dados fiscais que **devem ser obtidas junto ao **contador, fiscal ou responsável tributário da empresa** antes de iniciar a parametrização.

************

************

************

********

********

************

************

************

************

| Dados Gerais | Percentuais | Percentuais |
| --- | --- | --- |
| Cidade: Uberlândia | Taxa Terceiros INSS: 5,8 | FGTS: 8% |
| CNPJ: 26.314.062/0001-61 | INSS Empresa: 20% | FGTS Menor Aprendiz: 2,00 |
| Não Optante Pelo Simples | Taxa de Seguro: 3% | Filantropia: 0 |
| Não desonera folha | ISS: 1 Prestador de serviço | FAP: 1% |
| Atividade | Códigos | RAT |
| CNAE: 6203100 | INSS Terceiros: 115 | 15 anos: 12 |
| IRF: 561 | SAT: 62031 | 20 anos: 9 |
| FPAS: 515 | GPS: 2100 | 25 anos: 6 |

 

1. Acesse a tela **Registro Fiscal **(Pessoal+ > Cadastros).

2. Clique em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39124874464279)

 **Cadastrar Registro Fiscal**.

3. Preencha primeiro os dados principais da empresa, pois eles serão a base para o cálculo dos encargos e envio das informações ao eSocial.

- 

**Cód. Registro: ** código identificador do registro fiscal. Pode ser incluído de forma manual ou automática, dependendo da configuração realizada na opção **Numeração** presente no botão** 

![botão-configuração-da-tela-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/39124874466839)

 Configuração da Tela** localizado na parte superior direita desta tela.

1. 

**Descrição**: nome utilizado para identificar o registro fiscal da empresa. Utilize a razão social ou nome de fácil reconhecimento.

4. Clique em 

![botão Salvar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/39125064372247)

 **Salvar [F7]**.

![cadastro-reg-fiscal.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39125315332631)

5. Preencha as abas abaixo conforme as necessidades da empresa.

#### **

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315109373335)

Aba Geral**

Nesta aba são definidos os **dados fiscais principais da empresa**, utilizados na apuração da folha, encargos e geração dos eventos periódicos do eSocial.

- 

##### **Identificação**

  - 

**Cidade**
Município da empresa, utilizado em regras fiscais e obrigações acessórias.

  1. 

**Código das opções pelo Simples**
Indica se a empresa é optante pelo regime tributário Simples Nacional.

  1. 

**Indicador de contribuição Simples Nacional**
Define se a contribuição previdenciária é:

    - 

Substituída

    - 

Não substituída

    - 

Mista

  1. 

**Indicativo de substituição da Contribuição Previd. Patronal**
Define se a contribuição patronal é total ou parcialmente substituída, conforme o enquadramento tributário da empresa.

********

****

| ⚠️ Atenção Utilize essa configuração quando a empresa estiver enquadrada em regimes com desoneração parcial ou total da CPP, conforme a Lei nº 12.546/2011. Esse dado será enviado ao eSocial no evento S-1280 – Informações Complementares aos Eventos Periódicos. |
| --- |

  1. 

**Tipo de CAEPF**
Indica o tipo de inscrição da empresa:

    - 

Segurado especial

    - 

Produtor rural

    - 

Contribuinte individual

  1. 

**Taxa Terceiros - INSS**
Contribuições adicionais.

********

************

    - ********
    - ****
    - ********
    - ****

| ⚠️ Atenção A partir da competência 05/2026, o sistema calcula automaticamente o adicional de 0,2% referente ao SENAI no campo Taxa Terceiros - INSS para empresas enquadradas nas seguintes condições:  possuir FPAS 507 (Indústria) ou 833 (Agroindústria);  utilizar o código de terceiros (codTerc) 0079;  possuir mais de 500 empregados, considerando a consolidação pela raiz do CNPJ;  processar folha a partir da competência 05/2026.  Não é necessário realizar qualquer ajuste manual nesse campo. |
| --- |

  1. 

**Percentual de INSS**
Percentual patronal.

  1. 

**Taxa de seguro**
Percentual de taxa de seguro de acidente do trabalho relacionado ao SAT/RAT. Componente importante do custo com folha de pagamento.

  1. 

**Percentual FGTS**
Percentual de contribuição ao Fundo de Garantia do Tempo de Serviço (FGTS). Padrão 8% sobre folha de pagamento.

  1. 

**Percentual do FGTS para Menor Aprendiz**
Percentual de contribuição ao FGTS. Reduzido a 2% sobre folha de pagamento.

  1. 

**Percentual Isenção Filantropia**
Percentual de isenção de contribuições para entidades filantrópicas. Aplicado quando empresa é beneficiária de isenções especiais.

  1. 

**Fator Acidentário de Prevenção (FAP)**
Percentual de fator que ajusta o RAT.

  1. 

**Percentual do FGTS Verde Amarelo**
Percentual de contribuição ao FGTS. Reduzido a 2% sobre folha de pagamento.

  1. 

**ISS Autônomo-Responsável pela retenção**
Indica quem recolhe o ISS sobre o serviço de autônomos:

    - 

**Prestador**

    - 

**Tomador**

Impacta diretamente retenções de autônomos.

  1. 

**INSS Emp. Func** e **INSS Emp. C. Indiv.**
Indica se o INSS será calculado e retido pela empresa.

  1. 

**Salário mínimo vigente**
Valor do salário mínimo vigente.

1. 

##### **Inscrição**

  - 

**Tipo CNPJ/CEI**: tipo de inscrição da empresa.

  - 

**CNPJ/CEI**: identificação utilizada nos envios.

  - 

**Obra Própria**: será exibida quando o **Tipo CNPJ/CEI** for **CNO**.

  - 

**CNPJ Responsável**: será exibido quando a opção **Obra Própria** for ativada.

********

****

| ⚠️ Atenção Para CNO, é necessário informar o CNPJ responsável conforme regras do eSocial. |
| --- |

1. 

##### **Atividade**

  - 

**CNAE/IBGE**: define a atividade econômica utilizada em enquadramentos fiscais, RAT e eSocial.

  - 

**IRF**: código de retenção de Imposto sobre Renda na Fonte (IRF).

  - 

**Cód. FPAS**: código do Fundo de Pensão e Assistência Social para classificação de contribuições previdenciárias e sociais.

1. 

##### **Códigos**

  - 

**INSS Terceiros: **percentual de contribuição ao INSS para terceiros ou regimes especiais. Utilizado para cálculo de retenções em folha de pagamento.

  - 

**SAT**: código de Seguro de Acidentes do Trabalho - classificação para cálculo de contribuições ao INSS relacionadas a acidentes laborais.

  - 

**GPS**: código utilizado na geração da guia de recolhimento do INSS.

1. 

##### **RAT – Agentes Nocivos**

  - Define percentuais para aposentadoria especial:

    - 

15 anos;

    - 

20 anos;

    - 

25 anos.

1. 

##### **PIS sobre a folha**

  - 

**Empresa contribuinte: **indica se a empresa for contribuinte do PIS sobre a folha de pagamento.

  - 

**Alíquota**: será habilitado para preenchimento quando a opção acima estiver ativada.

  - 

**Código da Receita**: será habilitado para preenchimento quando a opção **Empresa contribuinte** estiver ativada.

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315109373335)

**Aba Desoneração da Folha**

Nesta aba, informe os **percentuais aplicados sobre a receita bruta** quando a empresa estiver enquadrada na **desoneração da folha de pagamento**, conforme a legislação vigente.

O preenchimento deve ser realizado de forma separada para:

- 

Folha mensal;

- 

13º salário.

****

************

| ℹ️ Nota Essas informações são utilizadas no cálculo da substituição da contribuição previdenciária patronal e impactam diretamente o Resumo da Folha, a Guia GPS e o envio do evento S-1280 ao eSocial. |
| --- |

 

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315109373335)

**Aba Contabilização**

Esta aba define as regras utilizadas na **integração contábil da folha de pagamento**, garantindo que os lançamentos sejam gerados conforme a política contábil da empresa:

- 

Provisionamento de eventos por média;

- 

Baixa antecipada em férias.

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315109373335)

**Aba** **Histórico Registro Fiscal**

Esta aba apresenta, de forma automática, o **histórico das informações do registro fiscal utilizadas nos cálculos já processados**.

Os dados são alimentados pelo sistema após o **fechamento da folha**, permitindo rastrear quais configurações estavam vigentes em cada competência.

********

****

| ⚠️ Atenção Não permite edição, pois tem função exclusivamente de consulta e auditoria. |
| --- |

 

#### 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315109373335)

**Aba Processos de Terceiros**

Utilize esta aba quando a empresa possuir **processos administrativos ou judiciais relacionados a terceiros**, que impactem encargos ou recolhimentos previdenciários.

Informe o número do processo cadastrado previamente na tela **Processos** (Pessoal+ > Cadastros).

****

| 💡 Dica Após concluir o cadastro, realize um cálculo teste da folha e valide os encargos gerados no Resumo da Folha e na Central do eSocial, garantindo que as alíquotas, códigos de recolhimento e regras de desoneração estejam consistentes. |
| --- |

 

### **4. Pontos de Atenção**

- 

Cada empresa precisa ter **um registro fiscal**.

- 

**Não** é possível cadastrar **mais de um registro fiscal para a mesma empresa**.

- 

Alterações impactam diretamente:

  - 

Cálculo da folha

  - 

Encargos

  - 

eSocial

- 

Alterações realizadas no **Registro Fiscal** não recalculam automaticamente as competências que já foram calculadas ou fechadas.

Se uma alteração precisar refletir em uma competência que já foi processada, é necessário:

  1. excluir o cálculo da folha da competência;

  1. realizar o novo cálculo com as informações atualizadas do Registro Fiscal;

  1. confirmar e fechar a folha novamente.

Dessa forma, o **Resumo da Folha** e os demais valores calculados para a competência passam a considerar a nova configuração.

- 

O campo **INSS sobre receita bruta não é calculado automaticamente, deve ser informado manualmente.**

- 

O **FAP deve ser atualizado antes do cálculo da folha.**

- 

Para empresas com desoneração ou PIS sobre a folha, verifique corretamente o enquadramento legal.

### **5. Dicas de Usabilidade**

- 

Utilize uma **descrição clara**, como: “Registro Fiscal - Empresa X”.

- 

Revise os percentuais com base no **contador ou área fiscal** antes de salvar.

- 

Utilize a opção **Configuração de Tela** para ocultar campos que não são utilizados.

## **Perguntas frequentes (FAQ)**

**1. Posso alterar o Registro Fiscal depois que a folha já foi fechada?**

Pode, mas a alteração **não corrige automaticamente a competência já fechada**.

Os novos valores serão considerados apenas nas próximas competências.

**2. Alterei o Registro Fiscal, mas o Resumo da Folha ou o histórico continuam com os valores anteriores. O que fazer?**

As alterações realizadas no **Registro Fiscal** não atualizam automaticamente uma folha que já tenha sido calculada ou fechada.

Para que os novos valores sejam considerados na competência:

1. exclua o cálculo da folha;

1. recalcule a folha;

1. confirme e realize o fechamento novamente.

Após o novo processamento, o **Resumo da Folha** e o histórico passarão a considerar os valores atualizados.

**3. Recebi um novo valor de FAP da contabilidade. Quando devo atualizar no sistema?**

O **FAP (Fator Acidentário de Prevenção)** deve ser atualizado no **Registro Fiscal antes do cálculo da folha**.

Se você atualizar depois que a folha já foi calculada ou fechada, o sistema não irá corrigir automaticamente os valores já apurados.

**4. A contabilidade me passou o valor de INSS sobre a receita bruta. Onde e como devo informar?**

Esse valor deve ser preenchido diretamente no **Registro Fiscal**.

É importante saber que o sistema **não calcula esse valor automaticamente**, então o preenchimento manual correto é fundamental.

**5. Posso alterar dados do Registro Fiscal durante a competência em andamento?**

Sim.
Mas se a folha já tiver sido calculada, será necessário recalcular.

**6. O que pode acontecer se eu não atualizar o Registro Fiscal quando há mudanças fiscais?**

A falta de atualização pode gerar:

- 

Cálculo incorreto de encargos.

- 

Diferenças em guias de recolhimento.

- 

Inconsistências no eSocial.

- 

Risco de multas e autuações.

Por isso, sempre valide as mudanças com a contabilidade.

**7. Em quais situações devo revisar o Registro Fiscal, mesmo sem erro aparente?**

A revisão é recomendada sempre que houver:

- 

Nova competência iniciando.

- 

Alterações de FAP.

- 

Mudanças legais ou tributárias.

- 

Orientações da contabilidade.

Essa prática evita erros silenciosos que só aparecem depois do fechamento.

**8. Existe algum cuidado especial ao alterar dados como FAP, RAT ou percentuais de INSS?**

Sim. Esses campos impactam diretamente o cálculo da folha.

Antes de alterar:

- 

Verifique a competência atual;

- 

Confirme se a folha já foi calculada;

- 

Valide o valor com a contabilidade.

Alterações incorretas podem gerar retrabalho e inconsistências legais.

 

## **Artigos Relacionados**

- 

[Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311)

- 

[Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)

- 

[PIS sobre a Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543)

- 

[Cadastro de Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311)
- [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)
- [PIS sobre a Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543)
- [Cadastro de Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503)