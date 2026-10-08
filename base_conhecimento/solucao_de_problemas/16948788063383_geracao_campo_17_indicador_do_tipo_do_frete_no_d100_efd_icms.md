# Geração campo 17 "Indicador do tipo do frete" no D100 (EFD-ICMS/IPI e EFD CONTRIBUIÇÕES)

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16948788063383-Gera%C3%A7%C3%A3o-campo-17-Indicador-do-tipo-do-frete-no-D100-EFD-ICMS-IPI-e-EFD-CONTRIBUI%C3%87%C3%95ES](https://ajuda.sankhya.com.br/hc/pt-br/articles/16948788063383-Gera%C3%A7%C3%A3o-campo-17-Indicador-do-tipo-do-frete-no-D100-EFD-ICMS-IPI-e-EFD-CONTRIBUI%C3%87%C3%95ES)  
> **ID:** `16948788063383` | **Última Atualização:** 2026-07-22T14:54:09Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948802517271)

SOLUÇÃO:**

Para as seguintes versões de layout:

- EFD-ICMS/IPI, versão de layout 5 ou superior

- EFD CONTRIBUIÇÕES, versão de layout 2 ou superior

 

O sistema tem o seguinte comportamento para construção do Tipo de Frete (Apresentando em forma hierárquica):
 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 Se a origem for financeira, o campo fica = 1

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 Se for uma entrada, também será = 1

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 Se o valor do frete estiver com valor 0, fica = 9

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 Se o parceiro do CT-E for igual ao destinatário, fica = 1

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 Se o parceiro da nota for igual remetente = 0

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450538934295)

 E se nenhuma das condições acima forem satisfeitas, o sistema vai lançar a opção 2 no campo 17   (Indicador do tipo do frete) do registro D100 dos EFD's.