# Crédito de ICMS-ST de forma automática no Registro de Apuração do ICMS-ST com CFOP 1949

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24311196415639-Cr%C3%A9dito-de-ICMS-ST-de-forma-autom%C3%A1tica-no-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS-ST-com-CFOP-1949](https://ajuda.sankhya.com.br/hc/pt-br/articles/24311196415639-Cr%C3%A9dito-de-ICMS-ST-de-forma-autom%C3%A1tica-no-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS-ST-com-CFOP-1949)  
> **ID:** `24311196415639` | **Última Atualização:** 2026-07-22T14:47:03Z

---

O sistema olha para o CFOP 1949 para considerar créditos de ST no Registro de Apuração do ICMS-ST, em análise da query vimos as sequentes validações:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25170156900503)

 Na primeira condição, verifica-se o campo **"CODIGO CFOP"** da tela **"Cadastro Livro ICMS/IPI"** se contém um dos valores listados: 1203, 1204, 1410, 1411, 1414, 1415, 1603, 1660, 1661, 1662, 2203, 2204, 2410, 2411, 2414, 2415, 2603, 2660, 2661, 2662. Posteriormente, verifica-se em outra condição novamente o campo CODIGO CFOP da tela Cadastro Livro ICMS/IPI olhando para os valores: 1949 ou 2949. Se CODIGO CFOP for igual a qualquer um desses valores, a condição será verdadeira;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25170147985559)

 Verifica se o campo "**Origem" **da tabela LIV é igual a 'E';

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25170156906007)

 Verifica se existe pelo menos uma linha na tabela TGFCAB (cabeçalho da nota) em que o campo **"NUNOTA"** é igual ao campo NUNOTA da tabela LIV (tela "Cadastro Livro ICMS/IPI") e o campo **TIPMOV** (tipo de movimento) é igual a 'D' (devolução de venda). Se essa linha existir, a subcondição será verdadeira.

 

Sendo assim, para que o valor do crédito de ICMS/ST do CFOP 1949 seja considerado, o TIPMOV da operação deve ser igual a 'D-Devolução de venda'. Diferente disso não irá ser considerado na apuração como crédito de ST.