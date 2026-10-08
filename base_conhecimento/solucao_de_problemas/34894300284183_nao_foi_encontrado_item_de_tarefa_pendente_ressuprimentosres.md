# Não foi encontrado item de tarefa pendente (Ressuprimentos/Restrições)

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34894300284183-N%C3%A3o-foi-encontrado-item-de-tarefa-pendente-Ressuprimentos-Restri%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/34894300284183-N%C3%A3o-foi-encontrado-item-de-tarefa-pendente-Ressuprimentos-Restri%C3%A7%C3%B5es)  
> **ID:** `34894300284183` | **Última Atualização:** 2026-07-22T14:26:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894300273303)

 **MENSAGEM**

Não foi encontrado item de tarefa pendente: Possíveis causas: Ressuprimentos pendentes. Restrições de usuários/equipamento. Agrupamento de pedido em sep. convencional.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445690111255)

 **SITUAÇÃO**

A mensagem aparece quando o usuário tenta **iniciar uma separação** no sistema WMS, mas não consegue prosseguir devido a **dependências pendentes**, **restrições de configuração** ou **incompatibilidades entre equipamento e endereços**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894300273943)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445705276311)

 Acesse a tela **"Gerência do WMS"** (WMS » Gerência » Gerência do WMS), filtre a separação que será iniciada e verifique em **"Itens da Tarefa"** o campo **"Depende de outras"**. Se estiver marcado como **"Sim (Pendente)"**, clique no botão **"Dependentes"** para identificar a tarefa dependente. Caso seja reabastecimento, realize o reabastecimento antes de iniciar a separação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445705278999)

 Acesse a tela **"Tipos de Equipamento"** (WMS » Cadastros » Tipos de Equipamento), identifique o equipamento utilizado e valide o **nível mínimo**, **nível máximo**, **tarefas permitidas** e **unidades permitidas** para o equipamento.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445690119191)

 Acesse a tela **"Endereço de Armazenamento"** (WMS » Cadastros » Endereço de Armazenamento), filtre o endereço de origem e destino e valide o nível do endereço na aba **"Medidas"**, campo **"Nível"**. O nível do equipamento deve estar dentro do nível do endereço de origem e destino.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445705283351)

 Acesse a tela **"Configurações por Usuário"** (WMS » Rotinas » Configurações por Usuário), filtre o usuário executante e valide as **unidades permitidas** e **tarefas permitidas** para o usuário.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445705285783)

 Acesse a tela **"Área de Separação"** (WMS » Cadastros » Área de Separação), filtre a área de separação da tarefa e verifique se o usuário separador está cadastrado dentro da área de separação na aba **"Separadores"**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894304431639)

 **CAUSA**

A mensagem ocorre quando existe um **ressuprimento pendente**, **restrição de usuário ou equipamento**, ou **falta de configuração** para o separador no sistema WMS.