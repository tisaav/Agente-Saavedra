# E0101 esocialevtAdmissao/trabalhador/endereco/brasil/codMuncic

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36670904661655-E0101-esocialevtAdmissao-trabalhador-endereco-brasil-codMuncic](https://ajuda.sankhya.com.br/hc/pt-br/articles/36670904661655-E0101-esocialevtAdmissao-trabalhador-endereco-brasil-codMuncic)  
> **ID:** `36670904661655` | **Última Atualização:** 2026-08-18T19:53:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670904660887)

** MENSAGEM:**

E0101 esocialevtAdmissao/trabalhador/endereco/brasil/codMuncic

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670942487831)

** SITUAÇÃO:**

A mensagem de erro é apresentada ao tentar realizar o envio do **evento S-2200 **(Admissão) pela Central do eSocial.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670904661015)

** SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36694142845975)

 Acesse a tela ****[''Cidades''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)** **(Configurações » Cadastros » Endereços » Cidades).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36694142848023)

 Na aba **''Geral''**,** **o campo **''Mun. domicílio fiscal'' **deve** **estar preenchido conforme a **tabela do IBGE**.

 

![image (73).png](https://ajuda.sankhya.com.br/hc/article_attachments/36694158106903)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36694158108183)

 Em seguida, acesse a tela ****[''Endereços''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602274-Endere%C3%A7os)** **(Configurações » Cadastros » Endereços » Endereços), e verifique se o campo ''**Cód. Logradouro p/ E-social''** está preenchido corretamente.

 

![image (74).png](https://ajuda.sankhya.com.br/hc/article_attachments/36694142853015)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36694142853655)

 Após as devidas correções, gere novamente o evento **S-2200 **e libere-o para envio.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670942487959)

Conforme o leiaute eSocial, a tag [dtAvPrv](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html) (Data de concessão do aviso prévio) deve obrigatoriamente ser preenchida com uma data válida que atenda aos seguintes critérios:

**Validação:** se informada, deve ser igual ou posterior à data de admissão e igual ou anterior a [dtDeslig](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#2299_infoDeslig_dtDeslig).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670904661399)

** CAUSA:**

O erro ocorre porque o** **layout do eSocial **exige que essas informações estejam corretamente cadastradas** para envio do evento.

Campos como **Município do domicílio fiscal** e **Código do Logradouro para eSocial** são obrigatórios, e qualquer inconsistência impede a validação do S-2200.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36670904661527)


---

### 🔗 Links e Referências Internas:

- [''Cidades''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [''Endereços''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602274-Endere%C3%A7os)