# Configurar a lei da transparência no rodapé do cupom fiscal

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044228173-Configurar-a-lei-da-transpar%C3%AAncia-no-rodap%C3%A9-do-cupom-fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044228173-Configurar-a-lei-da-transpar%C3%AAncia-no-rodap%C3%A9-do-cupom-fiscal)  
> **ID:** `360044228173` | **Última Atualização:** 2026-07-22T15:59:53Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200420637847)

 SITUAÇÃO:**

As informações da Lei da Transparência, não estão sendo apresentadas no rodapé dos cupons fiscais. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200420640535)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200458384279)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*

Aba: **Impostos**

Campos:

**"% Carga Média Trib. Estadual":** TGFPRO.PERCCMTEST

**"% Carga Média Trib. Federal":** TGFPRO.PERCCMTFED

**"% Carga Média Trib. Nacional":** TGFPRO.PERCCMTNAC

 

![cupom_fiscal.png](https://ajuda.sankhya.com.br/hc/article_attachments/14536550172695)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200458387479)

 OBSERVAÇÃO:**

Preencha a % Carga Média Trib. Estadual: e % Carga Média Trib. Federal:, ou preencha a % Carga Média Trib. Nacional:. Não pode preencher ambos.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200458389271)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

No cadastro de TOP de cupom fiscal, na aba **Impostos **a **"Classificação ICMS"** deve ser: Consumidor Final não contribuinte;

 

![cupom_fiscal2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14536551911831)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200458391063)

 Acesse: *Configurações » Cadastros » Parceiros*

No cadastro de parceiro, na aba **Fiscal** a **"Classificação ICMS" **deve ser: **"Consumidor Final não contribuinte"**;

 

![cupom_fiscal3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14536595156631)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200420657431)

 Acesse: *Fast Service » Menu » Avançado » Preferencias » Todas as Preferencias*

Aba **Parâmetros Iniciais**:

**"Imprimir nas observações do cupom":** marque a opção '**Lei da ****Transparência**'.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200420659607)

 Acesse: *Configurações » Avançado » Preferências*

Parâmetro: "**LEI12741FONTE -Fonte do cálculo da Carga Média Tributária"**

Para cumprimento desta norma configure o parâmetro Fonte do cálculo da Carga Média Tributária (LEI12741FONTE), que estará ativado desde que exista qualquer caractere em seu campo texto.

É aconselhável que o usuário digite neste campo o nome da fonte na qual conseguiu as porcentagens médias. Para apresentação dos totais de tributação ao consumidor final, essa informação sairá impressa junto com o percentual e o valor calculado destas tributações.

Após a configuração mostrada, todo cupom fiscal emitido terá no rodapé dele a porcentagem de Carga Média Tributária para os produtos configurados.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200458397975)

 CAUSA:**

Quando não configurado o parâmetro e dados sobre os percentuais de carga tributária nos produtos, as informações da Lei da Transparência não é apresentada no cupom.