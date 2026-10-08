# E0702 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228186534039-E0702-Rejei%C3%A7%C3%A3o-Se-o-valor-for-informado-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-o-valor-do-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228186534039-E0702-Rejei%C3%A7%C3%A3o-Se-o-valor-for-informado-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-o-valor-do-servi%C3%A7o)  
> **ID:** `37228186534039` | **Última Atualização:** 2026-07-22T14:14:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228186528407)

 **MENSAGEM**

E0702 Rejeição: Se o valor for informado, então deve ser igual ou maior que 0 e menor ou igual o valor do serviço.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170375959)

 **SITUAÇÃO**

Durante a emissão de um documento fiscal eletrônico (NF-e ou NFC-e) com itens de serviço, a nota foi apresentada com um valor informado fora do intervalo aceito para esse tipo de operação, resultando na rejeição do documento pelo sistema.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170376727)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170377367)

 Acesse o documento fiscal que foi rejeitado e localize o **campo de valor relacionado ao serviço** que gerou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170378263)

 Verifique se o **valor informado é maior ou igual a zero** (0). Valores negativos não são permitidos.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228186530199)

 Certifique-se de que o **valor informado não ultrapassa o valor total do serviço** prestado. O valor deve ser menor ou igual ao valor do serviço.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228186530583)

 Corrija o valor conforme necessário, garantindo que ele esteja **dentro do intervalo permitido** (≥ 0 e ≤ valor do serviço).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170381591)

 Salve as alterações realizadas no documento fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170382487)

 Reenvie o documento fiscal eletrônico para a SEFAZ para validação.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228170382999)

 **CAUSA**

Esta rejeição ocorre quando o **valor informado no campo relacionado ao serviço** não atende às regras de validação da SEFAZ. A validação exige que, caso um valor seja informado, ele deve ser **maior ou igual a zero (0)** e **menor ou igual ao valor total do serviço** prestado. Valores negativos ou superiores ao valor do serviço violam essa regra e resultam na rejeição do documento fiscal.