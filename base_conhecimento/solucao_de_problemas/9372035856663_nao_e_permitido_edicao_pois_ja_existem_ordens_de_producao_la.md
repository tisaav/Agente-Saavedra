# Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9372035856663-N%C3%A3o-%C3%A9-permitido-edi%C3%A7%C3%A3o-pois-j%C3%A1-existem-Ordens-de-Produ%C3%A7%C3%A3o-lan%C3%A7adas-para-este-Processo-Produtivo-Crie-uma-nova-vers%C3%A3o-para-realizar-edi%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/9372035856663-N%C3%A3o-%C3%A9-permitido-edi%C3%A7%C3%A3o-pois-j%C3%A1-existem-Ordens-de-Produ%C3%A7%C3%A3o-lan%C3%A7adas-para-este-Processo-Produtivo-Crie-uma-nova-vers%C3%A3o-para-realizar-edi%C3%A7%C3%A3o)  
> **ID:** `9372035856663` | **Última Atualização:** 2026-07-22T15:08:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984056343)

 MENSAGEM:**

[PROD_E00266]: Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702988375319)

 SITUAÇÃO:**

Ao tentar realizar alteração das matérias primas na tela composição do produto após já ter Ordens de Produção lançada na versão atual do processo produtivo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984087447)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702988380823)

 Habilite os parâmetros **"PERMITEDITLSTMP/PERMITEDITMP"** para que o sistema permita editar as MPs na composição dos produtos e não valide a versão do processo;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984094487)

 Caso deseje manter o comportamento de validar a versão e não permitir alteração sem versionar, mantenha os parâmetros PERMITEDITLSTMP/PERMITEDITMP desabilitados;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984100887)

 Acesse a tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado » Preferências),* informe o parâmetro PERMITEDITMP e desligue o mesmo:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9371980001047)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702988400023)

 Acesse a tela Preferências *(Caminho de acesso: Configurações » Avançado » Preferências),* informe o parâmetro PERMITEDITLSTMP e desligue o mesmo:

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/9372031473047)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984108951)

 CAUSA:**

Alterar as matérias primas na composição de produto após lançamento de OP sem versionar o processo produtivo.

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702984112919)

 O botão Despublicar na tela** "Processo produtivo nova"** *(Caminho de acesso: Produção » Cadastros » Processo Produtivo - Nova)* não permite despublicar e alterar o processo e será desabilitado nas próximas versões.