# Produto: XX Diferença na quantidade de bens digitados

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577734-Produto-XX-Diferen%C3%A7a-na-quantidade-de-bens-digitados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577734-Produto-XX-Diferen%C3%A7a-na-quantidade-de-bens-digitados)  
> **ID:** `360043577734` | **Última Atualização:** 2026-08-14T14:28:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108280388759)

 MENSAGEM**:

[CORE_E01832] Produto: XX Diferença na quantidade de bens digitados!

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284199575)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284200471)

** Caso o lançamento seja de um produto Imobilizado, a TOP está configurado para ** Atualizar BEM**, então neste caso deverá lançar o código do Bem.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284201495)

 Na grade Itens, selecione o item Imobilizado, clique no botão **"[...]Outras Opções"** » **"Bens"** e selecione a opção de acordo com o documento, pesquise pelo bem e selecione.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108280401303)

** Caso o lançamento não seja de um produto Imobilizado, considere trocar a TOP do lançamento da nota ou ajustar a configuração da TOP para não Atualizar BEM, acessando:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284201495)

 Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284201495)

 Aba: **"Estoque"**,

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284201495)

Campo "**Atualização do BEM": **Não Atualizar. Com esta opção marcada, não irá validar o BEM no ato do lançamento do documento. (Marcação histórica, após ajuste, deverá lançar o documento novamente.)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108284209943)

 CAUSA**:

Ocorre quando o documento lançado possui itens do tipo Imobilizado e a TOP está configurado para atualizar bem e o bem não foi vinculado ao produto lançado ou a TOP não deveria atualizar bem e está configurado para atualizar.

Considere alinhar com a equipe interna para verificar o documentado lançado antes de fazer os ajustes informados acima.