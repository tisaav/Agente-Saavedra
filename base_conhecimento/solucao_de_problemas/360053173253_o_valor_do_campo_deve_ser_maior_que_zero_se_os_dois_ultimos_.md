# O valor do campo deve ser maior que zero, se os dois últimos dígitos do CST_ICMS = 20 ou 70."- EFD ICMS/IPI

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360053173253-O-valor-do-campo-deve-ser-maior-que-zero-se-os-dois-%C3%BAltimos-d%C3%ADgitos-do-CST-ICMS-20-ou-70-EFD-ICMS-IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053173253-O-valor-do-campo-deve-ser-maior-que-zero-se-os-dois-%C3%BAltimos-d%C3%ADgitos-do-CST-ICMS-20-ou-70-EFD-ICMS-IPI)  
> **ID:** `360053173253` | **Última Atualização:** 2026-07-22T15:29:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357980078871)

 MENSAGEM**:

O valor do campo deve ser maior que zero, se os dois últimos dígitos do CST_ICMS = 20 ou 70.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357980086295)

 CAUSA:**

Os CSTs 20 e 70 - Com redução da Base de Calculo. Estes CSTs devem apresentar redução de base, mensagem será apresentada quando essa redução for zero.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357943531927)

 SOLUÇÃO:**

- Advertência apresentada na geração do EFD ICMS/IPI -  SPED Fiscal, no Registro C190 campo 10 - VL_RED_BC  - Valor não tributado em função da redução da base de cálculo  o ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357980100503)

 Acesse a central dessa nota (Portal de Compras ou Portal de Vendas);

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357943545239)

 Selecione o item, botão outras opções >> selecionar a Opção: **'Consultar/Alterar dados impostos do item" (**tela que chamamos de TGFDIN no dicionário de dados do sistema, essa tela fica presente as linhas de cada imposto envolvido no produto-item/nota);

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357980117783)

 Na linha correspondente ao ICMS, verificar os campos:

- 
**Base**:50,67

- 
**Base Calc. Reduzida**.:20,87

(valores utilizado para exemplificação de um caso)

- Quando lançado item com CST 20 ou CST 70, que é "Com redução da BC", as colunas de 'Base de Calculo' e 'Base de Cálculo Reduzida' são diferentes, e esta **diferença do valor**, destes campos, que  é levada para o campo 10 do C190.

- Ou seja, a geração do campo 10-VL_RED_BC do registro C190 é com base na diferença entre os campos BASE e BASERED da TGFDIN.

- A rejeição ocorrerá se utilizado os CST'S 20 ou 70 e não existir essa diferença de valor (0,00)

Neste exemplo o campo 10 - VL_RED_BC , recebe o valor de 29,80.E a advertência não ocorrerá no EFD ICMS/IPI quando importar para o PVA.