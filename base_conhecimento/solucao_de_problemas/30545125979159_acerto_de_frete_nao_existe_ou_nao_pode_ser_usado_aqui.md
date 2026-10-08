# Acerto de Frete não existe ou não pode ser usado aqui

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30545125979159-Acerto-de-Frete-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/30545125979159-Acerto-de-Frete-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui)  
> **ID:** `30545125979159` | **Última Atualização:** 2026-07-22T14:35:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30545128990999)

 **MENSAGEM:**

Acerto de Frete não existe ou não pode ser usado aqui.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30545125973527)

SOLUÇÃO:**

Execute um **SELECT** no **DBExplorer** *(Caminho: Configurações » Avançado » DBExplorer),* na tabela **TGFFRE**, utilizando os campos **NUACERTO** (Número de compensação/acerto) ou **NUFIN** (Número único).

O número de acerto pode ser encontrado no campo "**Nro compensação/acerto**" da tela **"Movimentação Financeira"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30545125974423)

 

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/30590350606615)

 **Select a ser realizado:**

 

**SELECT * FROM TGFFRE WHERE NUACERTO = XX**
 

![Acerto de frete não existe ou não pode ser usado aqui 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30590851146263)

 
Identifique o campo **TIPACERTO** e valide em qual tela foi realizado o processo para seguir com a tratativa:
 

**A= **Adiantamento/empréstimo

**P= **Baixa Parcial

**C= **Compensação (tela compensação financeira)

**G= **Compensação Garantia

**F= **Pagamento de Frete/ Pagamento de Frete por OC

**L= **Acerto com fornecedores

**N=**Antecipação de baixa

**X=** Crédito a compensar (Baixa de movimentação financeira com valor superior ao da receita gerando crédito a compensar)

**D= **Desconto de Títulos / Devolução de Pagamento

**R= **Renegociação de Títulos

**V= **Compensar devolução
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30545125974935)

CAUSA:**
Ocorre quando se tenta localizar um **Nro de Acerto** em uma tela onde ele não foi criado.