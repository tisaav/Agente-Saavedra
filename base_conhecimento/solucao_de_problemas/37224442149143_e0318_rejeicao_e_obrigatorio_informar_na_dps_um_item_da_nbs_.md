# E0318 Rejeição: É obrigatório informar na DPS um item da NBS para casos de exportação de serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224442149143-E0318-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-na-DPS-um-item-da-NBS-para-casos-de-exporta%C3%A7%C3%A3o-de-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224442149143-E0318-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-na-DPS-um-item-da-NBS-para-casos-de-exporta%C3%A7%C3%A3o-de-servi%C3%A7o)  
> **ID:** `37224442149143` | **Última Atualização:** 2026-09-24T23:16:25Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/37224442136087)

**MENSAGEM**

E0318 Rejeição: É obrigatório informar na DPS um item da NBS para casos de exportação de serviço.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37224458858007)

**SITUAÇÃO**

A rejeição ocorre ao transmitir a Declaração de Prestação de Serviço (DPS) de uma operação de exportação de serviço, na NFS-e Padrão Nacional. O documento foi enviado sem o **código NBS** (Nomenclatura Brasileira de Serviços) no item, e isso bloqueia a emissão da nota e o faturamento.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37224458859799)

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37224442141463)

 Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos >> Serviços) e localize o serviço que está sendo exportado.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/37224458861335)

 Na aba **"Impostos"**, confira o campo **"Código NBS"**:

- 
**Campo vazio:** preencha com o código NBS do serviço prestado, conforme a tabela oficial da Nomenclatura Brasileira de Serviços.

- 
**Campo não aparece na tela:** clique na engrenagem da tela, pesquise por "NBS" e adicione o campo à aba "Impostos".

- 
**Código incorreto:** corrija conforme a tabela NBS vigente.
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224458862231)

 Ainda no cadastro do serviço, acesse a aba **"Configuração por Empresa"**. Se o **"Código NBS"** também estiver preenchido ali, remova-o e mantenha o código somente na aba **"Impostos"**.

**Importante:** o preenchimento nos dois lugares pode fazer o código ser enviado com os últimos dígitos cortados, e a SEFAZ o considera inválido.

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/37224442143639)

Acesse a tela **"Cidades"** (Comercial >> Arquivo >> Cadastros >> Cidades) e localize a cidade do emitente. Na aba **"NFS-e"**, marque a opção **"Enviar o Código NBS no JSON"** e salve.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/37224458864535)

 Acesse o **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) e localize a nota rejeitada.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/37224442144663)

 Abra a nota e redigite o item: apague a quantidade e informe-a novamente. Assim a nota passa a usar os dados atualizados do cadastro.
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/43746384622871)

 Gere novamente o lote de envio e transmita o documento.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37224458866199)

**CAUSA**

A rejeição vem de uma validação da NFS-e Padrão Nacional: em operações de exportação de serviço, a DPS precisa informar o código NBS do serviço prestado. As principais causas são:

- O campo "Código NBS" está vazio ou incorreto no cadastro do serviço.

- O código está duplicado entre as abas "Impostos" e "Configuração por Empresa", o que corta os dígitos no envio.

- A opção "Enviar o Código NBS no JSON" está desmarcada no cadastro da cidade.

- A nota foi lançada antes da correção do cadastro e não foi atualizada.