# E0694 Rejeição: O valor do PIS informado não corresponde ao resultado da BC PIS/COFINS x Alíquota PIS, que foram informados na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228058663703-E0694-Rejei%C3%A7%C3%A3o-O-valor-do-PIS-informado-n%C3%A3o-corresponde-ao-resultado-da-BC-PIS-COFINS-x-Al%C3%ADquota-PIS-que-foram-informados-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228058663703-E0694-Rejei%C3%A7%C3%A3o-O-valor-do-PIS-informado-n%C3%A3o-corresponde-ao-resultado-da-BC-PIS-COFINS-x-Al%C3%ADquota-PIS-que-foram-informados-na-DPS)  
> **ID:** `37228058663703` | **Última Atualização:** 2026-07-22T14:14:24Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058649623)

 **MENSAGEM**

E0694 Rejeição: O valor do PIS informado não corresponde ao resultado da BC PIS/COFINS x Alíquota PIS, que foram informados na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058650519)

 **SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) contendo informações de **PIS**, o sistema realizou o cálculo do valor do imposto aplicando a **alíquota de PIS sobre a base de cálculo**. No entanto, o **valor final do PIS** informado no documento não corresponde ao resultado esperado pela Sefaz, considerando a multiplicação da **Base de Cálculo de PIS/COFINS** pela **Alíquota de PIS** declarada na DPS (Declaração Prévia de Serviços).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058651415)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058651799)

 Acesse a tela **"Alíquotas de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **verifique se a alíquota cadastrada** está correta conforme orientação do setor fiscal ou contador.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058653079)

 Confirme se o **"Código de Situação Tributária - CST"** está preenchido corretamente no cadastro da alíquota de PIS, de acordo com a operação fiscal realizada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228075171607)

 No campo **''% Red. base'' **verifique se existe algum percentual de redução de base. Caso, exista certifique-se de que ele está sendo aplicado corretamente no cálculo.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228075172887)

 Acesse a tela ****["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa), na aba **"Propriedades"**, e verifique as seguintes configurações:

- 

Se a marcação **"Deduzir valor do ICMS na BC do PIS e COFINS?"** está habilitada ou configurada conforme necessário.

- 

Se a marcação **"Deduzir valor do ICMS/ST na BC do PIS e COFINS?"** está configurada adequadamente.

- 

Se a marcação **"Considera Repasse ICMS na BC PIS/COFINS?"** está habilitada, caso aplicável à operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058655255)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058656663)

 Na aba **"Impostos"**, e verifique se as marcações relacionadas à **dedução de ICMS ou ICMS/ST na base de cálculo do PIS/COFINS** estão configuradas corretamente para a TOP utilizada no lançamento.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37615453215383)

 Caso o **valor do PIS tenha sido informado manualmente** no documento fiscal, recalcule o valor aplicando a fórmula:

```text
Vlr. PIS = Base de Cálculo de PIS/COFINS × Alíquota de PIS
```

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228075175447)

 Acesse o **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), na aba **"Impostos" **confirme se o **"Grupo PIS"** está preenchido corretamente para o produto em questão.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226850012695)

 Certifique-se de que existe uma **regra de alíquota de PIS cadastrada** para o **Grupo PIS** informado no produto, filtrando por empresa, TOP, parceiro e tipo de operação (Saída/Entrada).

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37615423667351)

 Após realizar os ajustes necessários, **refature a nota fiscal** ou **redigite os itens** no documento e gere um novo lote para transmissão. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228058661655)

 **CAUSA**

A rejeição ocorre quando o **valor do PIS informado no documento fiscal** não corresponde ao resultado da multiplicação entre a **Base de Cálculo de PIS/COFINS** e a **Alíquota de PIS** declarada. Isso pode acontecer devido a:

- 

**Alíquota de PIS incorreta** ou não cadastrada no sistema;

- 

**Base de cálculo de PIS/COFINS calculada incorretamente**, considerando ou não deduções de ICMS, ICMS/ST ou ISS;

- 

**Percentual de redução de base** aplicado de forma inadequada;

- 

**Valor do PIS informado manualmente** de forma divergente do cálculo automático;

- 

**Configurações incorretas** nas preferências da empresa ou na TOP utilizada no lançamento.


---

### 🔗 Links e Referências Internas:

- ["Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)
- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)