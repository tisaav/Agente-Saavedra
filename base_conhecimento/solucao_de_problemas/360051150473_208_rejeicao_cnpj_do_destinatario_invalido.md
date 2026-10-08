# 208 - Rejeição: CNPJ do destinatário inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051150473-208-Rejei%C3%A7%C3%A3o-CNPJ-do-destinat%C3%A1rio-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051150473-208-Rejei%C3%A7%C3%A3o-CNPJ-do-destinat%C3%A1rio-inv%C3%A1lido)  
> **ID:** `360051150473` | **Última Atualização:** 2026-07-22T15:30:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588952926615)

 MENSAGEM**:

208 - Rejeição: CNPJ do destinatário inválido.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588952935959)

 CAUSA:**

Ocorre quando se informado CNPJ com zeros ou dígito de controle inválido.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588968902807)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588952955159)

 Configurações » Cadastros » Parceiros

1.1-Verifique e corrija o CNPJ do destinatário: Se informado CNPJ com zeros ou dígito de controle inválido, a rejeição será apresentada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588968912407)

 Deve-se consultar o CNPJ correto do destinatário no [SINTEGRA](http://www.sintegra.gov.br/) e ajustar no cadastro do parceiro.Após corrigido, redigite o cabeçalho da nota e gere um novo lote.

**Importante:**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588968918167)

 Ao realizar a consulta no [SINTEGRA](http://www.sintegra.gov.br/), certifique-se que a situação Cadastral do parceiro encontra-se ATIVA/HABILITADA:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18588952970391)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588952985111)

 Ao gerar o XML em conferência, estará sendo validado nessa rejeição, as informações enviadas na tag **<CNPJ>**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18588968955543)

 Para parceiros 'estrangeiros' lembre-se de preencher o parâmetro CODPAISBRASIL [55]. Mais detalhes, acesse:[Quais as principais configurações para emissão de nota de exportação - parceiro estrangeiro ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)


---

### 🔗 Links e Referências Internas:

- [Quais as principais configurações para emissão de nota de exportação - parceiro estrangeiro ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)