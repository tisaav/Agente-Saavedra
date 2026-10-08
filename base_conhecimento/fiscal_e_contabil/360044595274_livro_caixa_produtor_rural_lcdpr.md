# Livro Caixa Produtor Rural - LCDPR

> **Módulo:** Fiscal e Contábil | **Subseção:** Declarações federais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274-Livro-Caixa-Produtor-Rural-LCDPR)  
> **ID:** `360044595274` | **Última Atualização:** 2026-09-15T17:36:08Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315781336087)

 **Módulo:** Livros Fiscais > Conexão      
```

Através desta rotina, será possível incluir as informações, realizar configurações e gerar o Arquivo do Livro Caixa Digital do Produtor Rural.

[Painel Principal](#painelprincipal)[Aba Geral](#abageral)

[Aba 0000](#aba0000)[Aba 0010](#aba0010)

[Aba 0040](#aba0040)[Aba 0050](#aba0050)

[Aba Q100](#abaq100)[Aba Q200](#abaq200)

[Aba 9999](#aba9999)[Botões no topo da tela](#botesnotopodatela)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

 

## 
Painel Principal

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4415575433751)

Neste Painel, deve-se configurar a **"Empresa"** que terá o Arquivo do Livro Caixa Digital do Produtor Rural gerado, bem como, informar a **"Dt. Inicial"** e a **"Dt. Final"** para a geração.

## 
Aba Geral

No campo **"Versão do Layout"** encontra-se a versão definida pela Receita, a qual será entregue o Arquivo do Livro Caixa Digital do Produtor Rural.

O campo **"Indicador do Início do Período"** possui as seguintes opções:

- 
**Início de obrigatoriedade da escrituração no curso do ano calendário:** Esta opção deverá ser selecionada quando o produtor rural, no curso do ano caléndário, adquiriu algum processo administrativo.

- 
**Abertura:** Deve-se selecionar esta opção quando o produtor rural obteve operações com a atividade rural naquele ano da entrega do livro.

- 
**Regular:** Seleciona-se esta opção quando o produtor rural já realiza operações da atividade rural, ou seja, suas operações não são recentes.

Deve-se preencher o campo **"Indicador de Situação Especial e Outros Eventos"** para indicar a situação do produtor rural no ano calendário da entrega do livro. Neste campo, tem-se as opções a seguir:

- Espólio;

- Falecimento;

- Normal;

- Saída definitiva do País.

O campo **"Data da Situação Especial"** possui relação com o campo Indicador de Situação Especial e Outros Eventos, ou seja, deve-se selecionar a data em que ocorreu a situação especial.

No campo **"Forma de Apuração"** seleciona-se a forma escolhida pelo produtor rural para executar a apuração de suas atividades rurais, sendo elas:

- Apuração do lucro pelo disposto no art. 5º da Lei nº 8.023, de 1990;

- Livro Caixa.

Se você não realizar a habilitação da marcação **"Construir histórico do registro Q100 de forma automática?"**, o histórico do registro Q100 será obtido a partir da tela [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753); caso contrário ocorrerá da seguinte forma:

- 
**Se Receita:** Recebimento ref. - NF Nº XXX - Razão Social do Parceiro + Histórico do financeiro;

- 
**Se Despesa:** Pagamento ref. - NF Nº XXX - Razão Social do Parceiro + Histórico do financeiro.

Quando a marcação **"Considerar naturezas do rateio da Movimentação Financeira para gerar o Q100?"** for habilitada, o sistema exibirá as informações de despesas/receitas considerando as naturezas do rateio do título lançado na Movimentação Financeira da seguinte forma:

- Caso exista no rateio mais de uma natureza e uma delas estiver com a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"** da tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas) desabilitada, o valor rateado referente a essa natureza não será considerado na declaração;

- Se a marcação Considerar naturezas do rateio da Movimentação Financeira para gerar o Q100? for selecionada, e o lançamento não possuir rateio, o sistema utilizará a informação do campo **"Natureza"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), desde que esta seja configurada para gerar LCDPR.

[[voltar ao topo]](#top)

## 
Aba 0000

Esta aba tratará sobre informações relativas ao **"Registro 0000 - Abertura do Arquivo Digital e Identificação da Pessoa Física"**.

![print_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408238522007)

[[voltar ao topo]](#top)

## 
Aba 0010

Nesta aba, teremos as informações referentes ao **"Registro 0010 - Parâmetros de Tributação"**:

![print_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408238561815)

No campo **"Forma de Apuração" **deve-se selecionar se a apuração será realizada de acordo com o **"Livro Caixa"** ou com a **"Apuração do lucro pelo disposto no art. 5º da Lei nº 8.023, de 1990"**.

[[voltar ao topo]](#top)

## 
Aba 0030

Essa aba, refere-se ao **"Registro 0030 - Dados Cadastrais do Contribuinte"**.

![print_4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408249562391)

[[voltar ao topo]](#top)

## 
Aba 0040

Tem-se nesta aba as informações referentes ao **"Registro 0040 - Cadastro dos Imóveis Rurais"**; assim, esta aba tem por objetivo controlar as aquisições, as quantidades e preencher o Registro 0040 do arquivo LCDPR.

**Observação:** o registro 0040 buscará as informações de todos os imóveis rurais definidos no Q100 e o registro 0045 carregará os dados da aba **"Livro Caixa Digital Produtor Rural"** da tela Preferências da Empresa para cada um dos imóveis.

![print_5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408238614935)

 

**Sub-aba 0045**

Quando configurados os campos desta sub-aba, será preenchido o **"Registro 0045 - Cadastro de Terceiros"**. Nesta sub-aba deve-se realizar o cadastro das informações relativas a contratos e dados da contraparte do imóvel.

![0045.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408249584535)

[[voltar ao topo]](#top)

## 
Aba 0050

Nesta aba, deve-se inserir as informações relativas às contas bancárias do produtor rural, para que o **"Registro 0050 - Cadastro das Contas Bancárias do Produtor Rural"**.

![0050.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408238637207)

Para a obtenção do **"Código Sequencial da Conta Bancária" **e **"Código da conta bancária"** dos registros [Q100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#abaq100) e [0050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#aba0050), teremos a seguinte hierarquia de busca caso estes estejam preenchidos:

- Campo **"Classificação da conta Produtor Rural"**;

- O campo **"Número da conta Produtor Rural"**;

- Os três primeiros dígitos do **"Código da Conta Bancária"**.

[[voltar ao topo]](#top)

## 
Aba Q100

Esta aba, refere-se ao **"Registro Q100 - Demonstrativo do Resultado da Atividade Rural"** e trará informações dos financeiros para os imóveis rurais associados à empresa em questão, no intervalo definido no cabeçalho da Movimentação Financeira.

![q100.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408238652823)

Para que você efetue a geração do Registro Q100, primeiramente, realize as configurações abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)

|  | Na tela , defina da seguinte forma os campos: |
| --- | --- |

- Defina o campo **"Classificação ICMS"** com a opção **"Produtor Rural"**;

- Habilite a marcação **"Produtor tem NF"**;

- Preencha o campo **"CPF Prod. Rural"**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)

|  | Logo depois, na tela : |
| --- | --- |

- Acione a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"**;

- Nos campos **"Cód. CAFIR"** e **"Cód. CAEPF"**, informe os códigos correspondentes a eles;

- Defina ainda um **"Tipo de Exploração"**;

- Depois, na sub-aba desta aba, inclua o parceiro produtor rural vinculado e determine um **"Percentual de Exploração"**, uma vez que, essa informação será utilizada no Registro Q100 quando o sistema efetuar o cálculo do valor de entrada e saída.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)

|  | Logo após, na tela : |
| --- | --- |

- 
Adicione uma natureza com característica de receita e nesta, acione a marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)

|  | Já na tela : |
| --- | --- |

- 
Lembre-se de desabilitar a marcação **"Desconsiderar Conta na Geração do Livro Caixa Digital do Produtor Rural"** no registro da conta bancária utilizada para a baixa.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)

|  | No : |
| --- | --- |

- 
Realize a criação de um imposto com o **"Nome"** igual a SENAR;

- 
Depois, defina o campo **"Tipo"** com a opção **"apenas os que tenham a coluna “calcular” MARCADA"**;

- 
No campo **"Tipo Imposto"**, escolha a opção **"SENAR"**;

- 
Configure o campo **"Usar para itens da nota"** com a opção **"Preço da Nota"**;

- Realize a definição da opção **"Valor do Pagamento" **no campo** "Base para Impostos do Financeiro"**.

-  

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro)

|  | Na aba  ainda na tela Cadastro de Impostos, configure os campos da seguinte forma: |
| --- | --- |

- 
**Parceiro:** parceiro criado anteriormente;

- 
**Na nota:** Já incluso;

- 
**No Financeiro Origem Financeiro:** Nenhum;

- 
**No Financeiro Origem Estoque:** Subtrair;

-  

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abatop)

|  | Posteriormente, na aba  da mesma tela: |
| --- | --- |

- 
**Alíquota:** 0,20;

- 
**Na nota:** Já incluso;

- 
**No Financeiro Origem Financeiro:** Nenhum;

- 
**No Financeiro Origem Estoque:** Subtrair;

-  

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa)

|  | Ainda na mesma tela, na aba : |
| --- | --- |

- 
Informe a** "Empresa"** a ser utilizada na venda;

- 
**Alíquota:** 0,20;

- 
**Na nota:** Já incluso;

- 
**No Financeiro Origem Financeiro:** Nenhum;

- 
**No Financeiro Origem Estoque:** Subtrair;

- Habilitar marcação **"Calcular"**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaproduto)

|  | Na mesma tela, aba , configure: |
| --- | --- |

- 
O **"Produto"** que será utilizado na venda;

- 
**Alíquota:** 0,20;

- **Na nota:** Já incluso.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)

|  | Já na tela , aba : |
| --- | --- |

- 
Preencha o campo **"Tipo Documentado Rural"**;

- 
Configure também o registro do título a ser lançado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)[Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)

|  | Em , aba : |
| --- | --- |

- Após criar um Tipo de Negociação, informe o Tipo de Título criado anteriormente;

- 
Em seguida, na Parcela 1, defina o campo **"Natureza Padrão"** da receita cadastrada para a geração do LCDPR;

- 
No campo **"Tipo de Financeiro (REC/DESP)"**, utilize a opção **"Usar da Natureza Padrão"**;

- Já na Parcela 2, cadastre a Natureza Padrão da despesa para o imposto;

- 
Realize a configuração do campo **"Tipo de Parceiro"** com a opção **"C - Constante"**;

- 
No **"Parceiro"**, defina o Parceiro responsável pelo recebimento do imposto;

- 
Já o campo **"Fórmula"** deve ser utilizado para que a parcela seja gerada considerando os outros impostos;

- Em seguida, configure a opção **"Usar da Natureza Padrão"** no campo **"Tipo de Fincanceira (REC/DESP)"**.

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315843318423)

|  | Caso tenha dúvidas referentes ao preenchimento do campo, consulte a documentação deste nesta aba. |
| --- | --- |

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)

|  | Nas  do sistema: |
| --- | --- |

- 
No parâmetro **"Naturezas de títulos não apresentados na nota - NATTITNAONOT"**, insira a natureza de despesa criada e informada na Parcela 2 do Tipo de Negociação.

```text
                                                                               

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16315843319191)

       Caso a natureza não seja inserida no parâmetro, ao emitir uma Nota Fiscal para a SEFAZ, será
       apresentada a seguinte mensagem:
       ***"866 - Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior
       que****** o total da nota" ***
