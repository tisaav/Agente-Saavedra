# E0400 REJEIÇÃO: O CEP não deve ser informado quando o endereço da atividade de evento ocorrer no exterior do país

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229540593815-E0400-REJEI%C3%87%C3%83O-O-CEP-n%C3%A3o-deve-ser-informado-quando-o-endere%C3%A7o-da-atividade-de-evento-ocorrer-no-exterior-do-pa%C3%ADs](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229540593815-E0400-REJEI%C3%87%C3%83O-O-CEP-n%C3%A3o-deve-ser-informado-quando-o-endere%C3%A7o-da-atividade-de-evento-ocorrer-no-exterior-do-pa%C3%ADs)  
> **ID:** `37229540593815` | **Última Atualização:** 2026-07-22T14:13:55Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229540572055)

 **MENSAGEM**

E0400 Rejeição: O CEP não deve ser informado quando o endereço da atividade de evento ocorrer no exterior do país.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229523827735)

 **SITUAÇÃO**

A rejeição está relacionada à emissão de um documento fiscal de evento em que o local de realização da atividade está informado como sendo no exterior, com o preenchimento de CEP no endereço do evento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229540572951)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229523828887)

 Acesse a tela** ''Parceiros''** (Configurações » Cadastros » Parceiros) e localize o endereço do local da atividade.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229540576791)

 Acesse a tela **"Estados" **(Configurações » Cadastros » Endereços » Estados), busque pelo Estado do parceiro (prestador de serviço). Neste, verifique se o campo **"País"** está preenchido com um país diferente do Brasil (código diferente de 1058).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229523830423)

 Retorne ao passo 1, busque pelo parceiro (prestador de serviço). Na aba **''Endereço''**, certifique-se de que o campo **"CEP"** esteja quando o endereço for no exterior.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229523831063)

 Preencha corretamente os campos específicos para endereços no exterior:

- 

**"Endereço"**: informe o endereço completo no exterior;

- 

**"Número"**: informe o número do endereço;

- 

**"País"**: selecione o país correspondente (diferente do Brasil);

- 

**"Código Postal"**: informe o código postal do país de destino (se aplicável).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229540579991)

 Acesse a tela **''Cidade''** (Configurações » Cadastros » Endereços » Cidades) e verifique a configuração para o exterior:

- 

**"Cód. UF"**: deve estar vinculado ao estado "EXTERIOR" (sigla "EX");

- 

**"Mun. domicílio fiscal"**: deve estar preenchido com **"9999999"** para parceiros do exterior.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229523834519)

 Salve as alterações e **retransmita o evento** ou **gere novamente o documento fiscal**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229540581655)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida que o campo CEP não deve ser informado** quando o **endereço da atividade do evento está localizado no exterior**. O CEP é um código específico do sistema postal brasileiro e **não se aplica a endereços internacionais**. Para endereços no exterior, devem ser utilizados os campos **"Código Postal"** e **"País"**, deixando o campo **"CEP" em branco**.