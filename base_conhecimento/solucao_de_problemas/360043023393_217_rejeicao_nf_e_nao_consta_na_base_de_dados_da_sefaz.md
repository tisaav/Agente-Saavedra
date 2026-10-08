# 217 Rejeição: NF-e não consta na base de dados da SEFAZ

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023393-217-Rejei%C3%A7%C3%A3o-NF-e-n%C3%A3o-consta-na-base-de-dados-da-SEFAZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023393-217-Rejei%C3%A7%C3%A3o-NF-e-n%C3%A3o-consta-na-base-de-dados-da-SEFAZ)  
> **ID:** `360043023393` | **Última Atualização:** 2026-07-22T16:10:01Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16457581089815)

**MENSAGEM:**

217 Rejeição: NF-e não consta na base de dados da SEFAZ

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16457581091735)

**SOLUÇÃO:**

  Primeiramente, acesse a tela **"Preferências da Empresa"** (Comercial >> Preferências >> Empresa), vá até a aba **"Documentos eletrônicos"**, sub aba **"NF-e/NFC-e"**, em seguida, sub aba **"NF-e"** e marque a opção **"Usar modo síncrono para envio do XML?"**.

**Observação:** Caso a aba **"Documentos eletrônicos"** esteja oculta, será necessário ajustar a visualização através da **"Configuração de Tela"** (ícone de engrenagem no canto superior direito) para reapresentar a aba em questão.

 

![NF-e não consta na base de dados da SEFAZ.png](https://ajuda.sankhya.com.br/hc/article_attachments/35619172128919)

 

**Caso o primeiro passo não resolva a rejeição, execute as ações abaixo:**

![Passo 2](https://ajuda.sankhya.com.br/hc/article_attachments/16457581098903)

 Consulte a Chave de Acesso no Portal Nacional da Sefaz ou no Portal Estadual da Sefaz. Feita essa consulta, siga as orientações abaixo:

- Se não encontrar a NF-e no [Portal Nacional da Sefaz](http://www.nfe.fazenda.gov.br/portal/principal.aspx), tente consultar no Portal Estadual.

 

![Passo 3](https://ajuda.sankhya.com.br/hc/article_attachments/16457596348439)

 Feita a consulta, você terá duas situações: 1 - a NF-e pode estar autorizada ou 2 - a NF-e pode não ser encontrada (não autorizada). Sempre é recomendado entrar em contato com a SEFAZ para verificar se o portal está com instabilidades na recepção.

 

![Passo 4](https://ajuda.sankhya.com.br/hc/article_attachments/35619172129943)

 No sistema, aguarde a SEFAZ estabilizar e consulte a nota novamente.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16457596354711)

**CAUSA:**

  A **Rejeição 217** ocorre principalmente devido à obrigatoriedade da resposta síncrona para lotes com uma única NF-e, que entrou em vigor em 13/10/2025. Quando o parâmetro **"Usar modo síncrono para envio do XML?"** não está ativado nas preferências da empresa, a SEFAZ retorna esta rejeição.

  Também ocorre quando consultada uma NF-e que ainda não foi autorizada, inexistente na Sefaz Estadual, ou se a NF-e for consultada no ambiente errado.

Exemplos adicionais:

![Marcador](https://ajuda.sankhya.com.br/hc/article_attachments/28458187473687)

 Quando a NF-e é emitida em Produção e a Chave de Acesso é consultada em Homologação e vice-versa;

![Marcador](https://ajuda.sankhya.com.br/hc/article_attachments/28458187473687)

 Quando a NF-e ainda não foi autorizada e a Chave de Acesso é consultada;

Em suma, esse problema ocorrerá se no momento da consulta da Chave de Acesso da NF-e no Webservice da Sefaz, a mesma não identificar esse documento em seu banco de dados.