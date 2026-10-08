# O título está em cobrança registrada e não pode ser excluído

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712214-O-t%C3%ADtulo-est%C3%A1-em-cobran%C3%A7a-registrada-e-n%C3%A3o-pode-ser-exclu%C3%ADdo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712214-O-t%C3%ADtulo-est%C3%A1-em-cobran%C3%A7a-registrada-e-n%C3%A3o-pode-ser-exclu%C3%ADdo)  
> **ID:** `360043712214` | **Última Atualização:** 2026-07-22T16:00:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200944634391)

 MENSAGEM:**

Erro ao remover entidade:

ORA-20101: O título está em cobrança registrada e não pode ser excluído.

ORA-06512: em "SANKHYA.TRG_INC_UPD_TGFFIN_MONIOCOREM", line 79

ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TGFFIN_MONIOCOREM'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200918578967)

 SITUAÇÃO:**
Ao tentar efetuar o cancelamento de uma Nota, ocorre a mensagem.
 
**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200918580247)

 SOLUÇÃO:**
Para proceder com o cancelamento da nota fiscal eletrônica é necessário permitir desvincular o(s) financeiro(s) gerado(s) da respectiva remessa bancária.
 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200944641559)

 **Para essa permissão é necessário que o parâmetro** "PERDESVFINREM"** esteja 'ligado'.

- Acesse: Configurações » Avançado » Preferências

- Chave: PERDESVFINREM - Permite desvincular financeiro de remessa?

- Ligado/Desligado: ligado

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200944642839)

 Acesse: *Financeiro » EDI Bancário » Registro de Alteração Financeiro*
Faça um filtro e pesquise pelo título, caso haja registro dele nesta tela, exclua-o. Se não houver, tente Desvincular Remessa na Movimentação Financeira.
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200918588183)

 Após verificar o parâmetro, localize o financeiro na tela **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)"**, no botão **"Outras Opções"** clique em **"Desvincular Remessa"**.
 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200918590359)

 Feito isso, teste o cancelamento da NF-e.
 
**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16200944647831)

 CAUSA**
Ocorre quando ao tentar cancelar NF-e que possui financeiro(s) vinculado(s) a arquivo de remessa bancária, será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)