# O Grupo de usuário 'X' não pode usar a TOP 'Y'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7116849779351-O-Grupo-de-usu%C3%A1rio-X-n%C3%A3o-pode-usar-a-TOP-Y](https://ajuda.sankhya.com.br/hc/pt-br/articles/7116849779351-O-Grupo-de-usu%C3%A1rio-X-n%C3%A3o-pode-usar-a-TOP-Y)  
> **ID:** `7116849779351` | **Última Atualização:** 2026-07-22T15:14:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490877854871)

 MENSAGEM:**

[CORE_E02939] O Grupo de usuário 'X' não pode usar a TOP 'Y'.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490877857175)

 CAUSA:**

Ocorre quando está sendo utilizado um usuário, vinculado a um grupo de usuários, que tenha restrições e/ou validações em relação a 'TOP' utilizada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490877863063)

 SOLUÇÃO:**

TOP com restrições/exceções:

Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450954647063)

 Acesse a tela **"Tipos de Operação - TOP"** *(Caminho de acesso: Comercial » Arquivo » Cadastros*).

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450954647063)

 Acione o botão **"Outras Opções",** em seguida clique em:** "Restrições/Exceções".**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15938758696471)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450954647063)

 Verifique se existem regras vinculadas para** "Usuário/Grupo Usuário"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15938777940119)

 

- No exemplo acima, a TOP não poderá ser lançada por **usuários que estão vinculados ao grupo de usuário 34 - CAIXA PDV**;

- Para utilização dessa TOP com esse grupo de usuários, essa linha deverá ser excluída de exceções. Para tal, realize alinhamento interno e compreenda se essa exclusão é válida para o cenário atual da empresa.

- Caso a marcação fosse para 'Restrições' (só pode ser usado com), o grupo de usuário desejado deverá constar nessa lista.