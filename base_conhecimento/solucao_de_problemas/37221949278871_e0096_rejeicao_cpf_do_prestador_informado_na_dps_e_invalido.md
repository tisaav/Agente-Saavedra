# E0096 Rejeição: CPF do prestador informado na DPS é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221949278871-E0096-Rejei%C3%A7%C3%A3o-CPF-do-prestador-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221949278871-E0096-Rejei%C3%A7%C3%A3o-CPF-do-prestador-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37221949278871` | **Última Atualização:** 2026-07-22T14:18:14Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949219223)

 **MENSAGEM**

E0096 Rejeição: CPF do prestador informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949224087)

 **SITUAÇÃO**

A mensagem de rejeição aparece durante o processo de **transmissão da DPS** (Declaração de Prestação de Serviços) quando o **CPF do prestador de serviços** cadastrado no sistema está **inválido, zerado ou com dígito verificador incorreto**. Esta validação é realizada pela SEFAZ no momento da transmissão do documento fiscal eletrônico.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949227799)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221964981015)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **prestador de serviços** vinculado à DPS rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949241495)

 Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"** e verifique se o CPF informado está correto: 

- 

Certifique-se de que o CPF possui **11 dígitos numéricos**;

- 

Verifique se o CPF está **sem pontos, traços ou espaços em branco**;

- 

Confirme se o **dígito verificador** (últimos dois números do CPF) está correto;

- 

Assegure-se de que o CPF **não está zerado** (00000000000).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949247511)

 Caso o CPF esteja incorreto, **corrija a informação** inserindo um CPF válido e ativo na Receita Federal do Brasil.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37834810824343)

 Salve as alterações realizadas no cadastro do parceiro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221964997399)

 Retorne ao documento fiscal e **redigite as informações** do prestador para que o sistema atualize os dados cadastrais.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221965001495)

 Gere um **novo lote de transmissão** da DPS com as informações corrigidas. 
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37834810827543)

 OBSERVAÇÃO:** Caso o problema persista após as correções, inutilize a numeração do documento, exclua a DPS e gere uma nova com os dados atualizados.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221949262359)

 **CAUSA**

A rejeição ocorre quando a DPS é transmitida com o **CPF do prestador de serviços inválido**. Isso acontece quando o CPF informado no cadastro do parceiro está **zerado, com sequência numérica incorreta, com dígito verificador inválido ou não está ativo** na base da Receita Federal. A SEFAZ valida a autenticidade do CPF no momento da transmissão e, caso identifique inconsistências, retorna a rejeição E0096.