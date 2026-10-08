# Falha Não foi possível confirmar a folha de pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10621819206679-Falha-N%C3%A3o-foi-poss%C3%ADvel-confirmar-a-folha-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/10621819206679-Falha-N%C3%A3o-foi-poss%C3%ADvel-confirmar-a-folha-de-pagamento)  
> **ID:** `10621819206679` | **Última Atualização:** 2026-07-29T13:16:19Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19036148516247)

 MENSAGEM:
**Falha: Não foi possível confirmar a folha de pagamento!

Motivo: javax.ejb.CreateException: Programação de Férias já existe no banco de dados ou um índice único foi violado.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19036148527767)

 CAUSA:**

Ocorre quando existe mais de um período aquisitivo de férias em aberto.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19036177693975)

 SOLUÇÃO:**

Verifique se existe mais de um período aquisitivo em aberto. Exemplo:

![FÉRIAS 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19036148535191)

Se houver dois períodos aquisitivos em aberto: 2021/2022 e 2022/2023, e estiver tentando fazer o cálculo do período mais antigo, no caso 2021/2022, o sistema irá considerar e apresentar na tela o período mais novo em aberto, neste exemplo: 2022/2023. Nesse contexto, ao confirmar o cálculo será apresentada a mensagem citada acima:

Diante disso, o correto é alimentar apenas a última que ainda não foi gozada.

Sendo assim, acesse a tela **Consulta de Férias** *(Caminho de acesso à tela: Pessoal+ » Rotinas Folha » Consulta de Férias),*  clique sobre o período aquisitivo, feito isso, o sistema te direcionará para tela de requisições, nela clique no botão **Aquisitivos **e apague (usando a lixeira) o período aberto indevidamente:  2022/2023.

![periodo aquisitivo 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19036148540567)

Após o ajuste, o cálculo pode ser feito considerando o período aquisitivo correto, e não apresentará erro ao confirmar.