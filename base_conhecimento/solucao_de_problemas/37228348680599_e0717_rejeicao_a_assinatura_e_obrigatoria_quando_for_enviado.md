# E0717 Rejeição: A assinatura é obrigatória quando for enviado para o Web Service.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228348680599-E0717-Rejei%C3%A7%C3%A3o-A-assinatura-%C3%A9-obrigat%C3%B3ria-quando-for-enviado-para-o-Web-Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228348680599-E0717-Rejei%C3%A7%C3%A3o-A-assinatura-%C3%A9-obrigat%C3%B3ria-quando-for-enviado-para-o-Web-Service)  
> **ID:** `37228348680599` | **Última Atualização:** 2026-07-22T14:14:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228395659031)

 **MENSAGEM**

E0717 Rejeição: A assinatura é obrigatória quando for enviado para o Web Service.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228395662103)

 **SITUAÇÃO**

Ao tentar enviar um **evento de NF-e** (como Registro de Consumo, Cancelamento ou outro evento fiscal) para o **Web Service da SEFAZ**, o sistema rejeitou o envio informando que a **assinatura digital do documento não foi encontrada ou está inválida**. O usuário tentou transmitir o evento, mas o XML não continha a assinatura digital obrigatória ou o certificado digital utilizado apresentou problemas.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348661911)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348663447)

 Verifique se o **certificado digital A1 ou A3** da empresa está **válido e instalado corretamente** no computador ou servidor onde o sistema está sendo executado.

- 

Acesse o gerenciador de certificados do Windows e confirme se o certificado está dentro do prazo de validade.

- 

Caso o certificado esteja vencido, providencie a renovação junto à Autoridade Certificadora.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348664983)

 Acesse a tela **"Empresa"** (Configurações » Cadastros » Empresa) e verifique se o **certificado digital está corretamente vinculado** à empresa emissora do evento.

- 

Na aba **"NF-e / NFC-e"**, confirme se o campo **"Certificado Digital"** está preenchido com o certificado correto.

- 

Caso necessário, reimporte o certificado digital clicando no botão correspondente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228395667223)

 Verifique se o **XML do evento está sendo assinado digitalmente** antes do envio ao Web Service. O sistema deve aplicar a assinatura digital automaticamente ao gerar o XML do evento.

- 

Caso o XML não esteja sendo assinado, verifique se há alguma configuração ou parâmetro desabilitado que impeça a assinatura.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348670871)

  Caso o problema persista, verifique se há **problemas na cadeia de certificação** do certificado digital. A rejeição pode ocorrer se a cadeia de certificação estiver incompleta ou corrompida.

- 

Reinstale o certificado digital e suas cadeias intermediárias.

- 

Consulte a Autoridade Certificadora para obter os certificados intermediários atualizados.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348671767)

  Após realizar as correções necessárias, **gere novamente o evento** e reenvie ao Web Service da SEFAZ para validação.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348675479)

 **CAUSA**

Esta rejeição ocorre quando o **XML do evento enviado ao Web Service da SEFAZ não contém a assinatura digital obrigatória** ou quando o **certificado digital utilizado para assinar o documento está inválido, vencido ou com problemas na cadeia de certificação**. A assinatura digital é obrigatória para garantir a **autenticidade, integridade e validade jurídica** dos eventos fiscais eletrônicos transmitidos aos órgãos fazendários.