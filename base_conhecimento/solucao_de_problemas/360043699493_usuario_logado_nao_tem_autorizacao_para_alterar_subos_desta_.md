# Usuário logado não tem autorização para alterar SubOS desta fila

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043699493-Usu%C3%A1rio-logado-n%C3%A3o-tem-autoriza%C3%A7%C3%A3o-para-alterar-SubOS-desta-fila](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043699493-Usu%C3%A1rio-logado-n%C3%A3o-tem-autoriza%C3%A7%C3%A3o-para-alterar-SubOS-desta-fila)  
> **ID:** `360043699493` | **Última Atualização:** 2026-07-22T16:02:26Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743468951)

MENSAGEM:**

Usuário logado não tem autorização para alterar SubOS desta fila.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743473559)

 SITUAÇÃO:**

Ao tentar alterar uma Ordem de Serviço, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163775648023)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743477911)

 *Configurações » Controle de Acesso » Relacionamento entre Usuários*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163775658519)

 Com o usuário que está tentando alterar a SubOS, caso seja diferente do usuário que lançou a OS-Ordem de Serviço.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163775658519)

 Insira o usuário na aba **"Gerente"**, de forma que o usuário que lançou a negociação seja Subordinado a ele e esteja devidamente cadastrado na aba **"Subordinado".**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163775658519)

 Nesta tela também é possível configurar usuário Membro de alguma Fila, inserindo o mesmo na aba: Membros da Fila. 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743481367)

Para conseguir alterar a SubOS o parâmetro **"SERVGERALTSUB"** deve estar ligado.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14713235309847)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743483287)

 Após os ajustes, execute novamente o processo.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163743484823)

 CAUSA:**

Ocorre quando a tentativa de alteração na Ordem de Serviço é realizada por outro usuário e/ou seu respectivo Gerente, que não efetuou o lançamento inicial e não é membro da fila.