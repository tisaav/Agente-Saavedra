# E0247 Rejeição: Email inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223050001815-E0247-Rejei%C3%A7%C3%A3o-Email-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223050001815-E0247-Rejei%C3%A7%C3%A3o-Email-inv%C3%A1lido)  
> **ID:** `37223050001815` | **Última Atualização:** 2026-07-22T14:17:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223049974039)

 **MENSAGEM**

E0247 Rejeição: Email inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223049974679)

 **SITUAÇÃO**

O documento fiscal eletrônico (NF-e, NFC-e, CT-e ou MDF-e) foi emitido com um endereço de e-mail informado nos dados cadastrais que não está em conformidade com o formato esperado, resultando na rejeição pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033719063)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033724055)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033726103)

 Localize o cadastro do **destinatário** ou **emitente** relacionado ao documento fiscal rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033727767)

 Na aba **''Endereço''**, no campo **''E-mail''**, certifique-se de que o endereço eletrônico está preenchido corretamente, seguindo o formato padrão:

- 

usuario@dominio.com

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033728407)

 Corrija possíveis erros de digitação, como:

- 

Ausência do símbolo **"@"**;

- 

Espaços em branco antes, durante ou depois do endereço;

- 

Caracteres especiais inválidos;

- 

Falta de domínio (exemplo: .com, .com.br, .gov.br);

- 

E-mail preenchido com zeros ou informações genéricas inválidas.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033728791)

 Caso o documento seja um **CT-e** ou **MDF-e**, verifique também o e-mail cadastrado na tela **''Empresas''** (Configurações » Cadastros » Empresas), na aba **''Endereço''**, no campo **''E-mail''**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223049980695)

 Se o documento possuir informações de **Responsável Técnico**, acesse a tela de configuração correspondente e valide o campo **"E-mail do Responsável Técnico"**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223049982231)

 Após realizar as correções necessárias, **salve o cadastro** e retorne à tela de emissão do documento fiscal.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223049983255)

 **Redigite o documento fiscal** para que as informações atualizadas sejam carregadas no XML.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38195981701783)

 **Gere um novo lote** e tente transmitir o documento novamente para a Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223033734551)

 **CAUSA**

A rejeição **E0247** é causada pelo **preenchimento incorreto ou inválido** do endereço de e-mail no cadastro do parceiro, empresa ou responsável técnico. A Sefaz valida o formato do e-mail informado no XML do documento fiscal e, caso não esteja em conformidade com os **padrões técnicos estabelecidos** (presença de "@", domínio válido, ausência de caracteres especiais inválidos, etc.), o documento é rejeitado.