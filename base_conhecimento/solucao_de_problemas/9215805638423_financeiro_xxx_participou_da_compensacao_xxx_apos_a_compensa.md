# Financeiro xxx participou da Compensação xxx após a compensação que está sendo desfeita, neste caso a compensação null deve ser desfeita primeiro pois ela foi uma compensação total, ou seja, o título foi baixado por ela

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9215805638423-Financeiro-xxx-participou-da-Compensa%C3%A7%C3%A3o-xxx-ap%C3%B3s-a-compensa%C3%A7%C3%A3o-que-est%C3%A1-sendo-desfeita-neste-caso-a-compensa%C3%A7%C3%A3o-null-deve-ser-desfeita-primeiro-pois-ela-foi-uma-compensa%C3%A7%C3%A3o-total-ou-seja-o-t%C3%ADtulo-foi-baixado-por-ela](https://ajuda.sankhya.com.br/hc/pt-br/articles/9215805638423-Financeiro-xxx-participou-da-Compensa%C3%A7%C3%A3o-xxx-ap%C3%B3s-a-compensa%C3%A7%C3%A3o-que-est%C3%A1-sendo-desfeita-neste-caso-a-compensa%C3%A7%C3%A3o-null-deve-ser-desfeita-primeiro-pois-ela-foi-uma-compensa%C3%A7%C3%A3o-total-ou-seja-o-t%C3%ADtulo-foi-baixado-por-ela)  
> **ID:** `9215805638423` | **Última Atualização:** 2026-07-22T15:09:24Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16691587082647)

** Mensagem**

[FIN_E00298]: Financeiro XXX participou da Compensação xxx após a compensação que está sendo desfeita, neste caso a compensação xxx deve ser desfeita primeiro pois ela foi uma compensação total, ou seja, o título foi baixado por ela.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39596528467095)

** Situação**

Ao tentar desfazer uma compensação financeira na tela **"Compensação Financeira"** (Financeiro >> Rotinas >> Compensação Financeira), o sistema apresenta a mensagem informando que existe outra compensação posterior que precisa ser desfeita primeiro. Porém, ao tentar desfazer a compensação indicada, o sistema retorna uma mensagem similar apontando para a compensação anterior, criando um **"loop de dependência"** entre as compensações.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16691587083671)

** Solução**

Para resolver o erro de dependência circular entre compensações, siga o procedimento abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16691544617495)

 Acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira) e localize os títulos envolvidos nas compensações.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16691587088791)

 Identifique no campo **"Nro Compensação/Acerto"** os números das compensações vinculadas a cada título financeiro.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39596507255191)

 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39596528473111)

 Verifique a **"ordem cronológica"** das compensações realizadas, identificando qual foi executada primeiro e qual foi executada posteriormente.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39596507257879)

 Acesse a tela **"Compensação Financeira"** (Financeiro >> Rotinas >> Compensação Financeira).
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39596507258391)

 No campo **"Acerto"**, clique na **"lupa"** e pesquise pela última compensação realizada (a mais recente cronologicamente).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39596528474135)

 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39596507259159)

 Selecione a compensação e clique no **"Botão Desfazer"** para reverter a operação.
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39596507260695)

 Após desfazer a compensação mais recente, retorne à tela e localize a compensação anterior.
 

![8](https://ajuda.sankhya.com.br/hc/article_attachments/39596528479511)

 Clique novamente no **"Botão Desfazer"** para reverter a compensação anterior.
 

![9](https://ajuda.sankhya.com.br/hc/article_attachments/39596528481303)

 Verifique na tela **"Movimentação Financeira"** se os títulos retornaram aos seus valores e parcelas originais.
 

**Observações adicionais para casos específicos:**

Se o título já tiver sido contabilizado, será necessário avaliar o estorno junto à contabilidade.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16691544619031)

** Causa**

O erro ocorre quando um mesmo título financeiro participa de múltiplas compensações em sequência. O sistema exige que as compensações sejam desfeitas respeitando a ordem cronológica inversa, ou seja, a última compensação realizada deve ser desfeita primeiro.

Quando existe uma compensação posterior vinculada à compensação que se tenta estornar, o sistema bloqueia a operação para preservar a integridade dos dados financeiros. Isso é especialmente importante quando a compensação posterior foi uma compensação total, que baixou completamente o título.

Além disso, o problema pode ser agravado quando as compensações são realizadas de forma inadequada, como compensar múltiplos títulos de despesa simultaneamente contra múltiplos títulos de receita. Esse procedimento pode gerar parcelas adicionais indevidas e causar divergências entre os valores de receita e despesa, resultando em erros contábeis e dificuldades no estorno das operações.