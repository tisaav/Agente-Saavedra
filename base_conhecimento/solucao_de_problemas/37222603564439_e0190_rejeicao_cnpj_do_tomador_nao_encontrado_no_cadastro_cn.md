# E0190 Rejeição: CNPJ do tomador não encontrado no cadastro CNPJ.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222603564439-E0190-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-n%C3%A3o-encontrado-no-cadastro-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222603564439-E0190-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-n%C3%A3o-encontrado-no-cadastro-CNPJ)  
> **ID:** `37222603564439` | **Última Atualização:** 2026-08-25T17:54:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222584566423)

 **MENSAGEM**

E0190 Rejeição: CNPJ do tomador não encontrado no cadastro CNPJ.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222584567575)

 **SITUAÇÃO**

Ao emitir um **CT-e (Conhecimento de Transporte Eletrônico)**, a nota é rejeitada pela SEFAZ com a mensagem informando que o **CNPJ do tomador não foi encontrado no cadastro** da Receita Federal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222584568087)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222603557143)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador do serviço** informado no CT-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222603557399)

 Verifique se o **CNPJ informado no campo "CNPJ/CPF"** está correto e **devidamente cadastrado na Receita Federal**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222603557527)

 Consulte o CNPJ do tomador no **SINTEGRA** ou no **Cadastro Centralizado de Contribuintes** para confirmar: 

- 

Se o CNPJ está **ativo e válido**;

- 

Se o número do CNPJ está **digitado corretamente**, sem erros de digitação;

- 

Se o CNPJ possui **situação cadastral regular** junto à Receita Federal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222584570007)

 Caso identifique que o **CNPJ está incorreto ou inválido**, retorne ao passo 1 e 2 e corrija a informação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222603558423)

 Após realizar a correção, **redigite o CT-e** e gere um novo lote para transmissão à SEFAZ.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222603558551)

 Caso o CNPJ esteja correto mas ainda assim apresente a rejeição, **oriente o tomador a regularizar sua situação cadastral** junto à Receita Federal, pois o CNPJ pode estar **inativo, suspenso ou inexistente** na base de dados. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222584570775)

 **CAUSA**

A rejeição ocorre quando o **CNPJ do tomador informado no CT-e** não consta na base de dados da **Receita Federal**, seja por estar **digitado incorretamente**, por estar **inativo, suspenso, cancelado** ou por **não existir** no cadastro nacional de pessoas jurídicas.