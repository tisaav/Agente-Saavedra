# 1031 Rejeição: Valor do Diferimento da UF difere do calculado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37100070998807-1031-Rejei%C3%A7%C3%A3o-Valor-do-Diferimento-da-UF-difere-do-calculado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37100070998807-1031-Rejei%C3%A7%C3%A3o-Valor-do-Diferimento-da-UF-difere-do-calculado-nItem-999)  
> **ID:** `37100070998807` | **Última Atualização:** 2026-07-22T14:19:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100070983447)

 **MENSAGEM**

1031 Rejeição: Valor do Diferimento da UF difere do calculado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100070985111)

 **SITUAÇÃO:**

A rejeição ocorre quando o valor do diferimento estadual (IBS-UF) informado na nota fiscal eletrônica não corresponde ao valor calculado pela SEFAZ. O sistema compara o valor informado com o valor calculado automaticamente para validar a nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100070985495)

 **SOLUÇÃO:**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100052020247)

 Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100052022551)

 Verifique se o CST selecionado possui o indicador que exige o uso de diferimento (ind_gDif = 1).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100052023063)

 Confira se o grupo de diferimento (gIBSUF/gDif) está corretamente informado na nota fiscal.

- 

Este grupo é **obrigatório** quando o CST utilizado exige o uso de diferimento.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100052023703)

 Certifique-se se os valores utilizados para o cálculo do diferimento estão corretos:

- 

Base de cálculo (vBC)

- 

Percentual do IBS da UF (pIBSUF)

- 

Percentual do diferimento (pDif) 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100070994199)

 Acesse a tela ****[''Assistente de Configuração Integral da Reforma Tributária''](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37528095054103)

 Verifique e ajuste as configurações de diferimento do IBS Estadual.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37528079101975)

 Após realizar as alterações, redigite o item na nota fiscal para que o sistema recalcule o valor do diferimento conforme a fórmula:

```text
vDif = vBC x (pIBSUF / 100) x (pDif / 100).
```

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37100070994967)

 **CAUSA:**

A rejeição 1031 ocorre quando o valor do diferimento da UF (vDif) informado no documento fiscal **não corresponde ao valor calculado pela Sefaz**.

Conforme a regra de validação **UB23-10 estabelecida na Lei Complementar 214/2025**, **o valor do diferimento deve ser resultante da multiplicação da Base de Cálculo pelo Percentual do IBS da UF e pelo Percentual do Diferimento**, seguindo a fórmula: vDif = vBC x (pIBSUF / 100) x (pDif / 100).

Esta validação é aplicada quando o **CST do IBS/CBS** informado possui indicador que exige o uso de diferimento (ind_gDif = 1) e o grupo de diferimento (gIBSUF/gDif) está informado na nota fiscal.

Qualquer divergência entre o valor informado e o calculado resultará na rejeição do documento fiscal.


---

### 🔗 Links e Referências Internas:

- [''Assistente de Configuração Integral da Reforma Tributária''](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria)