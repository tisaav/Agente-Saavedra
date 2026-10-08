# 931 Rejeição: CST não corresponde ao tipo de código de benefício fiscal [nItem: nnn].(NT2019.001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043052693-931-Rejei%C3%A7%C3%A3o-CST-n%C3%A3o-corresponde-ao-tipo-de-c%C3%B3digo-de-benef%C3%ADcio-fiscal-nItem-nnn-NT2019-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043052693-931-Rejei%C3%A7%C3%A3o-CST-n%C3%A3o-corresponde-ao-tipo-de-c%C3%B3digo-de-benef%C3%ADcio-fiscal-nItem-nnn-NT2019-001)  
> **ID:** `360043052693` | **Última Atualização:** 2026-09-26T00:14:43Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/41814388716567)

**MENSAGEM**

[931] Rejeição: Informado código de benefício fiscal incompatível com CST e UF [nItem:1]

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/41814410467351)

**SITUAÇÃO**

Esta rejeição ocorre durante a emissão de nota fiscal eletrônica (NF-e/NFC-e) quando o sistema identifica que o código de benefício fiscal informado no item da nota não é compatível com o código de situação tributária (CST) utilizado ou com a unidade federativa da operação.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/41814388719895)

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41814388720535)

 Consulte a tabela de código de benefício fiscal publicada no portal nacional da NF-e para verificar qual código é adequado para o CST utilizado e para a UF da operação. Esta validação deve ser realizada junto ao contador responsável pela empresa.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41814388721047)

 Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos) e localize o produto que está gerando a rejeição.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41814410471575)

 Navegue até a aba **"Impostos"** e localize o campo **"Cód. de Benefício Fiscal na UF"**. Verifique se o código informado corresponde ao CST com benefício fiscal.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41814388723223)

 Corrija o código de benefício fiscal conforme orientação do contador e salve as alterações.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/41814388724375)

 Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa) e navegue até a aba **"NFe/NFC-e"**.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/41814410478231)

 Habilite o campo **"Considere Benefícios ao incluir/alterar item da nota"**.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/41814388726295)

 No campo **"Atualização Cód. Beneficio no Faturamento pelo Produto"**, selecione **"Sempre Atualizar"** e salve.

![8](https://ajuda.sankhya.com.br/hc/article_attachments/41814410480791)

 Retorne à nota, exclua o item e adicione-o novamente para que o sistema aplique as novas configurações.

![9](https://ajuda.sankhya.com.br/hc/article_attachments/41814388727703)

 Gere o lote da nota fiscal novamente para transmissão à SEFAZ.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/41814388728983)

**CAUSA**

A rejeição 931 ocorre quando há incompatibilidade entre o código de benefício fiscal informado e o CST (Código de Situação Tributária) utilizado, conforme estipulado por cada secretaria da fazenda. A SEFAZ valida esta correspondência no momento da transmissão, rejeitando documentos com inconsistências.

 

![Observação](https://ajuda.sankhya.com.br/hc/article_attachments/17857155198487)

**OBSERVAÇÕES IMPORTANTES**

- 

Nota Técnica (NT2019.001): Implementação a critério da UF, por modelo de DF-e e por CST.
 

1. 

Para geração da tag cBenef são permitidos 8 ou 10 dígitos. Caso a UF permita apenas 8, esta deve estar vinculada ao parâmetro **"UFPER8CTAGCBENE"**.
 

1. 

Os CSTs que geralmente exigem código de benefício fiscal são: **20, 30, 40, 41, 50, 51, 60, 70 e 90**.