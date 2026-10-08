# 853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35384537690903-853-Rejei%C3%A7%C3%A3o-Dados-de-cobran%C3%A7a-n%C3%A3o-devem-ser-informados-para-pagamento-%C3%A0-vista](https://ajuda.sankhya.com.br/hc/pt-br/articles/35384537690903-853-Rejei%C3%A7%C3%A3o-Dados-de-cobran%C3%A7a-n%C3%A3o-devem-ser-informados-para-pagamento-%C3%A0-vista)  
> **ID:** `35384537690903` | **Última Atualização:** 2026-07-22T14:25:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384496278551)

 MENSAGEM:**

853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537684247)

 SOLUÇÃO:**

### **Identifique o Tipo de Operação:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384496286871)

 Acesse o **Portal de Vendas ou Compras**, selecione a **nota que recebeu a rejeição**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537685655)

 Na nota rejeitada, veja no cabeçalho o **"Tipo de operação" **que está sendo usado. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537688727)

 Em seguida, acesse a tela **'Tipos de Operação" **e verifique se a TOP usada na nota está adequada para operação em questão. Caso não esteja, faça o devido ajuste.

 

### **Configure a condição de pagamento:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384496286871)

 Ainda na nota rejeitada, veja se o campo **"Tipo Negociação" **está como **"A vista". **Caso esteja e o **pagamento realmente seja à vista, realize os ajustes abaixo:**

 

![853 Rejeição 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/35391907929495)

 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537685655)

 Vá até a aba **"Financeiro" **e, no campo **"Tipo de título",** selecione uma condição que seja condizente com pagamento à vista como, **Dinheiro ou Pix;**

 

![853 Rejeição 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/35391907934743)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537688727)

 **Também na aba Financeiro garanta que:**

- 

a operação tenha apenas **uma parcela;**

 

![853 Rejeição 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/35391923362327)

 

- 

e a data de **vencimento esteja igual **a data de **emissão.**

 

![853 Rejeição 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/35391923367063)

 

### **Configure a condição de pagamento:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384496286871)

 Ainda nota rejeitada, na aba Financeiro, acesse a **"Movimentação financeira" **dela e garanta que o campo **"Nro Duplicata" **esteja vazio. Não informe um número de duplicata para operações à vista.

 

![853 Rejeição 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/35392051176471)

 

![853 Rejeição 6.png](https://ajuda.sankhya.com.br/hc/article_attachments/35392066735255)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384537685655)

  E caso haja duplicatas ligadas a nota, remova todas elas. 

 

### **Ajuste de parâmetro**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35384496286871)

 Por fim, acesse a tela **"Preferências" **e desabilite o parâmetro **"ESCDETDUPLNFE - Esconder detalhes do campo Fatura/Duplicata na NFE". **

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35393308617239)

 Observação:**** **o **parâmetro** foi **criado como paliativo até que fosse concluída a entrada da nota técnica**. No entanto, **ao utilizá-lo, o sistema deixa de levar para o XML e para o DANFE informações de operações a prazo**, nas quais esses dados são obrigatórios.

Por isso, é fundamental **manter o sistema atualizado **para as** versões **que já** contemplam as implementações da NT 2025.001**, **eliminando **a necessidade de** usar o parâmetro ESCDETDUPLNFE.**

**As versões adequadas são:**

- 4.31b179

- 4.32b160

- 4.33b159

- 4.34b193

- 4.35B159

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35391907945367)

 CAUSA:**

Essa rejeição ocorre quando a NF-e está configurada com pagamento à vista (campo <indPag> = 0). No entanto, o** XML enviado contém o grupo de cobrança (<cobr>, <dup>), ou duplicatas com vencimento igual à data de emissão.**

A Sefaz considera que, **para pagamento à vista, não se deve informar dados de parcelamento, duplicatas ou vencimentos.**

**Ou seja**: se a nota é “à vista”, não se pode misturar com dados de cobrança (duplicatas, vencimentos, etc.).