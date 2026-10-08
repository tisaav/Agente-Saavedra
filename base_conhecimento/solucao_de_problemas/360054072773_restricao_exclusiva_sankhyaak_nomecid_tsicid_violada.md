# Restrição exclusiva (SANKHYA.AK_NOMECID_TSICID) violada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360054072773-Restri%C3%A7%C3%A3o-exclusiva-SANKHYA-AK-NOMECID-TSICID-violada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360054072773-Restri%C3%A7%C3%A3o-exclusiva-SANKHYA-AK-NOMECID-TSICID-violada)  
> **ID:** `360054072773` | **Última Atualização:** 2026-07-22T15:28:42Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605743189527)

 MENSAGEM**:

[CORE_E04348] Erro ao obter dados do CEP: ORA-00001: restrição exclusiva (SANKHYA.AK_NOMECID_TSICID) violada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605733825431)

 CAUSA:**

Ocorre quando ao buscar pelo CEP o sistema encontra duas ou mais cidades com mesmo nome, caso exista, excluir deixando apenas um registro.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605733827607)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605733832215)

 Acesse do cadastro de **cidades ** (Configurações » Cadastros » Endereços » Cidades)
Pesquise pelo nome da Cidade, ao encontrar duas ou mais cidades com o mesmo nome, considere excluir e deixar apenas uma cidade.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605743214743)

 Caso esteja efetuando manutenção ou cadastro de um parceiro, repita a operação.