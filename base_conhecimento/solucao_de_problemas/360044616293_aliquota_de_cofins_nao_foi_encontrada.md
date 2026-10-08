# Alíquota de "COFINS" não foi encontrada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616293-Al%C3%ADquota-de-COFINS-n%C3%A3o-foi-encontrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616293-Al%C3%ADquota-de-COFINS-n%C3%A3o-foi-encontrada)  
> **ID:** `360044616293` | **Última Atualização:** 2026-07-22T15:54:11Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415523720215)

 MENSAGEM:**

'Erro durante a confirmação: 4649'
Local: Calculando COFINS
Alíquota de "COFINS" não foi encontrada.
Grupo: "YYYY", Tipo: "E", Empresa: "1", Parceiro: "AAAA", TOP: "X"
Verifique se nos cadastros de alíquota e de produto não existe espaço em branco no início ou no final do campo Grupo COFINS.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534920983)

 SITUAÇÃO:**

Ao tentar confirmar uma Nota de Compra/Venda é apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534922775)

 SOLUÇÃO:**
Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534925591)

 Acesse: *Comercial » Preferências » Empresa* / Aba: Propriedades
Campo:

- **"Calcula COFINS?"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534927383)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*/ Aba: Impostos
Campo:

- **"Tem COFINS"**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534930839)

 Acesse: *Configurações » Cadastros » Produtos* / Aba: Impostos

Campo:

- **"Grupo COFINS"**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415534934039)

 Efetue a configuração de acordo com a movimentação de Nota. Se para entrada, crie uma regra de PIS específica para Entrada com a respectiva alíquota e CST. 

- *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS*

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458084784791)

 Recomenda-se criar especificamente regras de Entrada e regras de Saídas, pois o CST são diferentes para ambos.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16415523740823)

 CAUSA:**

Ocorre quando a nota está incidindo no cálculo de COFINS, geralmente em relação ao cadastro da Empresa, Produto e TOP. Também quando não possui uma Regra de Alíquotas de COFINS devidamente configurado.