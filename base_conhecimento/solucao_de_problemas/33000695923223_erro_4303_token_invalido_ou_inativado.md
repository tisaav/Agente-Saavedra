# Erro 4303 - Token Invalido ou Inativado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33000695923223-Erro-4303-Token-Invalido-ou-Inativado](https://ajuda.sankhya.com.br/hc/pt-br/articles/33000695923223-Erro-4303-Token-Invalido-ou-Inativado)  
> **ID:** `33000695923223` | **Última Atualização:** 2026-07-22T14:29:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33000695909399)

 **MENSAGEM:**

Erro 4303 - Token Invalido ou Inativado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33000681439895)

SOLUÇÃO:**

Este erro indica que houve uma incompatibilidade entre a URL e a AppKey informadas na tentativa de autenticação na API da Sankhya.

Para que a autenticação funcione corretamente, é fundamental utilizar a **URL e a AppKey correspondentes ao ambiente desejado**:

- 
**Ambiente de Produção:**
Utilize a AppKey vinculada ao ambiente de produção e a URL:

```text
https://api.sankhya.com.br
```

A AppKey de produção é destinada exclusivamente para integrações com bases do tipo **produção** no SankhyaOM.

- 
**Ambiente de Sandbox (Testes):**
Utilize a AppKey específica para o ambiente de testes e a URL:

```text
https://api.sandbox.sankhya.com.br
```

Esta AppKey deve ser usada apenas para **bases de teste ou treinamento**, mais informações na documentação oficial:  [Obter AppKey - Sankhya Developer](https://developer.sankhya.com.br/reference/obter-appkey)
 

**OBSERVAÇÃO:**

- AppKeys de produção não funcionam no ambiente Sandbox.

- AppKeys de Sandbox não funcionam no ambiente de produção.
Sempre valide se a URL e a AppKey estão corretas e compatíveis com o ambiente que está sendo acessado.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33000695914903)

CAUSA:**

O erro é gerado quando há tentativa de autenticação utilizando **URL de produção** com AppKey do ambiente de testes, ou **AppKey de produção** com URL de Sandbox.


---

### 🔗 Links e Referências Internas:

- [Obter AppKey - Sankhya Developer](https://developer.sankhya.com.br/reference/obter-appkey)