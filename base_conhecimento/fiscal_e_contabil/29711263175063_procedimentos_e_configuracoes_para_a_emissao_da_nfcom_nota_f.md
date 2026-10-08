# Procedimentos e configurações para a emissão da NFCom (Nota Fiscal Fatura de Serviços de Comunicação Eletrônica)

> **Módulo:** Fiscal e Contábil | **Subseção:** NFCom  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/29711263175063-Procedimentos-e-configura%C3%A7%C3%B5es-para-a-emiss%C3%A3o-da-NFCom-Nota-Fiscal-Fatura-de-Servi%C3%A7os-de-Comunica%C3%A7%C3%A3o-Eletr%C3%B4nica](https://ajuda.sankhya.com.br/hc/pt-br/articles/29711263175063-Procedimentos-e-configura%C3%A7%C3%B5es-para-a-emiss%C3%A3o-da-NFCom-Nota-Fiscal-Fatura-de-Servi%C3%A7os-de-Comunica%C3%A7%C3%A3o-Eletr%C3%B4nica)  
> **ID:** `29711263175063` | **Última Atualização:** 2026-09-15T16:56:07Z

---

```text
 Versão disponível: A partir da 4.33
```

A NFCom (Nota Fiscal Fatura de Serviços de Comunicação Eletrônica) é um documento eletrônico que o cliente recebe ao contratar serviços de telecomunicação ou outros oferecidos pela operadora.

Ela substitui as notas fiscais de [modelo 21 e 22](https://ajuda.sankhya.com.br/hc/pt-br/articles/7405986347799-Configura%C3%A7%C3%B5es-Para-Emiss%C3%A3o-de-NF-Modelo-21-e-22) através do modelo eletrônico 62.

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29712047969559)

 Saiba mais sobre esses modelos no artigo: [FUST/FUNTTEL](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409827525783-FUST-FUNTTEL).

Para iniciar as configurações de emissão do modelo 62 é necessário ter as configurações dos modelos anteriores conforme os documentos de apoio e seguir com as novas configurações para emissão do novo modelo.

#### ****
[Cadastro de Produtos ou Cadastro de Serviços](#CadastrodeProdutosouCadastrodeServi%C3%A7os)
[Cadastro de Parceiros](#CadastrodeParceiros)
[Tipos de Operação - TOP](#TiposdeOpera%C3%A7%C3%A3oTOP)
[Configuração do Layout da Nota](#Configura%C3%A7%C3%A3odoLayoutdaNota)
[Modelos de Nota Fiscal/Duplicatas/Boleto(s)](#ModelosdeNotaFiscal/Duplicatas/Boleto(s))
[Procedimentos para Substituição, Cancelamento e Contingência](#ProcedimentosparaSubstitui%C3%A7%C3%A3oCancelamentoConting%C3%AAncia)
[Obrigações acessórias](#Obriga%C3%A7%C3%B5esacess%C3%B3rias)

| Passo a passo |
| --- |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

### 
**Cadastro de Produtos ou Cadastro de Serviços**

Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) (do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)) ou aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abageral) (do [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)):

**1.** Preencha o campo **"Cód. Item NFCom"**, na seção **NFCom**, conforme o produto ou serviço configurado.

**Nota:** o campo Cód. Item NFCom é alimentado por uma tabela específica informada pela [Sefaz](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass), inserida no sistema, podendo ser consultada pela tela **"Código de Itens da NFCom"**.

![Código de Itens da NFCom.png](https://ajuda.sankhya.com.br/hc/article_attachments/29711263156887)

**2.** Informe o **"Tipo de Utilização"**.

**Observação:** caso selecione a opção **"1 - Telefonia"**, será necessário informar na aba [Números dos Terminais Telefônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#aban%C3%BAmerosdosterminaistelef%C3%B4nicos), da tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), as seguintes informações:

- 

**Número de Identificação do Terminal Telefônico**;

- 

**UF**;

- 

Se é o número “**Principal”** ou não.

**Importante:** essa aba será habilitada quando o parâmetro **"Habilita de campos de Comunicação e Telecomunicação - UTILCAMPOCT"** for ligado.

**3.** Na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) (do Cadastro de Produtos) ou aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) (do Cadastro de Serviços)

Configure os campos **"Calcular FUNTTEL?"** e **"Calcular FUST?"**, selecionando **"Sim"** ou **"Não"**. 

[[voltar ao topo]](#top)

### 
**Cadastro de Parceiros**

No campo **"Tipo Cliente de Serviços de Comunicação"**, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), escolha uma das opções disponíveis. 

O campo **Código de identificação do consumidor ou assinante** (tag `iCodAssinante`) na aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) é mais flexível:

- 
**Novo Limite:** O sistema permite informar um código com até **30 caracteres** (anteriormente o limite era menor).

- 
**Validação:** Se você tentar inserir um código que ultrapasse esse limite de 30 caracteres, o sistema bloqueará a operação e mostrará uma mensagem de alerta.

### **Regras para Destinatários no Exterior (UF = EX)**

Para facilitar a emissão de notas para fora do Brasil, o sistema agora gerencia de forma inteligente os campos de país:

Os campos “**País"** e "**Nome do País"** só aparecerão para preenchimento quando a UF selecionada for **"EX"** (Exterior). Se a UF for qualquer uma das unidades federativas do Brasil, esses campos permanecerão ocultos para simplificar o preenchimento e evitar erros no XML.

**No XML:** As tags de país só serão incluídas no arquivo enviado à SEFAZ se a nota for de exportação (UF = EX).

[[voltar ao topo]](#top)

### 
**Tipos de Operação - TOP**

Em caso de operação de venda, cadastre uma **TOP de Venda** específica para serviços de comunicação e/ou telecomunicação. Em caso de operação de compra, cadastre uma **TOP de Compra **específica para serviços de comunicação e/ou telecomunicação. 

Na aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe) preencha o campo **"Modelo de Documento"** com a opção** "62 - Nota Fiscal Eletrônica de Serviços de Comunicação Eletrônica", **o campo**"Tipo de Emissão"**com a opção** "Normal"**, e o** "Modelo de Impressão de nota fiscal" **com a opção**"16 - NFCOM".**

Na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), configure os campos **"Calcular FUNTTEL?"** e **"Calcular FUST?"**, selecionando **"Sim"** ou **"Usar do Cadastro de Produto"**.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29711263158295)

 Informações adicionais acerca das operações:**

Além disso, nas operações de NFCom podem ser informados os CFOPs contidos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/29711304212119)

O Sankhya Om suporta a geração do campo** 'Sem Situação Tributária para o ICMS'** (tag `indSemCST`) na NFCom.

Para que o sistema gere essa informação automaticamente e suprima o envio do CFOP (conforme exigido pelo layout), é necessário que o item esteja configurado com o CST 41 (Não Tributado) e não possua base de cálculo, alíquota ou valor de ICMS. 

Essa validação previne rejeições em operações onde não há incidência do imposto de ICMS.

**1.** Na aba NFCom, selecione o modelo do documento no campo **"NFCom"** e o **"Tipo de Emissão"**.

**Observação:** lembre-se de informar os dados da NFCom, no pop-up [Controle Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao), no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...).

