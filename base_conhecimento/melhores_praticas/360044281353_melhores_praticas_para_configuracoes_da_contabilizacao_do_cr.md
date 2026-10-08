# Melhores Práticas para configurações da contabilização do crédito dos impostos PIS/COFINS sobre a depreciação dos ativos imobilizados

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044281353-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%B5es-da-contabiliza%C3%A7%C3%A3o-do-cr%C3%A9dito-dos-impostos-PIS-COFINS-sobre-a-deprecia%C3%A7%C3%A3o-dos-ativos-imobilizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044281353-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%B5es-da-contabiliza%C3%A7%C3%A3o-do-cr%C3%A9dito-dos-impostos-PIS-COFINS-sobre-a-deprecia%C3%A7%C3%A3o-dos-ativos-imobilizados)  
> **ID:** `360044281353` | **Última Atualização:** 2026-07-22T15:59:06Z

---

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458141147927)

 Veja as premissas**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295634854039)

 Primeiramente configure o cadastro do bem para geração do crédito conforme segue:

Configurações » Cadastros » Produtos » Produtos

Aba: Bens >> Sub Aba: Bens >> Sub aba: Geral

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295627659927)

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295634871447)

 **OBSERVAÇÃO:**

Esta aba é ativada decorrente da indicação da opção **"Imobilizado",** contida no campo **"Usado Como"**, aba ****["Geral"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) do **"****Cadastro do Produto"**.

- 

**"Tem Créd.PIS/COFINS sobre Dep.mensal"**: marcado;

- Campos **"Cód.Sit.Tributária PIS"** e **"Cód.Sit.Tributária COFINS"**: servem pra indicar o CST dos respectivos impostos;

- 
**"Alíquota PIS"**: informe o percentual referente à alíquota do imposto;

- 
**"Alíquota COFINS"**: informe o percentual referente à alíquota do imposto;

- 
**"Participa da MP540 PIS/CONFINS"**: marcado

- 
**"Nro.Parcelas Apr.Cred.PIS/COFINS"**: número de vezes em que o PIS e o COFINS serão creditados em cima do valor da depreciação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295627670423)

 Configure as contas para contabilização dos impostos conforme segue:

Configurações » Cadastros » Produtos » Produtos

Aba: Bens >> Sub Aba: Contas do Produto >> Sub Aba: PIS/COFINS

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13102032145687)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295627678615)

 Efetue o cálculo da depreciação do bem no MGE Imobilizado conforme segue:

MGEImobilizado>>Menu>>Rotinas>> Cálculo de depreciação mensal

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295634883607)

 Efetue a geração do lote de depreciação no MGE Imobilizado conforme segue:

MGEImobilizado>>Rotinas>>Geração de Lote de Depreciação

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295634889239)

 Efetue a geração do lote de contabilização do crédito dos impostos PIS/COFINS sobre o valor depreciado:

Contabilização » Rotinas » Contabilização dos Créditos de PIS/COFINS do Ativo Imobilizado

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13102130431127)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295627691927)

 Confira os lotes tanto de depreciação quanto de crédito dos impostos sobre a depreciação que foram gerados:

Contabilidade » Arquivos » Lotes Contábeis

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13102132994839)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295634899991)

 Confira os valores que foram gerados nos lançamentos contábeis do lote que foi gerado, exemplo: Lote 1300, do caso de teste.

Contabilidade » Arquivos » Lançamentos contábeis

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458141147927)

 Veja os cálculos:**

Valor da depreciação para o mês de julho: **136,67**
Alíquota de PIS:1,65%
Alíquota de COFINS: 7,6%

O valor da depreciação será a base para o cálculo do crédito dos impostos, sendo assim:

PIS: 136,67 * 1,65%= **2,26**
COFINS:136,67 * 7,6%= **10,39**


---

### 🔗 Links e Referências Internas:

- ["Geral"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral)