# Nota NFC-e possui CFOPs inválidos. Os CFOPs válidos são (5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933)

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697853-Nota-NFC-e-possui-CFOPs-inv%C3%A1lidos-Os-CFOPs-v%C3%A1lidos-s%C3%A3o-5101-5102-5115-5401-5403-5405-5656-5933](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697853-Nota-NFC-e-possui-CFOPs-inv%C3%A1lidos-Os-CFOPs-v%C3%A1lidos-s%C3%A3o-5101-5102-5115-5401-5403-5405-5656-5933)  
> **ID:** `360043697853` | **Última Atualização:** 2026-07-22T16:02:42Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163328536343)

 MENSAGEM:**

[CORE_E02526] Nota NFC-e possui CFOPs inválidos os cfops validos são 5101 5102 5103 5104 5115 5405 5456 5667 5933 

[CORE_E02536] Nota NFC-e possui CFOPs inválidos. Os CFOPs válidos são (5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163328539671)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163328553495)

 Caso trate-se de "entrada" de uma nota, a inclusão de um documento com Modelo 65 não será aceita:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343247895)

 O modelo 65 - Nota Fiscal Eletrônica de Venda a Consumidor é **específico e exclusivo para saída de mercadoria para uso e consumo**. Esse modelo não é contemplado para escrituração da entrada na nota fiscal destinada a uso e consumo. O sistema validará qualquer inclusão a partir do lançamento no qual será informado o modelo, mesmo marcando a opção para não atualizar Livro Fiscal.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343247895)

 Para que o sistema confirme o lançamento desse documento deverá ser o modelo 01 ou 55 para obtê-lo em seu Controle Gerencial. Sugerimos que seja solicitado ao fornecedor uma nota fiscal eletrônica (modelo 55).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343248279)

 Para notas de saída, atente-se primeiramente na utilização de um parceiro com endereço com a mesma UF (Estado) da Empresa Emitente. 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343247895)

 Em Operações acobertadas por NFC-e, é **permitido apenas que sejam Estaduais** (idDest = 1). Para Operações Interestaduais ou com o Exterior, opte pela emissão de uma NF-e (modelo 55). Para corrigir a NFC-e, deve-se informar a Operação como Estadual. 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343250199)

 Caso não trate-se de uma operação Estadual, sintonize com o contador e avalie a possibilidade de emissão de uma NF-e (Modelo 55).

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343265943)

 Se tratar-se de uma NFC-e, certifique-se que as configurações de CFOP foram realizadas corretamente:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343247895)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba:** "Livro Fiscal"**, campo** "CFOP's para Dentro do Estado": **CFOP'S iniciadas com 5.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14707160938647)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163328568599)

 Se necessário ajustes na TOP, inutilize a NFC-e rejeitada e proceda com uma nova emissão.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163343273623)

 CAUSA:**

Ao emitir e/ou lançar no sistema notas fiscal com modelo do documento 65 a mensagem poderá ser apresentada se o CFOP utilizado for diferente de: 5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933.