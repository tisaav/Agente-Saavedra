# 1130 Rejeição: Mais de um documento fiscal referenciado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097505979671-1130-Rejei%C3%A7%C3%A3o-Mais-de-um-documento-fiscal-referenciado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097505979671-1130-Rejei%C3%A7%C3%A3o-Mais-de-um-documento-fiscal-referenciado-nItem-999)  
> **ID:** `37097505979671` | **Última Atualização:** 2026-09-15T14:27:56Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097514305943)

 MENSAGEM

Rejeição 1130: Mais de um documento fiscal referenciado.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097514306839)

 SITUAÇÃO

A Rejeição ocorre porque foi referenciado mais de uma chave de acesso em um tipo de nota fiscal que exige apenas um documento de origem, como é o caso de uma **NF-e complementar**

 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097514307607)

 SOLUÇÃO

Para solucionar esta rejeição, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097514307991)

 Acesse os Portais de Vendas / Compras  (Comercial » Consulta » Portal de Vendas/Portal de Compras).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097505974807)

 Localize o documento que originou a emissão da NF-e e verifique os documentos vinculados à operação no botão **"Documentos Relacionados".**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37097514308503)

Caso existam múltiplas notas fiscais referenciadas, identifique qual documento deve permanecer vinculado à nota fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097514309271)

Será preciso gerar novamente a nota fiscal para que o XML seja criado com apenas uma ocorrência da tag **DFeReferenciado**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097514310295)

 **CAUSA**

A rejeição ocorre porque o XML da NF-e foi gerado com mais de um documento referenciado na tag **DFeReferenciado**, situação não permitida para esse tipo de operação.

Conforme a **Nota Técnica NFe 2025.002**, a referência de múltiplos documentos é permitida apenas nos seguintes casos:

- 
**Nota de Débito** (*tpNFDebito = 3* – Débitos de notas fiscais não processadas na apuração);

- 
**Nota Fiscal de Devolução** (*finNFe = 4*).

Conforme a regra de validação:

![rejeicao1130.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/38335061927575)