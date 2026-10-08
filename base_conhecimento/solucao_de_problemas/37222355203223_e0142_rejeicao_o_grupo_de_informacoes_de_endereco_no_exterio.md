# E0142 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o prestador for identificado pelo NIF e o emitente por CNPJ.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222355203223-E0142-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-prestador-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222355203223-E0142-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-prestador-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ)  
> **ID:** `37222355203223` | **Última Atualização:** 2026-07-22T14:17:51Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355192087)

 **MENSAGEM**

E0142 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o prestador for identificado pelo NIF e o emitente por CNPJ.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355192983)

 **SITUAÇÃO**

Ao emitir um documento fiscal eletrônico onde o **prestador de serviço é identificado pelo NIF** (Número de Identificação Fiscal estrangeiro) e o **emitente é identificado por CNPJ**, o sistema apresenta a rejeição E0142 quando as **informações de endereço no exterior do prestador não foram preenchidas** adequadamente no cadastro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355193751)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355194647)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **prestador de serviço estrangeiro**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355195415)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o **NIF do prestador**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355195671)

 Na aba **"Endereço"**, localize a seção de **endereço do parceiro** e preencha obrigatoriamente os seguintes campos relacionados ao **endereço no exterior**: 

- 

**"País"**: selecione o país de origem do prestador;

- 

**"Endereço"**: informe o endereço completo no exterior;

- 

**"Número"**: informe o número do endereço;

- 

**"Cidade"**: informe a cidade no exterior;

- 

Outros campos complementares de endereço, conforme necessário.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355196183)

 Certifique-se de que o **estado **esteja configurado como **"EX"** (Exterior), indicando que se trata de um **parceiro estrangeiro**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222340685079)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222355199127)

 Realize um novo lançamento do documento fiscal eletrônico e tente emiti-lo novamente. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222340689815)

 **CAUSA**

A rejeição E0142 ocorre quando o **documento fiscal eletrônico é emitido** com um **prestador de serviço identificado pelo NIF** (Número de Identificação Fiscal estrangeiro) e o **emitente é identificado por CNPJ**, mas o **grupo de informações de endereço no exterior não foi preenchido** no cadastro do parceiro. A Sefaz exige que, nesta situação específica, as **informações completas de endereço no exterior sejam obrigatoriamente informadas** para validação do documento fiscal.