# E0692 Rejeição: A alíquota do Cofins deve ser igual ou maior que 0 e menor ou igual a 100%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37230524892823-E0692-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-Cofins-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/37230524892823-E0692-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-Cofins-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100)  
> **ID:** `37230524892823` | **Última Atualização:** 2026-07-22T14:13:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524873111)

 **MENSAGEM**

E0692 Rejeição: A alíquota do Cofins deve ser igual ou maior que 0 e menor ou igual a 100%.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524874519)

 **SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e), o sistema retorna uma rejeição relacionada ao valor da **alíquota do COFINS** informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524875031)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524876311)

 Acesse a tela **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e localiza a rega de alíquota que está sendo utilizada na operação fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524878487)

 Verifque se o campo** ''Alíquota'' **está informado com **valores entre 0 e 100**. Caso o valor esteja incorreto, ajuste para um percentual válido conforme a legislação vigente:

- 

Para operações com **incidência cumulativa**, a alíquota padrão é **3,00%**.

- 

Para operações com **incidência não-cumulativa**, a alíquota padrão é **7,60%**.

- 

Para operações **sem incidência** ou com **alíquota zero**, informe **0%**. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38100431353623)

 Caso a operação seja **isenta, não tributada ou com suspensão**, verifique se o campo** "****Cód. sit. tributária****"** está configurado corretamente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38100431357975)

 Mesmo que a incidência seja **zero**, é necessário criar uma alíquota com **valor 0%** para que os dados de COFINS sejam gerados corretamente no XML da NF-e no momento da confirmação/aprovação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230524881431)

 Após realizar os ajustes **salve as alterações.**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38100431358487)

 Retorne à **Nota Fiscal** e **redigite os itens** ou **relance a nota** para que as novas configurações sejam aplicadas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38100475740311)

 Gere novamente o **lote de transmissão** e busque a **autorização da SEFAZ**. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230534044823)

 **CAUSA**

A rejeição ocorre porque o sistema enviou para a SEFAZ um **valor de alíquota do COFINS inválido**, ou seja, **menor que 0% ou maior que 100%**. Isso pode acontecer devido a:

- 

**Erro no cadastro de alíquotas:** o campo **"Alíquota COFINS (%)"** foi preenchido com um valor fora do intervalo permitido.

- 

**Configuração incorreta do CST:** o **Código de Situação Tributária** do COFINS não está adequado à operação fiscal.

- 

**Falta de alíquota cadastrada:** não existe uma alíquota de COFINS configurada para a operação, fazendo com que o sistema envie um valor nulo ou inválido.

- 

**Inconsistência nos cálculos:** problemas no rateio proporcional ou na base de cálculo podem gerar valores incorretos de alíquota.