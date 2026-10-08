# E0707 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228242317335-E0707-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228242317335-E0707-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100)  
> **ID:** `37228242317335` | **Última Atualização:** 2026-07-22T14:14:12Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242270231)

 **MENSAGEM**

E0707 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228255346327)

 **SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o documento fiscal foi **rejeitado pela SEFAZ** com a mensagem acima, indicando que uma **alíquota informada está fora do intervalo permitido**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242273047)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242273943)

 **Identifique o imposto com alíquota inválida**

- 

Analise a mensagem de rejeição detalhada e verifique qual tributo está com a alíquota fora do intervalo permitido, como **ICMS, IBS, CBS, PIS, COFINS** ou outro imposto informado no documento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242277911)

 Acesse o cadastro da alíquota correspondente:

- 

Para **ICMS**, acesse a tela ''**Alíquotas de ICMS'' **(Comercial » Relatórios » Cadastros » Alíquotas de ICMS).

- 

Para **IBS**, **''Aliquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS).

- 

Para **CBS ****''Aliquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242280855)

 Localize a **regra de alíquota** que foi aplicada ao produto ou serviço da nota fiscal rejeitada.

Utilize os filtros disponíveis para facilitar a busca, como:

- 

"Tipo de Operação"

- 

"UF de Origem"

- 

"UF de Destino"

- 

"Código de Situação Tributária - CST"

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228255355671)

 Verifique o campo **"Alíquota"** ou **"Percentual (%)"** da regra identificada e certifique-se de que o valor está **entre 0 e 100**. Caso o valor esteja fora desse intervalo, corrija-o imediatamente. 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228255356311)

 Caso o erro esteja relacionado a **campos de redução de base de cálculo** ou **alíquotas de crédito**, verifique também esses campos e ajuste os valores para que estejam dentro do intervalo permitido

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228255357207)

 Salve as alterações realizadas no cadastro de alíquotas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242295319)

 Retorne à nota fiscal rejeitada, **inutilize a numeração** caso necessário e realize um **novo faturamento**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242297495)

 Confira se as **alíquotas aplicadas** estão corretas e dentro do intervalo permitido antes de confirmar a nota.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242302487)

 Proceda com a **autorização da NF-e ou NFC-e** junto à SEFAZ. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228242304663)

 **CAUSA**

A rejeição E0707 ocorre quando o sistema identifica que **alguma alíquota tributária informada no documento fiscal está fora do intervalo válido**, ou seja, possui valor **menor que 0% ou maior que 100%**. Essa validação é realizada pela SEFAZ para garantir a **consistência dos dados tributários** transmitidos.

As principais causas incluem:

- 

Cadastro incorreto de **alíquotas de ICMS, IBS, CBS, PIS ou COFINS** com valores negativos ou superiores a 100%.

- 

Erro de digitação ao informar o **percentual da alíquota** no cadastro de regras tributárias.

- 

Configuração inadequada de **campos de redução de base de cálculo** ou **alíquotas de crédito**.

- 

Utilização de **regras tributárias desatualizadas** ou incompatíveis com a legislação vigente.

**Importante:** Esse ajuste deve ser realizado por um **usuário com conhecimento fiscal e tributário**, preferencialmente com orientação do contador responsável, para evitar impactos indevidos na apuração de impostos.