# O registro de "Vendedor" (TGFVEN) selecionado não está cadastrado, ou não está ativo, ou não é analítico

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673153-O-registro-de-Vendedor-TGFVEN-selecionado-n%C3%A3o-est%C3%A1-cadastrado-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673153-O-registro-de-Vendedor-TGFVEN-selecionado-n%C3%A3o-est%C3%A1-cadastrado-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico)  
> **ID:** `360043673153` | **Última Atualização:** 2026-07-22T16:03:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018496151)

 MENSAGEM:**

ORA-20101: O registro de "Vendedor" (TGFVEN) selecionado não está cadastrado, ou não está ativo, ou não é analítico.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135005088279)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018503063)

 Busque no lançamento realizado todos os códigos de vendedores vinculados.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018503831)

 Para lançamentos na **"Central *(Vendas/Compras/Mov.Interna)"*** essa informação pode ser observada no cabeçalho, nos itens e na aba financeiro, conforme abaixo:

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14635574913047)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018504727)

 Identificado os códigos de vendedores vinculados no respectivo lançamento, acesse a tela **"Vendedores/Compradores"** *(Configurações » Cadastros)*, selecione os mesmos e faça uma análise do campo **Ativo**:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14635491239319)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135005091863)

 Caso esse campo esteja desmarcado, sintonize internamente o responsável por tê-lo desativado, avaliando se a ativação ocorrerá ou se um vendedor que difere desse deverá ser utilizado em seu lançamento.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135005092759)

 Realizado os devidos ajustes, prossiga com o lançamento.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018506391)

 OBSERVAÇÃO:**

Saiba como configurar campos invisíveis no Layout da nota, acessando este artigo: **"******[Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)**"**

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135018507543)

 CAUSA:**

Ao faturar/devolver um pedido/nota, a mensagem ocorre quando o Vendedor/Comprador, vinculado ao parceiro como preferencial ou digitado direto na nota está 'inativo' em seu cadastro.

 

![495b9bfc-3e43-423b-ba7c-4aef8cbd564c](https://ajuda.sankhya.com.br/hc/article_attachments/32231406945943)

 Caso o vendedor/comprador seja um ex-colaborador, será necessário reativar seu cadastro, seguir com o lançamento e depois desativá-lo novamente. Nativamente não é possível utilizar cadastros inativos.


---

### 🔗 Links e Referências Internas:

- [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)