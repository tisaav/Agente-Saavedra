# A linha referenciada na tabela TGFVEND não está cadastrada ou não está ativa ou não analítica

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865514-A-linha-referenciada-na-tabela-TGFVEND-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-anal%C3%ADtica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865514-A-linha-referenciada-na-tabela-TGFVEND-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-anal%C3%ADtica)  
> **ID:** `360042865514` | **Última Atualização:** 2026-07-22T16:05:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090339461271)

 MENSAGEM:**

Erro durante o processo de faturamento.
Número único XXXXXX.
ORA-20101: A LINHA REFERENCIADA NA TABELA TGFVEND NÃO ESTÁ CADASTRADA OU NAO ESTÁ ATIVA OU NÃO ANALÍTICA.
ORA-06512: em "SANKHYA.STP_POPULA_MSG", line 5
ORA-06512: em "SANKHYA_TRG_INC_TGFITE", line 81
ORA-04088: erro durante a execução do gatilho 'SANKHYA_TRG_INC_TGFITE'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090339464855)

 SITUAÇÃO:**

Ao faturar/devolver um pedido/nota é apresentado a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090339468567)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090393069079)

 Acesse a Nota/Pedido, verifique no cabeçalho e também nos itens o código do vendedor.

Empresas que trabalham com **Múltiplas Comissões de Vendedores**, apresentará a aba: **"Comissões no rodapé da nota"** que também terá os códigos dos vendedores.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090393073303)

 Acesse a tela **"[Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores)"** *(Caminho de acesso: Configurações » Cadastros » Vendedores/Compradores)*

Acesse com o código do vendedor, o cadastro, e verifique o campo **"Ativo"**. Caso esteja desmarcado, verifique a possibilidade de ativá-lo ou substituir por outro vendedor no pedido/nota caso o vendedor esteja desligado da empresa.

Caso seja um Lançamento novo de nota/pedido e ocorrer o mesmo incidente, acesse o **"[Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** da nota *(Caminho de acesso: Configurações » Cadastros » Parceiros)*, aba **"Identificação"**, campo **"Vend. Preferencial"**, executar o mesmo procedimento e verifique se está ativo.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090393076503)

 Após os ajustes, fature novamente o pedido/nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16090339489559)

 CAUSA:**

Ocorre quando o Vendedor/Comprador, vinculado ao Parceiro como preferencial ou digitado direto na nota/pedido esta 'inativo' em seu cadastro.


---

### 🔗 Links e Referências Internas:

- [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores)
- [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)