# Esta nota participa de um frete para múltiplas notas, portanto o financeiro referente a esse frete deve ser excluído antes de excluirmos a nota

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9135504383255-Esta-nota-participa-de-um-frete-para-m%C3%BAltiplas-notas-portanto-o-financeiro-referente-a-esse-frete-deve-ser-exclu%C3%ADdo-antes-de-excluirmos-a-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/9135504383255-Esta-nota-participa-de-um-frete-para-m%C3%BAltiplas-notas-portanto-o-financeiro-referente-a-esse-frete-deve-ser-exclu%C3%ADdo-antes-de-excluirmos-a-nota)  
> **ID:** `9135504383255` | **Última Atualização:** 2026-07-22T15:10:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604991581847)

 MENSAGEM:**

[CORE_E00895] Esta nota participa de um frete para múltiplas notas, portanto o financeiro referente a esse frete deve ser excluído antes de excluirmos a nota.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604977553559)

 SITUAÇÃO:**

Ao tentar excluir pedido de venda a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604991596055)

 CAUSA: **

Tentar excluir um pedido e/ou nota que possui frete.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18604991597847)

 SOLUÇÃO:**

Para conseguir excluir a nota é necessário antes desvincular o financeiro do frete, para isso é necessário identificar qual o financeiro de frete através do SELECT que deverá ser consultado na tela DBEXPLORER "SELECT * FROM TGFFNF WHERE NUNOTA = XXXX"

Na movimentação financeira botão **Outras opções**->**Vincular**/**Desvincular ****financeiro de frete à nota. **

Para maiores informações sobre esse campo acesse o link abaixo:

[Movimentação Financeira - Botão Outras Opções – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira - Botão Outras Opções – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)