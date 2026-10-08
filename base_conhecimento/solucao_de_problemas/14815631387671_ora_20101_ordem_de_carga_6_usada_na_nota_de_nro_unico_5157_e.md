# ORA-20101: Ordem de carga 6 usada na nota de Nro Único: 5157 está fechada e não pode ser alterada. ORA-06512: em "SDETESTE4.TRG_INC_UPD_TGFCAB_ORD", line 167 ORA-04088: erro durante a execução do gatilho

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14815631387671-ORA-20101-Ordem-de-carga-6-usada-na-nota-de-Nro-%C3%9Anico-5157-est%C3%A1-fechada-e-n%C3%A3o-pode-ser-alterada-ORA-06512-em-SDETESTE4-TRG-INC-UPD-TGFCAB-ORD-line-167-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho](https://ajuda.sankhya.com.br/hc/pt-br/articles/14815631387671-ORA-20101-Ordem-de-carga-6-usada-na-nota-de-Nro-%C3%9Anico-5157-est%C3%A1-fechada-e-n%C3%A3o-pode-ser-alterada-ORA-06512-em-SDETESTE4-TRG-INC-UPD-TGFCAB-ORD-line-167-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho)  
> **ID:** `14815631387671` | **Última Atualização:** 2026-07-22T14:57:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16638201061655)

 MENSAGEM:**

[ORA-20101]: Ordem de carga 6 usada na nota de Nro Único: 5157 está fechada e não pode ser alterada.

[ORA-06512]: em "SDETESTE4.TRG_INC_UPD_TGFCAB_ORD", line 167

[ORA-04088]: erro durante a execução do gatilho 'SDETESTE4.TRG_INC_UPD_TGFCAB_ORD'

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16638209843095)

 CAUSA:**

Ocorre ao tentar alterar utilizar uma ordem de carga fechada em um novo pedido ou nota quando o parâmetro ALTOCFECFORMOC está desabilitado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16638209840791)

 SOLUÇÃO:**

Para utilizar uma ordem de carga fechada em novas notas/pedidos, ative o parâmetro **"****ALTOCFECFORMOC"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14815613116951)