# Certificado Transmissor sem CNPJ

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023773-Certificado-Transmissor-sem-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023773-Certificado-Transmissor-sem-CNPJ)  
> **ID:** `360043023773` | **Última Atualização:** 2026-07-22T16:09:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455301099671)

 MENSAGEM:**

[CORE_E04925] 282 - Rejeição: Certificado Transmissor sem CNPJ.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455316365719)

 SOLUÇÃO:**

A mensagem indica que o certificado utilizado para assinar o documento fiscal eletrônico não possui um CNPJ vinculado. Todo certificado digital utilizado para transmissão de documentos fiscais eletrônicos, deve obrigatoriamente possuir um CNPJ vinculado.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455316371863)

 Para solução, solicite ao órgão emissor do certificado que regularize tal questão e emita um novo certificado digital A1, válido.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455316378775)

 Após o ajuste, registre o novo certificado através da tela "**[Console NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734)"** (Caminho de acesso:* Comercial » Configuração » Console NFe*), se for preciso "**Forçar reinicialização"**, execute-o. [Para mais detalhes: [Como realizar troca de certificado digital?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023933)]

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455301123991)

 Efetue a geração do lote da nota novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455301131671)

 CAUSA:**

Ocorre quando falta a extensão de CNPJ no Certificado (OtherName - OID=2.16.76.1.3.3) ou a extensão de CPF (OtherName - OID=2.16.76.1.3.1) que deve ser regularizado pelo órgão emissor do certificado.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16455301144087)

 OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)


---

### 🔗 Links e Referências Internas:

- [Console NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734)
- [Como realizar troca de certificado digital?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023933)