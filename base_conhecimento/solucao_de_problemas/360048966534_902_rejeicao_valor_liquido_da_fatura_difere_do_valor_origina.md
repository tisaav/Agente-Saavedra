# 902 - Rejeição: Valor Liquido da Fatura difere do Valor Original menos o Valor do Desconto

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360048966534-902-Rejei%C3%A7%C3%A3o-Valor-Liquido-da-Fatura-difere-do-Valor-Original-menos-o-Valor-do-Desconto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048966534-902-Rejei%C3%A7%C3%A3o-Valor-Liquido-da-Fatura-difere-do-Valor-Original-menos-o-Valor-do-Desconto)  
> **ID:** `360048966534` | **Última Atualização:** 2026-07-22T15:31:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604738065687)

 MENSAGEM**:

902 - Rejeição: Valor Liquido da Fatura difere do Valor Original menos o Valor do Desconto.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604738067351)

 CAUSA:**

Rejeição acontecerá quando o Valor Líquido da Fatura [<vLiq>] for diferente do Valor Original da Fatura [<vOrig>] - Valor do Desconto [<vDesc>].

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604726772247)

 Rejeição acontecerá quando o Valor Líquido da Fatura [<vLiq>] for diferente do Valor Original da Fatura [<vOrig>] - Valor do Desconto [<vDesc>].

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604726773655)

 Considere o exemplo abaixo:

*<fat>*
***<vOrig>55.90</vOrig>***
***<vDesc>0.00</vDesc>***
***<vLiq>58.90</vLiq>***
*</fat>*

 

Note que o Valor Líquido da Fatura [58,90] difere do Valor Original - Valor do Desconto : 55,90 - 0,00

Uma das causas dessa rejeição no sistema é a configuração do parâmetro abaixo:

- 
**Destaca imp.federais na NF-e mista qdo.não retido?  - ****DESTIMPNRETNFEM**

Caso alguma UF precise trabalhar com esse parâmetro **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM** ligado, recomendamos que essa UF seja listada no parâmetro abaixo:

- Chave: **UFs que somam os impostos retidos na NFe - UFSSOMAIMPRET**
Descrição: UFs que somam os impostos retidos na NFe

1. Este parâmetro poderá conter as UFs que precisam dos parâmetros **Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT** e **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM** ligados, necessários normalmente somente para estados que emitem notas mistas.

1. Caso se preencha no parâmetro uma ou mais UFs, os parâmetros

1. 
**Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT** e **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM**

1. serão considerados apenas para os estados emitentes informados no parâmetro (separados por vírgula). Para os demais estados, os parâmetros serão considerados desligados.

------------------------------------------------------------------------------------------

Outra causa identificada para essa rejeição:

Quando temos o parâmetro **Destaca imp.federais na NF-e mista qdo.no retido? - DESTIMPNRETNFEM** habilitado, o sistema está deduzindo o valor do frete da tag <vOrig>, gerando rejeição.

[-] SOLUÇÃO: Foi ajustado o sistema para somar na tag vOrig o valor do frete e de outros impostos (tag vOutro) caso exista na nota.

- Para esse caso, atualize a base de teste com a versão mais atual, validar as operações e rotinas da empresa e só depois atualizar a base de produção com segurança: Correção disponível na versão 4.0b127 ou versões superiores.