# Iniciar Web Connection junto com navegador se desmarcando

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30262095641623-Iniciar-Web-Connection-junto-com-navegador-se-desmarcando](https://ajuda.sankhya.com.br/hc/pt-br/articles/30262095641623-Iniciar-Web-Connection-junto-com-navegador-se-desmarcando)  
> **ID:** `30262095641623` | **Última Atualização:** 2026-07-22T14:36:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30262111744023)

 **SITUAÇÃO:**

Navegador Sankhya desmarca sozinho a opção **'Iniciar Web Connection junto com navegador'**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30262111747735)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30275546946199)

 **Feche** o **Navegador Sankhya** completamente. 

 

![52a3f95f-f5a6-4c32-a7dd-1bd3735f408b](https://ajuda.sankhya.com.br/hc/article_attachments/30277518139799)

 Acesse o **Explorador de Arquivos** do computador e navegue até o seguinte caminho:

 
`C:\Users\NOME_DO_USUARIO_LOGADO\AppData\Roaming\Navegador\Sankhya\db\`

 

** 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30275546946839)

OBSERVAÇÃO: **

 

Se a pasta **AppData** não estiver visível, ative a exibição de itens ocultos:

- No **Explorador de Arquivos**, clique em **Exibir** (ou **Visualizar**).

- Em seguida, selecione **Mostrar > Itens Ocultos**.

![480438612_598803079643923_6044108970397623800_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/30262111755287)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30275554656151)

 Dentro da pasta **"db"**, **exclua** o arquivo chamado **"config.db"**.

- Esse arquivo armazena as configurações do **Navegador Sankhya** e, ao removê-lo, as configurações serão redefinidas.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30275546951319)

  **Reabra** o **Navegador Sankhya**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30275554657175)

 **Ative novamente** a opção:

- Acesse as configurações e marque **"Iniciar Web Connection junto com navegador"**.

6 **Feche e abra** o navegador mais uma vez para validar a correção.

 

 Após seguir esses passos, a opção **"Iniciar Web Connection junto com navegador"** deverá permanecer ativada de forma permanente.