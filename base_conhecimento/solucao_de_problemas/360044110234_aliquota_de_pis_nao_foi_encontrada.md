# Alíquota de "PIS" não foi encontrada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110234-Al%C3%ADquota-de-PIS-n%C3%A3o-foi-encontrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110234-Al%C3%ADquota-de-PIS-n%C3%A3o-foi-encontrada)  
> **ID:** `360044110234` | **Última Atualização:** 2026-07-22T15:53:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996445566487)

 MENSAGEM:**

'Erro durante a confirmação: 4649'
Local: Calculando PIS
Alíquota de "PIS" não foi encontrada.
Grupo: "YYYY", Tipo: "E", Empresa: "1", Parceiro: "AAAA", TOP: "X"
Verifique se nos cadastros de alíquota e de produto não existe espaço em branco no início ou no final do campo Grupo PIS.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996469190935)

 SITUAÇÃO:**

Ao tentar confirmar uma Nota de Compra/Venda, é apresentando a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996445568663)

 SOLUÇÃO:**
Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996445571223)

 Acesse: Comercial » Preferências » Empresa / Aba: **"Propriedades"**
Campos:

- **"Calcula PIS?"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996445572631)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP/ Aba: Impostos
Campos:

- **"Tem PIS"**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996469202071)

 Acesse: Configurações » Cadastros » Produtos / Aba: Impostos
Campos:

- **"Grupo PIS"**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996469205399)

 Efetue a configuração de acordo com a movimentação de Nota. Se para Entrada, crie uma regra de PIS especifica para Entrada com a respectiva alíquota e CST, acessando: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996469206423)

 **IMPORTANTE:**

Recomenda-se criar especificamente regras de Entrada e regras de Saídas, pois os CST's são diferentes para ambos.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16996469207447)

 CAUSA:**

Ocorre quando a nota está incidindo no cálculo de PIS, geralmente em relação ao cadastro da Empresa, Produto e TOP e não possui uma Regra de Alíquotas de PIS devidamente configurada.