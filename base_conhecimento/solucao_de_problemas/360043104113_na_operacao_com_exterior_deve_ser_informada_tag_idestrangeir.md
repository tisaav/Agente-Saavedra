# Na operação com Exterior deve ser informada tag idEstrangeiro

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104113-Na-opera%C3%A7%C3%A3o-com-Exterior-deve-ser-informada-tag-idEstrangeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104113-Na-opera%C3%A7%C3%A3o-com-Exterior-deve-ser-informada-tag-idEstrangeiro)  
> **ID:** `360043104113` | **Última Atualização:** 2026-07-22T16:08:12Z

---

[720 - Rejeição]: Na operação com exterior deve ser informada tag idEstrangeiro.

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/41126309782807)

 SITUAÇÃO

  Esta rejeição ocorre durante a emissão de nota fiscal eletrônica (NF-e ou NFC-e) quando o sistema identifica uma operação com o exterior (idDest = 3 ou CFOP iniciado em 7), porém o campo **"Identificação de estrangeiro"** (idEstrangeiro) não foi preenchido no cadastro do parceiro, impedindo a autorização do documento pela SEFAZ.

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16503875751063)

 SOLUÇÃO

  Para corrigir esta rejeição, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16503862643095)

 Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros).

- Na aba **"Identificação"**, localize o campo **"Identificação de estrangeiro"** e informe o número do passaporte ou outro documento legal para identificar a pessoa estrangeira.

  Após preencher o documento, salve as alterações e transmita a nota fiscal novamente.

**Exemplo da tag gerada:**
`<idEstrangeiro>ABC1234</idEstrangeiro>`

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16503862648727)

 CAUSA

  A legislação fiscal brasileira exige que, em operações com parceiros do exterior, seja informado um código de identificação no XML da nota fiscal. A ausência desta informação no cadastro do parceiro impede a geração da tag no arquivo XML, resultando na rejeição 720.

### 

![Observações](https://ajuda.sankhya.com.br/hc/article_attachments/16503862644631)

 OBSERVAÇÕES

  - Caso a operação não seja destinada ao exterior, verifique o cadastro de endereço do parceiro da nota e ajuste para um endereço dentro do Brasil.
  - Para mais detalhes técnicos, consulte o [Manual de Orientação do Contribuinte v.6](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=).