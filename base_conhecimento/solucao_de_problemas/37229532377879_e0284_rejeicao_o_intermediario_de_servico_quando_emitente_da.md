# E0284 Rejeição: O intermediário de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37229532377879-E0284-Rejei%C3%A7%C3%A3o-O-intermedi%C3%A1rio-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37229532377879-E0284-Rejei%C3%A7%C3%A3o-O-intermedi%C3%A1rio-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF)  
> **ID:** `37229532377879` | **Última Atualização:** 2026-07-22T14:13:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229532357783)

 MENSAGEM**

E0284 Rejeição: O intermediário de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229532361495)

 SITUAÇÃO**

Ao emitir uma **DPS (Documento de Prestação de Serviços)** em que a empresa atua como **intermediário de serviço**, o sistema rejeitará o documento caso a **identificação do intermediário** não esteja preenchida com **CNPJ ou CPF válido**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229484446999)

 SOLUÇÃO**

Para resolver a rejeição **E0284**, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229484448407)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229484450583)

 Na grade** ''Cabeçalho''**, verifique se o campo **"Intermediador da Transação"** está preenchido corretamente:

- 

Certifique-se de que o **CNPJ** ou **CPF** do intermediário está informado;

- 

Confirme que o **CNPJ ou CPF** está válido e ativo;

- 

Não utilize outros tipos de identificação além de CNPJ ou CPF.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229484451863)

 Caso o **intermediário** não esteja cadastrado, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e realize o cadastro completo do intermediário, incluindo:

- 

**CNPJ ou CPF** válido;

- 

Dados cadastrais completos e atualizados.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229532370199)

 Retorne à tela de emissão da **DPS** e atualize as informações do **intermediário** com o **CNPJ ou CPF** correto.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38099786078359)

 Salve as alterações realizadas no documento. 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229532373655)

 Tente emitir novamente a **DPS** e verifique se a rejeição foi solucionada. 
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37229484456855)

 CAUSA**

A rejeição **E0284** ocorre quando a **DPS é emitida por um intermediário de serviço** e a **identificação do intermediário** não está preenchida com **CNPJ ou CPF válido**. Conforme as regras de validação da Sefaz estabelecidas pela **Lei Complementar nº 214/2025**, no contexto da **Reforma Tributária**, quando o intermediário atua como emitente da DPS, é **obrigatório** que ele seja identificado exclusivamente por **CNPJ ou CPF**, não sendo permitidos outros tipos de identificação. A ausência ou incorreção dessa informação impede a autorização do documento fiscal.