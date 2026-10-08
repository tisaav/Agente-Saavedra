# E0242 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o tomador for identificado pelo NIF e o emitente por CNPJ.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229481561367-E0242-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-tomador-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229481561367-E0242-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-tomador-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ)  
> **ID:** `37229481561367` | **Última Atualização:** 2026-07-22T14:13:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481534999)

 **MENSAGEM**

E0242 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o tomador for identificado pelo NIF e o emitente por CNPJ.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229462304919)

 **SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (CT-e, NF-e ou NFC-e) em que o **tomador do serviço ou destinatário é identificado pelo NIF** (Número de Identificação Fiscal do exterior) e o **emitente é identificado por CNPJ**, o documento é rejeitado pela SEFAZ caso o grupo de informações de endereço no exterior não esteja preenchido corretamente no cadastro do parceiro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229462305559)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229462307223)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do parceiro estrangeiro que será o tomador ou destinatário do documento fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481543959)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o **NIF (Número de Identificação Fiscal)** ou outro documento legal que identifique o parceiro estrangeiro, como passaporte.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481546135)

 Ainda na aba **"Identificação"**, localize a seção de **endereço do parceiro** e preencha obrigatoriamente os seguintes campos relacionados ao endereço no exterior:

- 

**"Logradouro"**: informe o endereço completo no exterior;

- 

**"Número"**: informe o número do endereço;

- 

**"Complemento"** (se aplicável);

- 

**"Bairro/Distrito"**: informe o bairro ou distrito;

- 

**"Cidade"**: informe a cidade no exterior;

- 

**"UF"**: selecione a opção **"EX - Exterior"**;

- 

**"País"**: selecione o país correspondente ao endereço do parceiro;

- 

**"CEP"** (se aplicável no país de origem).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481550487)

 Certifique-se de que o campo **"UF"** esteja configurado como **"EX - Exterior"**, pois esta configuração é essencial para que o sistema identifique corretamente a operação com o exterior.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229462312471)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481553303)

 Retorne ao documento fiscal e realize uma nova tentativa de emissão.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229481554327)

 **CAUSA**

A rejeição ocorre porque a **SEFAZ exige que o grupo de informações de endereço no exterior seja preenchido obrigatoriamente** quando o tomador do serviço ou destinatário da mercadoria for identificado pelo **NIF (Número de Identificação Fiscal do exterior)** e o emitente do documento for identificado por **CNPJ**. Caso o endereço no exterior não esteja completo ou a **UF não esteja configurada como "EX - Exterior"**, o sistema não consegue gerar corretamente as informações necessárias para a validação da SEFAZ, resultando na rejeição do documento.