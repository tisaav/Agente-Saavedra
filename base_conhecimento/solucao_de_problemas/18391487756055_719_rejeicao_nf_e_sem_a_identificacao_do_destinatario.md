# 719 - Rejeição: NF-e sem a identificação do destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18391487756055-719-Rejei%C3%A7%C3%A3o-NF-e-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/18391487756055-719-Rejei%C3%A7%C3%A3o-NF-e-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio)  
> **ID:** `18391487756055` | **Última Atualização:** 2026-07-22T14:52:36Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18391460556695)

 **MENSAGEM:**

719 - Rejeição: NF-e sem a identificação do destinatário.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18391481521431)

CAUSA:**

Ao realizar a emissão de uma NF-e (mod. 55) sem a identificação do Destinatário (grupo **<dest>**, tags **<CNPJ>**, **<CPF>** ou **<idEstrangeiro>**), o órgão autorizador retorna a rejeição “719 – NF-e sem identificação do Destinatário”.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18391496278551)

SOLUÇÃO:**

Localize a nota rejeitada e acione no Botão "NF-e" a opção "Gerar XML da NF-e em arquivo para conferência", encontre no XML o grupo **<infNFe>**/**<dest>** que deve conter uma das opções de identificação (**<CNPJ>**, **<CPF>** ou **<idEstrangeiro>**). 

Se não tiver informação nessas Tags será apresentada a mensagem de erro e para corrigir é necessário popular o campo "Identificação de Estrangeiro" na aba identificação conforme as informações do seu fornecedor ou popular o campo "CNPJ" com "00000000000000" se não tiver nenhuma informação. 

 

![parceiro 19-10.png](https://ajuda.sankhya.com.br/hc/article_attachments/18399943730071)