# O campo Meio de Pagamento deve ser preenchido com a opção Sem Pagamento (NT2016/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102173-O-campo-Meio-de-Pagamento-deve-ser-preenchido-com-a-op%C3%A7%C3%A3o-Sem-Pagamento-NT2016-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102173-O-campo-Meio-de-Pagamento-deve-ser-preenchido-com-a-op%C3%A7%C3%A3o-Sem-Pagamento-NT2016-002)  
> **ID:** `360043102173` | **Última Atualização:** 2026-07-22T16:08:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16484717321111)

 MENSAGEM:**

[871 - Rejeição]: O campo Meio de Pagamento deve ser preenchido com a opção Sem Pagamento.  

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16484688314903)

 SOLUÇÃO:**

Avaliar a seguinte regra:

- Caso a NF-e possua finalidade 3 (NF-e Ajuste) ou 4 (Devolução), o campo **"tPag"** deve ser gerado com valor 90 – Sem pagamento.

- Caso a NF-e possua duplicatas, o campo **"tPag"** será gerado com valor 14 – Duplicata Mercantil.

- Caso a NF-e não atender a nenhuma das opções anteriores, o campo **"tPag"** será gerado com valor 99 – Outros.

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16484717330455)

 Acesse: *Financeiro » Arquivos » Cadastros » Tipos de Título* 

- Aba: **"Geral"**

- Campo **"Tipo de pgto para NFC-e / NF-e / CF-e"**: Configure observando as regras acima

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16484717333655)

 Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16484688321047)

 OBSERVAÇÃO:
**

(**NT2016/002**) - Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=XPcFD/sRNlQ=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=XPcFD/sRNlQ=)