### 
**Modelos de Nota Fiscal/Duplicatas/Boleto(s)**

Na tela de [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s), existe o modelo padrão conforme orientação da Sefaz com a opção **"16-NFCom"**, no entanto, cada um poderá personalizar o modelo conforme a necessidade da sua empresa.

### 
**Configuração do Layout da Nota**

Nesta tela, configure o layout para incluir os novos campos, como:

-  

  - 

**Indicador de Devolução;**

  - 

**Código do Item NFCom.**

Após realizadas as configurações acima o sistema está preparado para emissão da nota NFCom modelo 62, ou escrituração de uma compra NFCom modelo 62.

### **Aumento do Limite de Itens**

A estrutura da NFCom suporta operações de grande volume:

- 
**Até 9990 Itens:**** **é possível incluir, manipular e transmitir notas contendo até **9990 itens** em um único documento.

**Nota:** é importante notar que a validação final desse limite é feita pela própria SEFAZ através do arquivo de regras (XSD) no momento da transmissão.

[[voltar ao topo]](#top)

### 
**Procedimentos de Substituição, Cancelamento e Contingência:**

Para emissões de substituição ou em contingência, deve seguir os seguintes passos:

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311697110039)

 Substituição:**

Para emitir uma nota de substituição, siga os passos:

1. 

