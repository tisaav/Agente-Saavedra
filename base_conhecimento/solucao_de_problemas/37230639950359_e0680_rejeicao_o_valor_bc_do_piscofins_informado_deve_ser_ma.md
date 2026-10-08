# E0680 Rejeição: O valor BC do Pis/Cofins informado deve ser maior que zero e menor que o valor do serviço informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37230639950359-E0680-Rejei%C3%A7%C3%A3o-O-valor-BC-do-Pis-Cofins-informado-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37230639950359-E0680-Rejei%C3%A7%C3%A3o-O-valor-BC-do-Pis-Cofins-informado-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS)  
> **ID:** `37230639950359` | **Última Atualização:** 2026-07-22T14:13:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230639943319)

 **MENSAGEM:**

E0680 Rejeição: O valor BC do Pis/Cofins informado deve ser maior que zero e menor que o valor do serviço informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230639943959)

 **SITUAÇÃO: **

Ao emitir um **documento fiscal de serviço (DPS)**, o sistema calculou a **Base de Cálculo do PIS/COFINS** com valor zerado ou com valor igual ou superior ao valor total do serviço prestado, violando a regra de validação da SEFAZ que exige que este valor seja **maior que zero e menor que o valor do serviço** informado no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230639944471)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634039831)

 Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634042519)

 Localize a alíquota utilizada no documento fiscal rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634044439)

 Na aba **''Tributação''**, verifique se o campo **"Código de situação tributária - CST"** está configurado corretamente para permitir a **tributação de PIS/COFINS**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230639945495)

 Certifique-se de que o **percentual de redução de base de cálculo** não está configurado com valor que resulte em base de cálculo zerada ou igual ao valor do serviço.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634045207)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o TOP utilizado na operação.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634046103)

 Na aba **"Impostos"**, verifique as configurações relacionadas à dedução de valores na base de cálculo do PIS/COFINS:

- 

Verifique se a opção **"Deduzir valor do ICMS na BC do PIS e COFINS?"** está configurada adequadamente.

- 

Verifique se a opção **"Deduzir valor do ICMS/ST na BC do PIS e COFINS?"** está configurada adequadamente.

- 

Certifique-se de que as deduções não estão **zerando ou igualando** a base de cálculo ao valor do serviço.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230639947415)

 Revise o **valor do serviço** informado no documento fiscal e certifique-se de que está correto e **maior que zero**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555693696279)

 Após realizar os ajustes necessários, **reemita o documento fiscal** para que o cálculo da Base de Cálculo do PIS/COFINS seja processado corretamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230634046871)

 **CAUSA**

A rejeição ocorre quando a **Base de Cálculo do PIS/COFINS** informada no documento fiscal de serviço está com **valor zerado**, **negativo** ou **igual ou superior ao valor total do serviço**. Isso pode acontecer devido a:

- 

**Configuração incorreta** do CST na alíquota, impedindo a tributação adequada.

- 

**Percentual de redução de base** configurado de forma inadequada, resultando em base de cálculo inválida.

- 

**Deduções excessivas** configuradas no TOP (ICMS, ICMS/ST, ISS) que eliminam ou excedem o valor da base de cálculo.

- 

**Valor do serviço** informado incorretamente no documento fiscal.

- 

**Erro no cálculo proporcional** de despesas acessórias que impactam a base de cálculo do PIS/COFINS.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)