# Existe faturamento posterior a esta data: XX/XX/XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9649899746327-Existe-faturamento-posterior-a-esta-data-XX-XX-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9649899746327-Existe-faturamento-posterior-a-esta-data-XX-XX-XXXX)  
> **ID:** `9649899746327` | **Última Atualização:** 2026-07-22T15:07:02Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19035425758999)

 MENSAGEM:**

[CORE_E04683] Existe faturamento posterior a esta data: XX/XX/XXXX.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19035409288855)

 SITUAÇÃO:**

- Ao realizar pedido no PDV web e fazer a importação dele para o caixa ou;

- Lançar uma nota com data retroativa a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19035409296023)

 CAUSA:**

Poderá ocorrer quando a data do servidor de aplicação está atrasada em relação ao lançamento ou o parâmetro **"Permitir faturamento com data retroativa? - ****FATRETRO" **não está ligado para permitir o lançamento com data retroativa.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19035409305879)

 SOLUÇÃO:**

- Se for lançamento de pedido no PDV Web é necessário verificar data/hora do servidor de aplicação, para isso, é necessário solicitar que seu TI faça essa verificação e ajuste caso necessário.

- Ao lançar a nota, caso deseje realizar o lançamento retroativo, é necessário acessar a tela **Preferências** *(Caminho para acesso à tela: Configurações » Avançado » Preferências) *e ligar o parâmetro **"Permitir faturamento com data retroativa? - ****FATRETRO".**

![fatretro 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19035409314455)