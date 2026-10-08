# Esta TOP não pode ser lançada nesta opção

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697673-Esta-TOP-n%C3%A3o-pode-ser-lan%C3%A7ada-nesta-op%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697673-Esta-TOP-n%C3%A3o-pode-ser-lan%C3%A7ada-nesta-op%C3%A7%C3%A3o)  
> **ID:** `360043697673` | **Última Atualização:** 2026-07-22T16:02:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148826730007)

 MENSAGEM:**

ORA-20101: Esta TOP não pode ser lançada nesta opção.Nota de Nro Único: 
ORA-06512: em "SANKHYA.TRG_UPD_TGFCAB", line 945
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_UPD_TGFCAB'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148790664343)

 SITUAÇÃO:**

Ao tentar efetuar o lançamento, usando uma TOP de Destino, a seguinte mensagem é apresentada.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458156350871)

 CASO:**

Mensagem pode ser apresentada ao **"Consultar Situação Atual da Nota"** de uma NF-e com Status **Denegada** na SEFAZ e diferente desse no sistema.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148790668823)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148790670999)

 Verifique no cadastro de **"******[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**"** se existe uma **Top Denegada** para o mesmo Tipo de Movimento da nota analisada.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458156350871)

 EXEMPLO:** Mensagem ocorrendo para uma nota de **Devolução de Venda**, dessa forma é necessário uma Top Denegada com o tipo de movimento Devolução de Venda.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148790675479)

 Caso não exista, configure a mesma e/ou duplique uma atual (que tenha sido validada junto ao Consultor de sua Franquia), alterando apenas o Tipo de Movimento.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148826754967)

 Anote o código da Top Denegada criada e vincule a mesma na aba **"NF-e/NFC-e"** » Campo '**Tipo de Operação NF-e Denegada**' da TOP utilizada no lançamento que originou a mensagem. 

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148790683287)

 Realizado tais ajustes, refaça a Consulta situação atual da nota, dessa forma o Status deverá ser devidamente atualizado para Denegada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16148826766103)

 **CAUSA:**

Ocorre quando uma TOP de Destino não pode ser usado com o tipo de movimento adequado.

Observação: Essa validação pode ocorrer no portal de importação de xml,  a configuração do campo "Top para simulação de impostos" nas 'Preferências para importação de NF-e' influência diretamente na geração da nota de emissão própria. Caso a nota gerada não seja a configurada com a top  como emissão própria, analisar o campo 'Top para simulação de impostos'


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)