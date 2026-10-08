# Sankhya Tax - Auditoria de Documentos Fiscais (Integração de Notas Fiscais com a Plataforma ASIS no Sankhya)

> **Módulo:** Fiscal e Contábil | **Subseção:** Sankhya TAX  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28129797729559-Sankhya-Tax-Auditoria-de-Documentos-Fiscais-Integra%C3%A7%C3%A3o-de-Notas-Fiscais-com-a-Plataforma-ASIS-no-Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/28129797729559-Sankhya-Tax-Auditoria-de-Documentos-Fiscais-Integra%C3%A7%C3%A3o-de-Notas-Fiscais-com-a-Plataforma-ASIS-no-Sankhya)  
> **ID:** `28129797729559` | **Última Atualização:** 2026-07-29T16:13:04Z

---

```text
 Módulo: Configurações > Rotinas            Versão disponível: A partir da 4.32
```

O Portal de Integração - ASIS permite a integração de **notas fiscais eletrônicas** com a plataforma ASIS, otimizando a **análise tributária** no sistema Sankhya. Com essa funcionalidade, é possível enviar **arquivos XML** já disponíveis para a ASIS e obter uma **avaliação detalhada** de cada documento fiscal.

Essa análise fornece **informações completas** sobre o cenário tributário de cada documento, facilitando a gestão fiscal, garantindo conformidade e reduzindo a complexidade do processo. Os resultados podem ser consultados diretamente na plataforma ASIS.
 

****
[Configuração inicial](#Configura%C3%A7%C3%A3oinicial)
[Integração de Documentos Fiscais](#Integra%C3%A7%C3%A3odeDocumentosFiscais)
[Consulta e Reenvio de Documentos](#ConsultaeReenviodeDocumentos)
[Aba Documentos Fiscais](#AbaDocumentosFiscais)
[Aba Obrigações Acessórias](#AbaObriga%C3%A7%C3%B5esAcess%C3%B3rias)

| Como utilizar a jornada? |
| --- |
|  |
|  |
|  |
|  |
|  |

### 
**Configuração inicial**

Para utilizar a integração com a ASIS, é necessário configurar a Chave de Integração, representada pela **Account Key** (chave de acesso de 64 caracteres fornecida pela ASIS).

Após salvar as chaves de acesso, o sistema envia uma solicitação a ASIS para validar a autenticação, e o Portal de Integração apresenta todas as empresas ou CNPJs vinculados a essa credencial. 

Se precisar de mais detalhes, consulte: [Como realizar a autenticação](https://developers.asisprojetos.com.br/autenticacao.html).

[[voltar ao topo]](#top)

### 
**Integração de Documentos Fiscais**

Com a Account Key configurada, é possível integrar documentos fiscais de duas formas.

- 
**Integração manual: **utilizada em documentos ou obrigações com data anterior a 30/01/2025. Para fazer a integração manual, utilize o botão **"Integrar" **e preencha os dados da empresa, informações de envio e obrigações acessórias.

- 
**Integração automática: **disponível para documentos incluídos no ERP a partir de 30/01/2025. Nesse caso, o sistema pode fazer o processamento automático por meio da opção** “Integrar Automático”**.

**Observações importantes sobre integração automática**

Apenas notas fiscais autorizadas ou canceladas, que possuem o padrão de XML estabelecido pelo [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), são enviadas para auditoria na ASIS.

Para notas de entrada, a análise só pode ser feita se o arquivo XML estiver disponível, ou seja, o documento deve ser importado previamente pelo Portal de Importação de XML.

Para atender às obrigações acessórias, mais de um arquivo de conferência pode ser gerado no mesmo mês. Caso necessário, esses arquivos podem ser excluídos e gerados novamente.

É possível configurar a integração para os seguintes documentos:

- 

**Documentos Fiscais: **NF-e e NFC-e.

- 

**Obrigações Acessórias: **EFD Contribuições e SPED Fiscal.

[[voltar ao topo]](#top)

### 
**Aba Documentos Fiscais**

![Aba Documentos Fiscais (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/30229469011863)

Nesta aba, os documentos são exibidos conforme a seleção feita pelo usuário. Os tipos disponíveis são:

- 

NF-e

- 

NFC-e

O Portal de Integração é muito utilizado e permite ajustar a visualização da planilha por meio de filtros, como **Empresa**, **Data Inicial** e **Data Final**.

Caso um documento contenha erro, ele poderá ser reenviado. Se a reintegração for bem-sucedida, o status será alterado para **Enviado**. Se não for, o status continuará como **Erro**.

**Limitação do botão "Reenviar"**: este botão pode ser utilizado apenas uma vez a cada 5 minutos.

Se o botão for clicado antes desse tempo, a seguinte mensagem será exibida:

***"Não foi possível obter o retorno do documento. Verifique o motivo na tela de acompanhamento e tente novamente dentro de alguns minutos."***

[[voltar ao topo]](#top)

### 
**Aba Obrigações Acessórias**

***

![Obrigações Acessórias 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/28297392836631)

***

Esta aba funciona da mesma forma que a aba Documentos Fiscais, apresentando os documentos integrados conforme a seleção do usuário.

Se houver erro no envio, o usuário pode consultar a ASIS utilizando a opção **"Consultar ASIS"**, que permite atualizar o status do documento.

Limitação do botão** "Consultar ASIS"**: assim como o botão Reenviar, o intervalo mínimo entre as tentativas é de 5 minutos.

[[voltar ao topo]](#top)

### 
**Consulta e reenvio de documentos**

Após a integração, cada linha exibirá um Status Sefaz por nota fiscal:

- 

**Aprovada**: NFE aprovada na Sefaz

- 

**Cancelada**: NFE cancelada na Sefaz

A coluna Auditado também segue essa configuração:

- 

**Não**: para notas ainda sem retorno da API da ASIS

- 

**Sim**: para notas integradas e com retorno com sucesso

- 

**Erro**: para notas que falharem na integração

Se a autenticação falhar, o sistema exibirá a seguinte mensagem:

**"Problema: Não foi possível realizar a autenticação. Verifique os dados de integração informados no portal Kolossus, tente novamente ou entre em contato com a ASIS."**

Se houver erro na integração, é possível:

- 

Reenviar o documento para uma nova tentativa de processamento.

- 

Consultar a ASIS para atualizar o status do documento.

Lembre-se que o reenvio e a consulta possuem um intervalo mínimo de 5 minutos entre as tentativas.

Os relatórios detalhados podem ser acessados diretamente no **Portal Kolossus da ASIS**, onde é possível visualizar a auditoria de cada documento.

Caso seja necessário ajustar as credenciais de uma empresa, basta editar a Account Key nas configurações.

A cor do status indica a situação da empresa:

- 

**Verde:** integrada ou apta para integração;

- 

**Vermelha:** não integrada ou não apta.

![Status da empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/28129797726999)

[[voltar ao topo]](#top)

### 
**Parâmetros que influenciam esta rotina**

- 

**Registro de log detalhado da integração – IALOGDETINT:**
Habilite este parâmetro para rastrear todas as etapas da integração com a ASIS. Isso permite que o suporte identifique e resolva falhas rapidamente.

1. 

**Período de armazenamento de dados – IAQTDPLIMP:**
Define por quantos dias o sistema manterá os arquivos armazenados no portal. O padrão é 30 dias, mas esse período pode ser ajustado conforme necessário.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)