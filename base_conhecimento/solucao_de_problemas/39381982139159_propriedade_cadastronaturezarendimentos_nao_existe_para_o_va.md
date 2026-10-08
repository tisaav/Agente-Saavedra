# Propriedade 'CadastroNaturezaRendimentos' não existe para o ValueObject  'Financeiro.ValueObject'

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39381982139159-Propriedade-CadastroNaturezaRendimentos-n%C3%A3o-existe-para-o-ValueObject-Financeiro-ValueObject](https://ajuda.sankhya.com.br/hc/pt-br/articles/39381982139159-Propriedade-CadastroNaturezaRendimentos-n%C3%A3o-existe-para-o-ValueObject-Financeiro-ValueObject)  
> **ID:** `39381982139159` | **Última Atualização:** 2026-07-22T13:32:47Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39381966301591)

 MENSAGEM**

Falha detectada

Propriedade 'CadastroNaturezaRendimentos' não existe para o ValueObject 
'Financeiro.ValueObject'

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39381982134679)

 SITUAÇÃO**

Ao tentar exportar dados da tela **"Movimentação Financeira"** (Financeiro > Rotinas > Movimentação Financeira) para uma planilha Excel (.xls), o sistema apresenta mensagens de erro e não permite a conclusão da exportação.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39381966302743)

 SOLUÇÃO**

 

**Solução: Ajuste as colunas apresentadas na grade**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39381966303383)

 Acesse a tela **"Movimentação Financeira"** (Financeiro > Rotinas > Movimentação Financeira).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39381966303895)

 Clique no ícone de configurações (engrenagem) e posteriormente clique em **"Configurar Grade".**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39381982135703)

 Em "Colunas Selecionadas" remova os campos **“Código Natureza Rendimento” e “Descrição Natureza Rendimento”** .

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41865136539927)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39381982137239)

 Realize novamente a exportação para Excel.
 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39381966304791)

 CAUSA**

Campos como **"Natureza de Rendimento"** **e “Descrição Natureza Rendimento”** são calculados dinamicamente e não podem ser exportados para Excel, pois não possuem vínculo com a tabela TGFFIN.