**Configuração da TOP:**

Defina o **tipo de movimento** como **venda**.

-  

  - Na aba NFCom, configure:

    - 

**NFCom:** Normal;

    - 

**Tipo de Emissão:** Substituição.

**Importante: **a aba **NFCom** só será habilitada se o campo **"Modelo do Documento"**, na aba [NF-e/NFC-CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe), estiver definido como **62**.

1. 

**Configuração nas ******[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:**

- 

Na aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais), seção **"Nota Fiscal de Conta de Comunicação/Telecomunicação (NFCom)"**, informe:

  - 

**Alíquota FUST;**

  - 

**Alíquota FUNTTEL.**

3. Na sub-aba NFCom (aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)), no campo **"Ambiente NFCom"**, selecione a opção correspondente ao ambiente desejado:

-  

  -  

    - **Não usa;**

    - **Produção;**

    - **Homologação.**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29711304214167)

 Substituição de Documentos:

- 

**Substituição de Modelo 62 por Modelo 62:**

No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), clique no botão "**NFCom"** encontrado na [Grade - Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo) e acione a opção **"NFCom de Substituição"**.

![Portal de Vendas.png](https://ajuda.sankhya.com.br/hc/article_attachments/29711263166359)

Escolha o **"Motivo da Substituição"** no pop-up exibido:

- 

 

  - 

01 – Erro de Preço;

  - 

02 – Erro Cadastral;

  - 

03 – Decisão Judicial;

  - 

04 – Erro de Tributação;

  - 

05 – Descontinuidade do Serviço;

  - 

06 – Complemento de Valores.

O motivo será registrado no grupo **gSub (informações da substituição)** na tag **<motSub>** do XML da NFCom.

Ao confirmar ou **"Gerar lote"**, se a nota for aprovada, a situação será alterada para **"S" **(Substituído da NFCom Substituída).

- 

**Substituição de Modelos 21 ou 22 por Modelo 62**

Siga o mesmo processo da substituição Modelo 62 por Modelo 62, adicionando a geração das tags do grupo **gNF (informação da NF modelo 21/22 referenciada)**:

- 

**CNPJ:** CNPJ do Emitente;

- 

**mod:** Modelo do Documento;

- 

**série:** Série do Documento Fiscal;

- 

**nNF:** Número do Documento Fiscal;

- 

**CompetEmis:** Ano e mês da emissão (AAAAMM);

- 

**hash115:** Hash do registro no arquivo do Convênio 115.

Ao confirmar ou Gerar lote, se a nota for aprovada, a situação será alterada para S (Substituído da NFCom Substituída).

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/29711263167127)

 **Atenção:**

O Fisco determina que cada UF é responsável pelo tratamento da **nota fiscal de substituição** nas obrigações acessórias e nos livros fiscais. Cabe ao usuário ajustar no seu próprio sistema conforme necessário, seja nos livros fiscais ou na apuração.

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311697110039)

 Contingência:**

Para emitir **NFCom em contingência**, siga estas configurações:

1. 

Configuração do Ambiente NFCom:

Acesse a sub-aba NFCom, aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa): 

No campo **"Ambiente NFCom"**, selecione umas das opções:

- 

 

  - 

 

    - 

