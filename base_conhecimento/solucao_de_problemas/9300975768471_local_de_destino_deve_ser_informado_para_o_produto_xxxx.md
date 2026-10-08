# Local de Destino deve ser informado para o produto XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9300975768471-Local-de-Destino-deve-ser-informado-para-o-produto-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9300975768471-Local-de-Destino-deve-ser-informado-para-o-produto-XXXX)  
> **ID:** `9300975768471` | **Última Atualização:** 2026-07-22T15:08:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604459640343)

 MENSAGEM:**

[CORE_E00779] Local de Destino deve ser informado para o produto XXXX.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604459653271)

 SITUAÇÃO:**

Ao lançar uma nota ou processar o Arquivo XML na tela Portal de Importação de XML a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604499454999)

 CAUSA: **

Quando existirem itens configurados com controle de estoque por local, e esse local não foi informado no respectivo lançamento ou existir uma customização relacionada ao parâmetro **Módulos Java para regras da central -MODREGCENTRAL.**

**SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604499464727)

 Na tela **'Produtos'***(Configurações » Cadastros » Produtos)*verificar dentre os itens do lançamento realizado, quais possuem a marcação "Usa Local":

- Aba Medidas e Estoque >> Sub-Aba 'Estoque' >> Campo **'Usa Local'**:

![Produtos evidencia.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604459671831)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604499477911)

 Para os itens que possuem a marcação acima, o campo LOCAL da grade de itens deverá ser preenchido no lançamento realizado na respectiva 'Central':

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604499486231)

 Preenchido o campo acima, será possível salvar o lançamento.

Será necessário ainda verificar se existe alguma informação inserida no parâmetro **MODREGCENTRAL-Módulos Java para regras da central,** para consultar esse parâmetro é necessário acessar a tela **Preferências*** (Configurações » Avançado » Preferências), *caso tenha alguma informação nesse parâmetro significa que uma personalização está envolvida, sendo assim, é necessário solicitar o criador dessa personalização revise a mesma que está gerando o erro.

Temos ainda uma última situação onde essa mensagem será apresentada, que é:

- Analisar o XML da operação e verificar qual o CFOP informado, segue um exemplo: XML se trata de uma operação: "**CFOP 5907 - Retorno simbólico de mercadoria depositada em depósito fechado ou armazém geral**"

![xml evidencia.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604499492631)

NF de Origem, foi gerada por uma empresa, com isso o tipo de Movimento da TOP 706 está igual "**Transferência**" , e o sistema não possuí os dados de locais de Origem e Destino para definir nesse processo como está sendo tratado como uma possível "**Transferência**". 

 

![evidencia 27-10.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604459694487)

Na entrada dessa NF via portal de Importação de XML, deveria ser usado uma TOP do tipo de Movimento de Compras, pois dessa forma o sistema não tentará encontrar a NF de origem na mesma base e também não vai solicitar local Destino. **

Observação: **Quando é gerado uma Transferência, onde ambas empresas estão na mesma base, o sistema já trata essa questão dos locais e gera duas linha na TGFITE para o mesmo produto diferenciando movimentação de ENTRADA com SAIDA do estoque.