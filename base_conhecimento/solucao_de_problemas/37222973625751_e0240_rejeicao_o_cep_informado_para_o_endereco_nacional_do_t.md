# E0240 Rejeição: O CEP informado para o endereço nacional do tomador do serviço não existe ou não pertence ao município do endereço do tomador.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222973625751-E0240-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-tomador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222973625751-E0240-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-tomador)  
> **ID:** `37222973625751` | **Última Atualização:** 2026-09-01T12:43:01Z

---

[E0240] O CEP informado para o endereço nacional do tomador do serviço não existe ou não pertence ao município do endereço do tomador

[E058] Código do município do tomador do serviço não corresponde ao CEP informado

[E061] UF do tomador do serviço não corresponde ao CEP informado

[E062] CEP do logradouro do tomador do serviço inexistente

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989587991)

**SITUAÇÃO**

Ao tentar emitir uma **"NFS-e"** (Nota Fiscal de Serviço Eletrônica), o sistema apresenta rejeição indicando que o **"CEP"** do tomador não corresponde ao município, UF ou não existe na base dos Correios. Essa validação ocorre porque a prefeitura e a API dos Correios verificam automaticamente se o CEP informado é válido e pertence ao município e estado cadastrados.

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989588375)

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222973615383)

 Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros) e localize o tomador do serviço envolvido na NFS-e rejeitada.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222973616535)

 Na aba **"Endereço"**, verifique o campo **"CEP"** e o **"Cód.Cidade"** cadastrados para o tomador.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989589527)

 Acesse o site dos **"Correios"** e consulte se o CEP informado realmente existe e se pertence ao município cadastrado.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989590295)

 Caso o CEP esteja incorreto, corrija-o no cadastro do parceiro na aba **"Endereço"**, informando o CEP válido correspondente ao município.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989590679)

 Caso o município esteja incorreto, acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989591447)

 Verifique se o nome da cidade está cadastrado corretamente conforme o **"IBGE"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989593623)

 No cadastro da cidade, certifique-se de que os campos **"Nome"** e **"Mun. domicílio fiscal"** estejam idênticos aos dados da base do governo.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222973620247)

 Retorne à tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros). Na aba **"Endereço"**, atualize o campo **"Cód. Cidade"**, garantindo que o município selecionado seja condizente com o CEP informado.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37800107118103)

 Após salvar as alterações, gere um novo lote da NFS-e e reenvie para autorização. Se a rejeição persistir, inutilize ou exclua a nota anterior e refaça o lançamento completo.

### **ATENÇÃO:**

- Para evitar que novos cadastros gerem essa rejeição, utilize sempre a base oficial dos Correios para validar o CEP antes de preencher o cadastro do parceiro.

1. Após corrigir o CEP no cadastro do parceiro, acesse a **"Central de Vendas"** (Comercial >> Rotinas >> Central de Vendas), re-selecione o parceiro no cabeçalho da nota e salve o documento. Este procedimento garante que as novas informações de endereço sejam atualizadas no XML antes da geração do novo lote.

1. Evite o uso de CEPs terminados em "-000" (gerais da cidade). Algumas prefeituras e integradores de NFS-e exigem o CEP específico do logradouro para validar o endereço.

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37222989597207)

**CAUSA**

Esta rejeição ocorre quando o CEP informado no cadastro do endereço do tomador do serviço não existe na base dos Correios ou quando o CEP não pertence ao município cadastrado para o tomador. Situações comuns incluem:

- CEPs genéricos com final "000" não são aceitos pela validação da NFS-e.

1. CEP desatualizado ou digitado incorretamente no cadastro do parceiro.

1. Inconsistência entre CEP, município e UF no cadastro.

1. Código IBGE do município incorreto ou não preenchido na tela de cidades.