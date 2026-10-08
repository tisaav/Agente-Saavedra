# E0356 Rejeição: O preenchimento do campo nRE (Número do Registro de Exportação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 3.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224606214423-E0356-Rejei%C3%A7%C3%A3o-O-preenchimento-do-campo-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-3](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224606214423-E0356-Rejei%C3%A7%C3%A3o-O-preenchimento-do-campo-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-3)  
> **ID:** `37224606214423` | **Última Atualização:** 2026-07-22T14:16:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606189975)

 **MENSAGEM**

E0356 Rejeição: O preenchimento do campo nRE (Número do Registro de Exportação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 3.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606190999)

 **SITUAÇÃO**

Ao emitir uma NF-e de exportação com **CFOP iniciado em 7000**, o usuário configurou o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** com o valor **"3 - Operação com fim específico de exportação"**, porém **não preencheu o campo "Número do Registro de Exportação" (nRE)** nas informações de exportação do item. Ao tentar gerar o lote da nota, o sistema retorna a rejeição E0356, pois a Sefaz exige que o número do Registro de Exportação seja informado quando a operação está vinculada à movimentação temporária com fim específico de exportação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606192407)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606193559)

 Acesse o ****["Portal de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606194455)

 Abra a nota e acesse os **itens** da NF-e.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606197143)

 Clique em **"Outras Opções'' **(ícone de três pontos), e selecione a opção ''**Documentos relacionados"** para vincular a nota de origem (nota de importação ou entrada) que contém as informações da Declaração de Importação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606198167)

 Pesquise pela **nota de origem** e vincule-a aos itens da nota de exportação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606199319)

 Verifique se o campo **"Número do Registro de Exportação" (nRE)** foi preenchido automaticamente. Caso não tenha sido preenchido, insira manualmente o número do Registro de Exportação correspondente à operação.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606200471)

 Certifique-se de que o campo **"Número do Ato Concessório de Drawback"** também esteja preenchido, caso aplicável à operação.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606201751)

 Acesse a tela ****[''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)(Configurações » Avançado » Preferências).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606205847)

 Busque pelo parâmetro **"HABTAGDETEXPORT"** e verifique se ele está habilitado.

- 

Este parâmetro é necessário para a geração correta do grupo de tags de exportação no XML da NF-e.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606209431)

 Salve as alterações.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37883390392599)

 Gere novamente o lote da NF-e ou busque autorização, conforme o status atual da nota. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224606210839)

 **CAUSA**

A rejeição ocorre quando uma NF-e de exportação possui o campo **"Vínculo da Operação à Movimentação Temporária de Bens" (movTempBens)** preenchido com o valor **"3 - Operação com fim específico de exportação"**, mas o campo **"Número do Registro de Exportação" (nRE)** não foi informado. Segundo as regras da Sefaz, quando a operação está vinculada à movimentação temporária com fim específico de exportação, o preenchimento do número do Registro de Exportação é obrigatório para validação do documento fiscal eletrônico.


---

### 🔗 Links e Referências Internas:

- ["Portal de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)