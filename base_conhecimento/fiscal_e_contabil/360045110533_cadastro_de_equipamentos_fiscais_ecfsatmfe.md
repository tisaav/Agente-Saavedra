# Cadastro de Equipamentos Fiscais  - ECF/SAT/MFE

> **Módulo:** Fiscal e Contábil | **Subseção:** Cadastros e Configurações Fiscais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110533-Cadastro-de-Equipamentos-Fiscais-ECF-SAT-MFE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110533-Cadastro-de-Equipamentos-Fiscais-ECF-SAT-MFE)  
> **ID:** `360045110533` | **Última Atualização:** 2026-09-15T17:51:46Z

---

```text
**

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312047617943)

**

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312047621015)

****
```

| Módulo: Comercial > Arquivo > Cadastros    Versão disponível: A partir da 4.12 |
| --- |

Empresas que trabalham com ECF (Emissão de Cupom Fiscal), SAT (Sistema Autenticador e Transmissor de Cupons Fiscais Eletrônicos) ou MFE (módulo Fiscal Eletrônico), podem efetuar nesta tela o cadastro dos dados referentes ao equipamento fiscal.

```text
**

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16033256047127)

******
```

| Atenção: os equipamentos SAT e MFE são utilizados apenas no sistema operacional Windows |
| --- |

Assim, abordaremos neste artigo os seguintes tópicos:

