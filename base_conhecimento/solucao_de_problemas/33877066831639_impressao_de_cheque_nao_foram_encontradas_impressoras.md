# Impressão de Cheque: Não foram encontradas impressoras!

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33877066831639-Impress%C3%A3o-de-Cheque-N%C3%A3o-foram-encontradas-impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/33877066831639-Impress%C3%A3o-de-Cheque-N%C3%A3o-foram-encontradas-impressoras)  
> **ID:** `33877066831639` | **Última Atualização:** 2026-07-22T14:28:10Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877066821271)

 **MENSAGEM:**

Não foram encontradas impressoras!

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877066822551)

 **SITUAÇÃO:**

Ao tentar imprimir cheques pela tela **"Impressão de Cheque" **(Financeiro > Relatórios) o sistema não localiza impressoras disponíveis apresentando a mensagem de erro. 

**Importante:** Antes de iniciar a solução, verifique se a empresa utiliza o **SPS** (Sankhya Print Service). 

Para mais informações, consulte o artigo [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877049395735)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877049396887)

 Na tela **''Preferências''** (Configurações» Avançado» Preferências) desabilite o parâmetro **"USASERVIMP'', **caso o SPS não seja utilizado; 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877066826135)

 Desabilite o parâmetro **"USAAPPIMPRESSAO"** para garantir que o sistema utilize o plugin de impressão via WebConnection integrado, evitando conflito com aplicações externas; 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34024733706647)

 Se o SPS for utilizado e o parâmetro USASERVIMP estiver ativado, configure apenas um dos métodos de impressão do SPS, conforme o Sankhya Print Service:

- 

[Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)

- 

[Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)

- 

[Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso)

Configure apenas um método para evitar conflitos. Recomenda-se utilizar **"Impressoras e Servidores de Impressão"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34024733708311)

 Mesmo utilizando o SPS, mantenha o parâmetro USAAPPIMPRESSAO desabilitado, conforme orientado no **passo 2**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33877105313047)

 **CAUSA:**

A mensagem de erro pode ser exibida por diferentes motivos, geralmente relacionados à configuração do sistema para tratamento de impressão. Os mais comuns são:

- 

**Incompatibilidade entre os parâmetros de impressão**, especialmente quando o SPS não está em uso, mas o parâmetro USASERVIMP permanece ativado; 

- 

**Parâmetro USAAPPIMPRESSAO ativado**, fazendo com que o sistema aguarde uma aplicação externa de impressão, gerando conflito se não estiver corretamente configurada; 

- 

**Conflito na configuração simultânea dos três métodos de impressão do SPS**, ocultando as impressoras disponíveis mesmo que individualmente estejam corretas.


---

### 🔗 Links e Referências Internas:

- [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service)
- [Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)
- [Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)
- [Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso)