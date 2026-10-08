# E0354 Rejeição: O preenchimento dos campos nDI (Número da Declaração de Importação) ou do nRE (Número do Registro de Exportação) não é permitido quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 1.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224609898903-E0354-Rejei%C3%A7%C3%A3o-O-preenchimento-dos-campos-nDI-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-ou-do-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitido-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-1](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224609898903-E0354-Rejei%C3%A7%C3%A3o-O-preenchimento-dos-campos-nDI-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-ou-do-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitido-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-1)  
> **ID:** `37224609898903` | **Última Atualização:** 2026-07-22T14:16:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224625739415)

 **MENSAGEM**

E0354 Rejeição: O preenchimento dos campos nDI (Número da Declaração de Importação) ou do nRE (Número do Registro de Exportação) não é permitido quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 1.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609887767)

 **SITUAÇÃO**

Ao tentar processar uma Nota Fiscal Eletrônica (NF-e), o sistema apresenta a rejeição informando que **não é permitido preencher os campos de Declaração de Importação ou Registro de Exportação** quando a operação está vinculada à **movimentação temporária de bens**. O usuário estava emitindo uma nota fiscal com informações de importação ou exportação e, simultaneamente, indicou que a operação se refere a uma **movimentação temporária**, o que gera incompatibilidade nas informações fiscais.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224625741207)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609888919)

 Acesse o **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) ou o **"Portal de Compras"** (Comercial » Consulta » Portal de Compras), conforme o tipo de operação da nota fiscal que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609890199)

 Pesquise e acesse a nota fiscal que está apresentando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224625742359)

 Verifique se o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** está preenchido com o valor **"1 - Sim"**. Este campo indica que a operação se refere a uma movimentação temporária de mercadorias.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38323493393175)

 Identifique qual informação está incorreta na nota fiscal:

- 

Se a operação **não é uma movimentação temporária**, altere o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** para **"0 - Não"** ou deixe-o em branco.

- 

Se a operação **é realmente uma movimentação temporária**, remova as informações de **Declaração de Importação** ou **Registro de Exportação** dos itens da nota fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609892759)

 Para remover as informações de importação ou exportação, acesse os itens da nota e clique em **"Outras Opções"**:

- 

Selecione **"Declaração de Importação e Adições"** e remova os dados preenchidos no campo **"Número da Declaração de Importação (nDI)"**.

- 

Ou selecione **"Documentos Relacionados"** e remova as informações do campo **"Número do Registro de Exportação (nRE)"**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224625745559)

 Salve as alterações realizadas no cabeçalho e nos itens da nota fiscal.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609894039)

 Gere um novo lote da nota fiscal ou busque autorização novamente, conforme o status atual da NF-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224609895319)

 **CAUSA**

A rejeição ocorre quando a nota fiscal contém **informações de Declaração de Importação (nDI) ou Registro de Exportação (nRE)** e, ao mesmo tempo, o campo **"Vínculo da Operação à Movimentação Temporária de Bens (movTempBens)"** está preenchido com o valor **"1 - Sim"**. Segundo as regras de validação da SEFAZ, **operações de movimentação temporária de bens não podem conter informações de importação ou exportação**, pois são naturezas de operação distintas e incompatíveis entre si. A movimentação temporária refere-se ao envio ou recebimento de mercadorias que retornarão ao remetente, enquanto importação e exportação envolvem operações definitivas de entrada ou saída de mercadorias do país.