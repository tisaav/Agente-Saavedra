# Invalid content was found starting with element 'xNome'

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043100913-Invalid-content-was-found-starting-with-element-xNome](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043100913-Invalid-content-was-found-starting-with-element-xNome)  
> **ID:** `360043100913` | **Última Atualização:** 2026-07-22T16:08:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175552535)

 MENSAGEM:**

cvc-complex-type.2.4.a: Invalid content was found starting with element 'xNome'. One of '{"http://www.portalfiscal.inf.br/nfe":CNPJ, "http://www.portalfiscal.inf.br/nfe":CPF, "http://www.portalfiscal.inf.br/nfe":idEstrangeiro}' is expected.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504163209623)

 SOLUÇÃO****:**

Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175560983)

 Acesse: *Configurações » Cadastros » Parceiros*

Aba: **"Identificação"**

- Campo **"Nome"**

- Campo **"CNPJ/CPF"**

Verifique se o valor informado no campo CNPJ/CPF está correto e válido junto a Receita Federal.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175562135)

 Caso a nota que esteja emitindo seja uma nota de acompanhamento de cupom fiscal, o sistema vai trazer o parceiro "CONSUMIDOR" utilizado no lançamento do cupom fiscal, porém devido a regras de validação da SEFAZ será necessário cadastrar o novo parceiro para o qual está sendo emitido o acompanhamento e alterar o código do parceiro no lançamento da nota de acompanhamento. Feito isso, gere o lote novamente.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175563927)

 Em operações de exportações, parceiros destinatário do exterior (CFOP Iniciado em 7), verifique o parâmetro **"CODPAISBRASIL"**, esse deve ser configurado com o valor  "55".
Também informe o campo Identificação de Estrangeiro no cadastro de Parceiro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175567639)

 CAUSA**:

Ocorre quando é emitido uma NF-e de acompanhamento e o Parceiro é um cadastro 'curinga' para emissão de Cupom Fiscal e precisa posteriormente emitir uma Nota de Acompanhamento de Cupom Fiscal e não se cadastra definitivamente o Parceiro da Nota.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504163227927)

 OBSERVAÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458159552023)

 Consulta:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175575959)

CPF:

[https://www.receita.fazenda.gov.br/Aplicacoes/SSL/ATCTA/CPF/ConsultaSituacao/ConsultaPublica.asp](https://www.receita.fazenda.gov.br/Aplicacoes/SSL/ATCTA/CPF/ConsultaSituacao/ConsultaPublica.asp)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504175575959)

CNPJ:

[https://www.receita.fazenda.gov.br/pessoajuridica/cnpj/cnpjreva/cnpjreva_solicitacao2.asp](https://www.receita.fazenda.gov.br/pessoajuridica/cnpj/cnpjreva/cnpjreva_solicitacao2.asp)