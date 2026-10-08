# ORA-01012 log-on não estabelecido Alias: DBNSiade

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8215434391831-ORA-01012-log-on-n%C3%A3o-estabelecido-Alias-DBNSiade](https://ajuda.sankhya.com.br/hc/pt-br/articles/8215434391831-ORA-01012-log-on-n%C3%A3o-estabelecido-Alias-DBNSiade)  
> **ID:** `8215434391831` | **Última Atualização:** 2026-07-22T15:12:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585671171863)

 MENSAGEM**:

ORA-01012 log-on não estabelecido 
Alias: DBNSiade

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585671176855)

 SITUAÇÃO**

Mensagem apresentada ao tentar logar no MGE/MITRA/G1 : 

General SQL error.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585636341655)

 SOLUÇÃO:**

Crie o arquivo com a senha do usuário de banco de dados criptografada LICENSE.DAT com o aplicativo: [https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454/License.zip](https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454/License.zip) 

Tendo o arquivo gerado, coloque o no diretório raiz do MGE/MITRA/G1

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585671184407)

 CAUSA:**

Erro apresentado pelo fato da senha do banco de dados não ter sido definida corretamente, via arquivo LICENSE.DAT, que deve ficar no diretório raiz dos executáveis


---

### 🔗 Links e Referências Internas:

- [https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454/License.zip](https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454/License.zip)