# CNPJ do Transportador inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18253585515799-CNPJ-do-Transportador-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/18253585515799-CNPJ-do-Transportador-inv%C3%A1lido)  
> **ID:** `18253585515799` | **Última Atualização:** 2026-07-22T14:52:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253585487127)

 **MENSAGEM:**

542-Rejeição: CNPJ do Transportador inválido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253589663639)

CAUSA:**

Ocorre quando na validação do CNPJ do transportador informado na NF-e (Nota Fiscal Eletrônica)  é inválido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253628803479)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253589658775)

 Se a nota possuir uma transportadora vinculada na aba: "**Transporte"**, no rodapé da nota na tela da Central, ajuste o cadastro da Transportadora, acessando:

Acesse : "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: *Configurações » Cadastros » Parceiros*)

- Aba: "**Identificação"**

- Campo "**CNPJ"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253585499031)

 Se a nota for de Operação Estrangeira e/ou a Transportadora também siga o passo á passo:  

Ativar o Parâmetro **"Aceita CGC/CPF de Parceiro em branco? - ACEITACGCBRANCO".**

![Imagem](/attachments/token/luPeI5INLYtDvqV8nK6ZkD67m/?name=image.png)

 

Desmarcar o Campo como Obrigatório no cadastro do Parceiro Transportadora.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18298185197335)

Deixe o campo "**CNPJ"** em branco no cadastro do Parceiro Transportadora.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18298158954775)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18253605527191)

 Após os ajustes, redigite a Transportadora na nota e transmita novamente o lote.


---

### 🔗 Links e Referências Internas:

- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)