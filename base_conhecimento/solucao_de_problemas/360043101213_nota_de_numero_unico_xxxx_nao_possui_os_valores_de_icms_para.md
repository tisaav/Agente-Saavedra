# Nota de número único "xxxx" não possui os valores de ICMS para SIMPLES NACIONAL

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101213-Nota-de-n%C3%BAmero-%C3%BAnico-xxxx-n%C3%A3o-possui-os-valores-de-ICMS-para-SIMPLES-NACIONAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101213-Nota-de-n%C3%BAmero-%C3%BAnico-xxxx-n%C3%A3o-possui-os-valores-de-ICMS-para-SIMPLES-NACIONAL)  
> **ID:** `360043101213` | **Última Atualização:** 2026-08-20T15:13:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334459810967)

 **MENSAGEM:**

[CORE_E01567]: Nota de número único "XXX" não possui os valores de ICMS para SIMPLES NACIONAL.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444772759)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444773655)

 **Abra a nota através da **Central de Vendas/Compras**, selecione na grade Itens o primeiro produto.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334459814679)

 **No botão **"Outras Opções"** [...] »**"Consultar/alterar dados dos impostos do Item" **verifique se foi gerada uma linha para o Imposto ICMS.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444775959)

 Se constarem as informações de ICMS,** **busque pelo campo **"CST/CSOSN"** (Siga com o passo a passo para todos os demais itens da nota, até que seja localizado o item em que essa informação esteja em branco).

 

![consultar_alterar_dados_do_imposto.png](https://ajuda.sankhya.com.br/hc/article_attachments/14466846659863)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444776727)

 Identificado os itens nos quais a informação de CST/CSOSN encontra-se zerada, busque na linha desse item pela informação **"Cód.Alíq.ICMS"** (Caso essa informação não exista no seu layout, adicione a pelo Configurador de Layout da Nota).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334459819671)

 Acesse a tela **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"** e digite o ID localizado no item 4 ao lado esquerdo da tela ("Localizar"), pressione enter: será apresentado na tela a alíquota responsável pela tributação do item analisado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444779927)

 Nessa alíquota acesse a aba **"Simples Nacional"** e preencha o campo "**Código de Situação da Operação no Simples Nacional - CSOSN**".

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334459836439)

 Inutilize a nota rejeitada, refaça o lançamento, refaça a conferência da informação CST/CSOSN conforme Item 3 e confirme a nova nota lançada.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458212870679)

 ICMS não calculado:**

Para os casos onde a linha de ICMS não é localizada através do Consultar/alterar dados dos impostos do Item realize a verificação dos cadastros necessários ao cálculo desse imposto:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444782871)

 *Tipos de Operação » Aba Impostos » Cálculo de ICMS, IPI e ISS*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444782871)

 *Tipos de Operação » Aba Impostos » Tem ICMS*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444782871)

 *Produtos » Aba Impostos » Calcular ICMS*

 

Se necessário o ajuste de alguma dessas informações, lembre-se de inutilizar/excluir a nota rejeitada e refazer o lançamento.

Nesse novo lançamento confira se a linha de ICMS foi devidamente gerada para todos os itens, com os respectivos dados de CST/CSOSN conforme orientações do seu Contador.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458212870679)

 Correção "Manual":**

O passo a passo acima resulta na solução do problema através da causa raiz.

Diante necessidades urgentes, é possível inserir a informação CSOSN diretamente na nota ('Consultar/alterar dados dos impostos do Item' e linha do Item), contudo essa só será possível para os casos onde o Tipo de Operação - TOP está configurado como ***"Calcula e Digita"*** (aba Impostos, campo Cálculo de ICMS, IPI e ISS).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334444784535)

 CAUSA:**

Empresas Optantes pelo Simples Nacional, ao emitir NF-e com ausência de informações do ICMS e seu respectivo CSOSN, terão a rejeição apresentada.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)