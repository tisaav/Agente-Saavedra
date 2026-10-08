# O campo NIRE é obrigatório quando a escrituração possui registro na Junta Comercial. Caso contrário, o campo não deve ser preenchido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617293-O-campo-NIRE-%C3%A9-obrigat%C3%B3rio-quando-a-escritura%C3%A7%C3%A3o-possui-registro-na-Junta-Comercial-Caso-contr%C3%A1rio-o-campo-n%C3%A3o-deve-ser-preenchido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617293-O-campo-NIRE-%C3%A9-obrigat%C3%B3rio-quando-a-escritura%C3%A7%C3%A3o-possui-registro-na-Junta-Comercial-Caso-contr%C3%A1rio-o-campo-n%C3%A3o-deve-ser-preenchido)  
> **ID:** `360044617293` | **Última Atualização:** 2026-07-22T15:53:10Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981615645975)

 MENSAGEM:**

O campo NIRE é obrigatório quando a escrituração possui registro na Junta Comercial. Caso contrário, o campo não deve ser preenchido.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981615644183)

 SITUAÇÃO:**

Ao tentar transmitir o arquivo ECD, o seguinte erro é apresentado do validador

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981607462551)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981615648535)

 Acesse: Configurações » Cadastros » Empresas

- Aba: **"Naturezas"**

- Preencha os campos abaixo:

  - **"Reg. Junta Comercial (NIRE)"**

  - "**Data Registro na Junta (NIRE)"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981607464983)

 Acesse: Contabilidade » Preferências » Empresa

- Aba: **"ECD-Escrituração Contábil Digital"**

- Bloco:** "I"**
Registro "**I030":** marcado para gerar

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981607466007)

 Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD

- Aba: **"Parâmetros"**

- Opção **"Indicador de existência NIRE":** 1-Empresa possui NIRE

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981615656087)

 Gere o arquivo da ECD novamente.

 

** 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981615659927)

 OBSERVAÇÃO:**

O Registro I030, além do NIRE, gera outras informações que indicam o Termo de Abertura do Livro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981607472279)

 CAUSA:**

Ocorre quando os dados do NIRE, o registro e a opção na geração, não estão devidamente configurados conforme indicado acima.