# Restrição de integridade (SANKHYA.FK_TGFCTC_CODBCO_TSIBCO) violada - chave mãe não localizada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043607894-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFCTC-CODBCO-TSIBCO-violada-chave-m%C3%A3e-n%C3%A3o-localizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043607894-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFCTC-CODBCO-TSIBCO-violada-chave-m%C3%A3e-n%C3%A3o-localizada)  
> **ID:** `360043607894` | **Última Atualização:** 2026-07-22T16:01:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171932935319)

 MENSAGEM:**

ORA-02291: restrição de integridade (SANKHYA.FK_TGFCTC_CODBCO_TSIBCO) violada - chave mãe não localizada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171946316567)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171946319767)

 Verifique o 'Banco' vinculado ao respectivo cheque, através das informações de CMC7:

 

![banco2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14599928096279)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171932942743)

 Acesse a tela ****["Bancos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894) (Caminho de acesso: *Configurações » Cadastros » Bancários » Bancos*) e verifique se o banco constatado no item 1 encontra-se cadastrado. Em caso negativo, efetue o cadastro.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/12245792900119)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171946325655)

 Realizado o cadastro do Banco, teste o procedimento de baixa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16171932947479)

 CAUSA:**

Mensagem apresentada quando o 'Banco' utilizado na operação de baixa não está cadastrado no sistema.


---

### 🔗 Links e Referências Internas:

- ["Bancos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894)