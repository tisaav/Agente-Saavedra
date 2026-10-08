# Campo Obrigatório. 4- TIPO_MOV 'Tipo de Movimentação' - REGISTRO G125

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110654-Campo-Obrigat%C3%B3rio-4-TIPO-MOV-Tipo-de-Movimenta%C3%A7%C3%A3o-REGISTRO-G125](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110654-Campo-Obrigat%C3%B3rio-4-TIPO-MOV-Tipo-de-Movimenta%C3%A7%C3%A3o-REGISTRO-G125)  
> **ID:** `360044110654` | **Última Atualização:** 2026-07-22T15:53:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618813954071)

 MENSAGEM:**

Campo Obrigatório. 4- TIPO_MOV 'Tipo de Movimentação' - REGISTRO G125.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618794456983)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618813962135)

 Acesse a tela **"Tipo de Operação - TOP"**, localize o cód. TOP utilizado no respectivo lançamento.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458057432855)

 Aba Livros Fiscais » Campo **'Tipo de Mov. do Bem (SPED)'**: este campo indica o 'Tipo de Movimentação do Bem' para efeito de SPED, será o responsável por compor o campo 04 TIPO_MOV do registro G125.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14873352131735)

 

De acordo com orientações da Contabilidade, defina o campo com uma das opções abaixo:

- MC = Imobilização oriunda do Ativo Circulante;

- AT = Alienação ou Transferência;

- PE = Perecimento, Extravio ou Deterioração;

- OT = Outras Saídas do Imobilizado

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618813966999)

 IMPORTANTE: **o ajuste acima é histórico, dessa forma a configuração correta impedirá o erro para os próximos lançamentos. Para os lançamentos já impactados será necessário que os ajustes dessa referência sejam realizados diretamente no PVA.  Caso trate-se de um volume significativo, necessário ajustes via banco junto ao DBA da empresa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618794460823)

CAUSA:**

Mensagem apresentada quando o registro G125 é enviado sem informações do 'Tipo de Movimentação do Bem'.