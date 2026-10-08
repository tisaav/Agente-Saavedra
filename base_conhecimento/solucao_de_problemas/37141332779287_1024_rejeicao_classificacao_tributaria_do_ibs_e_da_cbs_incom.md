# 1024 Rejeição: Classificação Tributária do IBS e da CBS incompatível com o CST informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141332779287-1024-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-incompat%C3%ADvel-com-o-CST-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141332779287-1024-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-incompat%C3%ADvel-com-o-CST-informado-nItem-999)  
> **ID:** `37141332779287` | **Última Atualização:** 2026-07-28T10:28:18Z

---

[1023] Rejeição: Classificação Tributária do IBS/CBS informada inexistente [nItem: 999]

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37141332757015)

 SITUAÇÃO

Ao emitir uma NF-e ou NFC-e, o sistema retorna uma rejeição relacionada às informações de tributação do IBS e da CBS informadas no item da nota fiscal. Especificamente, ao tentar emitir com operação de **"Diferimento do ICMS (CST 410)"**, o sistema apresenta o erro de que a **"Classificação Tributária (cClassTrib: 510002)"** é inexistente ou incompatível, gerando falhas adicionais no cálculo de dedução da base de cálculo.

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37141324792471)

 SOLUÇÃO

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37141324793239)

 Acesse as telas **"Alíquotas de IBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) e **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de CBS). Para casos específicos como o **"CST 410"**, consulte a planilha oficial de classificação tributária do IBS/CBS no Portal da NF-e; o código correto a ser utilizado nestes casos é o **"515001"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/37141332759319)

 Verifique o campo **"Código da Situação Tributária"** configurado para o item. Lembre-se que o sistema permite o uso de tabelas específicas (TLFCSTIC, TLFCstIbsCbsMono, TLFCstIbsCbsMonoReg) dependendo do regime tributário.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/37141324794647)

 Verifique também o campo **"Código de Classificação Tributária"**. O sistema gerencia essas classificações através das tabelas TLFCLASTRIBIC, TLFClassTribIbsCbsMono e TLFClassTribIbsCbsMonoReg.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/37141332761879)

 Consulte a tabela de compatibilidade para identificar a combinação correta. Considere que para um mesmo NCM é possível ter múltiplas configurações dependendo do tipo de documento ou regime.

- Cada **"CST"** só pode ser utilizado com determinadas classificações tributárias, conforme regras da Lei Complementar nº 214/2025.

- Para operações de **"Diferimento (CST 410)"**, ajuste o campo **"Classificação Tributária do IBS/CBS (cClassTrib)"** para o código **"515001"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/37141324795927)

 Salve as alterações realizadas na parametrização.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/41262218306583)

 Retorne à emissão da **"Nota Fiscal Eletrônica"** (Comercial >> Movimentação >> Central de Vendas) e tente transmiti-la novamente.

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37141332775319)

 CAUSA

Esta rejeição ocorre devido às regras de validação **"UB14-10"** e **"UB14-20"** da Sefaz, que verificam a existência do código informado nas tabelas oficiais e a compatibilidade entre o **"CST"** do IBS/CBS e a classificação tributária informada. A Reforma Tributária (LC 214/2025) impõe regras rígidas, sendo que o código **"510002"** é considerado inexistente ou incompatível para operações com **"CST 410"**, sendo obrigatória a utilização do código **"515001"**.

A incompatibilidade também pode ocorrer por outros motivos, como:

- Utilização de uma classificação tributária que não se aplica ao tipo de operação indicada pelo **"CST"**;

- Configuração incorreta das alíquotas (PALIQCBSREG, PALIQIBSMUNREG, etc.) no cadastro do sistema;

- Seleção de uma classificação tributária que não está prevista na legislação para o **"CST"** específico.