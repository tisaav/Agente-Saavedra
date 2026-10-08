# E0250 Rejeição: CNPJ do intermediário não encontrado no cadastro CNPJ.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223027912215-E0250-Rejei%C3%A7%C3%A3o-CNPJ-do-intermedi%C3%A1rio-n%C3%A3o-encontrado-no-cadastro-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223027912215-E0250-Rejei%C3%A7%C3%A3o-CNPJ-do-intermedi%C3%A1rio-n%C3%A3o-encontrado-no-cadastro-CNPJ)  
> **ID:** `37223027912215` | **Última Atualização:** 2026-07-22T14:17:07Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027898391)

 **MENSAGEM**

E0250 Rejeição: CNPJ do intermediário não encontrado no cadastro CNPJ.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027899159)

 **SITUAÇÃO**

Durante a emissão de uma **NF-e ou NFC-e** com informações de **intermediador da operação**, o sistema retorna a **rejeição E0250** no momento da validação do documento fiscal eletrônico.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223012773655)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027901207)

 Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223012775319)

 Localize o **cadastro do intermediador** da operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223012777239)

 Na aba **''Identificação''**, no campo **"CNPJ/CPF"** do intermediador certifique-se de que: 

- 

O **CNPJ está digitado corretamente**, sem zeros à esquerda ou dígitos inválidos.

- 

O **CNPJ possui 14 dígitos** válidos.

- 

O **dígito verificador está correto**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223012778263)

 Consulte o **CNPJ do intermediador** no site da ''**Receita Federal''** ou no ****[''SINTEGRA''](http://www.sintegra.gov.br/) para confirmar que: 

- 

O **CNPJ está ativo** e regularizado.

- 

A situação cadastral está como **"Ativa"**.

- 

Os dados cadastrais estão corretos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027904919)

 Caso o **CNPJ esteja incorreto ou inválido**, corrija a informação no cadastro do parceiro intermediador, inserindo o **CNPJ válido e ativo**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027906839)

 Após realizar a correção, **redigite o cabeçalho da nota fiscal** ou **emita uma nova nota**, garantindo que as informações do intermediador estejam corretas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798557067671)

 **Gere um novo lote** e reenvie a NF-e para processamento na SEFAZ. 
 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798557068439)

 IMPORTANTE:** Se o CNPJ do intermediador estiver **baixado, suspenso ou com situação cadastral irregular**, não será possível emitir a nota fiscal até que a situação seja regularizada junto à Receita Federal. Neste caso, oriente o intermediador a **regularizar sua situação cadastral** antes de prosseguir com a emissão.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223027908247)

 **CAUSA**

A rejeição E0250 ocorre quando o **CNPJ informado no grupo de intermediador** da NF-e ou NFC-e **não está cadastrado na base de dados da Receita Federal**, está com **dígitos inválidos**, contém **zeros** ou possui **situação cadastral irregular**. A SEFAZ valida se o CNPJ do intermediador é válido e está ativo antes de autorizar a emissão do documento fiscal.