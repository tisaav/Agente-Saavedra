# Estoque inválido, comunique ao seu Gerente

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674213-Estoque-inv%C3%A1lido-comunique-ao-seu-Gerente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674213-Estoque-inv%C3%A1lido-comunique-ao-seu-Gerente)  
> **ID:** `360043674213` | **Última Atualização:** 2026-07-22T16:03:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145410215191)

 MENSAGEM**:

[CORE_E00997] Estoque inválido, comunique ao seu Gerente.
[Produto: 999, Série: XPTO12345]
Código: CORE_E00997

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145426387991)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

- Produtos de Controle Adicional por **série**, precisam ser minuciosamente controlados com mais rigor, pois sempre existirá uma **série** para atender a uma quantidade do produto. Exemplo: Aparelhos celulares.

- Em todos os movimentos de produtos controlados por **série**, o sistema irá verificar se existe alguma **série** com saldo incorreto, ou seja, os valores de saldo para as **séries** devem ser = 0(zero), (significa que a **série** não está disponível) ou = 1 (um), (significa que a **série** pode ser utilizada).

- Caso o resultado seja <> (diferente) do desejado acima, a mensagem de Estoque inválido é apresentada e significa que já houve movimentação dessa série em outra nota.

*A mensagem será apresentada caso houver uma inconsistência de saldo de estoque independente da série do lançamento da nota, então deve ser ajustado o saldo de estoque da série que for informada na mensagem.*

**Observação: **caso a mensagem seja apresentada ao baixar uma matéria prima controlada por série em uma nota de produção, será necessário verificar como está configurado o campo **"Usado como"** da MP no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos). O mesmo deve ser configurado como **"Matéria prima"** ou **"Prod.Intermediário"** para produtos consumidos na produção. Se o produto possuir outras finalidades com maior relevância (Exemplo: Revenda), o campo **"Tipo do item p/ SPED"** deverá ser configurado conforme maior relevância para uso do material, visto que esse campo é utilizado para declaração do SPED.

**CONSIDERAÇÕES DE ANÁLISE DE ESTOQUE:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145410219159)

 Faça uma análise de estoque através da "****[Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055072414)" *(Caminho de acesso: Comercial » Consulta » Consulta de Produtos )* - Utilize o painel "**Série"**

- Ative o painel Série, pelo botão: 
Aba: **"Outras Informações"**
Opção **"Série": **modo Link ou Painel

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145426392471)

 Verifique nos Portais de (Compra/Venda) se existe alguma movimentação do Produto/Série, no qual a nota ainda não foi confirmada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145410226455)

 Identifique se existe alguma inconsistência de estoque através da rotina "**[Verificação de Saldo de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054)"** *(Caminho de acesso: Configurações » Avançado » Verificação de Saldo de Estoque)*, se houver faça a correção.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145410227735)

 Faça uma contagem de estoque e utilize a rotina "**[Ajuste de Estoque Por Série"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673)** para o acerto de estoque.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145410229911)

 **CAUSA:**

Ocorre quando alguma série está com inconsistência de saldo no sistema, diferente de 1 (um) quando tem estoque ou 0 (zero) quando não tem estoque. Ou seja, não pode haver estoque negativo ou mais que 1 (um) para série.


---

### 🔗 Links e Referências Internas:

- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)
- [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055072414)
- [Verificação de Saldo de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054)
- [Ajuste de Estoque Por Série"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673)