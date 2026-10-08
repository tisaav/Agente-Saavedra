# Não foi possível realizar a compensação automática pois uma liberação de limites do Evento '24 - Autorização de Pagamento' foi lançada ao tentar baixar os títulos

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7867539538967-N%C3%A3o-foi-poss%C3%ADvel-realizar-a-compensa%C3%A7%C3%A3o-autom%C3%A1tica-pois-uma-libera%C3%A7%C3%A3o-de-limites-do-Evento-24-Autoriza%C3%A7%C3%A3o-de-Pagamento-foi-lan%C3%A7ada-ao-tentar-baixar-os-t%C3%ADtulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/7867539538967-N%C3%A3o-foi-poss%C3%ADvel-realizar-a-compensa%C3%A7%C3%A3o-autom%C3%A1tica-pois-uma-libera%C3%A7%C3%A3o-de-limites-do-Evento-24-Autoriza%C3%A7%C3%A3o-de-Pagamento-foi-lan%C3%A7ada-ao-tentar-baixar-os-t%C3%ADtulos)  
> **ID:** `7867539538967` | **Última Atualização:** 2026-07-22T15:12:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541526342295)

 MENSAGEM**:

[CORE_E01707] Não foi possível realizar a compensação automática pois uma liberação de limites do Evento '24 - Autorização de Pagamento' foi lançada ao tentar baixar os títulos.
O processo de compensação automática não é compatível com liberação de limites. Configure o sistema para que os títulos envolvidos na compensação não necessitem de liberações para serem baixados."

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543084951)

SOLUÇÃO:**

Verifique as seguintes configurações:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541526349719)

 Analise qual TOP está configurada no parâmetro (tela de **"****Preferências"**) **"****TOPBAIDESPCOMP";**

 

![Não foi possível realizar a compensação automática pois uma 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543091223)

 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543093399)

  Tela de Tipo de Operação - TOP, localize a top informada no parâmetro mencionado acima; 

 

![Não foi possível realizar a compensação automática pois uma 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543095575)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541526363543)

 Verifique a informação do campo: **'Valor mínimo p/Autorização de Pagamento:'**

Se estiver com valor informado ali, o sistema emite aquela mensagem solicitando a liberação.

 

![Não foi possível realizar a compensação automática pois uma 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543100823)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541543101847)

CAUSA:**

O erro ocorre quando se configurou a compensação automática utilizando uma TOP de baixa que está com campo Valor mínimo p/Autorização de Pagamento diferente de 0,00.