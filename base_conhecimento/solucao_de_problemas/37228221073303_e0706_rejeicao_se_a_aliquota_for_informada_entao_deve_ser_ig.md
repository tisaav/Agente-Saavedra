# E0706 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228221073303-E0706-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228221073303-E0706-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100)  
> **ID:** `37228221073303` | **Última Atualização:** 2026-07-22T14:14:13Z

---

##### **

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228221048855)

 MENSAGEM**

E0706 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

 

##### **

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237712663)

 SITUAÇÃO**

Esta rejeição ocorre quando o usuário tenta emitir uma **NF-e ou NFC-e** e alguma **alíquota tributária** informada no documento fiscal está **fora do intervalo permitido**. O sistema da Sefaz valida se os percentuais de alíquotas (ICMS, IBS, CBS, PIS, COFINS, entre outros) estão dentro do **limite de 0% a 100%**, e ao identificar um valor inválido, rejeita o documento.

 

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37610043760407)

 SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237714199)

 Identifique o imposto com alíquota incorreta

- 

Verifique no XML de retorno da rejeição ou na mensagem de erro qual tributo apresentou o problema: **ICMS, IBS, CBS, PIS, COFINS, etc.**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237715351)

 Acesse o cadastro de alíquotas correspondente ao imposto rejeitado:

- 

Para **ICMS, **acesse a tela **"Alíquotas de ICMS"** (Comercial » Relatórios » Cadastros » Alíquotas de ICMS).

- 

Para **IBS**, acesse a tela **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS).

- 

Para **CBS**, acesse a tela **"Alíquotas CBS"** (Livros Fiscais » Cadastros » Aliquotas de CBS).

- 

Para **PIS**, acesse a tela **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

- 

Para **COFINS**, acesse a tela **"Alíquotas de COFINS'' **(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228221052183)

 Localize a regra de alíquota aplicada

- 

Identifique a configuração específica que incidiu sobre o produto ou operação da nota fiscal rejeitada, utilizando os filtros de pesquisa disponíveis.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228221056663)

 No campo **“Alíquota”** ou **“Percentual (%)”**, certifique-se de que o valor esteja entre **0 e 100**. Corrija qualquer valor que esteja:

- 

Negativo (menor que 0)

- 

Superior a 100

- 

Com formatação incorreta (ex.: 1000 ao invés de 10,00)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237717527)

 Se necessário, verifique também os campos de ''**Redução de Base''**, ''**Alíquota para Crédito''** e outros percentuais relacionados, garantindo que todos estejam dentro do intervalo válido.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237718935)

 Salve as alterações realizadas no cadastro de alíquotas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228221059223)

 **Inutilize a numeração** da NF-e ou NFC-e rejeitada, caso necessário.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237721239)

 Realize um **novo faturamento** do documento fiscal, garantindo que as **alíquotas corretas** sejam aplicadas automaticamente pelo sistema.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228221064087)

 Confira os valores das alíquotas no documento antes de transmitir.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226860360087)

 Proceda com a **autorização da nota** junto à Sefaz.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37610019751703)

 OBSERVAÇÃO:** Este ajuste é de natureza **fiscal e tributária**, devendo ser realizado por um **usuário com conhecimento** sobre a rotina e, preferencialmente, com **orientação do contador**, para evitar impactos indevidos nas demais operações.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228237723927)

 **CAUSA**

A rejeição **E0706** é gerada pela **validação da Sefaz** que verifica se todos os **percentuais de alíquotas tributárias** informados no XML do documento fiscal estão dentro do **intervalo permitido de 0% a 100%**.

As causas mais comuns para esta rejeição são:

- 

**Cadastro incorreto** de alíquotas no sistema, com valores negativos ou superiores a 100%

- 

**Erro de digitação** ao configurar percentuais (exemplo: digitar 1000 ao invés de 10,00)

- 

**Importação de dados** com formatação inadequada

- 

**Configurações tributárias desatualizadas** ou inconsistentes

- 

**Parametrizações manuais** realizadas sem validação prévia dos valores

A Sefaz não aceita valores de alíquotas fora do padrão estabelecido, pois isso **comprometeria a integridade** dos cálculos tributários e da **escrituração fiscal**.