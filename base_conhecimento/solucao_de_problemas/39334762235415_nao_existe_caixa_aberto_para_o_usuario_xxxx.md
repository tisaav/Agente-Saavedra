# Não existe caixa aberto para o usuário XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39334762235415-N%C3%A3o-existe-caixa-aberto-para-o-usu%C3%A1rio-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/39334762235415-N%C3%A3o-existe-caixa-aberto-para-o-usu%C3%A1rio-XXXX)  
> **ID:** `39334762235415` | **Última Atualização:** 2026-09-18T19:34:25Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334754604055)

** MENSAGEM**

[COM_E00853]: Não existe caixa aberto para o usuário XXXX

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762233367)

** SOLUÇÃO**

A mensagem é apresentada quando o usuário que está tentando realizar a venda no PDV Web não possui permissão de caixa.

Para solucionar esta pendência, verifique as configurações abaixo, caso o usuário em questão deva ser do tipo **Caixa.**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762233879)

 Acesse a tela **“Usuários”** (Configurações >> Controle de Acesso)
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762234007)

 Busque pelo usuário que utiliza o **PDV Web** e verifique, na aba **“Identificação”**, se a opção **“Caixa”** está marcada.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762234391)

Após isso, acesse a aba **“Contas p/ Baixa”** e vincule uma conta ao usuário.
 

![Imagem](/attachments/token/A3tWNZDwgCHhrpiNzw5U2PyvB/?name=image.png)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762234647)

 Em seguida, acesse as **Configurações do Usuário** por meio do botão **“Outras Opções”**.
 

![Imagem](/attachments/token/rpzVLGnRRQtNYKxrfLiooBAAU/?name=image.png)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762234775)

 Será aberto um pop-up chamado **“Configurações do Usuário”**. No campo **“Número da conta padrão na baixa”**, deve estar vinculada a mesma conta informada anteriormente na aba **“Contas p/ Baixa”**.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39611918680471)

****Importante:**

Após realizar essas configurações, será possível efetuar a **abertura e fechamento de caixa no PDV Web** normalmente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39334762232599)

** CAUSA**

Isso ocorre porque o sistema exige que o usuário esteja configurado como “Caixa”, com uma conta vinculada para movimentação financeira.  Quando essa configuração não está completa, o sistema interpreta que não há um caixa válido aberto, bloqueando a operação de venda.