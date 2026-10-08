# E0453 Rejeição: O valor percentual para dedução/redução deve ser maior que 0 e menor ou igual a 100%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225472004247-E0453-Rejei%C3%A7%C3%A3o-O-valor-percentual-para-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-deve-ser-maior-que-0-e-menor-ou-igual-a-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225472004247-E0453-Rejei%C3%A7%C3%A3o-O-valor-percentual-para-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-deve-ser-maior-que-0-e-menor-ou-igual-a-100)  
> **ID:** `37225472004247` | **Última Atualização:** 2026-07-22T14:15:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225471988375)

 **MENSAGEM**

E0453 Rejeição: O valor percentual para dedução/redução deve ser maior que 0 e menor ou igual a 100%.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455720087)

 **SITUAÇÃO**

A nota fiscal eletrônica foi emitida com a informação de um percentual de dedução ou de redução da base de cálculo do IBS ou da CBS fora do intervalo permitido no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455723671)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225471991831)

 Acesse a tela** ''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e/ou **''Alíquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455726359)

 Localize a **regra de alíquota** que foi aplicada na nota fiscal rejeitada. Utilize os filtros disponíveis para facilitar a busca, como **"Produto"**, **"TOP"** (Tipo de Operação) ou **"Parceiro"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455727895)

 Ao identificar a regra, **verifique os campos relacionados** ao percentual de dedução ou redução: 

- 

**"% Redução de Alíquota IBS"**: percentual de redução de alíquota IBS;

- 

**"% Redução de Alíquota CBS"**: percentual de redução de alíquota CBS;

- 

**"% do Diferimento IBS"**: percentual de diferimento aplicado ao IBS;

- 

**"% do Diferimento CBS"**: percentual de diferimento aplicado ao CBS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455729175)

 Certifique-se de que **todos os percentuais informados** estejam dentro do intervalo válido:

- 

**Maior que 0 (zero) e menor ou igual a 100**.

- 

Caso algum campo esteja com valor igual a 0 (zero), negativo ou superior a 100, **corrija o valor** conforme a legislação aplicável.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225471995543)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225455732887)

 Retorne à nota fiscal rejeitada e **redigite os itens** ou **relance a nota** para que o sistema recalcule os tributos com os percentuais corrigidos.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225471999127)

 **Gere o lote** e clique em **"Buscar Autorização"** para transmitir novamente a nota fiscal à Sefaz. 
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38297741744407)

 OBSERVAÇÃO:** É importante que esse ajuste seja realizado por um **usuário certificado** na utilização do sistema e que compreenda os **impactos fiscais e tributários** relacionados à Reforma Tributária. Em caso de dúvidas sobre os percentuais corretos a serem aplicados, **consulte seu contador**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225471999639)

 **CAUSA**

A rejeição ocorre porque o sistema da Sefaz **valida os percentuais de dedução e redução** informados nos grupos de tributação do IBS e CBS da nota fiscal eletrônica. Quando o percentual está **fora do intervalo permitido** (igual a 0, negativo ou superior a 100%), a validação falha e a nota é rejeitada com a mensagem E0453, em conformidade com as **regras estabelecidas pela Lei Complementar nº 214/2025** e pela **Emenda Constitucional 132/2023**, que regulamentam a Reforma Tributária.