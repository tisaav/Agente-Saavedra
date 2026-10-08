# WMS_E01107: foram feitos novos ajustes neste inventário. O ajuste só pode ser desfeito após desfazer os ajustes mais recentes

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35043505723799-WMS-E01107-foram-feitos-novos-ajustes-neste-invent%C3%A1rio-O-ajuste-s%C3%B3-pode-ser-desfeito-ap%C3%B3s-desfazer-os-ajustes-mais-recentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35043505723799-WMS-E01107-foram-feitos-novos-ajustes-neste-invent%C3%A1rio-O-ajuste-s%C3%B3-pode-ser-desfeito-ap%C3%B3s-desfazer-os-ajustes-mais-recentes)  
> **ID:** `35043505723799` | **Última Atualização:** 2026-07-22T14:26:07Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043475841175)

 **MENSAGEM**

[WMS_E01107] Foram feitos novos ajustes neste inventário. O ajuste só pode ser desfeito após desfazer os ajustes mais recentes.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470791244055)

 **SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta **desfazer um ajuste de inventário** que possui **ajustes posteriores** vinculados ao mesmo inventário no sistema WMS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043505714327)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470791246871)

 Acesse a tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470818435607)

 Identifique o **inventário** que está tentando desfazer o ajuste.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470818438167)

 Valide o **número de ajuste** vinculado ao inventário.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470818440983)

 Verifique se existem **ajustes posteriores** gerados para o mesmo inventário.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470818444055)

 Desfaça primeiro o **ajuste mais recente** gerado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35470818448279)

 Continue desfazendo os ajustes na **sequência inversa** até chegar ao ajuste desejado.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043505715479)

 **CAUSA**

A mensagem é exibida porque existem **múltiplos ajustes** gerados para o mesmo inventário posteriormente ao ajuste que está sendo desfeito. O sistema exige que os ajustes sejam desfeitos em **ordem cronológica inversa** para manter a integridade dos dados de estoque.