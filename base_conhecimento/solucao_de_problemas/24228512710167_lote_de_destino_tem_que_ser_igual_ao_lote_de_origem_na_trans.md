# Lote de destino tem que ser igual ao lote de origem na transferência

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24228512710167-Lote-de-destino-tem-que-ser-igual-ao-lote-de-origem-na-transfer%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/24228512710167-Lote-de-destino-tem-que-ser-igual-ao-lote-de-origem-na-transfer%C3%AAncia)  
> **ID:** `24228512710167` | **Última Atualização:** 2026-07-22T14:47:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24228512695319)

 **MENSAGEM:**

[CORE_E03252] Lote de destino tem que ser igual ao lote de origem na transferência

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24228488008983)

 **SOLUÇÃO:**

Para resolver o erro siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24943906518935)

 Acesse a tela **"Produtos" ***(Caminho: Configurações » Cadastros » Produtos » Produtos), *vá até a aba **"Medidas e estoque" **e na opção **"Controle adicional", **observe no campo **"Controlar por" **qual a forma de controle está sendo utilizada.

 

![Lote de destino tem que ser igual ao lote de origem na transferência 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/24943912398231)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24943912403607)

 Depois, verifique se a forma descrita no controle de origem e de destino é a forma definida no campo Controla por. Também veja se a forma de controle indicada na origem e no destino são iguais. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24228512706455)

**CAUSA:
**

A validação ocorre quando usuário, em uma movimentação de Transferência, informa o 'LOTE' DE ORIGEM diferente do 'LOTE' DE DESTINO. Ela só é apresentada para os produtos que possuem o Controle adicional = 'Lote' e o parâmetro **"LOTEDTVAL"** **Usar data de validade junto com Lote?** esteja = LIGADO.