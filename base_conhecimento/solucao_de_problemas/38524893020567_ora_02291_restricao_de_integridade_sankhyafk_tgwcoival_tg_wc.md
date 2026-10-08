# ORA-02291: restrição de integridade (SANKHYA.FK_TGWCOIVAL_TG_WCOI) violada – chave mãe não localizada.

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38524893020567-ORA-02291-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGWCOIVAL-TG-WCOI-violada-chave-m%C3%A3e-n%C3%A3o-localizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/38524893020567-ORA-02291-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGWCOIVAL-TG-WCOI-violada-chave-m%C3%A3e-n%C3%A3o-localizada)  
> **ID:** `38524893020567` | **Última Atualização:** 2026-07-22T14:01:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524882713111)

**** ****MENSAGEM**

ORA-02291: restrição de integridade (SANKHYA.FK_TGWCOIVAL_TG_WCOI) violada – chave mãe não localizada.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524893008407)

**** ****SITUAÇÃO**

Ao finalizar a recontagem de entrada, quando o produto possui mais de um lote/data de validade.
 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524882714263)

**** ****SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524893009815)

 Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524893011479)

 Busque pelo parâmetro **"USARECCUMCONENT-Utiliza recontagem cumulativa na conf. entrada.''**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524882720151)

 Habilite o parâmetro para permitir que um mesmo produto seja recontado mais de uma vez antes da finalização da conferência.

- 

Quando o parâmetro estiver desabilitado, o coletor permitirá que cada produto seja recontado apenas uma única vez para envio e conclusão da recontagem.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524882720535)

**** ****CAUSA**

O erro ocorre quando o parâmetro “USARECCUMCONENT – Utiliza recontagem cumulativa na conferência de entrada” não está habilitado, pois, nessa condição, o sistema permite que o produto seja recontado apenas uma única vez.

Como consequência, não é possível informar múltiplas datas de validade ou lotes para o mesmo produto durante a conferência.