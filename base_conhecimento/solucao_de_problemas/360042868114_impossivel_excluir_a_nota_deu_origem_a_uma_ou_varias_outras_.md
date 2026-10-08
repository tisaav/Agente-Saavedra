# Impossível excluir. A nota deu origem a uma ou várias outras notas - SankhyaOM

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042868114-Imposs%C3%ADvel-excluir-A-nota-deu-origem-a-uma-ou-v%C3%A1rias-outras-notas-SankhyaOM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042868114-Imposs%C3%ADvel-excluir-A-nota-deu-origem-a-uma-ou-v%C3%A1rias-outras-notas-SankhyaOM)  
> **ID:** `360042868114` | **Última Atualização:** 2026-07-22T16:05:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113159853975)

 MENSAGEM:**

Impossível excluir. A nota deu origem a uma ou várias outras notas.

ORA-06512: em "SANKHYA.TRG_DLT_TGFCAB", line 353

ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_DLT_TGFCAB'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113159857175)

 SITUAÇÃO:**

Ao tentar excluir/cancelar algum documento lançado no sistema, que deu origem a outro documento, será apresentada a mensagem.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113143780247)

 **SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113143786007)

 **Abra o documento a ser excluído/alterado na tela Central (Compra/Venda/Mov. Interna);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113130172055)

 No quadrante dos Itens » Outras Opções » Documentos Relacionados, identifique os documentos de destino, conforme exemplo abaixo:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14555169151511)

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12065993987223)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113130174615)

 **Abra o documento identificado e sintonize junto a equipe de faturamento à respeito do mesmo.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113174811927)

 **Caso trate-se de um documento recebido pela SEFAZ, não será permitido sua exclusão. Dessa forma, é necessário sintonias com o Contador da empresa sobre o melhor processo.

**Exemplo:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113174814487)

 Faturou a nota de devolução de venda X, através da nota de venda Y.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113174814487)

 Não é possível excluir ou alterar a nota de venda Y, sem excluir/cancelar a nota de devolução X, visto que ambas estão ligadas.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113143805847)

 OBSERVAÇÕES: **

O sistema disponibiliza da opção **"Desligar a nota dos pedidos"**, dentro de **"Outras Opções"** da Central. Executando esse procedimento, será possível desvincular tais documentos.

Essa opção deve ser utilizada com cautela, visto que as informações que ligam um documento ao outro serão desfeitas, tornando os documentos de origem pendentes, gerando impactos nas análises de faturamento da empresa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16113136331159)

 CAUSA**:

Ocorre quando os produtos da nota já foram faturados/entregues/devolvidos, não sendo possível processar a exclusão da nota.