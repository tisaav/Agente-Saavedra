# 'Vend. do lanç. de comissão' não pode ser combinado com outros vendedores

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14864479027991--Vend-do-lan%C3%A7-de-comiss%C3%A3o-n%C3%A3o-pode-ser-combinado-com-outros-vendedores](https://ajuda.sankhya.com.br/hc/pt-br/articles/14864479027991--Vend-do-lan%C3%A7-de-comiss%C3%A3o-n%C3%A3o-pode-ser-combinado-com-outros-vendedores)  
> **ID:** `14864479027991` | **Última Atualização:** 2026-07-22T14:57:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621475124375)

 MENSAGEM:**

[COM_E00585]: 'Vend. do lanç. de comissão' não pode ser combinado com outros vendedores!

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621475137559)

CAUSA:**

Ocorre porque em algum momento o parâmetro LANCAR COMISSAO MULTIPLA ter sido  habilitado e  a marcação CALCULAR COMISSAO MUTIPLA foi marcada na tela de **"Cálculo de comissão"** e, em seguida, o parâmetro foi **desabilitado**. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621463307671)

SOLUÇÃO:**

Na tela Comercial » Avançado » Cálculo de Comissão por Fórmula, ao marcar a opção para calcular para "Vendedor da nota" estava retornando o aviso 'Vendedor/Executante dos itens' não pode ser combinado com outros vendedores!
Porém consta somente uma marcação.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14864406538007)

 

É provável que em algum momento o parâmetro **"LANCCOMMULT' Lançar Comissão p/Múltiplos Vendedores?"** foi ativado.

E ao tentar realizar a busca dos dados para calcular a comissão não estava sendo possível, sendo assim, ative novamente o parâmetro, desabilite a opção vendedor da comissão múltipla que estava retornando ativo, descarte o cache da administração do servidor e feche a tela calcular comissão por fórmula.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14864472209943)

 

Após realizar este processo, abra novamente a tela e busque pela nota.