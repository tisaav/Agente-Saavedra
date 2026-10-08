# Foram encontrados documentos de CT-e com modais diferentes na mesma ordem de carga

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360053500874-Foram-encontrados-documentos-de-CT-e-com-modais-diferentes-na-mesma-ordem-de-carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053500874-Foram-encontrados-documentos-de-CT-e-com-modais-diferentes-na-mesma-ordem-de-carga)  
> **ID:** `360053500874` | **Última Atualização:** 2026-07-22T15:28:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16417287718935)

 MENSAGEM**:

[CORE_E01477] Foram encontrados documentos de CT-e com modais diferentes na mesma ordem de carga. Todos os documentos de CT-e devem possuir o mesmo modal.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16417287721879)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

Caso a empresa emitente da MDF-e, seja prestadora de serviços de transporte. Poderá haver em uma MDF-e, Notas Fiscais de vendas e também CT-e's-**na mesma ordem de carga. **

Diante disso, considere ativar o parâmetro **"****GERASOCTEMDFE-Extrair somente CT-e de OC contendo NF-e/CT-e" **(Configurações » Avançado » Preferências).

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453240951319)

 Quando o parâmetro estiver ligado, ao criar a viagem, somente os Conhecimentos de Transporte serão considerados na criação da viagem.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16417287727639)

 Caso a viagem seja Modal Rodoviário, a TOP da CT-e deverá estar configurada na aba: **"CT-e/MD-e"** o campo **"****Modal CT-e": ** **Rodoviário**, para todas as TOPs de CT-e, vinculado à mesma OC-Ordem de Carga.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16417287727639)

 Caso a viagem seja Modal Aquaviário, a TOP da CT-e deverá estar configurada na aba: **"CT-e/MD-e"** o campo **"****Modal CT-e":** **Aquaviário**, para todas as TOPs de CT-e, vinculado à mesma OC-Ordem de Carga.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453240951319)

 Acesse a TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba: **"CT-e/MD-e"**:

![Foram_encontrados_documentos_de_CT-e_com_modais_diferentes.png](https://ajuda.sankhya.com.br/hc/article_attachments/14524955172247)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16417287730199)

 CAUSA:**

Ocorre quando em uma MDF-e, pode existir CT-e e Notas de Vendas no qual para a mesma Ordem de Carga, existas CT-e com Tipos de Modal diferentes (Aquaviário/Rodoviário).