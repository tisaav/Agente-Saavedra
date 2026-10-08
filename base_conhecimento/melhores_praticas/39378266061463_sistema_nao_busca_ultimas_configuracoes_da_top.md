# Sistema não busca últimas configurações da TOP

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39378266061463-Sistema-n%C3%A3o-busca-%C3%BAltimas-configura%C3%A7%C3%B5es-da-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/39378266061463-Sistema-n%C3%A3o-busca-%C3%BAltimas-configura%C3%A7%C3%B5es-da-TOP)  
> **ID:** `39378266061463` | **Última Atualização:** 2026-08-01T01:01:32Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378266045207)

 **Situação**

O sistema apresenta inconsistência ao não processar as alterações realizadas nas configurações da tabela **"TGFTOP"**, especificamente no campo **"DHTIPOPER"** (Data e hora da alteração do tipo de operação) da tela **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP). O comportamento impede que as atualizações de parâmetros recentes sejam aplicadas corretamente nas transações do sistema.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378266055703)

 **Causa**

Esta ocorrência geralmente é causada por retenção de cache na camada de aplicação ou pendência de sincronização entre o banco de dados e o servidor de instâncias do ERP Sankhya, impedindo a leitura da versão mais recente do registro.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378266056215)

 **Solução**

Para normalizar a busca das configurações, siga os passos abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378202925207)

 Acesse a tela **"Cache do Servidor"** (Configurações » Avançado » Cache do Servidor).
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378266056983)

 Selecione as opção "Descartar Cache Agora"
 

**Obs: Os tipos de operações são históricos, lançamentos já realizados não irão buscar novas configurações, necessário que seja realizado um novo lançamento para que as novas configurações seja acatadas. **