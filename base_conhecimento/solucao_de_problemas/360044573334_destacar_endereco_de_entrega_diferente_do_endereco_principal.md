# Destacar endereço de entrega diferente do endereço principal do parceiro

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573334-Destacar-endere%C3%A7o-de-entrega-diferente-do-endere%C3%A7o-principal-do-parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573334-Destacar-endere%C3%A7o-de-entrega-diferente-do-endere%C3%A7o-principal-do-parceiro)  
> **ID:** `360044573334` | **Última Atualização:** 2026-07-22T15:51:36Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586485699991)

 SITUAÇÃO:**

Na Emissão de uma NF-e, existe casos em que o endereço de entrega é diferente do endereço principal do parceiro, como configurar para resolver esta situação?

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586517565463)

 CAUSA:**

Quando a configuração do endereço de entrega não esta configurado corretamente, e a TOP não esta devidamente sinalizado o que destacar na geração do endereço de entrega.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586517572631)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586517575575)

 Configurações » Cadastros » Parceiros

- Aba: Endereço de Entrega: [*Preencher os dados do endereço de entrega nesta aba, com endereço diferente do Endereço Principal].*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586485733143)

 Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: NF-e/NFC-e

- Campo: Gerar endereço de entrega no XML da NF-e:

[**Parceiro Principal**] - Se selecionado esta opção, sistema levara dados do 'Endereço de Entrega' para o XML da Nota na tag <entrega>, caso o endereço de entrega seja diferente do endereço principal.[**Parceiro ****Destinatário**] - Se selecionado esta opção, sistema levara os dados do endereço, definido no campo 'Parceiro Destinatário', do Cabeçalho da Nota, caso esteja preenchido, caso não esteja preenchido, sistema não gerara, a tag <entrega> e seguira os dados do parceiro da nota normalmente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586485740183)

 Para a Impressão dos dados da Entrega, configure:

- Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: Impressão

- Campo: Modelo para Dados Adicionais de NF-e:

Crie um modelo em txt, utilizando-se de expressões/variáveis, afim de destacar na impressão os dados da aba: Endereço de Entrega do Parceiro da Nota.

*Lembrando que na impressão do DANFE, o sistema sempre imprimi o endereço do Parceiro Principal da nota e as informações relativas ao endereço de entrega, com a configuração acima, sera destacado no campo *'Informações Complementares*' do DANFE.

 

**Caso de Uso:**

Emitente da nota do estado de MG e Parceiro do Estado de São Paulo-Capital e a entrega, será em outro endereço diferente do endereço principal do parceiro, no caso em Santos. Destacar o endereço de Santos no XML e Danfe.