# Erro ao tentar logar com usuário caixa

> **Módulo:** Melhores Praticas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30589936502423-Erro-ao-tentar-logar-com-usu%C3%A1rio-caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/30589936502423-Erro-ao-tentar-logar-com-usu%C3%A1rio-caixa)  
> **ID:** `30589936502423` | **Última Atualização:** 2026-07-24T12:42:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30589936490135)

 **MENSAGEM:**

Falha ao tentar chamar o serviço 'AberturaCaixaSP.abreCaixaAtualizandoSessao'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30589930720919)

SOLUÇÃO:**

Verifique se a conta em questão está sendo utilizada por algum usuário e se permanece em aberto.

Para isso, utilize o seguinte comando no **DBExplorer** (*Configurações » Avançado » DBExplorer*):
**SELECT * FROM TGFCAI WHERE DTFECHAMENTO IS NULL**

 

**Exemplo:**

 

![Erro ao tentar logar com usuário caixa Falha ao tentar 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30596774127895)

 

Se houver registros com o campo **DTFECHAMENTO** em branco, significa que existem caixas em aberto. Nesse caso, o respectivo usuário deverá realizar o fechamento antes de prosseguir.

Caso não tenha acesso à tela **DBExplorer**, a consulta pode ser realizada por meio da tela "**Fechamento de Caixa"** (Financeiro » Relatórios » Fechamento de Caixa).

Aplique o filtro informando o período (preferencialmente um período relativamente grande) e os usuários que utilizam a conta.

Na grade, será possível identificar as contas e verificar se há caixas sem fechamento (campo "**Dt. Fechamento"** vazio).

Exemplo: 

 

![Erro ao tentar logar com usuário caixa Falha ao tentar 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30596774129559)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30596674583959)

 Observação:**

Para fechar o caixa, o usuário deve acessar o sistema e realizar o fechamento pela tela **PDV WEB**, caso o parâmetro **USAABFCAIXAPDV** esteja ativado.

Se o parâmetro **não** estiver ativado, o fechamento do caixa deverá ser realizado manualmente ao sair do sistema.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30589936491159)

CAUSA:**

Mensagem ocorre quando tenta logar no sistema com usuário caixa que tenha uma conta vinculada e a mesma esteja com caixa aberto aberto em outro usuário.