# O registro pai não pode ser analítico

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6426276337687-O-registro-pai-n%C3%A3o-pode-ser-anal%C3%ADtico](https://ajuda.sankhya.com.br/hc/pt-br/articles/6426276337687-O-registro-pai-n%C3%A3o-pode-ser-anal%C3%ADtico)  
> **ID:** `6426276337687` | **Última Atualização:** 2026-07-22T15:16:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461286722071)

  MENSAGEM: **

[CORE_E04993] O registro pai não pode ser analítico.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461286723991)

 CAUSA: **

O erro ocorre quando tenta-se cadastrar uma nova natureza (Registro pai) como analítica. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16461286727703)

 SOLUÇÃO **

Foi verificado que nessa determinada situação, estava sendo cadastrado um registro filho com uma matriz diferente do registro pai. Para entender na prática, no exemplo em questão, estava sendo cadastrada uma natureza nova, porém, essa natureza  seria um **registro pai,** ou seja, cadastraria novas ramificações para esta mesma natureza, de tal modo, ela não pode ser analítica, apenas os registros filhos podem ser analíticos.