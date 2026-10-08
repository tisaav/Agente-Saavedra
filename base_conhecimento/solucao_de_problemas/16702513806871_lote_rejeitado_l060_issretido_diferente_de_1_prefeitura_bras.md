# Lote rejeitado: L060 – ISSRetido diferente de 1 - Prefeitura BRASILIA

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16702513806871-Lote-rejeitado-L060-ISSRetido-diferente-de-1-Prefeitura-BRASILIA](https://ajuda.sankhya.com.br/hc/pt-br/articles/16702513806871-Lote-rejeitado-L060-ISSRetido-diferente-de-1-Prefeitura-BRASILIA)  
> **ID:** `16702513806871` | **Última Atualização:** 2026-07-22T14:54:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702513781271)

  MENSAGEM:**

L060 – ISSRetido diferente de 1. Possível solução: Informe ISSRedito = 1 para substituto tributário.

 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702488178327)

 CAUSA:**

Quando o serviço esta com dedução de ISS, a nota é gerada sem as informações de ISS e o XML apresenta com a tag ISSRetido = 2, mas a prefeitura exige que seja ISSRetido = 1

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16702109259159)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702504613015)

 SOLUÇÃO:**

 

Por meio do parâmetro **"****Permite ISS retido zero em NFS-e - NFSEISSRETZERO"** defina se será permitido enviar RPS à prefeitura com ISS retido zerado.

 

Na situação da rejeição, o parâmetro citado deve estar ligado.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16702525889559)

 

Feito o ajuste, basta gerar o lote novamente.