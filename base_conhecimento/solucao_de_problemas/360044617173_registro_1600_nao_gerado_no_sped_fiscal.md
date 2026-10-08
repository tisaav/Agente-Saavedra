# Registro 1600 não gerado no SPED FISCAL

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617173-Registro-1600-n%C3%A3o-gerado-no-SPED-FISCAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617173-Registro-1600-n%C3%A3o-gerado-no-SPED-FISCAL)  
> **ID:** `360044617173` | **Última Atualização:** 2026-07-22T15:53:18Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594936661271)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594894338711)

 Acesse a tela de **"Tipos de Título"** *(Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Título).*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594894341143)

 Localize os tipos de título utilizados nos lançamentos que não estão sendo enviados ao SPED.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594894343575)

 Na aba **"Fast Service"** verifique o campo **"Subtipo";**

- Configuração esperada: cartão de Débito ou Cartão de Crédito;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594894345879)

 Na **aba "Geral",** verifique o campo **"Parc.Administradora"**:

- Configuração esperada: informar o Parceiro Administradora do cartão;

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594936682903)

 Acesse a Tela **"Empresa"** **(Caminho de acesso: *Comercial » Preferências*), **aba **"EFD - Escrituração Fiscal Digital"** :

- Blocos e Registros:  Bloco 1 cadastrado / Gerar Registro: sim

- Registros: Registro 1600 / Gerar Bloco: sim

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15185613579287)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594936685079)

 Na tela de *Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI,* fique atento à marcação ***"Gerar registro 1600 pelo Resumo de Operações com Cartão?"***, pois quando ela estiver acionada o sistema utilizará os dados inseridos na tela** "Resumo de Operações com Cartão"** para tratar de forma manual as informações referentes ao Registro 1600 ao gerar o arquivo. Por outro lado,  desabilitada a marcação e gerando o arquivo, o sistema não utilizará os dados da tela Resumo de Operações com Cartão.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594894353431)

 OBSERVAÇÕES:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458057382167)

 É necessário que seja um financeiro de origem **estoque**.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458057382167)

 Tem que ser uma **receita** não renegociada ou um Financeiro/Receita renegociado, com nro de renegociação maior que 0, que tenha sido renegociada uma única vez.