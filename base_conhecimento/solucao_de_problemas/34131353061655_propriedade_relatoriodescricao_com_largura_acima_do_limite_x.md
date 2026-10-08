# "Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)" ao salvar um Relatório Formatado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34131353061655--Propriedade-Relatorio-DESCRICAO-com-largura-acima-do-limite-XX-XX-ao-salvar-um-Relat%C3%B3rio-Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/34131353061655--Propriedade-Relatorio-DESCRICAO-com-largura-acima-do-limite-XX-XX-ao-salvar-um-Relat%C3%B3rio-Formatado)  
> **ID:** `34131353061655` | **Última Atualização:** 2026-07-22T14:27:39Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131368300951)

 **MENSAGEM**

Propriedade 'Relatorio.DESCRICAO' com largura acima do limite: (XX > XX)

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34325489598871)

 **SITUAÇÃO**

O erro ocorre ao criar ou alterar um relatório formatado (**JRXML**) cuja descrição ultrapassa o número máximo de caracteres permitidos pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131353059735)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34325489600279)

  Ajuste a descrição do relatório para que tenha tamanho igual ou inferior ao limite informado na mensagem de erro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34325489601687)

  Conte também os caracteres de espaços e pontuação, pois eles são considerados no total.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131353060631)

 **CAUSA**

O campo **"Descrição"** do relatório possui um tamanho máximo definido pela aplicação. Ao inserir um texto com quantidade de caracteres superior a esse limite, o sistema bloqueia a operação e retorna a mensagem de erro.