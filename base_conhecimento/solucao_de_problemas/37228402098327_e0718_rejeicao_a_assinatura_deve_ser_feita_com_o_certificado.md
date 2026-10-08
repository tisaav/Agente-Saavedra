# E0718 Rejeição: A assinatura deve ser feita com o certificado digital do emitente da DPS

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228402098327-E0718-Rejei%C3%A7%C3%A3o-A-assinatura-deve-ser-feita-com-o-certificado-digital-do-emitente-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228402098327-E0718-Rejei%C3%A7%C3%A3o-A-assinatura-deve-ser-feita-com-o-certificado-digital-do-emitente-da-DPS)  
> **ID:** `37228402098327` | **Última Atualização:** 2026-07-22T14:14:04Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398659607)

 **MENSAGEM**

E0718 Rejeição: A assinatura deve ser feita com o certificado digital do emitente da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398659863)

 **SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar transmitir um **Documento de Prestação de Serviços (DPS)** quando o certificado digital utilizado para assinar o documento **não corresponde ao certificado do emitente** cadastrado na DPS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398660759)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398661527)

 Verifique se o **certificado digital instalado** no sistema corresponde ao **CNPJ ou CPF do emitente** da DPS:

- 

Acesse o cadastro da empresa emitente e confirme o **CNPJ-Base ou CPF** cadastrado.

- 

Verifique se o certificado digital utilizado foi **emitido para o mesmo CNPJ-Base ou CPF** do emitente.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398661783)

 Confirme a validade do certificado digital utilizado pela empresa:

- 

Acesse a tela **"Console NFe no Sankhya" **(Comercial » Configuração » Console NFe no Sankhya)

- 

Confirme se o certificado está **dentro do prazo de validade**.

- 

Caso o certificado esteja vencido, providencie a **renovação junto à Autoridade Certificadora**.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398663191)

 Reinstale o **certificado digital**:

- 

Remova o certificado atual do repositório do sistema.

- 

Instale novamente o certificado digital, seguindo as orientações da Autoridade Certificadora.

- 

Reconfigure o certificado no sistema Sankhya, garantindo que a empresa correta esteja vinculada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398665239)

 Gere novamente o documento fiscal:

- 

Após aplicar todas as correções necessárias, emita novamente o documento fiscal.

- 

Verifique se a transmissão é realizada com sucesso.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398666391)

 Após realizar as correções necessárias, **retransmita a DPS** utilizando o certificado digital correto do emitente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228398667159)

 **CAUSA**

A rejeição ocorre quando a **assinatura digital da DPS** é realizada com um certificado digital que **não pertence ao emitente** do documento. As principais causas são:

- 

**Certificado digital incorreto:** o documento foi assinado com um certificado de outra empresa ou pessoa;

- 

**CNPJ-Base ou CPF divergente:** o CNPJ-Base ou CPF do certificado digital utilizado é diferente do CNPJ-Base ou CPF do emitente cadastrado na DPS;

- 

**Certificado digital vencido:** o certificado utilizado está com a validade expirada;

- 

**Falta de cadeias de certificação:** as cadeias hierárquicas do certificado não estão corretamente instaladas no sistema;

- 

**Dados cadastrais incorretos:** o CNPJ ou CPF do emitente foi informado incorretamente no documento.