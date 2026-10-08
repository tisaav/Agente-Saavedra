# 1059 Rejeição: Índice de mistura do Biocombustível informado indevidamente superior ao obrigatório para esta Classificação Tributária do IBS e CBS [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141365200023-1059-Rejei%C3%A7%C3%A3o-%C3%8Dndice-de-mistura-do-Biocombust%C3%ADvel-informado-indevidamente-superior-ao-obrigat%C3%B3rio-para-esta-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-CBS-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141365200023-1059-Rejei%C3%A7%C3%A3o-%C3%8Dndice-de-mistura-do-Biocombust%C3%ADvel-informado-indevidamente-superior-ao-obrigat%C3%B3rio-para-esta-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-CBS-nItem-999)  
> **ID:** `37141365200023` | **Última Atualização:** 2026-07-22T14:19:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365195287)

 **MENSAGEM**

1059 Rejeição: Índice de mistura do Biocombustível informado indevidamente superior ao obrigatório para esta Classificação Tributária do IBS e CBS [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141349615639)

 **SITUAÇÃO**

Ao emitir o documento fiscal, o sistema retorna uma rejeição relacionada a um item que utiliza a **Classificação Tributária do IBS e CBS 620005**, considerando o **percentual do índice de mistura do Etanol Anidro na Gasolina C** informado no documento. A rejeição é apresentada no momento da validação e transmissão do documento fiscal eletrônico.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365196183)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365196439)

 Acesse a tela de **"Produtos"** (Configurações » Cadastros » Produtos » Produtos).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365196695)

 Na aba **''Combustível'',** localize o produto relacionado ao combustível que está gerando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37881448474263)

 No campo **''Percentural do Índice de Mistura''**, verifique e ajuste o valor para que ele seja inferiro ao percentual obrigatório, estabelecido pela legislação para a Classificação Tributária 620005.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365197207)

 Caso o percentual de mistura estiver correto, acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141365197591)

 Verifique se a **Classificação Tributária do IBS e CBS** está adequada para o produto em questão.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141349621143)

 Localize a **alíquota** utilizada no documento fiscal e verifique se o campo **“Código de Classificação Tributária”** está configurado corretamente. Caso identifique divergência, ajuste a classificação para uma opção compatível com o **percentual de mistura informado**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37881465708695)

 Após realizar os ajustes, **gere novamente o documento fiscal**, garantindo que a **tag pBio** seja preenchida corretamente com as informações atualizadas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141349621271)

 **CAUSA**

A rejeição ocorre devido à **incompatibilidade** entre o percentual do índice de mistura do Etanol Anidro na Gasolina C informado e a Classificação Tributária do IBS e CBS utilizada no documento fiscal. Conforme o artigo 179, inciso IIb da Lei Complementar 214/2025, quando utilizada a Classificação Tributária 620005, o percentual do índice de mistura do Etanol Anidro na Gasolina C **deve ser inferior ao obrigatório**. Caso o percentual informado seja superior ao obrigatório, o documento fiscal será rejeitado com o código 1059.

Além disso, é importante observar que, de acordo com a regra de validação UB14-40, quando utilizada a Classificação Tributária 620005, a finalidade da NFe (tag: finfe) deve ser diferente de 5 (Nota de crédito), conforme estabelecido no mesmo artigo da Lei Complementar.