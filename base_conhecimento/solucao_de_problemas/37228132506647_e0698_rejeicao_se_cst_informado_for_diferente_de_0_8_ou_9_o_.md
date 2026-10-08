# E0698 Rejeição: Se CST informado for diferente de 0, 8 ou 9, o tipo de retenção para Pis/Cofins deve ser informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228132506647-E0698-Rejei%C3%A7%C3%A3o-Se-CST-informado-for-diferente-de-0-8-ou-9-o-tipo-de-reten%C3%A7%C3%A3o-para-Pis-Cofins-deve-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228132506647-E0698-Rejei%C3%A7%C3%A3o-Se-CST-informado-for-diferente-de-0-8-ou-9-o-tipo-de-reten%C3%A7%C3%A3o-para-Pis-Cofins-deve-ser-informado)  
> **ID:** `37228132506647` | **Última Atualização:** 2026-07-22T14:14:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132487703)

 **MENSAGEM**

E0698 Rejeição: Se CST informado for diferente de 0, 8 ou 9, o tipo de retenção para Pis/Cofins deve ser informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228115792663)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com um Código de Situação Tributária de PIS/COFINS informado, sem o preenchimento da informação de retenção correspondente a esses tributos no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132490519)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132491287)

 Acesse a tela **"Alíquota de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e localize a alíquota utilizada no lançamento da nota fiscal que está sendo rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228115795735)

 Verifique o campo** ''Cód. sit. tributária''** configurado com o código na alíquota. Se o CST for **diferente de 0, 8 ou 9**, será necessário informar o tipo de retenção.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132492951)

 Consulte seu **contador ou setor fiscal** para identificar qual é o tipo de retenção correto a ser aplicado para PIS e COFINS, considerando a operação fiscal e a legislação vigente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228115797015)

 Na tela **"Alíquota de PIS"**, localize e preencha o campo **"Tipo de Retenção"** com a informação correta fornecida pelo setor fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132495383)

 Repita o mesmo procedimento na tela **"Alíquota de COFINS" **(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS), verificando o CST e preenchendo o campo **"Tipo de Retenção"** quando necessário.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132497047)

 Salve as alterações realizadas nas alíquotas de PIS e COFINS.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228115799831)

 Retorne à nota fiscal rejeitada e realize novamente a **emissão do documento eletrônico**.
 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228132499863)

 **CAUSA**

A rejeição ocorre porque a **Sefaz exige que seja informado o tipo de retenção** de PIS e COFINS quando o Código de Situação Tributária (CST) configurado na alíquota for diferente de 0 (Operação Tributável com Alíquota Básica), 8 (Operação sem Incidência da Contribuição) ou 9 (Operação com Suspensão da Contribuição).

Quando o campo **"Tipo de Retenção"** não é preenchido no cadastro das alíquotas de PIS e COFINS, o sistema não consegue enviar as informações fiscais completas para a Sefaz, resultando na rejeição do documento eletrônico.