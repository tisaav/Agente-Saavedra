# Erro ao tentar Cancelar uma Nota Fiscal de Serviço

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30479428310935-Erro-ao-tentar-Cancelar-uma-Nota-Fiscal-de-Servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/30479428310935-Erro-ao-tentar-Cancelar-uma-Nota-Fiscal-de-Servi%C3%A7o)  
> **ID:** `30479428310935` | **Última Atualização:** 2026-09-25T13:52:03Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/30479428306455)

 MENSAGEM**

Ao tentar cancelar NFS-e, o sistema apresenta a seguinte mensagem de erro:

**"código do erro: 1304 Mensagem: Erro ao cancelar NFS-e: Esta NFS-e não poderá ser cancelada pois já foi emitida a guia de recolhimento de ISS para ela"**

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/41262195390103)

 SITUAÇÃO**

Essa mensagen ocorre quando o usuário tenta cancelar uma nota fiscal através do sistema, mas existem impedimentos relacionados a registros em livros fiscais e fechamento de competência de ISS.

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/30479447494551)

 SOLUÇÃO**

A solução varia conforme o erro apresentado. Siga opasso a passo a seguir:
 

**Erro 1304 - NFS-e com guia de recolhimento de ISS emitida**

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41262181884567)

Verifique junto ao setor de NFS-e da Prefeitura qual é o período do fechamento da competência para cancelamento ou substituição. Caso o prazo esteja ultrapassado, verifique a possibilidade de processo administrativo para cancelamento.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41262195391767)

Após autorização da Prefeitura, acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades), aba **"NFS-e"**, e altere o campo **"Tipo de Cancelamento para NFS-e"** para a opção de "Cancelamento via Prefeitura sem numero de protocolo". Salve.

![Erro ao tentar Cancelar uma Nota Fiscal de Serviço 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30485179652503)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41262181886359)

Acesse o **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas), localize a nota e clique em **"Cancelar"**. Preencha os dados no pop-up e confirme.

![Erro ao tentar Cancelar uma Nota Fiscal de Serviço 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30485179655319)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41262181886615)

**Importante:** Após o cancelamento manual, retorne ao **"Cidades"** e volte o campo **"Tipo de Cancelamento para NFS-e"** para **"Via WebService"**.
 

 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/30479428308759)

 CAUSA**

O erro ao cancelar notas fiscais tem a seguinte causa:

• **Registro em livros fiscais:** Nota já escriturada nos livros de ICMS ou ISS.