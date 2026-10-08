# Código de aglutinação de linha totalizadora de demonstração contábil não deve constar no registro I052

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617313-C%C3%B3digo-de-aglutina%C3%A7%C3%A3o-de-linha-totalizadora-de-demonstra%C3%A7%C3%A3o-cont%C3%A1bil-n%C3%A3o-deve-constar-no-registro-I052](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617313-C%C3%B3digo-de-aglutina%C3%A7%C3%A3o-de-linha-totalizadora-de-demonstra%C3%A7%C3%A3o-cont%C3%A1bil-n%C3%A3o-deve-constar-no-registro-I052)  
> **ID:** `360044617313` | **Última Atualização:** 2026-07-22T15:53:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593175738263)

 MENSAGEM:**

Código de aglutinação de linha totalizadora de demonstração contábil não deve constar no registro I052.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593200498199)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593200503319)

 Acesse: *Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD*

Para os Demonstrativos do ECD, para cada um (Balanço Patrimonial, DRE, DMPL e etc.) a estrutura Hierárquica deverá seguir a sequencia logica.

 

**Exemplo**:
Se o Balanço Patrimonial tem os códigos aglutinadores 1 e 2, a DRE deve começar do 3 em diante, se a DRE tem do 3 até o 13, a DMPL deve começar do 14 em diante, se a DMPL tem do 15 até o 20, a DFC deve começar do 21 em diante, de modo que um demonstrativo nunca tenha o mesmo código aglutinador que o outro

 

![BP_dre_.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360061081353)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593175751063)

CAUSA:**

Esse erro ocorre porque os códigos aglutinadores se repetem entre os demonstrativos, por exemplo:

**Balanço patrimonial:**

1
1.1
2
2.1

**DRE**:

1
2