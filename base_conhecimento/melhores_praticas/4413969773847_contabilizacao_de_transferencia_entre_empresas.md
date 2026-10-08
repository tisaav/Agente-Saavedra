# Contabilização de Transferência entre empresas

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4413969773847-Contabiliza%C3%A7%C3%A3o-de-Transfer%C3%AAncia-entre-empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413969773847-Contabiliza%C3%A7%C3%A3o-de-Transfer%C3%AAncia-entre-empresas)  
> **ID:** `4413969773847` | **Última Atualização:** 2026-07-22T15:20:34Z

---

Pelo fato de existirem movimentos de saída para uma empresa e entrada para outra, as fórmulas de contabilização devem considerar os movimentos dos livros fiscais, ou seja: as notas devem ser sempre escrituradas nos livros. Antes de iniciar o passo a passo, a configuração de um determinado parâmetro deve ser observado.

Entre na tela preferências (Configurações » Avançado » Preferências) e habilite o  parâmetro **CTBZLIVFILMVLIV. **

 

![Contabilização de Transferência entre empresas 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16202735040151)

 

********

| CTBZLIVFILMVLIV= Para mudar a instância do filtro da contabilização por Livro Fiscal de "Cabeçalho/Nota" para "Movimento Livro Fiscal", o parâmetro "Filtrar contabilização do livro pela TGFLIV? - CTBZLIVFILMVLIV"= deve estar habilitado. Ao ativar o parâmetro, os filtros já existentes para a contabilização por Livro Fiscal com a instância Cabeçalho/Nota deverão ser recriados. |
| --- |

 

Após a configuração do parâmetro, siga os passos abaixo para a contabilização de transferência entre empresas. 

1. Entre na tela Contabilização>> Arquivos>>** TOP Contabilização:**

 

![Contabilização de Transferência entre empresas 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16202704300183)

 

****

****

| Abaixo seguem as fórmulas de  uma forma mais detalhada caso seja necessário realizar a cópia.  EMPRESA DE ORIGEM:  D- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRICMS,0) C- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRICMS,0) > CONTA TRANSITORIA X   D- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRIPI,0) C- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRIPI,0) > CONTA TRANSITORIA Y   D- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.ICMSRETENCAO,0) C- IF(quelote.CODEMP = PDES('CODEMP','TGFCAB','NUNOTA='+NUNOTA),Formula.ICMSRETENCAO,0) > CONTA TRANSITORIA Z   EMPRESA DE DESTINO:  C- IF(quelote.CODEMP = PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRICMS,0) D- IF(quelote.CODEMP = PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRICMS,0) > CONTA TRANSITORIA X   C- IF(quelote.CODEMP = PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRIPI,0) D- IF(quelote.CODEMP = PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.LIVVLRIPI,0) > CONTA TRANSITORIA Y   C- IF(quelote.CODEMP = PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.ICMSRETENCAO,0) D- IF(quelote.CODEMP =PDES('CODEMPNEGOC','TGFCAB','NUNOTA='+NUNOTA),Formula.ICMSRETENCAO,0)  > CONTA TRANSITORIA Z |
| --- |

 

2. Configuradas as fórmulas, é hora de contabilizar! Vamos utilizar a seguinte nota como exemplo para melhor entendimento, no qual a transferência ocorre da empresa 25 para a empresa 1:

 

![Contabilização de Transferência entre empresas 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16202704302103)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451026129431)

 Gerar a nota nos livros fiscais conforme já explicado anteriormente **

Menu **Contabilização> Rotinas>Agendamento**

Faça dois agendamentos, um para a empresa de origem e outro para a empresa de destino. Tomando este exemplo, foi configurado os agendamentos 20 e 21 para as empresas de origem e destino respectivamente.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451026129431)

 Primeiro contabiliza a saída da empresa 25: **

Exemplo de filtro:

MovimentoLivroFiscal.DHMOV >= ?:{entidade=MovimentoLivroFiscal;campo=DHMOV} AND

MovimentoLivroFiscal.DHMOV<= ?:{entidade=MovimentoLivroFiscal;campo=DHMOV} AND

MovimentoLivroFiscal.CODEMP= ?:{entidade=MovimentoLivroFiscal;campo=CODEMP} AND

MovimentoLivroFiscal.NUNOTA= ?:{entidade=MovimentoLivroFiscal;campo=NUNOTA}

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4413969716247)

 

MovimentoLivroFiscal.DHMOV = ${dia-a-dia} AND

MovimentoLivroFiscal.CODEMP = 25

Seguem os lançamentos contábeis que foram gerados para a saída na empresa 25:

 

**

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/12655205002647)

 **

 

#### **Contabilização da entrada na empresa 1: **

Mesmo filtro apenas substituindo o código da empresa, no agendamento também deve-se utilizar o código da empresa 1:

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4413969739415)

 

#### **Lançamentos contábeis da empresa 1**

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/12655239213079)