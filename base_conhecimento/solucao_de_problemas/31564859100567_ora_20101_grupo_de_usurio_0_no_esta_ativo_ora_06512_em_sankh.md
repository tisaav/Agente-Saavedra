# ORA-20101: Grupo de usu?rio 0 n?o esta ativo. ORA-06512: em "SANKHYA.TRG_INC_UPD_TSIUSU"

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31564859100567-ORA-20101-Grupo-de-usu-rio-0-n-o-esta-ativo-ORA-06512-em-SANKHYA-TRG-INC-UPD-TSIUSU](https://ajuda.sankhya.com.br/hc/pt-br/articles/31564859100567-ORA-20101-Grupo-de-usu-rio-0-n-o-esta-ativo-ORA-06512-em-SANKHYA-TRG-INC-UPD-TSIUSU)  
> **ID:** `31564859100567` | **Última Atualização:** 2026-07-29T13:19:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31564859095319)

 **MENSAGEM:**

[ORA-20101]: Grupo de usuário 0 não está ativo.
[ORA-06512]: em "SANKHYA.TRG_INC_UPD_TSIUSU", linha 16
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TSIUSU'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31564859097495)

SOLUÇÃO:**

Para que o usuário possa ser criado no Sankhya Om, é necessário que o grupo de usuários ao qual ele será associado esteja ativo. Para ativá-lo, acesse a tela **Grupo de Usuário** *(Configurações » Controle de Acesso » Grupo de Usuários),* localize o grupo desejado para realizar a ativação e ative-o.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31570959507223)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31564827905303)

CAUSA:**

O grupo de usuários ao qual o funcionário está sendo vinculado está desativado.