# Informado NCM inexistente[nItem:nnn] (2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062833-Informado-NCM-inexistente-nItem-nnn-2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062833-Informado-NCM-inexistente-nItem-nnn-2015-002)  
> **ID:** `360043062833` | **Última Atualização:** 2026-07-22T16:09:08Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477528858775)

**MENSAGEM**

[778 - Rejeição]: Informado NCM inexistente [nItem:nnn]
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477520536599)

**SITUAÇÃO**

Durante a emissão da nota fiscal eletrônica (NF-e ou NFC-e), ao tentar confirmar ou transmitir o documento, o sistema apresenta a rejeição 778, indicando que o código NCM informado no item da nota não existe ou não está mais válido na tabela oficial da Receita Federal. Esta rejeição bloqueia o processamento e a autorização da nota.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477528865559)

**SOLUÇÃO**

Para corrigir a rejeição 778, siga os passos abaixo:
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477520530071)

 Identifique o item com NCM incorreto: Caso a NF-e possua múltiplos itens, utilize a tela **"Portal de Vendas"** (Comercial >> Consulta), selecione a nota, clique em **"NF-e"** >> **"Gerar XML da NF-e em arquivo para Conferência"**. Abra o XML em um editor de texto e utilize a busca (Ctrl+F) pelo termo 'nItem' para localizar o item apontado na rejeição.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477520532119)

 Consulte a validade do NCM: Acesse o portal oficial da Receita Federal ([https://portalunico.siscomex.gov.br/classif/#/sumario?perfil=publico)](https://portalunico.siscomex.gov.br/classif/#/sumario?perfil=publico)) ou utilize os links de consulta fornecidos nas observações abaixo para verificar se o código NCM foi desativado ou substituído.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477520534679)

 Atualize o cadastro no sistema: Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos >> Produtos), localize o item identificado, acesse a aba **"Geral"** e altere o campo **"NCM"** pelo código válido encontrado na consulta.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39446396983191)

 Reenvie a nota: Retorne à tela **"Central de Vendas"** (Comercial >> Central de Vendas), exclua o item antigo da nota e insira-o novamente para que o sistema capture o **"NCM"** atualizado. Realize a transmissão da nota fiscal.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16477528879255)

**CAUSA**

A rejeição ocorre quando o código **"NCM"** informado no item da nota não existe na tabela oficial da Receita Federal ou foi desativado ou substituído. A Nomenclatura Comum do Mercosul passa por atualizações periódicas e, quando o cadastro do produto está defasado, a SEFAZ bloqueia a autorização.
 

**OBSERVAÇÕES:**

![Marcador](https://ajuda.sankhya.com.br/hc/article_attachments/28458159695255)

[Consulta NCM SEFAZ](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=)
 

![Marcador](https://ajuda.sankhya.com.br/hc/article_attachments/28458159695255)

[Tabela TIPI Oficial](http://receita.economia.gov.br/acesso-rapido/legislacao/documentos-e-arquivos/tipi-1.pdf/view)
 

![Marcador](https://ajuda.sankhya.com.br/hc/article_attachments/28458159695255)

 Tabela NCM Nota Técnica 2016.003 (Vigência 01/04/2022): [Link](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=&AspxAutoDetectCookieSupport=1)