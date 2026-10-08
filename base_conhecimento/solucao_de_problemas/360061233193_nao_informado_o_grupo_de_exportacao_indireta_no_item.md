# Não informado o grupo de Exportação indireta no item

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360061233193-N%C3%A3o-informado-o-grupo-de-Exporta%C3%A7%C3%A3o-indireta-no-item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061233193-N%C3%A3o-informado-o-grupo-de-Exporta%C3%A7%C3%A3o-indireta-no-item)  
> **ID:** `360061233193` | **Última Atualização:** 2026-07-22T15:26:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282321370519)

 MENSAGEM**:

[340 - Rejeição] Não informado o grupo de Exportação indireta no item.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282321373335)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282381832983)

 Tenha em mãos os dados da nota de Origem (nota que deu entrada dos produtos no sistema, que pode ser consultada no portal de Compras). Esta nota deve estar devidamente com os dados da Declaração de Importação, preenchidas e APROVADA na Sefaz.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282381836439)

 Acesse o **"Portal de Vendas"** em: *Comercial » Consulta » Portal de Vendas*
Pesquise e acesse a nota que esta apresentando a rejeição.
Acesse a nota e clique nos itens, na opção 'Outras Opções>>Documentos relacionados'
Pesquise pela Nota de Origem (nota de Importação) e vincule aos itens.
Caso não seja preenchido automático *(ver Observação abaixo)* os campos, **Número do Registro de Exportação** e **Número do Ato Concessório de Drawback,** preencha com os dados necessários.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282321381911)

 Nas Preferências da Empresa *(Caminho de acesso: Configurações » Avançado » Preferências)*, o parâmetro **"****HABTAGDETEXPORT"** deve estar ligado.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282321384215)

 Após ajustes, gere novamente o lote da Nota.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282381845271)

 OBSERVAÇÃO**:

Quando emite-se uma nota para fim de exportação, 
CFOP **7501** (Saída) ou **3503** (Entrada). Se faz necessário:

> Para CFOP 7501, gerar o grupo de tags **<detExport>**.
> Para CFOP 3503, gerar o grupo de tags **<exportInd>**.

Geração do grupo <detExport>, este grupo é gerado através de 'Documentos Relacionados', que no caso é a informação da nota de Compra. ***No sistema existem duas possibilidades para sua geração***:

     1- A nota de Compra gerar uma Remessa, gerando a nota de Vendas, preenchendo então os 'Documentos Relacionados'
     2- No item da nota de Venda, botão 'Outras Opções' > Documentos Relacionados, preencher manualmente o vínculo com a nota de Compra.(Passo 2, indicado acima).

**Verifique o parâmetro HABTAGDETEXPORT o mesmo deve estar ligado para gerar a TAG <detExport>**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16282321392407)

 CAUSA:**

Ocorre na NF-e de Exportação (mod. 55) quando o item tem**<****CFOP****> ****= ****[3503] **ou** [7501]**(grupo **<****infNFe****>**/**<****det****>**/**<****prod****>**, tag**<****CFOP****>**) e não é informado o grupo de controle para a exportação indireta (**<****prod****>**/**<****detExport****>**/**<****exportInd****>**). Ou o parâmetro HABTAGDETEXPORT está desligado.