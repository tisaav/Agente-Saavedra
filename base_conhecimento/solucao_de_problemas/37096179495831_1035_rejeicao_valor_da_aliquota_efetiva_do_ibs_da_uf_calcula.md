# 1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096179495831-1035-Rejei%C3%A7%C3%A3o-Valor-da-Al%C3%ADquota-Efetiva-do-IBS-da-UF-calculado-incorretamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096179495831-1035-Rejei%C3%A7%C3%A3o-Valor-da-Al%C3%ADquota-Efetiva-do-IBS-da-UF-calculado-incorretamente-nItem-999)  
> **ID:** `37096179495831` | **Última Atualização:** 2026-07-22T14:21:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179483927)

 **MENSAGEM**

1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096188108951)

 **SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com o grupo de Redução de Alíquota do IBS da Unidade Federada (gIBSUF/gRed), o sistema identificou que o valor da Alíquota Efetiva (pAliqEfet) foi calculado incorretamente, resultando na rejeição do documento fiscal pela SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096188109719)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179486871)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação utilizada está configurada corretamente para a tributação do IBS da UF.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096188111511)

 Acesse as telas** ''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se as alíquotas do IBS da UF estão configuradas corretamente para o produto e operação em questão.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179488791)

 Verifique se o **CST** utilizado permite a aplicação de redução de alíquota. Caso o CST não permita, remova a informação de redução de alíquota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179490455)

 Se o CST permitir redução de alíquota, verifique se o **percentual de redução** está configurado corretamente e se é válido para a classificação tributária utilizada.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179490839)

 Verifique se a **Alíquota Efetiva** está sendo calculada corretamente conforme a fórmula:

- 

Para operações **sem compra governamental**:

```text
pAliqEfet = pIBSUF × (1 - (pRedAliq / 100))
```

- 

Para operações com compra governamental:

```text
pAliqEfet = pIBSUF × (1 - (pRedAliq / 100)) × (1 - (pRedAliqGov / 100)).
```

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38025570284695)

 Após realizar as correções necessárias, tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096179493015)

 **CAUSA**

A rejeição ocorre quando o valor da Alíquota Efetiva (pAliqEfet) do IBS da UF informado no documento fiscal não corresponde ao resultado do cálculo esperado pela SEFAZ. Conforme a regra de validação UB28-10, quando informado o grupo de Redução de Alíquota (gIBSUF/gRed), a Alíquota Efetiva deve ser calculada considerando o percentual de redução aplicado à alíquota original do IBS da UF.

Esta validação está em conformidade com as regras estabelecidas pela Lei Complementar 214/2025, que regulamenta a implementação do Imposto sobre Bens e Serviços (IBS) no âmbito da Reforma Tributária. O cálculo incorreto pode ocorrer devido a erros na configuração das alíquotas, percentuais de redução incompatíveis com o CST utilizado, ou falhas no processamento do cálculo pelo sistema.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)