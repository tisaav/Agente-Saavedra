# Gestão de Fechamento de Caixa

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24340556304919-Gest%C3%A3o-de-Fechamento-de-Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/24340556304919-Gest%C3%A3o-de-Fechamento-de-Caixa)  
> **ID:** `24340556304919` | **Última Atualização:** 2026-07-29T14:18:13Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311635042839)

 Módulo: **Comercial > Arquivo                

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311635043863)

** Versão disponível: **A partir da 4.29
```

Na tela Gestão de Fechamento de Caixa é possível consultar os fechamentos de caixas de períodos anteriores. Esta tela permite ainda lançar ocorrências, confirmar os fechamentos e transferir o saldo da conta caixa para a conta tesouraria.

#### ****

[Requisitos para utilizar essa rotina](#Requisitosparautilizaressarotina)

[Filtros](#Filtros)

[Confirmar Caixa](#ConfirmarCaixa)

[Ocorrências](#Ocorr%C3%AAncias)

[Botão Outras Opções](#Bot%C3%A3oOutrasOp%C3%A7%C3%B5es)

| Funcionalidades da tela |
| --- |
|  |
|  |
|  |
|  |
|  |

## **Requisitos para utilizar essa rotina**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25101216404631)

 Os caixas PDVs devem estar cadastrados na tela [Cadastro de PDV](https://ajuda.sankhya.com.br/hc/pt-br/articles/20060894293399-Cadastro-de-PDV);

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25101171806743)

 O acesso a essa tela deve ser liberado na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854);

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25994187050007)

 O perfil do usuário, seja Gerente de Caixa ou Gerente Financeiro (configuração realizada na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), por meio das marcações **"Gerente Caixa"** e **"Gerente Financeiro"**), determinará os recursos que serão disponibilizados na tela;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25101216414871)

 Para acompanhar os fechamentos de caixa, ao realizar o login no **Sankhya Om** com o usuário Gerente Financeiro, se houver caixas fechados com data anterior ao login e com quebra de caixa, uma notificação será exibida em seu sistema.

[[voltar ao topo]](#top)

## **Filtros**

### **Filtros Rápidos**

Na parte superior da tela são apresentados os Filtros Rápidos, que facilitam a busca dos registros. Pode-se informar a **"Empresa"**, o **"Cód. PDV"** e a data de fechamento de caixa.

No filtro **"Situação do Caixa PDV"** é possível filtrar o registro **"Fechado"**, **"Validado" **ou **"Confirmado"**.

Em **"Divergentes + Conformes"**, pode-se indicar a situação do caixa, isto é, se está **"Sem divergências"**, **"Positiva"** ou **"Negativa"**.

![Filtros-Rápidos.png](https://ajuda.sankhya.com.br/hc/article_attachments/24558261137559)

### **Filtros Personalizados**

Além dos filtros fixos descritos acima é possível utilizar o botão 

![Filtros FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24558261141655)

 **"+Filtros"** para criar filtros personalizados, que permitem uma exibição mais ágil e específica dos registros.

![Filtros personalizados.png](https://ajuda.sankhya.com.br/hc/article_attachments/24340658223895)

[[voltar ao topo]](#top)

## **Confirmar Caixa**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/24648108595863)

 Este botão estará disponível para usuários logados que tenham a marcação **"Gerente Financeiro"** configurada no cadastro de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana).

Para confirmar o caixa, selecione um registro cujo **"Status Caixa"** esteja igual a** "Fechado"** ou **"Validado"** e clique em 

![Botão Confirmar Caixa Final.png](https://ajuda.sankhya.com.br/hc/article_attachments/24559953994135)

 **"Confirmar Caixa"**.

![Tela Gestão de Fechamento de Caixa.png](https://ajuda.sankhya.com.br/hc/article_attachments/24340658211223)

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34837315650583)

 Impacto na Devolução de NF-e**

A confirmação do caixa é um processo que **finaliza a conciliação** dos movimentos registrados (incluindo vendas, suprimentos, sangrias e **devoluções**).

Uma vez que o caixa esteja **"Confirmado"**, qualquer Nota Fiscal Eletrônica (NF-e) de **devolução** cujo movimento tenha sido registrado neste caixa terá o seu **cancelamento bloqueado** pelo sistema. O vínculo do movimento com o caixa fechado prevalece sobre o prazo legal de 24 horas para cancelamento da NF-e, resultando na mensagem: **'O caixa desse cupom já foi fechado.'**.

Por esta razão, certifique-se de que não há pendências de cancelamento de documentos fiscais vinculados aos movimentos do caixa **antes de proceder com a confirmação**. Em casos de necessidade de cancelamento de NF-e de devolução após a confirmação do caixa, será necessário buscar um **ajuste contábil/fiscal** apropriado para desfazer a operação.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24560856569623)

 Caso o caixa apresente divergências (positivas ou negativas), o sistema não permitirá a confirmação e exibirá a seguinte mensagem:

***"Caixa PDV com divergências. Ajuste os lançamentos das ocorrências para confirmação posterior."***

**Entendendo a Divergência e a Quebra de Caixa**

O sistema considera uma **divergência** quando o valor **Informado** é diferente do valor **Calculado** na tela de **Funções de Caixa**. O valor **Calculado** é o total das vendas, enquanto o valor **Informado** é a soma do dinheiro físico no caixa com os valores de sangria e suprimento.

**Exemplo:** Se as vendas à vista totalizaram **R$ 100,00** e foi feita uma sangria de **R$ 10,00**, o dinheiro físico no caixa será de **R$ 90,00**. No entanto, o sistema considerará o valor **Informado** como **R$ 100,00** (a soma dos R$ 90,00 no caixa com a sangria de R$ 10,00). Neste caso, **não há quebra de caixa**, e o fechamento pode ser confirmado sem a necessidade de lançar ocorrências.

A coluna **Vlr. Quebra de Caixa** na grade inferior da tela **Gestão de Fechamento de Caixa** é apenas **informativa**. Ela não impede a confirmação do fechamento, a menos que haja uma divergência real. Se você lançar uma ocorrência para ajustar uma "quebra" inexistente, o sistema pode interpretar isso como uma nova divergência, bloqueando a confirmação.

Após a confirmação do caixa, se a conta bancária do PDV tiver saldo positivo, um pop-up será exibido para sugerir a transferência do valor.

- 

O pop-up exibe o **saldo total da conta bancária**, não apenas o saldo do caixa que está sendo fechado.

- 

A transferência é opcional; você pode fechar o pop-up e o caixa será confirmado normalmente.

![Pop-up Transferencia de Saldo.png](https://ajuda.sankhya.com.br/hc/article_attachments/24560856573079)

Para realizar a transferência, informe os campos abaixo:

- Cód. Tipo Operação;

- Vlr. Lançamento;

- Lançamento Origem;

- Lançamento Destino;

- Histórico.

Com essas informações preenchidas, clique em **"Transferir"**. Desse modo, o sistema efetuará a transferência do saldo entre as contas, e irá registrar a operação na [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653). Além disso, o [Saldo Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606234) das contas de origem (conta caixa do PDV) e destino (conta tesouraria do PDV) serão atualizados.

[[voltar ao topo]](#top)

## 
**Ocorrências**

Caso queira cadastrar uma ocorrência no caixa PDV, selecione o registro e acione o botão **"Ocorrência"** no painel inferior. 

![Painel inferior - botão Ocorrência.png](https://ajuda.sankhya.com.br/hc/article_attachments/24569764972951)

Na tela que será apresentada serão exibidas todas as ocorrências cadastradas no caixa selecionado.

![Ocorrências.png](https://ajuda.sankhya.com.br/hc/article_attachments/24569772438423)

**Importante:** não é possível excluir uma ocorrência que já possui registros financeiros gerados.

Para registrar uma ocorrência, clique em **"Adicionar Ocorrência" **e preencha os dados obrigatórios.

![Cadastrar Registro.png](https://ajuda.sankhya.com.br/hc/article_attachments/24570373623063)

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24560856569623)

 Se a opção **"Gera Título Financeiro?"** não estiver marcada, o campo **"Motivo de não gerar título Financeiro"** deve ser preenchido.

### **Análise de Ocorrências de Caixa**

#### **Pré-Visualizar Títulos**

Ao acionar o botão** "Pré-Visualizar Títulos"**, será possível visualizar na grade inferior o cálculo prévio dos valores financeiros de receita ou despesa que serão posteriormente gerados na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

![Análise de Ocorrências de Caixa.png](https://ajuda.sankhya.com.br/hc/article_attachments/24590119037463)

**Cálculo do Título:**

- Se o resultado da subtração (soma das ocorrências de receita do parceiro menos (-) a soma das ocorrências de despesa do parceiro) for negativo, o título gerado para o parceiro será de receita (contas a receber).

- Se o resultado da subtração (soma das ocorrências de receita do parceiro menos (-) a soma das ocorrências de despesa do parceiro) for positivo, o título gerado para o parceiro será de despesa (contas a pagar).

**Cálculo do Vencimento dos Títulos:**

- A **"Dt. Vencimento"** dos títulos será calculada considerando a "data atual + o valor definido no campo **"Período até o Vencimento (em dias)"**. Considere o seguinte exemplo:

Se o valor do campo Período até o Vencimento (em dias) for igual a **"7"** (sete) dias, e a data atual for 23/04/2024, então a Dt. Vencimento será 30/04/2024.

 

#### **Gerar Títulos**

Após selecionar um ou mais títulos na pré-visualização dos financeiros e clicar em** "Gerar Títulos"**, o sistema irá gerar todos os títulos selecionados na Movimentação Financeira.

Ao acessar a tela Movimentação Financeira e selecionar o título gerado, o número da ocorrência poderá ser verificado no campo** "Nr. da Ocorrência Caixa"** na guia [Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal).

**Importante:** para excluir um título financeiro gerado a partir de ocorrências, é necessário limpar as informações do campo Nr. da Ocorrência Caixa.

[[voltar ao topo]](#top)

## 
**Botão Outras Opções**

### **Analisar Ocorrências**

Ao selecionar esta opção, a tela **"Análise de Ocorrências de Caixa"** é exibida. Ela permite que você revise todas as ocorrências de todos os caixas e decida se os lançamentos financeiros devem ser feitos ou não.

É importante notar que esta função é propositalmente global. Ela não filtra as ocorrências por caixa, pois o objetivo é ter uma visão completa para análise e ajustes financeiros.

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24601860011415)

 Acesse também:

[PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047)


---

### 🔗 Links e Referências Internas:

- [Cadastro de PDV](https://ajuda.sankhya.com.br/hc/pt-br/articles/20060894293399-Cadastro-de-PDV)
- [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854)
- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)
- [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana)
- [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653)
- [Saldo Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606234)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)
- [Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal)
- [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047)