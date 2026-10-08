# Conciliação de Cartão

> **Módulo:** Financeiro e Patrimônio | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334-Concilia%C3%A7%C3%A3o-de-Cart%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334-Concilia%C3%A7%C3%A3o-de-Cart%C3%A3o)  
> **ID:** `360044606334` | **Última Atualização:** 2026-07-29T14:39:12Z

---

```text
 Módulo: Financeiro > Rotinas
```

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16195776354327)

 A apresentação/utilização desta tela no Jiva Om, é vinculada ao produto **"20490 - JIVA-PROCES. DO RETORNO CARTÃO CREDITO"**.

O objetivo desta rotina é permitir a realização de maneira automatizada, a baixa bancária das movimentações financeiras que utilizaram como forma de pagamento o cartão, seja ele crédito ou débito. A tela foi desenvolvida exclusivamente para conciliação de transações de cartão — **PIX TEF não é suportado**.

Este processo acontece com base em um extrato de pagamento, onde a operadora de cartão demonstra o valor repassado ao estabelecimento comercial considerando as operações (vendas) de um determinado período. Normalmente, este arquivo é disponibilizado pela operadora de cartão a partir da adesão de um serviço adicional.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16195757764759)

 O processo tem por objetivo encontrar no sistema, os títulos equivalentes aos já existentes e processados, no entanto, lembre-se que a conciliação bancária ainda deverá ser feita manualmente.

Esta rotina faz sentido em estabelecimentos comerciais onde existe um alto volume de transações, pois, permite realizar o processo de baixa e conciliação bancária de suas vendas de uma forma bastante rápida e segura.

Neste artigo trataremos dos seguintes tópicos:

[Rotina de Processamento](#h_01ENTCKE2DMW0B6K8R23FB7MHW)                                           [Premissas](#h_01ENTCKMPNXCETY3KFDMGG2BH3)

[Campos](#h_01ENTCKX9B1GW8KSWA7D5C5XDF)                                                                    [Ações](#h_01ENTCM3H95BYE57YFBJMHMT2Y)

[Parâmetros que influenciam na rotina](#Par%C3%A2metrosqueinfluenciamnarotina)

 

### Rotina de Processamento

Inicialmente, para utilizar a tela de conciliação, faz-se necessário que você configure o(s) layout(s) para processamento dos arquivos de retorno. Caso ainda não tenha o layout configurado, basta seguir os seguintes passos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16195797069463)

 Acesse a tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054);

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16195797070999)

 Ao abrir a tela, acione o botão em 

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16196055424535)

 **"Outras Opções..."** e em seguida clique em **"Criar arquivo a partir de um modelo"** ou crie um layout do zero conforme a necessidade.

![layout.png](https://ajuda.sankhya.com.br/hc/article_attachments/8499078628887)

Vale ressaltar que a conciliação considera os seguintes campos para o processamento:

- 

TIP_MOVTO - Tipo de Movimento;

- 

NSU_TEF_POS - NSU gerado pelo TEF (Auttar, SiTef, PayGo etc);

- 

NSU_ADQUIRENTE - NSU gerado pela Autorizadora;

- 

COD_AUTORIZACAO - Código da autorização da transação gerado pela Autorizadora;

- 

DT_MOVTO - Data da transação;

- 

QTD_PARCELAS - Quantidade de parcelas da venda, quando a venda for parcelada;

- 

NRO_PARCELA - Número da parcela que está sendo paga;

- 

VLR_PARCELA_LIQ - Valor líquido da parcela (Sem taxa);

- 

VLR_PARCELA - Valor bruto da parcela (Com taxa);

- 

VLR_TAXA_AUTORIZACAO - Valor total da taxa cobrada do cliente pela Autorizadora;

- 

VLR_TRANSACAO - Valor total da transação;

- 

DT_PAGTO -  Se a marcação **"Baixar títulos na data do arquivo"** estiver ativa;

- 

NUM_CONTA_CORRENTE - Caso a marcação **"Priorizar Conta e Empresa do arquivo na baixa"** esteja feita, será usado o número da conta corrente do arquivo em conjunto com o DIGITO_CONTA também do arquivo;

- 

DIGITO_CONTA.

#### **Como é feito o processamento?**

O processamento do arquivo de retorno deverá ser realizado através da tela Conciliação de Cartão.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360081999853)

**Nota: **o processamento do arquivo de retorno da Conciliação de Cartão será realizado, a considerar que as informações em cada linha do arquivo são referentes a títulos distintos.

[[voltar ao topo]](#top)

### Premissas

- 

Ter título(s) não baixados lançados no sistema aguardando o processamento do arquivo para que seja realizada a baixa;

- 

Preencher os campos obrigatório para processamento do arquivo.

[[voltar ao topo]](#top)

### Campos

**Empresa Baixa:** Neste campo informe a empresa responsável pela baixa dos financeiros.

**Conta Bancária Baixa: **Indique aqui a conta que será considerada na baixa dos financeiros.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16195757764759)

 A conta associada ao arquivo não pode estar marcada como** "Exclusiva da empresa"** na aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros) da tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas). Caso essa marcação esteja ativada, o sistema exibirá a seguinte mensagem de erro ao tentar realizar a operação: 

***"A conta bancária não pode ser exclusiva"***

**Tipo Operação Baixa:** Neste campo você apontará o tipo de operação empregado na baixa dos financeiros.

**Lançamento:** Informe aqui o tipo de lançamento que será utilizado na baixa dos financeiros.

[[voltar ao topo]](#top)

### Ações

**Atualizar Taxa Administradora:** Quando esta marcação estiver habilitada, caso exista uma diferença entre a taxa da administradora do financeiro e a taxa do arquivo de retorno, será considerada a taxa do arquivo.

**Observação:** caso a marcação acima esteja ativada, o sistema irá considerar a taxaAdm como o vlrTaxa, se o vlrTaxa for diferente da taxaAdm.

**Priorizar Conta e Empresa do arquivo na baixa:** Esta marcação permite que você defina que na baixa das transações serão utilizadas as informações de Banco, Agência e Conta contidas no arquivo de retorno.

**Botão ****Prévia:** Ao acionar este botão, será exibida uma prévia do processamento do arquivo de retorno. Serão exibidas as informações dos registros que não podem ser baixados por algum motivo, pela rotina, em um arquivo texto. A prévia roda uma simulação de baixa e mostra os retornos do processamento, porém não efetua a baixa.

**Botão ****Processar:** Este botão realiza o processamento do arquivo de retorno baixando os títulos presentes com suas respectivas taxas administrativas.

Ao solicitar a prévia ou processamento do arquivo, a tela tem seu foco direcionado para o resultado do procedimento, onde tem-se os dados do arquivo de retorno da operadora de cartão além das respectivas mensagens de sucesso ou insucesso; nota-se também a possibilidade de criação e utilização de Filtros Personalizados, Filtros de processamento, Filtros de TEF e a busca por registros de acordo com os Usuários que os realizaram.

**Botão Log:** Ao acionar este botão, tem-se a exibição da tela de log para busca de processamentos ou prévias realizadas anteriormente.

**⚠️ Atenção**

Esta tela não suporta a conciliação de transações de **PIX TEF**. O PIX TEF utiliza estrutura e fluxo de processamento diferentes, incompatíveis com o processamento atual de cartão. Caso seja necessário conciliar PIX TEF por esta tela, abra um plano de melhoria.

[[voltar ao topo]](#top)

### **Parâmetros que influenciam na rotina**

**Substitui Conta do Financeiro com Conta Baixa - SUBSTCONTA:** quando este parâmetro está ligado, a conta informada no campo **"Conta"** no momento da baixa de títulos, ou a **"Conta do arquivo"** (caso a marcação **"Priorizar Conta e Empresa do arquivo na baixa"** esteja ativada), substituirá a conta registrada no campo **"Conta Baixa"** no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal) da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

Se o parâmetro estiver desligado, mesmo que uma conta diferente seja informada na baixa de títulos, o sistema manterá a conta registrada originalmente no campo Conta Baixa.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054)
- [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros)
- [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)
- [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)