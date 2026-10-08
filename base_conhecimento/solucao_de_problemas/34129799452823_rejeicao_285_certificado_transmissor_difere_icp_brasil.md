# Rejeição 285: Certificado Transmissor difere ICP-Brasil

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34129799452823-Rejei%C3%A7%C3%A3o-285-Certificado-Transmissor-difere-ICP-Brasil](https://ajuda.sankhya.com.br/hc/pt-br/articles/34129799452823-Rejei%C3%A7%C3%A3o-285-Certificado-Transmissor-difere-ICP-Brasil)  
> **ID:** `34129799452823` | **Última Atualização:** 2026-07-22T14:27:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34129799444119)

 **MENSAGEM**

Rejeição 285: Certificado Transmissor difere ICP-Brasil

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324502589079)

 **SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar transmitir uma nota fiscal eletrônica quando o certificado digital utilizado não está de acordo com o padrão ICP-Brasil exigido pela SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34129799445271)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324502590487)

  **Instabilidade na SEFAZ**

Aguarde alguns minutos e tente reenviar o documento, pois a rejeição pode ser causada por instabilidade temporária nos servidores da SEFAZ.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324502595991)

  **Falta de Cadeias de Certificação**

Verifique se o certificado digital está corretamente configurado e atualizado. Certifique-se de que todas as cadeias de certificação estejam instaladas.
 • Caso necessário, realize a correção da cadeia de certificado seguindo as orientações disponíveis em [Link correção Cadeia de certificado da sefaz](Link%20corre%C3%A7%C3%A3o%20Cadeia%20de%20certificado%20da%20sefaz).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324502602135)

 **Dados inválidos**  

Confira se os dados da nota fiscal, como **"CNPJ"**, **"CFOP"** e **"destinatário"**, estão corretos e completos.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324502602775)

 **Problemas de validação de XML**  

Valide o arquivo XML para garantir que ele segue o esquema exigido pela SEFAZ e não possui erros de formatação ou estrutura.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34324472025239)

 **Certificado digital vencido** 

Verifique se o certificado digital não está vencido. Caso esteja, providencie a renovação antes de tentar nova transmissão.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34129767840535)

 **CAUSA**

A rejeição ocorre quando o certificado digital utilizado, as cadeias de certificação, os dados da nota fiscal ou o arquivo XML estão em desconformidade com os requisitos da SEFAZ.