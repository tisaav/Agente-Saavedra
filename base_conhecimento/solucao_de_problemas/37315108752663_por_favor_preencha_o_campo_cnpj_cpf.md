# Por favor, preencha o campo 'CNPJ / CPF'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37315108752663-Por-favor-preencha-o-campo-CNPJ-CPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37315108752663-Por-favor-preencha-o-campo-CNPJ-CPF)  
> **ID:** `37315108752663` | **Última Atualização:** 2026-09-11T19:26:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393324970391)

 MENSAGEM: **

Por favor, preencha o campo 'CNPJ / CPF'

 

![image - 2026-01-02T082924.030.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393334385559)

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37315102091415)

 **SITUAÇÃO:**

Ao cadastrar um parceiro estrangeiro, o sistema exibe a mensagem acima mesmo com o endereço corretamente configurado como fora do Brasil.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37315102092311)

SOLUÇÃO: **

Para parceiros estrangeiros, não é obrigatório informar **CNPJ / CPF**. Porém, como a configuração do layout é global, quando o campo está marcado como **obrigatório**, o sistema exige o preenchimento independentemente do tipo de parceiro.

Para corrigir:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393324974103)

 Acesse a tela** ''Parceiros''** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393334388631)

 Na aba **''Identificação''** no campo ''**CNPJ / CPF''**, desmarque a opção **“Campo obrigatório”**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393324975639)

 Em seguida, acesse a tela ****[''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37393324976279)

 Desabilite os parâmetros:

- 

**ACEITACGCBRANCO** – Aceita CGC/CPF de Parceiro em branco?

- 

**ACEITACGCBRANF2** – Aceita CGC/CPF de Parceiro em branco (F2)?

Com essa configuração, o sistema permitirá o cadastro de **parceiros estrangeiros sem CNPJ/CPF** e continuará exigindo o preenchimento para **parceiros não estrangeiros**, garantindo a validação correta.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37315108751383)

CAUSA:**

Esse comportamento ocorre porque o campo **“CNPJ / CPF”** está configurado como **obrigatório** no layout do cadastro de parceiros. Essa configuração é **global** e se aplica a todos os parceiros, inclusive os estrangeiros.


---

### 🔗 Links e Referências Internas:

- [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)