```

- 
Em seguida, caso queira que o Registro Q100 e o campo **"Valor de entrada dos recursos"** desta aba sejam gerados com o valor bruto quando o título possuir um, ou mais lançamentos conforme a opção **"Vlr. do Desdobramento"** da Movimentação Financeira, ligue o parâmetro **"Gerar valor bruto de receita no Q100 do LCDPR - GERVLRBRTLCDPR"**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)

|  | Na : |
| --- | --- |

- Confira se o título está baixado;

- 
Além disso, certifique-se que a data da baixa está entre o período informado no LCDPR, e se esta foi gravada, pois não pode ser nula;

1. Tenha a certeza que o título lançado não é uma provisão.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458095457687)

|  | Por fim, na tela Livro Caixa Produtor Rural - LCDPR: |
| --- | --- |

- 
No campo **"Produtor"**, informe o parceiro utilizado;

- 
Em seguida, preencha o campo **"Versão do Layout"** com a Versão 0013;

- 
Defina o campo **"Indicador do início do período"** com a opção **"Regular"**;

- 
Referente ao campo **"Indicador de Situação Especial"**, defina-o com a opção **"Normal"**;

- Configure no campo **"Forma de Apuração"**, a opção **"Livro Caixa"**.

A seguir, teremos os seguintes campos na aba Q100:

Nos campos **"Valor de entrada dos recursos"** e **"Valor de saída dos recursos"**, o desdobramento do financeiro será proporcionalizado conforme o que foi definido na aba [Livro Caixa Produtor Rural](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrocaixaprodutorrural) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

O campo **"Valor total do lançamento"** exibe o total do desdobramento de cada financeiro, para conferência.

**Nota:** acionando-se os botões **"Conciliar"** e **"Desfazer Conciliação"**, tem-se o seguinte comportamento, executando-se a funcionalidade em todos os registros Q100 do mês escolhido:

![gif_concilia_ao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4408255520919)

**Importante:** os registros Q100 conciliados, não poderão ser editados ou excluídos e serão encaminhados para o arquivo, diferentemente dos que não foram conciliados.

Para a obtenção do **"Código Sequencial da Conta Bancária" **e **"Código da conta bancária"** dos registros Q100 e 0050, teremos a seguinte hierarquia de busca caso estes estejam preenchidos:

- Campo **"Classificação da conta Produtor Rural"**;

- O campo **"Número da conta Produtor Rural"**;

- Os três primeiros dígitos do **"Código da Conta Bancária"**.

**Observação:** os campos **"Conta Bancária"** e **"Cód. Natureza"** farão ligação com o Cadastro de [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) e a Natureza respectivamente.

[[voltar ao topo]](#top)

## 
Aba Q200

Nesta aba deve-se realizar o preenchimento das informações relativas ao **"Registro Q200 - Resumo Mensal do Demonstrativo do Resultado da Atividade Rural"**.

**Nota:** o registro Q200 faz o resumo mensal dos lançamentos no Q100.

![q200.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408249716119)

[[voltar ao topo]](#top)

## 
Aba 9999

Tem-se nesta aba as informações referentes ao **"Registro 9999 - Identificação do Contador e Encerramento do Arquivo Digital"**.

![9999.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408249826071)

[[voltar ao topo]](#top)

## 
Botões no topo da tela

A Geração do Arquivo LCDPR é composta por abas, as quais descrevemos até aqui e também por botões que executam diversas funções dentro desta rotina. Vejamos sobre eles:

Por meio do botão 

![botão filtros cinza FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315843320983)

 **"Filtros"**, o assistente de configuração de filtros personalizados para a tela será exibido.

No botão 

![botão Modo grade.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315781342359)

 **"Modo grade [F8]"**, alterna-se a visualização da tela entre modo grade e modo formulário; além disto, configura-se a grade da maneira almejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas conforme sua preferência.

Em 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315843324823)

 **"Cadastrar Livro Caixa Digital do Produtor Rural [F8]"**, tem-se a inicialização da Geração do Arquivo LCDPR.

Por meio dos botões 

![botao-anterior-e-proxima-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315781351319)

 **"Próxima"** e **"Anterior"**, o sistema que você navegue entre os registros já cadastrados.

No botão 

![Botão Excluir.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16315781354903)

 **"Excluir [F9]"**, realiza-se a exclusão do registro selecionado na tela.

Ao acionar o botão 

![botao-duplicar FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315843334423)

 **"Duplicar"**, o registro selecionado será duplicado, de forma que um novo registrado será adicionado à tela com as configurações equivalentes àquele primeiramente selecionado.

Quando você utilizar o botão 

![botão Atualizar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315843335831)

 **"Atualizar"**, recarrega-se toda a tela de Geração do Arquivo LCDPR.

Por meio do botão 

![processar FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315781359383)

 **"Processar"**, a apuração ou processamentos dos dados LCDPR, referente às tabelas que contemplam cada registro do layout será realizado. Assim, após esse processamento, o sistema emitirá uma mensagem o confirmando.

Quando você acionar o botão 

![botao-gerar-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16315843339287)

 **"Gerar"**, será gerado o arquivo .txt exigido pela Instrução Normativa RFB N. 1848/2018.

**Nota:** ao acionar este botão, será exibido um pop-up para confirmação da geração do arquivo LCDPR; confirmando esta ação, será exibido o pop-up **"Processos"** para acompanhamento da geração do arquivo. Esse pop-up trará informações detalhadas referentes ao processo de geração do arquivo, como os dados da empresa, o período e andamento dos registros.

O botão 

![botão-histórico-de-gerações.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16344182124311)

 **"Histórico de Gerações"**, exibirá todo o histórico de dados os últimos arquivos gerados.

Por meio do botão 

![botao-exportar-grade-para-pdf-FINAL.jpg](/guide-media/01H6743AM7C5181E5VX745E5ZA)

 **"Exportar grade para PDF"**, apresenta opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

Em 

![botao-anexo-FINAL.jpg](/guide-media/01H6748806TF4YTBWEJSKWJX68)

 **"Anexo"**, pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo LCDPR.

O botão 

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344182131735)

 **"Outras opções..."**, possui as funcionalidades **"Marcar Arquivo como Confirmado"**, **"Desmarcar Arquivo como Confirmado"** e **"Reprocessar Registros Totalizadores"**.

Quando o botão 

![botão-configuração-da-tela-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16344182133783)

 **"Configurações da Tela"** for acionado, pode-se realizar a configuração da tela e suas respectivas abas e campos de forma mais proveitosa e adequada para o usuário. Além disto, será possível determinar como ocorrerá a geração da numeração da tela, seja **"Automática"** ou **"Manual"**.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)
- [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)
- [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)
- [Q100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#abaq100)
- [0050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595274#aba0050)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)
- [Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)
- [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro)
- [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abatop)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa)
- [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaproduto)
- [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)
- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)
- [Livro Caixa Produtor Rural](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrocaixaprodutorrural)
- [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113)