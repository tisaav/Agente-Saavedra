# Problemas no cálculo de PIS/COFINS: Os CST's devem ser iguais e não vazios

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138434-Problemas-no-c%C3%A1lculo-de-PIS-COFINS-Os-CST-s-devem-ser-iguais-e-n%C3%A3o-vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138434-Problemas-no-c%C3%A1lculo-de-PIS-COFINS-Os-CST-s-devem-ser-iguais-e-n%C3%A3o-vazios)  
> **ID:** `360043138434` | **Última Atualização:** 2026-08-24T18:15:21Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16136103077399)

**MENSAGEM:**

Validar TGFDIN: Validação da TGFDIN. Nota Nro.Único: xxxxxx.
Problemas no cálculo de PIS/COFINS: Os CSTs devem ser iguais e não vazios.
PIS é obrigatório para NF-e.
COFINS é obrigatório para NF-e.
Procure o administrador do sistema

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/16136147779991)

**SITUAÇÃO:**

Ao tentar confirmar uma Nota Fiscal de Venda ou Devolução de Compra, ocorre a mensagem de erro acima, indicando falha no cálculo de PIS e COFINS.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16136147782295)

**SOLUÇÃO:**

Para correção, verifique as parametrizações seguindo a ordem:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16136103085463)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros)
      

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Aba **"Impostos", **campos: **"TEM PIS"** / **"TEM COFINS"**: Marcados

      

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Aba **"Livros Fiscais"**, campo: **"Atualização de Livro de ICMS"**: Configure de acordo com o movimento
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16136103091095)

 Acesse a tela **"Empresa"** (Comercial » Preferências)
      

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Aba: **"Propriedades"**, campos: **"Calcula PIS" **/** "Calcula COFINS"**: Marcados
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/16136147794455)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos)
     

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Aba: **"Impostos"**, campos: **"Grupo PIS" **/** "Grupo COFINS"**: Insira os respectivos grupos criados nas telas de alíquotas de PIS e COFINS, conforme orientados nos passos 4 e 5 que seguem abaixo. 
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/16136147796887)

 Acesse a tela "**Alíquotas de PIS**" (Comercial » Arquivo » Cadastros » Alíquotas):
    

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Nessa tela deverá criar uma regra para o Grupo de PIS vinculado ao respectivo produto, para o tipo de movimento utilizado (Entrada ou Saída). Atente-se a compreender o processo atual da empresa, validando exceções por TOP ou Parceiro, por exemplo.

     

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Informe o **Cód. sit. tributária** compatível com suas operações. Vale destacar que essa informação deve ser validada com o Contador da empresa.
 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136090335511)

 Acesse a tela "**Alíquotas de COFINS**" (Comercial » Arquivo » Cadastros » Alíquotas):
    

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Nessa tela deverá criar uma regra para o Grupo de COFINS vinculado ao respectivo produto, para o tipo de movimento utilizado (Entrada ou Saída). Atente-se a compreender o processo atual da empresa, validando exceções por TOP ou Parceiro, por exemplo.

     

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16136134031511)

 Informe o **Cód. sit. tributária** compatível com suas operações. Vale destacar que essa informação deve ser validada com o Contador da empresa.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16136103099927)

**CAUSA:**

O erro ocorre por configurações inadequadas (CST's vazios ou incoerentes), falta de grupos de impostos vinculados ao produto ou parametrizações de TOP ou Empresa incorretas para o tipo de movimentação realizada.