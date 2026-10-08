# E0298 REJEIÇÃO: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o intermediário for identificado pelo NIF e o emitente por CNPJ

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229535482135-E0298-REJEI%C3%87%C3%83O-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-intermedi%C3%A1rio-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229535482135-E0298-REJEI%C3%87%C3%83O-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-intermedi%C3%A1rio-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ)  
> **ID:** `37229535482135` | **Última Atualização:** 2026-07-22T14:13:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229487470487)

 **MENSAGEM**

E0298 REJEIÇÃO: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o intermediário for identificado pelo NIF e o emitente por CNPJ

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229487471383)

 **SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e com **intermediário identificado pelo NIF** (Número de Identificação Fiscal do exterior) e o **emitente identificado por CNPJ**, o documento fiscal é rejeitado pela Sefaz quando o **grupo de informações de endereço no exterior do intermediário** não está preenchido.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229535467927)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229535469463)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **intermediário da operação**. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229487475095)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o ''**NIF do intermediário''**. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229487475607)

 Ainda na aba **"Identificação"**, localize a seção de **endereço do parceiro** e preencha obrigatoriamente os seguintes campos relacionados ao **endereço no exterior**: 

- 

**"País"**: selecione o país de origem do intermediário;

- 

**"Logradouro"**: informe o endereço completo no exterior;

- 

**"Número"**: informe o número do endereço;

- 

**"Cidade"**: informe a cidade no exterior;

- 

**"Estado/Província"**: informe o estado ou província, se aplicável;

- 

**"Código Postal"**: informe o código postal do endereço no exterior

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229535471767)

 Certifique-se de que o campo **"UF"** esteja configurado como **"EX - Exterior"** para identificar corretamente que se trata de um endereço no exterior. 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229487477271)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229535477655)

 Realize um novo lançamento da NF-e ou NFC-e e tente transmitir o documento fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229535478423)

 **CAUSA**

A rejeição ocorre devido à **validação da Sefaz** que exige o preenchimento obrigatório do **grupo de informações de endereço no exterior** quando o intermediário da operação é identificado pelo **NIF** (Número de Identificação Fiscal do exterior) e o emitente do documento fiscal é identificado por **CNPJ**. Sem o preenchimento completo dos dados de endereço no exterior do intermediário, o documento fiscal não atende aos requisitos legais e é rejeitado pela Sefaz.