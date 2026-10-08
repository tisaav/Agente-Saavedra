# Impressoras não são apresentadas

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30654047127703-Impressoras-n%C3%A3o-s%C3%A3o-apresentadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/30654047127703-Impressoras-n%C3%A3o-s%C3%A3o-apresentadas)  
> **ID:** `30654047127703` | **Última Atualização:** 2026-07-22T14:35:07Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657458313111)

 Ao clicar em imprimir, nenhuma impressora é apresentada, mesmo possuindo impressoras instaladas na máquina.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30657458314007)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657458313111)

 Antes de seguir com a solução, é necessário entender se a empresa trabalha com **SPS (Sankhya Print Service)** ou não. Para mais informações, veja o artigo [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657485359639)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657458315671)

 Se o SPS não é utilizado, desabilite o parâmetro "**USASERVIMP - Usar o PrintService para impressão?**", na tela de **"Preferências" ***(Configurações » Avançado » Preferências)*.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657485361687)

 **Verifique também o parâmetro "**USAAPPIMPRESSAO"**, pois, quando ativado, o sistema entende que a aplicação externa de impressão será utilizada. Já, desabilitado, o sistema usará o plugin de impressão através do WebConnetion integrado. Neste caso, **desabilite** o parâmetro para voltar ao seu padrão.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657458317463)

 Se o SPS realmente é usado, e é necessário usar o parâmetro USASERVIMP ligado, verifique as questões abaixo:

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657485361687)

**Conforme mostra o artigo [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service), atualmente no componente **SPS**, existem 3 (três) métodos de configurar as impressoras:

1. [Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros) 

1. [Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)

1. [Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso) 

Mesmo que corretamente configuradas, se as três opções estiverem configuradas o sistema resulta em conflito, ocultando as impressoras no momento da impressão. Assim, é necessário que** apenas um dos métodos seja configurado**, e não todos. Sempre que possível, aconselhamos a utilização da configuração por **3- Impressoras e Servidores de Impressão**. Consulte o artigo citado para mais informações.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30657485361687)

**Mesmo utilizando o SPS, o parâmetro **USAAPPIMPRESSAO** citado no **passo 1**, tem a mesma função, ou seja, deve ser desabilitado.


---

### 🔗 Links e Referências Internas:

- [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service)
- [Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)
- [Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)
- [Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso)