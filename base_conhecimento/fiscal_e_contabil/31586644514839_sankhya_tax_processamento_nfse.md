# Sankhya Tax - Processamento NFSe

> **Módulo:** Fiscal e Contábil | **Subseção:** Sankhya TAX  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31586644514839-Sankhya-Tax-Processamento-NFSe](https://ajuda.sankhya.com.br/hc/pt-br/articles/31586644514839-Sankhya-Tax-Processamento-NFSe)  
> **ID:** `31586644514839` | **Última Atualização:** 2026-08-12T19:53:36Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315417205911)

 **Módulo: **Configurações > Rotinas         

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315420109847)

 **Versão disponível: **a partir da 4.31
```

A tela de **Processamento NFS-e** permite que o usuário preencha manualmente as informações necessárias para integrar uma Nota Fiscal de Serviço Eletrônica (NFS-e) ao sistema, mesmo quando não há um modelo de integração previamente configurado. Essa funcionalidade é especialmente útil para garantir que documentos fiscais sejam processados corretamente em situações mais específicas ou fora do padrão habitual.

![Procesamento NFSe.png](https://ajuda.sankhya.com.br/hc/article_attachments/31586644511511)

#### ****
[Quando utilizar essa tela?](#Quandoutilizaressatela)
[Campos da tela](#Camposdatela)
[Funcionamento](#Funcionamento)
[Parâmetros que influenciam a rotina](#Par%C3%A2metrosqueinfluenciamnessarotina)

| Funcionalidades da tela |
| --- |
|  |
|  |
|  |
|  |

### 
**Quando utilizar essa tela?**

Esta tela é utilizada para gerenciar a integração de NFS-e, permitindo configurar informações essenciais como **Empresa, Tipo de Operação, Natureza, Parceiro, Serviço**, entre outros campos relacionados à entrada de notas de serviço. Além disso, possibilita a **consulta dos registros já processados**, facilitando a verificação das configurações aplicadas em cada integração e oferecendo **maior controle e rastreabilidade do processo**.

#### **Como os dados chegam nessa tela?**

A origem dos dados apresentados na tela de vinculação manual é a **integração ASIS**, que realiza a captura automática das NFS-e diretamente da prefeitura ou do provedor do município.

Após a **configuração dos tokens de autenticação** e da integração NFS-e na plataforma **Kolossus (ASIS)**, as notas fiscais são recebidas e, quando o processo de integração automática não pode ser concluído (por ausência de modelo, dados inconsistentes, ou regras específicas de negócio), os dados são direcionados para a **tela de Processamento NFSE**, onde ficam disponíveis para vinculação manual.

Dessa forma, **toda a **[configuração de integração,](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados-ASIS)** tais como: adicionar e editar Nota Modelo**, antes obrigatória, será opcional.

### 
**C****ampos da tela**

Ao processar a nota, será possível preencher as informações das seguintes abas: **Informações da Nota**, **Dados do Prestador** e **Serviço Prestado**, dentro delas contém campos que devem ser preenchidos manualmente, sendo alguns deles obrigatórios para que a integração seja concluída com sucesso. 

São considerados obrigatórios os campos **Empresa**, **TOP (Tipo de Operação)**, **Tipo de Negociação**, **Parceiro** e **Serviço**, pois são essenciais para o correto entendimento e processamento da nota fiscal pelo sistema. 

Já os campos **Natureza**, **Centro de Resultado** e **Projeto** são opcionais e podem ser utilizados conforme a necessidade de classificação e controle interno da empresa.

[[voltar ao topo]](#top)

### 
**Funcionamento **

O preenchimento manual permite maior flexibilidade, especialmente em casos onde não há modelos previamente cadastrados. 

Se os dados da nota já tiverem sido vinculados anteriormente, como na empresa ou do tipo de serviço, o sistema reaproveita essas informações e permite que a integração ocorra sem a necessidade de preenchê-los novamente. 

Quando há alteração no tipo de serviço, o sistema exige que esse campo seja preenchido, pois ainda não há vínculo anterior para a nova configuração. Caso seja utilizado um modelo já cadastrado, os campos são preenchidos automaticamente, otimizando o tempo do usuário e garantindo maior consistência nas integrações. 

Vale destacar que, se o tipo de serviço informado na nota for diferente daquele previsto em contrato, o sistema emitirá um aviso, mas permitirá a continuidade do processamento normalmente.

Após o preenchimento dos campos, siga para **Validar importação**, feito isso, a nota que antes possui status de **“Com divergência” **passa a ter status de** “Processada”**, sendo possível ainda visualizar a nota integrada diretamente pela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), ao clicar no número visível na coluna **Nota Integrada**.

**Observação: **notas exibidas com o status **"Não processada" **são aquelas cuja requisição de integração não chegou a ser executada, geralmente devido à duplicidade de dados ou inconsistências que impedem o início do processamento.

#### **Informações importantes acerca desta rotina**

- Esta tela permite apenas visualizar a integração de notas fiscais de serviço, sem possibilidade de edição ou processamento manual.

- Não será possível integrar notas fiscais eletrônicas que contenham itens com tipos de serviço diferentes dentro do mesmo documento. Isso deve ser considerado no momento do uso, para evitar inconsistências ou falhas no processo de integração.

**Exemplos de uso:**

- Um exemplo comum de uso é quando o usuário precisa realizar a primeira vinculação manual de uma nota fiscal, preenchendo todos os campos obrigatórios para garantir a integração.

- Outro cenário é quando a nota já foi parcialmente vinculada em um momento anterior e os dados existentes são reaproveitados automaticamente, exigindo apenas ajustes pontuais.

- Também é possível utilizar a tela em conjunto com modelos previamente salvos, nos quais todas as informações são preenchidas de forma automática. 

- Além disso, se houver tentativa de integrar uma nota que já foi vinculada anteriormente, o sistema impedirá a duplicidade e informará o usuário sobre a situação. 

- Em casos em que o tipo de serviço diverge do contrato, o sistema alertará, mas permitirá que a integração seja concluída normalmente.

[[voltar ao topo]](#top)

### 
**Parâmetros que influenciam nessa rotina**

**TPVSEMVALNATCUS - Lista Tip.Mov. sem validação EXIGNATCFR/EXIGCRCFR:** esse parâmetro define uma **lista de Tipos de Movimento **que ficarão **isentos da exigência** dos parâmetros, logo, se o Tipo de Movimento da nota estiver incluída na lista deste parâmetro, os campos *Natureza* e *Centro de Resultado* continuam sendo exibidos, mas não serão obrigatórios, mesmo que o sistema esteja configurado para exigi-los, em geral.

**EXIGCRCFR - Exigir CR na central/financeiro/rateio?: **este parâmetro define se o **Centro de Resultado (CR)** será obrigatório nas telas de integração ou rateio de documentos financeiros.

- 
**Se estiver ativado**: o sistema irá exigir o preenchimento do campo *Centro de Resultado* ao integrar uma nota ou ao realizar lançamentos financeiros/rateios.
 

1. 
**Se estiver desativado**: o preenchimento do *Centro de Resultado* será opcional.

**EXIGNATCFR - Exigir natureza na central/financeiro/rateio?: **esse parâmetro determina se o campo **Natureza de Custo** será obrigatório nas telas de integração, financeiro e rateio.

- Se estiver ativado: o sistema obriga o preenchimento do campo Natureza de Custo para processar a integração ou lançamento.

- Se estiver desativado: o campo permanece opcional, permitindo seguir sem preenchê-lo.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [configuração de integração,](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados-ASIS)
- [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)