# E0130 Rejeição: O código do município para o endereço do prestador do serviço não existe conforme tabela de município do IBGE.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222294602903-E0130-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222294602903-E0130-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE)  
> **ID:** `37222294602903` | **Última Atualização:** 2026-07-22T14:17:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325767959)

 **MENSAGEM**

E0130 Rejeição: O código do município para o endereço do prestador do serviço não existe conforme tabela de município do IBGE.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222294589847)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)**, o sistema rejeitou o documento informando que o **código do município do prestador** não existe ou está inválido conforme a **Tabela de Municípios do IBGE**. Esta rejeição ocorre quando o código informado no cadastro não corresponde ao código oficial estabelecido pelo Instituto Brasileiro de Geografia e Estatística.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222294590999)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222294592023)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325771927)

 Na grade **''Cabeçalho''**, verifique se o campo **''Cidade''** está preenchido com o código da cidade conforme a tabela **TGFCAB**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325772951)

 Caso o campo ''Cidade'' não esteja preenchido, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **prestador do serviço**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325773719)

 Na aba **"Endereço"**, verifique o campo **"Cód. Cidade"** cadastrado para o prestador.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325775639)

 Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços) e localize a cidade identificada no passo anterior.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325776663)

 Na aba** ''Geral''**, verifique o conteúdo do campo **"Mun. domicílio fiscal"**.

- 

Este campo deve conter o **código oficial do município conforme o IBGE**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325777687)

 Acesse o site do ****[''IBGE''](https://cidades.ibge.gov.br/)**.**

- 

No campo **"Pesquisar"**, digite o nome da cidade do prestador;

- 

Ao abrir o conteúdo referente à cidade, localize a informação **"Código do Município"**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325778711)

 Retorne à tela "Cidades" (Configurações » Cadastros » Endereços) e corrija o campo "Mun. domicílio fiscal" com o código localizado no site do IBGE.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222294598679)

 Retorne ao passo 1, redigite os dados do cabeçalho para atualizar as informações e informe o código da cidade corretamente.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325782551)

 Realize o **cancelamento da NFS-e rejeitada** e emita novamente o documento fiscal.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38331508923415)

 OBSERVAÇÃO:** Caso não consiga localizar a informação no site do IBGE, solicite o código correto ao seu contador.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222325783191)

 **CAUSA**

Esta rejeição ocorre quando o **código do município do prestador** informado no sistema está **em branco, incorreto ou divergente** do código oficial estabelecido pela **Tabela de Municípios do IBGE**. Quando o campo **"CODCID"** não está preenchido no cabeçalho da nota, o sistema busca automaticamente o código cadastrado no endereço do parceiro. Se este código estiver incorreto ou não corresponder ao município da prefeitura que processará a NFS-e, a rejeição será apresentada.

**Exemplo**: Se a prefeitura é de **Lages - SC** e o parceiro está cadastrado com o código de **Uberlândia - MG**, haverá divergência entre os códigos, resultando na rejeição do documento.