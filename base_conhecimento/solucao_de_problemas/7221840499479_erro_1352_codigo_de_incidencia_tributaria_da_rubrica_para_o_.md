# Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido Pessoal W

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7221840499479-Erro-1352-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido-Pessoal-W](https://ajuda.sankhya.com.br/hc/pt-br/articles/7221840499479-Erro-1352-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido-Pessoal-W)  
> **ID:** `7221840499479` | **Última Atualização:** 2026-07-29T13:23:56Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504827972631)

 MENSAGEM**:

Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido. Ação Sugerida: O valor informado no campo deverá existir na Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504832639511)

 CAUSA:**

Ao enviar o evento S-1010, o sistema retorna com a mensagem supracitada devido ao preenchimento errado do campo “Incidência para IRRF”. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504832654871)

 SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504827999767)

 Acesse a aba “ESOCIAL” do do evento que apresentou o erro na rotina “Eventos”; 
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504832666391)

 **No campo “Incidência para IRRF”, altere para uma incidência válida conforme [Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://sindhosfil.com.br/wp-content/uploads/2020/02/Leiautes-do-Novo-eSocial-v1.0-Beta-Anexo-I-Tabelas.pdf) do eSocial:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482872740631)

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504828012951)

 **Clique em **“Confirmar Alterações”**;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482813608727)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504832673431)

 Após ajuste, na Central do eSocial, gere novamente o evento S-1010 e envie o mesmo. Desabilite a opção** “Utilizar a data de início padrão do sistema”** para informar a data de inicio; 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482800673687)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16482843501463)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/15939477935895)

 Acompanhe a validação do evento no eSocial.