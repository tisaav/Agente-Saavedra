# Erro de Bearer Token - Incompatibilidade entre Token de Produção e Ambiente Sandbox

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35268066233751-Erro-de-Bearer-Token-Incompatibilidade-entre-Token-de-Produ%C3%A7%C3%A3o-e-Ambiente-Sandbox](https://ajuda.sankhya.com.br/hc/pt-br/articles/35268066233751-Erro-de-Bearer-Token-Incompatibilidade-entre-Token-de-Produ%C3%A7%C3%A3o-e-Ambiente-Sandbox)  
> **ID:** `35268066233751` | **Última Atualização:** 2026-07-22T14:25:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35268060444311)

 **MENSAGEM**

O Bearer Token fornecido está associado ao ambiente Produção, mas a solicitação foi enviada para o ambiente Sandbox. Por favor, verifique se o Bearer Token e o ambiente correspondem corretamente.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/35656520496791)

   **SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta realizar uma integração via API do Sankhya e há uma incompatibilidade entre o **"Bearer Token"** utilizado e o ambiente de destino (ex: usar token de produção em ambiente sandbox). 
 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35268066230423)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656527862295)

 Identifique o **ambiente correto** que deseja utilizar:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656527863831)

 **Para ambiente de PRODUÇÃO, utilize**: 

- 
**URL:** [https://api.sankhya.com.br](https://api.sankhya.com.br/)

- 
**Tipo de Base:** SankhyaOM do tipo PRODUÇÃO 

- 
**Bearer Token:** Gerado especificamente para produção

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656527863831)

**** ****Para ambiente de SANDBOX (Testes), utilize**:

- 
**URL:** [https://api.sandbox.sankhya.com.br](https://api.sandbox.sankhya.com.br/) 

- 
**Tipo de Base:** SankhyaOM dos tipos teste ou treinamento 

**Bearer Token:** Gerado especificamente para sandbox

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656527872407)

 Verifique se a **URL da requisição** está correta:

- 
**Produção:** [https://api.sankhya.com.br/gateway/v1/mge/service.sbr](https://api.sankhya.com.br/gateway/v1/mge/service.sbr)

- 
**Sandbox:** [https://api.sandbox.sankhya.com.br/gateway/v1/mge/service.sbr](https://api.sandbox.sankhya.com.br/gateway/v1/mge/service.sbr)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656527873559)

 Confirme se está usando o **Bearer Token correto** para o ambiente escolhido;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656520506007)

 Certifique-se de que a **"Appkey"** foi gerada para o ambiente correto;

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656520507159)

 Se necessário, **regenere o Bearer Token** garantindo que seja para o ambiente apropriado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656520508183)

 **Atualize a configuração** da integração com a URL e token correspondentes ao ambiente desejado.

**Importante:** Nunca utilize tokens de produção em ambiente de testes e vice-versa. Esta separação garante a **segurança** e **integridade dos dados** em cada ambiente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35268066231575)

 **CAUSA**

Este erro é causado pela **incompatibilidade** entre o tipo de Bearer Token utilizado e o ambiente de destino da requisição. As situações mais comuns são: • Token de **Produção** sendo usado com URL do **Sandbox** • Token de **Sandbox** sendo usado com URL de **Produção** • **Configuração incorreta** dos endpoints nas integrações via API


---

### 🔗 Links e Referências Internas:

- [https://api.sankhya.com.br](https://api.sankhya.com.br/)
- [https://api.sandbox.sankhya.com.br](https://api.sandbox.sankhya.com.br/)
- [https://api.sankhya.com.br/gateway/v1/mge/service.sbr](https://api.sankhya.com.br/gateway/v1/mge/service.sbr)
- [https://api.sandbox.sankhya.com.br/gateway/v1/mge/service.sbr](https://api.sandbox.sankhya.com.br/gateway/v1/mge/service.sbr)