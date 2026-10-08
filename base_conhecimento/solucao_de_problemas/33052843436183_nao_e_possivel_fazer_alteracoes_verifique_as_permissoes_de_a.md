# Não é possível fazer alterações. Verifique as permissões de acesso. - Matriz de Analise de Giro

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33052843436183-N%C3%A3o-%C3%A9-poss%C3%ADvel-fazer-altera%C3%A7%C3%B5es-Verifique-as-permiss%C3%B5es-de-acesso-Matriz-de-Analise-de-Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/33052843436183-N%C3%A3o-%C3%A9-poss%C3%ADvel-fazer-altera%C3%A7%C3%B5es-Verifique-as-permiss%C3%B5es-de-acesso-Matriz-de-Analise-de-Giro)  
> **ID:** `33052843436183` | **Última Atualização:** 2026-07-22T14:29:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33052855288599)

 **MENSAGEM:**

Não é possível fazer alterações. Verifique as permissões de acesso.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33052843430935)

 SITUAÇÃO:**

Ao tentar **alterar uma matriz de Análise de Giro**, mesmo com o login de um usuário que possui todos os acessos liberados via tela de acessos, a mensagem de erro é apresentada, impedindo a edição.

Essa situação costuma gerar dúvidas, pois o erro ocorre mesmo quando os acessos tradicionais já foram concedidos via grupos e permissões usuais.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33052843431959)

SOLUÇÃO:**

Para que o usuário consiga editar a matriz desejada, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068115549719)

 Acesse a rotina **Análise de Giro (Comercial > Rotinas);**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068147118999)

 Selecione a matriz em questão;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068147120151)

 Clique no botão **“Segurança”;**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068115551895)

 No pop-up exibido, localize o usuário que precisa de acesso;

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068147122583)

 Marque as permissões desejadas (visualizar, editar, excluir, etc.);

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33068147122967)

 Salve as alterações.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33052855291927)

CAUSA:**

Quando o parâmetro** "Controla acesso por matriz de análise de giro? - CONTACESSMAT" ** está ativado, o sistema passa a utilizar uma **camada adicional de segurança específica para a Matriz de Análise de Giro**, controlada por meio da aba **Segurança** dentro da própria rotina.

Essa configuração permite definir permissões por **usuário e grupo** diretamente para cada matriz individual, de forma independente das permissões gerais de acesso do sistema.