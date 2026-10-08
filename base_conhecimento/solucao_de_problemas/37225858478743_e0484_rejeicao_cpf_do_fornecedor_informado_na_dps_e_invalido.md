# E0484 Rejeição: CPF do fornecedor informado na DPS é inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225858478743-E0484-Rejei%C3%A7%C3%A3o-CPF-do-fornecedor-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225858478743-E0484-Rejei%C3%A7%C3%A3o-CPF-do-fornecedor-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37225858478743` | **Última Atualização:** 2026-07-22T14:15:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37664657159831)

 **MENSAGEM**

E0484 Rejeição: CPF do fornecedor informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225874365207)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)** no sistema Sankhya, o usuário vinculou um parceiro cujo **CPF está incorreto** no cadastro. Durante a validação, o documento foi rejeitado porque o CPF informado apresenta **dígito verificador inválido, sequência numérica incorreta ou está preenchido apenas com zeros**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225874365719)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225874366487)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **parceiro **vinculado ao DPS rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225858468503)

 Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225858469143)

 Verifique se o campo **"Tipo de Pessoa"** está configurado como **"Física"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225858470423)

 Corrija o campo **"CNPJ / CPF"** inserindo um **CPF válido** com **11 dígitos**, sem pontos, traços ou espaços em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225874371735)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225858471959)

 Retorne ao **DPS** e redigite o cabeçalho do documento, garantindo que o fornecedor atualizado seja vinculado corretamente.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225874373143)

 Gere um novo lote e transmita o documento.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37664657160727)

 OBSERVAÇÕES:**

- 

Caso o fornecedor seja **estrangeiro**, certifique-se de que o campo **"Tipo de Pessoa"** está configurado como **"Física"**. 

- 

Para parceiros estrangeiros, o campo **"CNPJ / CPF"** pode permanecer em branco, desde que o parâmetro **"Aceita CGC/CPF de Parceiro em branco? - ACEITACGCBRANCO"** esteja ativado.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225858477207)

 **CAUSA**

A rejeição ocorre quando o **CPF do parceiro **informado no DPS está **inválido**. Isso pode acontecer quando o CPF é preenchido com **apenas zeros**, possui **sequência numérica incorreta** ou apresenta **dígito verificador (último número do CPF) inválido**. Ao validar a consistência do CPF durante o processamento do documento e, ao identificar inconsistências, retorna a rejeição E0484.