#  O parâmetro: "IGNORAVENDCOMP - Ignorar vendedor ac duplicar/faturar documentos nos portais” esta ligado, o campo vendedor/comprador foi zerado ao duplicar ou faturar. Lembre-se de preencher 0 campo vendedor ou comprador caso seja necessário

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10409174245527--O-par%C3%A2metro-IGNORAVENDCOMP-Ignorar-vendedor-ac-duplicar-faturar-documentos-nos-portais-esta-ligado-o-campo-vendedor-comprador-foi-zerado-ao-duplicar-ou-faturar-Lembre-se-de-preencher-0-campo-vendedor-ou-comprador-caso-seja-necess%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/10409174245527--O-par%C3%A2metro-IGNORAVENDCOMP-Ignorar-vendedor-ac-duplicar-faturar-documentos-nos-portais-esta-ligado-o-campo-vendedor-comprador-foi-zerado-ao-duplicar-ou-faturar-Lembre-se-de-preencher-0-campo-vendedor-ou-comprador-caso-seja-necess%C3%A1rio)  
> **ID:** `10409174245527` | **Última Atualização:** 2026-07-22T15:03:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18787183980823)

 MENSAGEM:**

O parâmetro **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP" **está ligado, e o campo vendedor/comprador foi zerado ao duplicar ou faturar. Lembre-se de preencher o campo vendedor ou comprador caso seja necessário".

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18787210774807)

 CAUSA:**

Quando o parâmetro **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP" **estiver ligado e for realizado o faturamento de uma nota ou duplicação de um pedido/nota nos Portais, caso o vendedor/comprador esteja inativo, o sistema irá completar o processo de faturamento ou duplicação, zerando o campo vendedor e apresentando a mensagem.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18787183983895)

 SOLUÇÃO:**

A mensagem será apresentada quando o parâmetro **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP" **estiver LIGADO:

- Tela 'Preferências' - Chave **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP"**

![preferencias 03-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18787183992087)

Quando o parâmetro **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP" **estiver ligado e for realizado o faturamento de uma nota ou duplicação de um pedido/nota nos Portais, caso o vendedor/comprador esteja inativo, o sistema irá completar o processo de faturamento ou duplicação, zerando o campo vendedor e apresentando a mensagem abaixo no Painel de Avisos do documento gerado:

***"O parâmetro IGNORAVENDCOMP - Ignorar Vend. ao duplicar/faturar doc. nos portais" ***está ligado, e o campo vendedor/comprador foi zerado ao duplicar ou faturar. Lembre-se de preencher o campo vendedor ou comprador caso seja necessário".

Por outro lado, se o parâmetro estiver desligado e existir um documento já confirmado com um vendedor ou comprador inativo informado, quando for duplicado ou faturado esse documento, o sistema impedirá o procedimento.