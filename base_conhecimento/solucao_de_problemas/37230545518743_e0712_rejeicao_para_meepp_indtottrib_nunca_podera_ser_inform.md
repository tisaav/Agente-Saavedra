# E0712 Rejeição: Para ME/EPP indTotTrib nunca poderá ser informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37230545518743-E0712-Rejei%C3%A7%C3%A3o-Para-ME-EPP-indTotTrib-nunca-poder%C3%A1-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37230545518743-E0712-Rejei%C3%A7%C3%A3o-Para-ME-EPP-indTotTrib-nunca-poder%C3%A1-ser-informado)  
> **ID:** `37230545518743` | **Última Atualização:** 2026-07-22T14:13:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230573050135)

 **MENSAGEM**

E0712 Rejeição: Para ME/EPP indTotTrib nunca poderá ser informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230573051927)

 **SITUAÇÃO**

Ao emitir uma **NF-e ou NFC-e**, a nota foi **rejeitada pela Sefaz** com a mensagem informando que o campo **"Indicador de Totalização de Tributos" (indTotTrib)** não pode ser preenchido quando a empresa emitente é optante pelo **Simples Nacional** e enquadrada como **Microempresa (ME)** ou **Empresa de Pequeno Porte (EPP)**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230573052695)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230545512471)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa emitente** da nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230545512983)

 Na aba **''Naturezas''**, verifique o campo **''Cód. Regime Tribut'' **e confirme se a empresa está configurada como optante pelo **''Simples Nacional''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230545513751)

 Caso a empresa não seja optante pelo** **''Simples Nacional'', ajuste o campo **"Cód. Regime Tributário"** para o regime correto (Lucro Real, Lucro Presumido ou outro aplicável).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230573056279)

 Se a empresa **realmente for optante pelo Simples Nacional**, verifique se existe alguma **configuração ou customização** que esteja forçando o preenchimento do campo **"Indicador de Totalização de Tributos" (indTotTrib)** no XML da nota fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230545514775)

 Remova qualquer **preenchimento manual ou automático** do campo **indTotTrib** nas configurações de emissão de documentos fiscais.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230545516055)

 Após realizar os ajustes necessários, **reemita a nota fiscal** e verifique se a rejeição foi solucionada.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37230573056663)

 **CAUSA**

A rejeição ocorre porque, de acordo com a **legislação tributária** e as **regras de validação da Sefaz**, empresas optantes pelo **Simples Nacional** enquadradas como **ME ou EPP** não devem informar o campo **"Indicador de Totalização de Tributos" (indTotTrib)** no XML da NF-e ou NFC-e.

Este campo é aplicável apenas para empresas que **não são optantes pelo Simples Nacional** e que estão sujeitas à **Reforma Tributária** com a obrigatoriedade de informar a totalização dos tributos IBS e CBS. Quando o sistema identifica que a empresa emitente é **ME/EPP optante pelo Simples Nacional** e o campo **indTotTrib** está preenchido, a nota é **rejeitada automaticamente** pela Sefaz.