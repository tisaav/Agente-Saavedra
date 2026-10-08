# O preenchimento dos campos "Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola" e "CPF do Responsável Técnico, emitente da receita" são obrigatórios para essa operação

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32452547844631-O-preenchimento-dos-campos-N%C3%BAmero-da-Receita-ou-Receitu%C3%A1rio-do-Agrot%C3%B3xico-Defensivo-Agr%C3%ADcola-e-CPF-do-Respons%C3%A1vel-T%C3%A9cnico-emitente-da-receita-s%C3%A3o-obrigat%C3%B3rios-para-essa-opera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/32452547844631-O-preenchimento-dos-campos-N%C3%BAmero-da-Receita-ou-Receitu%C3%A1rio-do-Agrot%C3%B3xico-Defensivo-Agr%C3%ADcola-e-CPF-do-Respons%C3%A1vel-T%C3%A9cnico-emitente-da-receita-s%C3%A3o-obrigat%C3%B3rios-para-essa-opera%C3%A7%C3%A3o)  
> **ID:** `32452547844631` | **Última Atualização:** 2026-07-22T14:31:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32452547831319)

 **MENSAGEM:**

[CORE_E08025] "Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola" e "CPF do Responsável Técnico, emitente da receita" são obrigatórios para essa operação.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605415038743)

 SITUAÇÃO:**

**Ao tentar gerar o lote de uma NFe é apresentada a mensagem acima. **

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32452516183063)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605438928407)

 Acesse a tela **"Empresa"** *(Comercial » Preferências » Empresa)*, em seguida, a aba **"Documentos Eletrônicos"**, sub-aba** "NF-e/NFC-e"** e sub-aba **"Nota Técnica NF-e" **e certifique-se de que a **NT: 2024.003 - v1.01, está ativa. **

 

![O preenchimento dos campos Tipo da Guia 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605632539415)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605438929815)

 Acesse a tela** "Configurador de Layout da Nota"*** (**Comercial » Configuração » Configurador de Layout da Nota**)*, abra o layout referente ao movimento da TOP que está sendo utilizado na emissão da NF-e. Em seguida, adicione no cabeçalho do layout os seguintes campos: **Número da Receita ou Receituário do Agrotóxico / Defensivo Agrícola** e **CPF do Responsável Técnico, emitente do receituário.**

 

![O preenchimento dos campos Tipo da Guia 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605632542487)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605438930839)

 Depois, abra a NF na tela da Central e preencha os campos anteriores conforme exemplo abaixo: 

 

![O preenchimento dos campos Tipo da Guia 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605632544279)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32605438932375)

 Por fim, salve o lançamento da NF e gere o lote da NF novamente. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32452516186263)

CAUSA:**

Conforme definição da ****[NT 2024.003,](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) essa informação é validada conforme NCM do produto informado. 

Vale destacar que, essa regra de validação é opcional e pode ser implementada a critério de cada UF. E ela está em vigor em produção desde de 01/04/2025, conforme estabelecido na NT 2024.003.