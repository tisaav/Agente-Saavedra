# Erro: [GW0001] O código de tributação informado é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Prestação de Serviços  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39378059308439-Erro-GW0001-O-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-informado-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/39378059308439-Erro-GW0001-O-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-informado-%C3%A9-inv%C3%A1lido)  
> **ID:** `39378059308439` | **Última Atualização:** 2026-09-11T12:35:30Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378059304983)

 **MENSAGEM**

[GW0001] O código de tributação informado é inválido.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39378059305367)

 **SITUAÇÃO**

Ao tentar autorizar uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, a nota pode ser rejeitada com a mensagem **GW0001**, indicando que o **Código de Tributação** informado é inválido.

A rejeição ocorre quando o código enviado à prefeitura não está no formato esperado pelo integrador responsável pela autorização da NFS-e.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39378035355287)

 **SOLUÇÃO**

PPara corrigir a rejeição **GW0001**, verifique e ajuste o **Código de Tributação Municipal** no cadastro do serviço:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39378035355543)

 Acesse a tela **"Serviços"** (Configurações » Cadastros » Produtos » Serviço) e localize o serviço que está sendo utilizado na nota fiscal rejeitada.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39378059306263)

 Acesse a aba **Alíquota de ISS** e localize o campo **Código de Tributação Municipal**, considerando a empresa e o município de emissão

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39378035355799)

 Verifique se o código está preenchido de acordo com o padrão aceito,  contendo **9 dígitos numéricos**, sem pontos, barras, hífens ou espaços. Caso esteja em formato diferente ou errado, ajuste-o conforme o padrão esperado.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39378059307031)

 Salve as alterações realizadas no cadastro do serviço.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39378035356311)

 Retorne à nota fiscal rejeitada e **redigite o item do serviço**, para que as informações tributárias atualizadas sejam carregadas na nota.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39378059307415)

 Gere um novo lote e reenvie a NFS-e para autorização.
 

**Observações importantes:**

- 

O **Código de Tributação Municipal** deve ser informado conforme o padrão exigido pelo integrador da Prefeitura em questão.

- 

Não informe o código utilizando **pontos, barras, hífens ou espaços**.

- 

Caso o campo esteja vazio, verifique qual código deve ser utilizado para o serviço antes de realizar o preenchimento.

- 

Verifique também as configurações da cidade em **Configurações > Cadastros > Endereços> Cidades**, principalmente as relacionadas ao tipo de emissão/envio da NFS-e.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39378059307671)

 **CAUSA**

A rejeição **GW0001** ocorre quando o **Código de Tributação** enviado na NFS-e não atende ao formato ou à estrutura esperada pelo webservice da prefeitura.