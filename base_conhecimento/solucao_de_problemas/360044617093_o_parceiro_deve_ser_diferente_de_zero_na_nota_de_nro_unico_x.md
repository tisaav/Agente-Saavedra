# O parceiro deve ser diferente de zero na nota de Nro Único: 'X'

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617093-O-parceiro-deve-ser-diferente-de-zero-na-nota-de-Nro-%C3%9Anico-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617093-O-parceiro-deve-ser-diferente-de-zero-na-nota-de-Nro-%C3%9Anico-X)  
> **ID:** `360044617093` | **Última Atualização:** 2026-07-22T15:53:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592671254935)

 MENSAGEM:**

[ORA-20101]: O parceiro deve ser diferente de zero na nota de Nro Único:

[ORA-06512]: em "SANKHYA.TRG_INC_TGFCAB", line 443

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFCAB'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592671260567)

SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592695284503)

 **Selecione a empresa utilizada no processo de inventário na tela "**Empresa**" *(Caminho de acesso: Comercial » Preferências)*.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592695288343)

 **Na aba **"Estoque/Preço"**, verifique as informações apresentadas nos campos **"Modelo Ajuste de Entrada de Estoque**" e "**Modelo Ajuste de Saída de Estoque**":

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15238735639447)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592671268631)

 **Busque pelos códigos de modelo localizados no item 2, através da tela "**Modelo de Notas e Pedidos**" *(Comercial » Consulta)*.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592695293335)

 Para ambos modelos, preencha o campo **"Parceiro"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15238828664855)

 

Aconselha-se ter o cadastro da empresa como parceiro e utilizá-lo para tal.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16592671275031)

 CAUSA:**

Ao tentar realizar ajuste de estoque, caso os modelos vinculados para esse ajuste não possuam o campo Parceiro informado, será apresentada a mensagem.