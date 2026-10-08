# Nome de coluna 'VITEM_IBSCBS' inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35163699510679-Nome-de-coluna-VITEM-IBSCBS-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/35163699510679-Nome-de-coluna-VITEM-IBSCBS-inv%C3%A1lido)  
> **ID:** `35163699510679` | **Última Atualização:** 2026-07-22T14:25:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163699483799)

 **MENSAGEM:**

Nome de coluna 'VITEM_IBSCBS' inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163699484567)

 **SITUAÇÃO:**

O erro é apresentado ao abrir os **Portais de Vendas**, **Portal de Compras**, **Portal de Importação XML** ou outras rotinas que utilizam a tabela **TGFITE**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163677384343)

SOLUÇÃO:**

Para correção, **é necessário atualizar o módulo ****Livros Fiscais** para a versão **5.16.2** ou superior (caso já esteja disponível uma versão mais recente).

**O processo de atualização deve ser realizado da seguinte forma:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163938763543)

  Solicite que** todos os usuários do sistema encerrem sua sessão;**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163916714519)

 Acesse a **"Administração do Servidor"** e selecione a opção **"Atualização do Sistema" **para abrir o WPM.

 

![Nome de coluna 'VITEM_IBSCBS' inválido..png](https://ajuda.sankhya.com.br/hc/article_attachments/35163916715159)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163916715671)

  No **WPM**, acesse a aba **"Atualização de Módulos"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163916717719)

  Selecione a versão **5.16.2** (ou superior) do módulo **Livros Fiscais**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163916718487)

  **Concluída a atualização, o problema estará corrigido.**

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163938770199)

 Observação:** **se o ambiente estiver hospedado em nuvem, a atualização deve ser solicitada à nuvem. Em caso de ambiente local, o processo deve ser conduzido pelo setor de TI da empresa.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35163677388183)

CAUSA:**

Erro de criação de script na versão anterior do modulo.