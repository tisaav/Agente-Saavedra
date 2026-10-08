#  As notas importadas devem possuir o mesmo emitente e destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4404428023959--As-notas-importadas-devem-possuir-o-mesmo-emitente-e-destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404428023959--As-notas-importadas-devem-possuir-o-mesmo-emitente-e-destinat%C3%A1rio)  
> **ID:** `4404428023959` | **Última Atualização:** 2026-07-22T15:23:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347400732439)

 MENSAGEM**:

 [CORE_E02466] As notas importadas devem possuir o mesmo emitente, destinatário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347400741399)

 SOLUÇÃO:**

Ao gerar um CT-e deve-se constar os mesmos emitentes e remetentes que a NF-e. Verifique no cabeçalho da notas, os campos:

- **"Parceiro Destinatário" (CODPARCDEST da TGFCAB)**

- 
**"Parceiro Remetente"** **(CODPARCREMETENTE da TGFCAB) **

Os campos CODPARCDEST e CODPARCREMETENTE devem possuir a mesma informação.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15330083962903)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347383044759)

 CAUSA:**

Existe a seguinte validação de emitente e destinatário para que o XML da NF-e seja importado para inclusão de um CT-e:

- O emitente do XML da NF-e (FornecedorNotaFiscal) deve possuir o mesmo CPF/CNPJ do parceiro Remetente do CT-e;

- O destinatário do XML da NF-e (EmpresaNotaFiscal) deve possuir o mesmo CPF/CNPJ do parceiro Destinatário do CT-e.

Se alguma dessas regras forem violadas, a seguinte mensagem será apresentada: "As notas importadas devem possuir o mesmo emitente, destinatário."