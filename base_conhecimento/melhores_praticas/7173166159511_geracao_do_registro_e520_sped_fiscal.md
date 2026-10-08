# Geração do registro E520 SPED FISCAL

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7173166159511-Gera%C3%A7%C3%A3o-do-registro-E520-SPED-FISCAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/7173166159511-Gera%C3%A7%C3%A3o-do-registro-E520-SPED-FISCAL)  
> **ID:** `7173166159511` | **Última Atualização:** 2026-07-22T15:14:52Z

---

Este registro deve ser preenchido para demonstração da apuração do IPI no período.

#### **Configurações:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16491100996759)

 **Tela: **"Preferências da Empresa"** (Comercial), aba **"EFD - Escrituração Fiscal Digital",** marque os seguintes Blocos e Registros:

**E001**
**E500**
**E520**
**E990**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15938850765335)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16491124029719)

 Tela: **"Registro de Apuração do IPI:"**

Informe a empresa e período de geração do EFD em que o registro citado precisa ser gerado, e clique:

Abrir> Salvar> Visualizar 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15938869205527)

 

Basicamente seriam essas as configurações realizadas e necessárias para a geração do registro. Agora segue análise de algumas informações adicionais sobre os processos e validações do sistema:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450938423063)

 Se o documento for de "Entrada" nos livros fiscais (Tela Cadastro Livro ICMS/IPI), o sistema vai olhar para o campo **"Dt. do movimento"**, para selecionar os documentos que serão enviado ao E520, porém se for documento de "Saída" o sistema vai priorizar o campo "Dt. do documento".

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450938423063)

 Os documentos devem estar com algum dos modelos de documento a seguir: 1, 4, 55, 65, 901;

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450938423063)

 Nos livros fiscais (Tela Cadastro Livro ICMS/IPI) a origem dos documentos deve ser: Estoque ou Complemento

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450938423063)

 No lançamento da nota, nos portais, na grade de itens do documento, os itens que tem valores a serem apresentados no E520 não podem estar com o campo CST IPI igual a: "(-1) Não sujeita ao IPI".