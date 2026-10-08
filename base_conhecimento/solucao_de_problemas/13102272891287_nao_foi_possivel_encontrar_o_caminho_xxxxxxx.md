# Não foi possível encontrar o caminho XXXXXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13102272891287-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-caminho-XXXXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/13102272891287-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-caminho-XXXXXXX)  
> **ID:** `13102272891287` | **Última Atualização:** 2026-07-22T15:00:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295656916631)

 MENSAGEM:**

 [CORE_E01751]: Não foi possível encontrar o caminho XXXXXXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295673358359)

 SOLUÇÃO:**

Verifique os parâmetros abaixo para validação da correta configuração (a frente dos parâmetros tem suas configurações):
 
**"SERVDIRMOD"**: /home/mgeweb/repositorio/impressao/
 
**"FREPBASEFOLDER"**: /home/sdeteste29/       

Repositório:     -----------------
 
Assim identificamos a divergência do caso, pois essa é a forma de validar as configurações de busca dos arquivos dentro do sistema: FREPBASEFOLDER + Repositório= SERVDIRMOD. Entretanto, caso o FREPBASEFOLDER esteja em desacordo com o SERVDIRMOD é recomendável que reveja dentro do Servidor se esse caminho descritos no parâmetro FREPBASEFOLDERexiste de fato. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17295673359511)

CAUSA:**

Ocorre quando há uma divergência entre as configurações de busca dos arquivos dentro do sistema: FREPBASEFOLDER + Repositório= SERVDIRMOD.