# Erro no cálculo da GRRF

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35316448710295-Erro-no-c%C3%A1lculo-da-GRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/35316448710295-Erro-no-c%C3%A1lculo-da-GRRF)  
> **ID:** `35316448710295` | **Última Atualização:** 2026-07-29T13:20:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41142957600023)

**MENSAGEM**

Divergência entre os valores da multa rescisória apresentados na GRRF (Guia de Recolhimento Rescisório do FGTS) gerada pelo sistema Sankhya e os valores constantes no FGTS Digital.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629470389783)

**SITUAÇÃO**

Ao emitir a GRRF através da tela **"Geração de Guias"** (Pessoal+ » Rotinas Folha » Geração de Guias), identifica-se que o valor apresentado no campo 31 não corresponde ao cálculo correto de 8% do FGTS informado no campo 26, gerando divergência nos valores da guia.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629470393879)

**SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629499755159)

 Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629499762455)

 Localize o evento que está causando a divergência no campo 31 da GRRF.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629470407575)

 Verifique a configuração do campo **"Identificação"** do evento.

![Erro no cálculo da GRRF 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629470409623)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629499771543)

 **Caso seja um evento padrão do sistema**, conforme orientado, altere ao valor do campo Identificação  para **"0 - Sem identificação"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629499776535)

 Salve as alterações realizadas no evento.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629499780375)

 Acesse novamente a tela **"Geração de Guias"** (Pessoal+ » Rotinas Folha » Geração de Guias) e emita uma nova GRRF para verificar a correção do campo 31.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35629470427799)

**CAUSA**

A divergência ocorre porque o evento estava configurado com o campo **"Identificação"** definido como **"102 – Evento FGTS"**. Esta identificação possui vínculo direto com a geração da guia do FGTS e corresponde especificamente ao evento de valor do FGTS calculado, fazendo com que o sistema inclua valores adicionais no campo 31, resultando na divergência observada.