# 1177 Rejeição: Total da CBS estornada difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098125049111-1177-Rejei%C3%A7%C3%A3o-Total-da-CBS-estornada-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098125049111-1177-Rejei%C3%A7%C3%A3o-Total-da-CBS-estornada-difere-da-soma-dos-itens)  
> **ID:** `37098125049111` | **Última Atualização:** 2026-07-22T14:20:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098111734807)

 **MENSAGEM**

1177 Rejeição: Total da CBS estornada difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125019543)

 **SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) com estorno de CBS, o sistema identifica que o valor total da CBS estornada informado no documento fiscal não corresponde à soma dos valores de CBS estornada de cada item da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125020823)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125026839)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125027735)

 Na aba **''Impostos''**, verifique se a opção **''Tem CBS''** está marcada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098111740823)

 Caso não esteja marcada, selecione esta opção para garantir que o sistema calcule corretamente a proporção da CBS estornada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125030935)

 Verifique também na aba **"IBS/CBS"** se as configurações de estorno de CBS estão corretas para a operação que está sendo realizada.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125031831)

 Após realizar os ajustes necessários, inutilize a NF-e rejeitada.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098125038103)

 Exclua o documento rejeitado e realize um novo lançamento com as configurações corretas. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098111753239)

 **CAUSA**

Esta rejeição ocorre quando o valor total da CBS estornada informado no documento fiscal é diferente da soma dos valores de CBS estornada de cada item da nota. De acordo com as regras de validação da Sefaz, o valor total da CBS estornada deve ser exatamente igual à soma dos valores de CBS estornada de todos os itens do documento fiscal.

A divergência pode ocorrer devido a arredondamentos incorretos, cálculos manuais ou configurações inadequadas no sistema, especialmente quando não está habilitada a opção de proporcionalidade da CBS em relação aos itens no cadastro do Tipo de Operação.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)