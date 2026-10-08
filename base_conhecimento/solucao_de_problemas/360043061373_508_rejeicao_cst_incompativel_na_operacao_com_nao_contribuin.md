# 508 Rejeição: CST incompatível na operação com Não Contribuinte - [nItem:999] (NT2015/003)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061373-508-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte-nItem-999-NT2015-003](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061373-508-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte-nItem-999-NT2015-003)  
> **ID:** `360043061373` | **Última Atualização:** 2026-07-22T16:09:18Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474323203735)

**MENSAGEM**

Rejeição 508: CST incompatível com não contribuinte.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39448993399319)

**SITUAÇÃO**

Esta rejeição ocorre quando o emissor tenta validar uma nota fiscal utilizando um Código de Situação Tributária (CST) que exige a condição de contribuinte do ICMS, porém o destinatário da nota está cadastrado como **"Não Contribuinte"** ou com o campo **"Indicador de IE"** incorreto na tela (Configurações >> Cadastros >> Parceiros).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474323215639)

**CAUSA**

O erro é gerado pela divergência entre a tributação aplicada (CST) e o perfil fiscal do parceiro destinatário. Algumas legislações estaduais impedem que determinados CSTs sejam utilizados em operações destinadas a pessoas que não possuem Inscrição Estadual (IE) ativa.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474300019223)

**SOLUÇÃO**

Para solucionar esta rejeição, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474300020759)

 Acesse a tela (Configurações >> Cadastros >> Parceiros) e localize o parceiro destinatário da nota.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474300022679)

 Verifique na aba **"Fiscal"** se o campo **"Classificação ICMS"** está preenchido corretamente como **"Não Contribuinte"** ou **"Isento"**, conforme o caso.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474300025239)

 Caso o parceiro seja realmente contribuinte, ajuste a **"Inscrição Estadual"** e altere o indicador para **"Contribuinte ICMS"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16474300028439)

 Se o parceiro for um consumidor final não contribuinte, revise a configuração da alíquota e do CST utilizado na operação na tela (Comercial >> Arquivo >> Cadastros>> Alíquotas), garantindo que o CST utilizado seja compatível com operações para não contribuintes.
 

![Imagem](/guide-media/01H532NS5KVBYNJ6CRSGDMZHCD)

 Após realizar as correções, salve o cadastro do parceiro e tente reenviar a nota fiscal pela tela (Comercial >> Consulta >> Central de Vendas).