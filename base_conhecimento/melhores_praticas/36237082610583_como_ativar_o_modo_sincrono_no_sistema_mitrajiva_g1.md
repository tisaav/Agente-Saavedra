# Como ativar o modo Síncrono no sistema Mitra/Jiva G1

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36237082610583-Como-ativar-o-modo-S%C3%ADncrono-no-sistema-Mitra-Jiva-G1](https://ajuda.sankhya.com.br/hc/pt-br/articles/36237082610583-Como-ativar-o-modo-S%C3%ADncrono-no-sistema-Mitra-Jiva-G1)  
> **ID:** `36237082610583` | **Última Atualização:** 2026-07-22T14:23:20Z

---

O **"modo síncrono"** para envio de XML no SankhyaW permite que a emissão de documentos fiscais eletrônicos ocorra de forma mais ágil, aguardando o retorno imediato da SEFAZ. Esta funcionalidade está disponível a partir da versão 4.66 do banco de dados.
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41801033445783)

 Acesse a opção**"Avançado"** (Avançado >> Preferências >> Empresa);
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41801033446935)

 Localize a empresa responsável pela emissão da NF-e e/ou NFC-e;
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41801033447831)

 Marque a opção **"Usar modo Síncrono para envio do XML"** ;
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41801033448471)

 Clique em **"Salvar"**;
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/41801033448599)

 Saia do sistema e acesse-o novamente para que a nova configuração seja aplicada corretamente.
 

![image (60).png](https://ajuda.sankhya.com.br/hc/article_attachments/36316973162775)

### **Outros documentos fiscais com modo síncrono**

Além da **NF-e**, o modo síncrono também está disponível para outros documentos fiscais eletrônicos via parâmetro:
 

- 

**NFC-e, CT-e e MDF-e.**
 

![Importante](https://ajuda.sankhya.com.br/hc/article_attachments/36320089521815)

**Importante:**
 

A partir das versões mais recentes dos webservices da SEFAZ (NF-e e NFC-e), o envio das notas fiscais passou a ser obrigatoriamente realizado no modo **"Síncrono"**. Isso significa que, ao transmitir a NF-e, o sistema aguarda a resposta imediata da SEFAZ, eliminando a necessidade de realizar consultas posteriores ao lote.