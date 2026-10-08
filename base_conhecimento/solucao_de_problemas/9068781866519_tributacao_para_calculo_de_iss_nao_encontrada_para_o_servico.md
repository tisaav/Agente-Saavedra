# Tributação para cálculo de ISS não encontrada para o serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9068781866519-Tributa%C3%A7%C3%A3o-para-c%C3%A1lculo-de-ISS-n%C3%A3o-encontrada-para-o-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/9068781866519-Tributa%C3%A7%C3%A3o-para-c%C3%A1lculo-de-ISS-n%C3%A3o-encontrada-para-o-servi%C3%A7o)  
> **ID:** `9068781866519` | **Última Atualização:** 2026-07-22T15:10:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882674132631)

 MENSAGEM:**

[CORE_E04488] Tributação para cálculo de ISS não encontrada para o serviço.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882681252375)

 SITUAÇÃO:**

Ao tentar faturar um contrato a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882681257239)

 SOLUÇÃO:**

Verifique as configurações a seguir:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882674151319)

 Acesse a tela '**Faturamento de Contratos'** (*Contratos e Serviços » Rotinas » Faturamento de Contratos*) clique na opção ' Configurações' e o campo 'Calcular ISS/IRF pelo Contrato' deve estar marcado (para ativar esta opção, o parâmetro IMPOSTCON deve estar habilitado);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882681266199)

 Acesse a tela **'Cadastro de produtos' **(*Configurações » Cadastros » Produtos » Serviço*) e marque o produto como 'SERVIÇO'.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882681267863)

 Acesse a tela de '**Preferências da empresa'** (*Comercial » Preferências » Empresa*) e confira se a aba CNAE está preenchida com os dados da cidade.

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882674169495)

 **IMPORTANTE:**

*O parâmetro 'Buscar retenção de ISS pelo contrato?? Chave ISSRETCONTRATO' quando ativado faz a retenção de ISS sempre de acordo com a definição indicada no campo Retém ISS do contrato e nunca de acordo com a configuração indicada no cadastro do parceiro.
*

*Na Central: Quando este parâmetro 'ISSRETCONTRATO?' estiver ligado e o parceiro de um documento for alterado, caso a nota possua um contrato vinculado, o ISS será retido ou não de acordo com o campo RETEM ISS do cadastro do contrato. Caso esteja desligado, funciona verificando o campo RETEM ISS do cadastro do parceiro.*

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882674179095)

 **OBSERVAÇÃO:**
Para mais informações sobre a rotina acesse: [Faturamento de Contratos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18882674181143)

CAUSA: **

Ocorre quando as configurações do ISS não estão devidamente configuradas.


---

### 🔗 Links e Referências Internas:

- [Faturamento de Contratos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos)