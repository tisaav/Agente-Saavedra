# ORA-20101: Não existe saldo, na tabela de saldos por empresa

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33251552944023-ORA-20101-N%C3%A3o-existe-saldo-na-tabela-de-saldos-por-empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/33251552944023-ORA-20101-N%C3%A3o-existe-saldo-na-tabela-de-saldos-por-empresa)  
> **ID:** `33251552944023` | **Última Atualização:** 2026-07-22T14:29:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33251506123031)

**MENSAGEM**

ORA-20101: Não existe saldo, na tabela de saldos para esta conta.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33251506123415)

**SITUAÇÃO**

Este erro ocorre em diferentes situações relacionadas à **gestão contábil e financeira** do sistema:

- 

Ao tentar **alterar ou excluir lançamentos contábeis** na tela **"Lançamentos Contábeis"** (Contabilidade >> Lançamentos >> Lançamentos Contábeis)
 

1. 

Ao tentar excluir lotes na tela **"Lotes Contábeis"** (Contabilidade >> Lançamentos >> Lotes Contábeis), principalmente em lotes gerados automaticamente
 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33251506125975)

**SOLUÇÃO**

### **Solução 1: Recomposição de Saldos Contábeis**

Quando o erro ocorre em **lançamentos contábeis**, lotes ou balancetes, execute a recomposição de saldos:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33251552935191)

 Acesse a tela **"Empresa"** (Contabilidade >> Preferências >> Empresa).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33251506127639)

 No campo **"Referência p/ recomposição"**, informe a data do último mês correto. Exemplo: se janeiro está correto e fevereiro apresenta erro, informe 28/02/2025.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33251552936343)

Clique no botão **"Outras Opções (...)"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33251506129559)

 Selecione a opção **"Recompor Saldos"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40608882700183)

 Confirme a operação e aguarde o processamento.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40608882701079)

 Após a conclusão, verifique se o problema foi resolvido gerando novamente o **"Balancete de Verificação"**.
 

 

### **Solução 2: Verificação do Parâmetro CTBUTISALEMPORG**

Se o erro persistir, verifique o parâmetro **"Utiliza Saldo Empresa Origem"** (**"CTBUTISALEMPORG"**) em **"Parâmetros do Sistema"** (Configurações >> Avançado >> Preferências). Para o processo padrão, este parâmetro deve permanecer desabilitado.

Onde na tela de preferências da empresa do contábil, pode ser realizado o mesmo processo de recomposição de saldos:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40608856984983)

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33251552933783)

**CAUSA**

Este erro indica que o sistema não localizou um saldo registrado para a conta, empresa e data informadas na tabela de saldos. Isso é necessário para garantir a integridade das informações contábeis durante exclusões ou novos lançamentos.

- 

**Ausência de saldo implantado:** A conta não possui saldo inicial para o período.
 

1. 

**Inconsistência nos saldos acumulados:** Desatualização devido a alterações manuais em lançamentos.
 

1. 

**Data de movimentação anterior à implantação:** A operação tenta afetar um período sem controle de saldo.
 

1. 

**Configuração de parâmetro:"CTBUTISALEMPORG"** habilitado indevidamente.