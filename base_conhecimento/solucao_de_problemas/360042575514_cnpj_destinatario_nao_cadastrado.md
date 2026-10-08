# CNPJ Destinatário não cadastrado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042575514-CNPJ-Destinat%C3%A1rio-n%C3%A3o-cadastrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042575514-CNPJ-Destinat%C3%A1rio-n%C3%A3o-cadastrado)  
> **ID:** `360042575514` | **Última Atualização:** 2026-08-01T00:46:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443622302487)

 MENSAGEM:**

[246 - Rejeição]: CNPJ Destinatário não cadastrado. 

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443622303639)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855669370647)

 Confira, no Cadastro de Parceiros, se o campo **CNPJ/CPF** foi digitado corretamente (erros de digitação são a causa mais frequente).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855678530711)

 Consulte a situação cadastral do CNPJ diretamente no site da Receita Federal (Consulta Cadastro Nacional da Pessoa Jurídica). A situação deve constar como **"Ativa"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855678534551)

 Se o CNPJ estiver **Baixado, Suspenso, Inapto ou Nulo**, não é possível emitir NF-e para esse parceiro até que ele regularize a situação junto à Receita Federal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855669390999)

 Após a regularização (ou correção do CNPJ cadastrado), refaça a nota informando novamente o parceiro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443663981335)

 CAUSA:**

Essa rejeição ocorre quando o CNPJ do destinatário informado na nota não é encontrado, ou não está com situação cadastral ativa, na base da Receita Federal. A SEFAZ consulta esse cadastro no momento da autorização da NF-e e recusa o documento quando o CNPJ está inválido, inexistente ou baixado.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443663981975)

OBSERVAÇÃO:**

Se, além dessa rejeição, o sistema também apontar problema na Inscrição Estadual, é necessário verificar separadamente a situação da IE no SINTEGRA ou no site da SEFAZ da UF do destinatário, esse é um cadastro distinto do CNPJ e tratado por outra rejeição.