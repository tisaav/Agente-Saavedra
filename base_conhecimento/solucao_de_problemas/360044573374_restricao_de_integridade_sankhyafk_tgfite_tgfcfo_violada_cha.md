# Restrição de integridade (SANKHYA.FK_TGFITE_TGFCFO) violada - chave mãe não localizada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573374-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFITE-TGFCFO-violada-chave-m%C3%A3e-n%C3%A3o-localizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573374-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFITE-TGFCFO-violada-chave-m%C3%A3e-n%C3%A3o-localizada)  
> **ID:** `360044573374` | **Última Atualização:** 2026-07-22T15:51:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664315980823)

 MENSAGEM:**

'ORA-02291: restrição de integridade (SANKHYA.FK_TGFITE_TGFCFO) violada - chave mãe não localizada'.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664315987863)

 SITUAÇÃO:**

Ao tentar faturar uma nota de Compra/Venda, ou na confirmação, apresenta a mensagem de erro, no Sankhya OM.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664315994519)

 CAUSA:**

Este erro ocorre quando o sistema tenta efetuar o cálculo de CFOP, e o CFOP calculada não existe no sistema.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664315998103)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664316012695)

 Ative o monitor de consultas, através da rotina:Configurações » Avançado » Monitor de Consultas

- Clique no botão: (Start) -Para iniciar o monitoramento

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664347599639)

 Volte na Central de Nota, e simule a Confirmação/Faturamento da nota.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664316026903)

 Assim que ocorrer o erro, volte na rotina 'Monitor de Consultas' e clique no botão (Stop).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664316028951)

 Baixe o Arquivo de Log. Abra o arquivo em um Bloco de Notas ou '[Notepad++](https://notepad-plus-plus.org/)'.

No último trecho do Log, irá apresentar a palavra 'ERRO..' indicando o trecho que o sistema apresentou o erro.
**Exemplo:**
======================================
ERRO: UPDATE TGFITE SET **CODCFO = ?**,DTALTER = ? WHERE TGFITE.NUNOTA = ? AND TGFITE.SEQUENCIA = ?
Params:
1 = **1551**
2 = 2014-05-26 09:55:09.0
3 = 96
4 = 1
======================================

Neste exemplo, de acordo com a Natureza da Operação, o calculo da CFOP foi 1551 e esta CFOP não está devidamente cadastrada no sistema.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664347611031)

 Para cadastro acesse: *Comercial » Arquivo » Cadastros » CFOP*

- Preencha corretamente todos os dados sobre a CFOP, salve o cadastro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664316038551)

 Acesse novamente a Nota e volte a Faturar/Confirmar.