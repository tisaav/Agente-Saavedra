# Nota que participa de pacote de remessa tem que ser cancelada, não pode ser excluída

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24309550455575-Nota-que-participa-de-pacote-de-remessa-tem-que-ser-cancelada-n%C3%A3o-pode-ser-exclu%C3%ADda](https://ajuda.sankhya.com.br/hc/pt-br/articles/24309550455575-Nota-que-participa-de-pacote-de-remessa-tem-que-ser-cancelada-n%C3%A3o-pode-ser-exclu%C3%ADda)  
> **ID:** `24309550455575` | **Última Atualização:** 2026-07-22T14:47:04Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24309550446487)

 **MENSAGEM: **

[CORE_E04192] Nota que participa de pacote de remessa tem que ser cancelada, não pode ser excluída

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24309541552151)

 **SOLUÇÃO:**

Não é permitido **"Cancelar"** diretamente a Nota de Remessa. Para isso, é **preciso primeiro cancelar/excluir a Nota/pedido de Venda ou Compra (Nota Principal) que gerou a Remessa e, então, serão canceladas as duas notas: a Nota Principal e também a de Remessa.** As Notas de Remessa são identificadas pelo campo "Número Remessa" (NUREM) preenchido no Cabeçalho da Nota (TGFCAB). A Nota Principal, que é a que poderá ser excluída/cancelada, é reconhecida pelo campo Tipo de operação remessa no cadastro da top.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24309550454167)

 **CAUSA: **

O erro é apresentado ao tentar excluir/cancelar uma nota de remessa que tenha o campo NUREM da tgfcab preenchido.