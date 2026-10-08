# Escritório de Contabilidade não cadastrado na SEFAZ. (NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101993-Escrit%C3%B3rio-de-Contabilidade-n%C3%A3o-cadastrado-na-SEFAZ-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101993-Escrit%C3%B3rio-de-Contabilidade-n%C3%A3o-cadastrado-na-SEFAZ-NT2015-002)  
> **ID:** `360043101993` | **Última Atualização:** 2026-07-22T16:08:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085762464023)

 MENSAGEM:**

487 - Rejeição: Escritório de Contabilidade não cadastrado na SEFAZ. (NT2015/002).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085778862615)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085762466839)

 Acesse: Comercial » Preferências » Empresa

- Selecione a mesma empresa emitente da NF-e, acesse a aba:** "Contador"**.
Verifique as informações cadastradas nesta aba:

1. Se estiver determinado um parceiro no campo "**Cód. Parceiro"**, acesse o cadastro de Parceiro *(Caminho de acesso: Configurações » Cadastros » Parceiros)* e verifique se os dados estão corretos e se os dados do Escritório de Contabilidade ou Contador estão cadastrados junto a SEFAZ.

 

![scrit_rio_de_Contabilidade_n_o_cadastrado_na_SEFAZ.png](https://ajuda.sankhya.com.br/hc/article_attachments/14555588588823)

 

Se não houver um código de parceiro vinculado:

- Confira os dados cadastrados nesta aba como: Nome Contador, CPF, CRC e etc.

- A marcação: Enviar responsável contábil na NFE?:, gerará no XML a tag <autXML> e filhas <CNPJ> ou a tag <CPF>.

- Após os ajustes, gere lote da NF-e novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085762468247)

 CAUSA:**

Quando for emitida uma NF-e e o CNPJ ou CPF do Escritório de Contabilidade, informado no Grupo de Autorização para obter o XML não estiver cadastrado na Sefaz, conforme a legislação estadual vigente, será retornada a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085762471831)

 Observação:**

1-(**NT2015/002**)

Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)