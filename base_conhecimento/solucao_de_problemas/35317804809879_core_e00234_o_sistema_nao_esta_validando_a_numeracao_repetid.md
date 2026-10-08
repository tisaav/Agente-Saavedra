# CORE_E00234 - O sistema não está validando a numeração repetida em um novo lançamento

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35317804809879-CORE-E00234-O-sistema-n%C3%A3o-est%C3%A1-validando-a-numera%C3%A7%C3%A3o-repetida-em-um-novo-lan%C3%A7amento](https://ajuda.sankhya.com.br/hc/pt-br/articles/35317804809879-CORE-E00234-O-sistema-n%C3%A3o-est%C3%A1-validando-a-numera%C3%A7%C3%A3o-repetida-em-um-novo-lan%C3%A7amento)  
> **ID:** `35317804809879` | **Última Atualização:** 2026-07-22T14:25:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712915148311)

 **MENSAGEM:**

[CORE_E00234] Numeração já utilizada em outro lançamento.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35317804801303)

 **SITUAÇÃO:**

Ao realizar lançamento em que a numeração já tenha sido utilizada em outro lançamento e a **"TOP"** está configurada para bloquear numeração repetida, com o campo **"Valida Numeração por"** definido em alguma opção **"PROIBIR"**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35317793409047)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712915149463)

 Verifique se a opção selecionada no campo **"Valida Numeração por"** corresponde ao tipo de numeração da **"TOP"**. Por exemplo, se utiliza Empresa/Série, selecione uma opção que também valide a série. Caso a configuração não contemple a série, poderá ocorrer lançamento para o mesmo parceiro com o mesmo número se a série for diferente.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35317793411223)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712907865751)

 Se a **"TOP"** estiver configurada com numeração automática (e se for esse o caso), além de configurar o campo **"Valida Numeração por"**, habilite o parâmetro **VALNUMNOTACONF**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35317793408535)

 **CAUSA:**

A mensagem ocorre quando há mais de um lançamento com a mesma numeração, devido a:

- 

O campo **"Valida Numeração por"** da **"TOP"** não está configurado.

- 

O campo **"Valida Numeração por"** está configurado com uma opção que apenas faz a validação, mas não bloqueia.

- 

A numeração da **"TOP"** é automática.