- [Configurações da tela](#Configura%C3%A7%C3%B5esdatela)   

- [Web Connection](#WebConnection)                                                            

- [Modo Homologação](#ModoHomologa%C3%A7%C3%A3o)

- [Compartilhamento do equipamento](#Compartilhamentodoequipamento)

- [Como vincular o equipamento ao usuário](#Comovincularoequipamentoaousu%C3%A1rio) 

![Screenshot_89.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/6921964576791)

### 
Configurações da tela

Para iniciar o cadastro, preencha o campo **"Cód. Equipamento"**, em seguida, busque no campo **"Empresa"**, o código da empresa que emite os cupons fiscais ou cupom fiscal eletrônico.

Agora, no campo **"Tipo Equipamento"** informe qual equipamento a empresa utiliza, **"ECF"**, **"SAT" **ou **"MFE"**.

**Observações:** 

- Para utilizar o equipamento SAT deve ser liberado o opcional **"30784 - CUPOM FISCAL ELETRÔNICO (SAT) / W"**, já para o equipamento MFE deve ser concedido o opcional **"30365 - CUPOM FISCAL ELETRÔNICO (MFE) / W"**.

- O cadastro dos equipamentos SAT e MFE será utilizado para a emissão de notas no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

**Nota: **o botão 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/19934150329239)

 **"Edição múltipla" **permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com os cadastros em modo grade na tela Cadastro de Equipamentos Fiscais - ECF/SAT/MFE selecione-os e em seguida clique no botão Edição múltipla, assim os campos poderão ser editados simultaneamente para os cadastros selecionados.

Para conhecer o cadastro de cada tipo de equipamento, clique nas opções abaixo:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312031367447)

[#ECF](#ECF)

![mceclip0__4_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312047624983)

[#SAT](#SAT)

![mfe.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312047625751)

[#MFE](#MFE)

|  |  |  |
| --- | --- | --- |

#### 

![Marcador](/guide-media/01H53308M80KR451JCYHFRPM3P)

 ** ****ECF**

Com a opção ECF selecionada, no topo da tela clique no botão **"Salvar"**. Desse modo, será apresentada a aba **"ECF"**.

![ECF_2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/6922021173783)

Primeiramente informe o** "Cód. Máquina"**. Em seguida, selecione a** "Marca"** da impressora conforme as opções abaixo:

- URANO

- BEMATECH

- DARUMA

- DATAREGIS

- ELGIN

- INTERWAY

- SWEDA

**Observação:** as marcas já configuradas são as que estão homologadas no sistema; caso haja alguma impressora nova, esta deverá ser implementada.

Insira o código da empresa que emite os cupons fiscais no campo** "Empresa"**.

Registre no campo** "Modelo Equipamento" **o modelo da impressora, por exemplo, para a marca BEMATECH o modelo poderia ser MP2100 TH FI.

Depois, preencha no campo** "Tipo Equipamento ECF" **o tipo de impressora; por exemplo, se for BEMATECH poderia ser ECF-IF.

Informe também o **"Código CNIEE" **(Código Nacional de Identificação de Equipamento ECF) que é fornecido pela Secretaria da Fazenda e necessário para a geração dos arquivos de movimentação exigidos.

No campo** "Modelo do Documento" **defina o modelo a ser utilizado na impressora fiscal. Temos as seguintes opções:

- 2B (para máquina registradora);

- 2C (para PDV);

- 2D (para ECF).

Configure o** "Tipo do Documento"** de acordo com as seguintes alternativas:

- PDV;

- ECF.

Indique no campo **"Fuso Horário"** qual o fuso horário do local, como exemplo: a base de dados poderá encontrar-se em um local do país e a impressora de cupom fiscal poderá estar em outro local; assim, pode acontecer de haver um fuso horário e, como a impressora fiscal valida esta data/hora, deve-se preencher este campo.

O campo** "Número ECF" **poderá ser preenchido por meio do documento que é emitido na liberação da impressora para utilização. Trata-se do número físico do checkout.

Em relação ao campo** "Número Usuário"**, este será preenchido automaticamente pelo sistema após a leitura da primeira Redução Z deste ECF.

Ainda sobre o campo acima, ele poderá ser informado por você ou pelo Fast Service. Além disso, quando já existir movimento para o ECF, este campo ficará desabilitado.

Realizadas as configurações acima, clique em **"Salvar"** para finalizar o cadastro.

[[voltar ao subtítulo]](#Configura%C3%A7%C3%B5esdatela) 

#### 

![Marcador](/guide-media/01H53308M80KR451JCYHFRPM3P)

 **SAT**

Com a opção SAT selecionada, no topo da tela clique no botão **"Salvar"**. Desse modo, será apresentada a aba **"SAT"**.

![sat_1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/6922023475735)

Primeiramente informe o **"Cód. Ativação"** do equipamento. 

Em seguida, selecione o **"Modelo"** do equipamento segundo as seguintes alternativas: 

- TANCA 

- DIMEP

- ELGIN

**Observação:** os modelos homologados, com suporte garantido, estão listados acima. Equipamentos de outras marcas ou modelos não citados necessitam de uma análise de viabilidade de mercado antes da sua implementação.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16033256047127)

 Estes modelos são para uso no [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367-Portal-de-Caixa) e [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

**Observação:** efetue a abertura de um ticket ao Service desk com o CNPJ no qual será associado o aparelho SAT, para que o consultor de atendimento realize o procedimento em credenciar e gerar uma chave criptografada do CNPJ do cliente com o nosso Software House.

Feito isso, preencha o campo **"Assinatura"** com a assinatura gerada a partir do contato com o nosso Service Desk.

Por meio do campo **"Histórico"**, você poderá obter as informações de retorno quando as opções do botão **"Outras Opções"** forem acionadas.

 

**Botão Outras Opções**

Através do botão Outras Opções, temos as seguintes funcionalidades para a rotina SAT:

![Imagens_ksnip_95_.png](https://ajuda.sankhya.com.br/hc/article_attachments/6922054177175)

Ao clicar na opção **"Ativar SAT"**, será realizada a comunicação dos aparelhos SAT com o Sankhya Om. 

Para efetuar testes de comunicação entre a Aplicação do Comercial (AC) e o Equipamento  SAT utilize a função **"Consulta SAT"**.

A opção **"Consultar Status Operacional"** é responsável por verificar a situação de funcionamento do Equipamento SAT. Sendo que, a consulta da AC para o Equipamento SAT deverá ser realizada através desta opção.

A função **"Teste Fim a Fim"** consiste em um teste de comunicação entre a AC, o Equipamento  SAT e a SEFAZ.

Pode-se ainda, por meio deste botão **"Associar Assinatura SAT"**, **"Atualizar Software SAT"** e **"Extrair Log SAT"**. 

Após utilizar estas opções, o retorno dos dados do aparelho serão exibidos no campo **"Histórico"**.

```text
**

![dica](https://ajuda.sankhya.com.br/hc/article_attachments/42312031370903)

******
********
```

| Dica: você pode exportar as informações apresentadas no campo Histórico, no formato "TXT.". Para isso, acione o botão "Extrair Histórico". |
| --- |

[[voltar ao subtítulo]](#Configura%C3%A7%C3%B5esdatela)

#### 

![Marcador](/guide-media/01H53308M80KR451JCYHFRPM3P)

 **MFE **

Com a opção MFE selecionada, clique no botão **"Salvar" **localizado no topo da tela. Desse modo, será apresentada a aba **"MFE"**.

**

![MFE_2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/7135306467607)

**

Primeiramente selecione o **"Modelo"** do equipamento de acordo com as seguintes alternativas: 

- TANCA

- DIMEP

- ELGIN

**Observação:** os modelos homologados, com suporte garantido, estão listados acima. Equipamentos de outras marcas ou modelos não citados necessitam de uma análise de viabilidade de mercado antes da sua implementação.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16033256047127)

 Estes modelos são para uso no [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367-Portal-de-Caixa) e [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

Em seguida, informe o **"Cód. Ativação"** do equipamento. 

**Observação:** efetue a abertura de um ticket ao Service desk com o CNPJ no qual será associado o aparelho MFE, para que o consultor de atendimento realize o procedimento em credenciar e gerar uma chave criptografada do CNPJ do cliente com o nosso Software House.

Feito isso, preencha o campo **"Assinatura"** com a assinatura gerada a partir do contato com o nosso Service Desk.

Por meio do campo **"Histórico"**, você poderá obter as informações de retorno quando as opções do botão **"Outras Opções"** forem acionadas.

 

**Botão Outras Opções **

Através do botão Outras Opções, temos as seguintes funcionalidades para a rotina MFE:

![Imagens_ksnip_155_.png](https://ajuda.sankhya.com.br/hc/article_attachments/7135386813335)

Ao clicar na opção **"Ativar MFE"**, será realizada a comunicação dos aparelhos MFE com o Sankhya Om. 

Para efetuar testes de comunicação entre a Aplicação do Comercial (AC) e o Equipamento  MFE, utilize a função **"Consulta MFE"**.

A opção **"Consultar Status Operacional"** é responsável por verificar a situação de funcionamento do Equipamento MFE. Sendo que, a consulta da AC para o Equipamento MFE deverá ser realizada através desta opção.

A função **"Teste Fim a Fim"** consiste em um teste de comunicação entre a AC, o Equipamento  MFE e a SEFAZ.

Pode-se ainda, por meio deste botão **"Associar Assinatura MFE"**, **"Atualizar Software MFE"** e **"Extrair Log MFE"**. 

Após utilizar estas opções, o retorno dos dados do aparelho serão exibidos no campo **"Histórico"**.

```text
**

![dica](https://ajuda.sankhya.com.br/hc/article_attachments/42312031370903)

******
********
```

| Dica: você pode exportar as informações apresentadas no campo Histórico, no formato "TXT.". Para isso, acione o botão "Extrair Histórico". |
| --- |

[[voltar ao subtítulo]](#Configura%C3%A7%C3%B5esdatela) [[voltar ao topo]](#top)

### 
Web Connection

O [Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection) é uma aplicação que trabalha separado do **Sankhya Om**, isto é, ele é a ponte de comunicação de aparelhos (hardware) com a plataforma **Sankhya Om** (software). Assim, Web Connection deve ser ativo na máquina onde o aparelho SAT ou MFE estiver instalado para haver a comunicação com o **Sankhya Om**. **
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22709285601175)

 **Considerações importantes sobre o MFE:**

- 
Deve-se utilizar o Web Connection 32 bits, devido ao uso da dll 32 bits dos modelos homologados, logo esteja atento a qual estrutura está instalada no [Navegador Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599474);

- 
A partir da versão 4.25 o uso do Web Connection na versão 2.0b605 não é mais restrito apenas para o Navegador Sankhya, ficando disponível o uso com browsers padrões, como, Chrome, Edge e Firefox.

**Importante: **o Web Connection deve sempre estar na última versão disponível e ser utilizado o Web Connection Externo ou o embarcado no Navegador Sankhya (32 ou 64 bits).

[[voltar ao topo]](#top)

### 
Modo Homologação

A seção** "Homologação"** está disponível nas abas SAT e MFE, nela você pode configurar os equipamentos em modo homologação, para isso, basta acionar a marcação **"Homologação"** e informar o **"CNPJ Software House"**.

```text

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16033256047127)

****

```

| Atenção: este procedimento é utilizado exclusivamente para validações e testes funcionais de comportamento do aparelho antes de ativado em outra Software House. |
| --- |

![Imagens_ksnip_157_.png](https://ajuda.sankhya.com.br/hc/article_attachments/7135504666391)

[[voltar ao topo]](#top)

### 
Compartilhamento do equipamento

A seção **"Compartilhamento do equipamento"** está disponível nas abas SAT e MFE, nela você pode configurar para que o uso do aparelho fiscal ocorra em mais de um computador. Para isso, habilite a marcação** "Compartilhado"** e preencha o campo **"IP de Compartilhamento"** com o IP da localização do aparelho mais a porta do Webconection que está em compartilhamento, por exemplo, **"0.0.0.0:9096"**.

![Imagens_ksnip_169_.png](https://ajuda.sankhya.com.br/hc/article_attachments/7570035789079)

**Nota:** no uso da marcação Compartilhado, apenas o IP da máquina a ser compartilhada será aceito.

[[voltar ao topo]](#top)

### 
Como vincular o equipamento ao usuário 

Com as configurações acima realizadas, vincule o cadastro do tipo de equipamento SAT ou MFE ao usuário, por meio do campo **"Equipamento Fiscal"**, presente na aba [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#AbaAcessosPDVWeb), da tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874). Desse modo, será permitido o uso das funções do botão **"CF-e"**, localizado na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo), da tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela).

![Imagens_ksnip_159_.png](https://ajuda.sankhya.com.br/hc/article_attachments/7137557059223)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web)
- [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367-Portal-de-Caixa)
- [Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection)
- [Navegador Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599474)
- [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#AbaAcessosPDVWeb)
- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo)
- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela)