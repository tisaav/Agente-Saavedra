# ./sannfe-service: bin/unpack200: /lib/ld-linux.so.2: bad ELF interpreter: Arquivo ou diretório não encontrado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616653--sannfe-service-bin-unpack200-lib-ld-linux-so-2-bad-ELF-interpreter-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616653--sannfe-service-bin-unpack200-lib-ld-linux-so-2-bad-ELF-interpreter-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado)  
> **ID:** `360044616653` | **Última Atualização:** 2026-07-22T15:53:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813942404119)

 MENSAGEM:**

./sannfe-service: bin/unpack200: /lib/ld-linux.so.2: bad ELF interpreter: Arquivo ou diretório não encontrado

Error unpacking jar files. Abortin.

you might need administrative priviledges for this operation

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813934258327)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813942412183)

  Acesse o putty com usuário **ROOT**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813942415255)

  Execute o comando: [root@linux ~] **yum install ld-linux.so.2**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813934266647)

  Selecione Y[Yes] quando solicitado e instale o pack **unpack200**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813934268823)

  Volte com o usuário mgeweb, acesse o SANNFE e inicie o novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16813934271127)

 CAUSA:**

Ocorre quando algumas distribuição do Linux estão recém instalada e/ou falta a biblioteca de JRE(Java).