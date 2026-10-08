# O título de número único XXXXXX possui ligação com remessa. Para continuar com a exclusão do título será necessário desvinculá-lo da remessa, pela tela Movimentação Financeira

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213893-O-t%C3%ADtulo-de-n%C3%BAmero-%C3%BAnico-XXXXXX-possui-liga%C3%A7%C3%A3o-com-remessa-Para-continuar-com-a-exclus%C3%A3o-do-t%C3%ADtulo-ser%C3%A1-necess%C3%A1rio-desvincul%C3%A1-lo-da-remessa-pela-tela-Movimenta%C3%A7%C3%A3o-Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213893-O-t%C3%ADtulo-de-n%C3%BAmero-%C3%BAnico-XXXXXX-possui-liga%C3%A7%C3%A3o-com-remessa-Para-continuar-com-a-exclus%C3%A3o-do-t%C3%ADtulo-ser%C3%A1-necess%C3%A1rio-desvincul%C3%A1-lo-da-remessa-pela-tela-Movimenta%C3%A7%C3%A3o-Financeira)  
> **ID:** `360044213893` | **Última Atualização:** 2026-07-22T16:00:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292496797591)

 MENSAGEM:**

[CORE_E02441] Erro ao remover entidade: ORA-20101: O titulo de número único XXXXXX possui ligação com remessa. Para continuar com a exclusão do título será necessário desvinculá-lo da remessa, pela tela Movimentação Financeira.
[ORA-06512]: em "SANKHYA.TRG_DLT_TGFFIN", line 300
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_DLT_TGFFIN'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292496811031)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292496825367)

 Acesse: Configurações » Avançado » Preferências

Parâmetro **"PERDESVFINREM - Permite desvincular financeiro de remessa?": **ligado

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292496828311)

 Acesse: Financeiro » Rotinas » Movimentação Financeira

Selecione na tela **"Movimentação financeira" **os financeiros da respectiva nota.

Clique no botão: Outras Opções...>>Desvincular Remessa

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292508259735)

 Realizado os procedimentos acima, proceda com a exclusão/cancelamento desejado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292496859031)

 CAUSA:**

Ocorre quando um ou vários títulos participaram de um arquivo de remessa para o banco, afim de geração de boletos para pagamentos.