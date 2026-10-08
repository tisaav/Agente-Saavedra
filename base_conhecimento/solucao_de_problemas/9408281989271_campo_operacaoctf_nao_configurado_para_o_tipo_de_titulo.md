# Campo OPERACAOCTF não configurado para o tipo de título

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9408281989271-Campo-OPERACAOCTF-n%C3%A3o-configurado-para-o-tipo-de-t%C3%ADtulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9408281989271-Campo-OPERACAOCTF-n%C3%A3o-configurado-para-o-tipo-de-t%C3%ADtulo)  
> **ID:** `9408281989271` | **Última Atualização:** 2026-07-22T15:07:55Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703298041239)

 MENSAGEM:**

[CORE_E05658]: Campo OPERACAOCTF não configurado para o tipo de título.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703298046231)

 SITUAÇÃO:**

Ao tentar receber a venda no cartão de crédito ou débito a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703304252183)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703298050455)

 Habilite o parâmetro** "USARECEBCARTCTF"** na tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado » Preferências).*

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9408131000087)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703298054423)

 Feito isso, acesse o cadastro do **"Tipo de título"*** (Financeiro » Arquivos » Cadastros » Tipos de Título)* utilizado no lançamento e configure corretamente o campo **"Operação CTF"**, na aba **"Preferências de cartão"** com a operação primordial a ser realizada pelo CTF, dentre as seguintes opções:

- Créd. a vista;

- Créd. Parcelado Lojista (sem juros);

- Créd. Parcelado Administradora (com juros);

- Débito;

- Voucher.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703298057751)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16703304265111)

 CAUSA:**

Ao realizar o recebimento de uma venda e o tipo de título não esteja com a Operação CTF definida.