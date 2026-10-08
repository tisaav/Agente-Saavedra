# E0080 Rejeição: CNPJ do prestador informado na DPS é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221875382423-E0080-Rejei%C3%A7%C3%A3o-CNPJ-do-prestador-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221875382423-E0080-Rejei%C3%A7%C3%A3o-CNPJ-do-prestador-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37221875382423` | **Última Atualização:** 2026-07-22T14:18:17Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221875361047)

 **MENSAGEM**

E0080 Rejeição: CNPJ do prestador informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221860317719)

 **SITUAÇÃO**

A mensagem aparece durante o processo de **transmissão da DPS** (Documento de Prestação de Serviços) quando o **CNPJ do prestador** cadastrado na empresa apresenta **dados inválidos**, como CNPJ zerado, nulo ou com dígito verificador (DV) incorreto.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221875362967)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221860318871)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e selecione a empresa emissora da DPS.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38333309820183)

 Verifique se o número do **CNPJ** informado está correto e válido.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221875363991)

 Caso o CNPJ esteja **zerado, nulo ou com dígito verificador inválido**, corrija as informações inserindo o **CNPJ válido** do prestador:

- 

Consulte o CNPJ correto na **Receita Federal** ou no **SINTEGRA**;

- 

Certifique-se de que a **situação cadastral** do CNPJ está **ATIVA/HABILITADA**;

- 

Insira o CNPJ com **14 dígitos**, sem pontos, traços ou espaços em branco.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221875373847)

 Salve as alterações realizadas no cadastro da empresa.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221875375255)

 Retorne à DPS, redigite o cabeçalho do documento e transmita novamente o lote para a SEFAZ.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221860322583)

 **CAUSA**

A rejeição ocorre quando o **CNPJ do prestador** informado na DPS está **zerado, nulo ou com dígito verificador (DV) inválido**. A SEFAZ valida o CNPJ durante a transmissão do documento e, ao identificar inconsistências nos dados, retorna a mensagem de erro **E0080**, impedindo o processamento da DPS.