# IE inválida [local de retirada/entrega]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043191573-IE-inv%C3%A1lida-local-de-retirada-entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043191573-IE-inv%C3%A1lida-local-de-retirada-entrega)  
> **ID:** `360043191573` | **Última Atualização:** 2026-07-22T16:06:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513316903575)

 MENSAGEM**:

[971 - Rejeição]: IE inválida [local de retirada/entrega].

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513332984855)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513332986519)

 Acesse: *Configurações » Cadastros » Parceiros:*

- Aba "**Contatos"**: realize o cadastro do contato/endereço de entrega.

![parceiros_aba_contatos.png](https://ajuda.sankhya.com.br/hc/article_attachments/12129068881815)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513332989463)

 IMPORTANTE:**

- Se parceiro for pessoa jurídica ou produtor rural, os campos de "**Endereço"** e** "Inscrição Estadual" **devem ser preenchidos na aba "**Contatos"** com uma I.E válida na UF do respectivo endereço. **Ex.:** Se endereço de entrega de SP, a IE deve ser de SP.

- Na tela "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (*Configurações » Avançado)* considere ligar o parâmetro "**PERMCNPJCONTATO"** para que seja possível informar CNPJ no Contato do parceiro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513342464023)

 Acesse: *Comercial » Configuração » Configurador de Layout da Nota*

- Selecione o layout utilizado na respectiva emissão.

- Insira no "**Cabeçalho"** desse layout o campo "**Contato de Entrega"**:

![IE_inv_lida_local_de_retirada_entrega.png](https://ajuda.sankhya.com.br/hc/article_attachments/14634532369047)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513383577623)

 **Ao realizar o lançamento, na **Central de Vendas/Compras**, informe no campo "**Contato de Entrega"** o contato cadastrado para entrega, conforme item 1.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513342473623)

 OBSERVAÇÕES:**

A rejeição acontecerá apenas se enviados os dados da <entrega>, essa tag será enviada no XML nas seguintes condições:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513332986519)

 Campo "**Contato de Entrega"** preenchido no cabeçalho da nota.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513342464023)

 Marcação "**Gerar endereço de entrega no XML da NF-e**" no cadastro da TOP;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513383577623)

 Quando for preenchida os dados da entrega, deixe o campo I.E em branco caso o parceiro de entrega seja isento de I.E.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513342477591)

 CAUSA**:

Se informado para o grupo de retirada/entrega uma Inscrição Estadual inválida para o respectivo Estado, será retornada a rejeição.

Quando forem preenchidos os dados da entrega, deixar o campo I.E em branco caso o parceiro de entrega seja isento de I.E.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)