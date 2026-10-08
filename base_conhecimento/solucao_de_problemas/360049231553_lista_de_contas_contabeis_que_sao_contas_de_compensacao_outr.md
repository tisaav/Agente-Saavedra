# Lista de Contas Contábeis que são contas de 'Compensação', 'Outras' e 'Conta de  Encerramento de Resultado' possuem valor de saldo final

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231553-Lista-de-Contas-Cont%C3%A1beis-que-s%C3%A3o-contas-de-Compensa%C3%A7%C3%A3o-Outras-e-Conta-de-Encerramento-de-Resultado-possuem-valor-de-saldo-final](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231553-Lista-de-Contas-Cont%C3%A1beis-que-s%C3%A3o-contas-de-Compensa%C3%A7%C3%A3o-Outras-e-Conta-de-Encerramento-de-Resultado-possuem-valor-de-saldo-final)  
> **ID:** `360049231553` | **Última Atualização:** 2026-07-22T15:31:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612003419799)

 MENSAGEM**:

 Erro gerado no arquivo do repositório: Lista de Contas Contábeis que são contas de ’Compensação’, ‘Outras’ e ‘Conta de  Encerramento de Resultado‘ possuem valor de saldo final.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612003432855)

 CAUSA:**

No plano de contas, é vinculado em contas referenciais somente em contas passivo, ativo e PL.
No caso da encerramento classifica-se como 04 - contas de resultado.

Essa é uma validação que previne futuros erros no ECF que aceita contas apenas Patrimoniais(Ativo, passivo, PL) e não de resultado, ou seja, no plano de contas a conta de encerramento não deve ter conta referencial, vinculada.

 

**SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612003438231)

 Contabilidade » Preferências » Empresa:

- Aba: Plano de Contas

- Identifique no campo '**Conta Contábil de Encerramento de Resultado**' o Código.**
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18611995662615)

 Contabilidade » Cadastros » Plano de Contas:

- Selecione a respectiva empresa do Plano de Contas e com o código anterior, pesquise pela Conta Contábil de Apuração de Resultado.

- Verifique na **aba**: **Conta Contábil Referencial**, se existe algum Cod. de Conta Referencial, se houver solicite a Exclusão.

- Verifique na **aba: Geral, se o campo Grupo de Conta:** = 4-Contas de Resultado, se não estiver deverá ajustar para este.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612003457303)

 Após os ajustes, efetuar a geração novamente do arquivo em ***Contabilidade » Conexão » ECD » Geração de Arquivo - ECD;***