**Não usa;**

    - 

**Produção;**

    - 

**Homologação.**

No campo** "Envio em Contingência"**, escolha:

- 

 

  - 

 

    - 

**Perguntar ao usuário;**

    - 

**Não usar contingência.**

No campo **"Tipo de Envio NFCom"**, selecione:

-  

  -  

    - 

**Preferir Contingência;**

    - 

**SEFAZ/Contingência;**

    - 

**Sempre Contingência.**

Feita essas configurações, deverá ser realizada a emissão manual da NFCom, da seguinte forma:

1. 

**Transmitir manualmente**:

  - 

No Portal de Vendas ou [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), selecione a nota e clique em **"Gerar Lote"**.

1. 

**Regras para Contingência Off-line (tpEmis = 2)**:

  - 

Não é necessário usar série específica ou papel especial.

  - 

Avance um número na sequência da numeração ao entrar em contingência para evitar rejeição por duplicidade.

1. 

**Transmissão da NFCom Após Resolver o Problema Técnico**:

  - 

Utilize a mesma chave de acesso, mantendo o código numérico original (cNF).

  - 

Após aprovação em produção sem contingência, altere o status da NFCom para **"Aprovada"**.

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311697110039)

 Cancelamento **

Para a Nota Fiscal Fatura de Serviço de Comunicação Eletrônica (NFCom), o cancelamento é permitido dentro do prazo regulamentar de até 120 horas após o último dia do mês de **autorização** (conforme Ajuste SINIEF 07/22), sendo vedado para notas de substituição ou substituídas.

O cancelamento fora do prazo regulamentar (após 120 horas do mês de autorização) é uma exceção. O sistema só processará essa solicitação quando o Fisco liberar o cancelamento fora do prazo via evento de Manifestação do Fisco (tipo ‘Liberação do Prazo de Cancelamento’), para ativar essa funcionalidade dentro do sistema Sankhya utilize a marcação "Permite cancelamento fora do prazo" na tela [Preferencias da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFCom](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#SubabaNFCom).

[[voltar ao topo]](#top)

### 
**Obrigações Acessórias**

O processo segue o mesmo fluxo de uma nota fiscal eletrônica. Para gerar e registrar as informações corretamente:

1. 

Gere o livro fiscal na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI).

1. 

Finalize a apuração na tela [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS).

1. 

As informações serão enviadas para:

  - 

[EFD Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI) (Bloco D700 – entradas e saídas da NFCom);

  - 

[EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es):

    - 

**D500** – Entradas (notas de aquisição com direito a crédito).

    - 

**D600** – Saídas (notas de venda).

1. 

**Registro D500**

  - 

Inclui a Nota Fiscal Fatura de Serviços de Comunicação Eletrônica (NFCom – Código 62), conforme a legislação.

  - 

O campo **"Chave" **do Documento Fiscal Eletrônico (CHV_DOC_E)** **é obrigatório para o modelo **62 (NFCom)**.

1. 
**Registro D600**

  - 

Ajustado para consolidar corretamente documentos fiscais relacionados à prestação de serviços.

  - 

Inclusão do modelo NFCom (Código 62) para escrituração adequada.

  - 

Atualização dos campos de complementação da prestação de serviços, garantindo a correta apuração dos tributos.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [modelo 21 e 22](https://ajuda.sankhya.com.br/hc/pt-br/articles/7405986347799-Configura%C3%A7%C3%B5es-Para-Emiss%C3%A3o-de-NF-Modelo-21-e-22)
- [FUST/FUNTTEL](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409827525783-FUST-FUNTTEL)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abageral)
- [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)
- [Números dos Terminais Telefônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#aban%C3%BAmerosdosterminaistelef%C3%B4nicos)
- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos)
- [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)
- [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Controle Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)
- [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...)
- [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais)
- [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)
- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [Grade - Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [NFCom](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#SubabaNFCom)
- [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI)
- [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS)
- [EFD Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI)
- [EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es)