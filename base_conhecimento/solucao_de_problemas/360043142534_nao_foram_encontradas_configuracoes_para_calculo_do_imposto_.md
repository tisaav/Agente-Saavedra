# Não foram encontradas configurações para cálculo do imposto 'PIS'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043142534-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-do-imposto-PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043142534-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-do-imposto-PIS)  
> **ID:** `360043142534` | **Última Atualização:** 2026-07-22T16:04:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146194521111)

 MENSAGEM:**

[CORE_E04491]  Não foram encontradas configurações para cálculo do imposto 'PIS'.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201839511)

 SITUAÇÃO:**

Ao tentar faturar/confirmar nota que possui incidência de PIS, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146194525847)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201842583)

 Acesse: *Comercial » Preferências » Empresa*

- Aba: **"Propriedades"**, campo **"Calcula PIS?"**: marcado

![N_o_foram_encontradas_configura__es_para_c_lculo_do_imposto__PIS_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14692327489559)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146194534551)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

- Aba: **"Impostos"**, campo **"Tem PIS"**: marcado

![N_o_foram_encontradas_configura__es_para_c_lculo_do_imposto__PIS__2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14692391594391)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201847959)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*

- Aba: **"Impostos"**, campo **"Grupo PIS"**:

![N_o_foram_encontradas_configura__es_para_c_lculo_do_imposto__PIS__3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14692446553367)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201848471)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS*

Realize um filtro com as informações referente ao seu lançamento, considerando os campos abaixo:

- Deve existir uma configuração nessa tela, com o mesmo **GRUPO** informado no cadastro do **produto**, com os campos TIPO (Entrada/Saída) e EMPRESA correspondentes.

- Se os campos PARCEIRO/TOP encontrarem-se como 0, significa que essa alíquota será utilizada para todos os parceiros/TOP'S referente aquele TIPO/GRUPO.

- Necessário compreender que se tratando de nota fiscal eletrônica, mesmo que não exista incidência desse imposto, as configurações citadas acima deverão existir, mesmo que para uma alíquota = 0 (zero).

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201851543)

 Após os ajustes, efetue a confirmação da nota novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16146201852951)

 CAUSA:**

Geralmente ocorre em relação ao cadastro da Empresa, Produto e TOP ou não possuir uma Regra de Alíquotas de PIS devidamente configurada.