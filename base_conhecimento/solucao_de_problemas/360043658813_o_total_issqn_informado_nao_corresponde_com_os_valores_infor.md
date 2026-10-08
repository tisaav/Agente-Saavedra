# O total ISSQN informado não corresponde com os valores informados. Número do RPS em que ocorreu o erro: 124

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043658813-O-total-ISSQN-informado-n%C3%A3o-corresponde-com-os-valores-informados-N%C3%BAmero-do-RPS-em-que-ocorreu-o-erro-124](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043658813-O-total-ISSQN-informado-n%C3%A3o-corresponde-com-os-valores-informados-N%C3%BAmero-do-RPS-em-que-ocorreu-o-erro-124)  
> **ID:** `360043658813` | **Última Atualização:** 2026-07-22T16:04:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142170936599)

 MENSAGEM:**

L041: O total ISSQN informado não corresponde com os valores informados. Número do RPS em que ocorreu o erro: 124

Possível solução: Verifique se os valores informados estão corretos.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142173873559)

 SITUAÇÃO:**

Ao gerar lote de uma NFS-e é apresentada a mensagem de rejeição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142170940823)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142173883415)

 Acesse: Configurações » Cadastros » Endereços » Cidades

- Aba:** NFS-e**

- Campo "**Método de arredondamento do valor ISS":** ABNT NBR 5891

 

![cidades.png](https://ajuda.sankhya.com.br/hc/article_attachments/14634690249751)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142173884823)

 Após os ajustes, redigite os serviços na NFS-e e transmita novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142170947607)

 CAUSA:**

Ocorre quando o valor do ISS apresenta dízima cuja a terceira casa decimal era 5 (cinco). A prefeitura de Cuiabá, por exemplo, entende que deveria arredondar para baixo e o sistema Sankhya, segue o arredondamento convencional.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458165766935)

** EXEMPLO:**
Base ISS: 24,50
Alíquota ISS: 5%
Valor ISS: 1,23

Efetuando a multiplicação da Base do ISS com a Alíquota ISS apresenta a dizima de R$ 1,225

A prefeitura de Cuiabá entende que o valor é R$ 1,22 e apresenta o erro.

Exemplo de Arredondamento seguindo a Norma ABNT NBR 5891:

********

********

********

********

********

********

********

********

********

| VALOR | ABNT |
| --- | --- |
| 0,346 | 0,35 |
| 0,3452 | 0,35 |
| 0,3450 | 0,34 |
| 0,342 | 0,34 |
| 0,336 | 0,34 |
| 0,3352 | 0,34 |
| 0,3350 | 0,34 |
| 0,332 | 0,33 |
| 0,3050 | 0,30 |