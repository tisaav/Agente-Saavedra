# Não foi possível determinar o tipo de emissão das notas da empresa X para o estado 'UF'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358933-N%C3%A3o-foi-poss%C3%ADvel-determinar-o-tipo-de-emiss%C3%A3o-das-notas-da-empresa-X-para-o-estado-UF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358933-N%C3%A3o-foi-poss%C3%ADvel-determinar-o-tipo-de-emiss%C3%A3o-das-notas-da-empresa-X-para-o-estado-UF)  
> **ID:** `360043358933` | **Última Atualização:** 2026-07-22T16:05:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858504471)

 MENSAGEM:**

[CORE_E04876] Não foi possível determinar o tipo de emissão das notas da empresa X para o estado 'UF'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858507415)

 SITUAÇÃO:**

Ao acessar o Portal de Vendas, selecionar uma NF-e e tentar consultar Situação do Serviço ou Gerar Lote, apresenta a mensagem.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841232663)

 CAUSAS:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858512663)

 Serviço inoperante ou com instabilidade de Recepção/Consulta da SEFAZ Estadual/Nacional.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841226391)

 Problemas na infra estrutura de rede ou no servidor onde está instalado o aplicativo SANNFE, impedindo a comunicação com a SEFAZ.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841228311)

 Certificado Digital vencido.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841235863)

 Atualizou o(s) Certificado(s), porém não reiniciou o SANNFE ou o **SankhyaW.**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858525207)

 Empresa sem um tipo de contingencia definido nas preferências da empresa, campo **"Envio em Contingência"** configurado como **"Não usar contingência"**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858509719)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115858512663)

 Entre em contato via telefone ou outro canal disponível com a Sefaz Estadual, para verificar Instabilidades no Serviço da SEFAZ.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841226391)

 Verifique com a área de TI da empresa se o Servidor onde está instalado o SANNFE está com acessos a porta 9090, liberado em firewall ou proxy e com acesso a Internet.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841228311)

 Efetue a substituição caso o Certificado Digital esteja vencido. O Certificado Digital A1 é o único compatível com os sistemas Sankhya, ele precisa ser substituído anualmente e podem ser adquiridos em sites específicos ou Correios, Caixa Econômica, Serasa e outros.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115841235863)

 Verifique se a URL informada na aba Status do Serviço campo** "Configuração e teste de conectividade com a internet"** está correto.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458166125719)

O SanNFe necessita de conexão com a internet para consumir os serviços da Receita Estadual ou Federal. Por esse motivo foi incluído teste de conectividade para evitar problemas na execução do serviços.

A lista de URLs informada no console tem por objetivo validar se a máquina a qual o SanNFe está instalado tem conexão com a Internet.
Ao ser instalado o SanNFe essa lista de URLs vem vazia, nesse caso, o SanNFe não executa a validação da conexão antes de executar algum serviço. Por isso, quando a máquina não tem conexão com a Internet, a falha vai ocorrer ao executar o serviço, ou seja, na emissão da nota pelo MGE, Mitra ou SankhyaW. Quando não configurado o teste e ao ocorrer o erro na execução a fim de facilitar a detecção de problemas o SanNFe faz o teste de conectividade com a URL: http://www.receita.fazenda.gov.br. Quando não há conexão, é incluído na mensagem de erro, que a possível causa pode ser a falta de conexão.
Quando informado alguma URL na lista, o SanNFe passa a validar a conexão por meio dessa URL, o teste de conexão consiste um acesso bem sucedido ao site endereçado pela URL. Em caso de falha, não será permitido a execução de nenhum serviço. Caso exista mais de uma URL na lista, a aplicação considera o teste bem sucedido para a primeira URL acessada. 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458166125719)

 Características do painel de testes:**

- Para adicionar uma url na lista, basta informar o endereço válido, exemplo: [http://www.sankhya.com.br](http://www.sankhya.com.br) em seguida, selecione o botão com ícone de + para incluir na lista;

- Após adicionado as URLs é necessário selecionar o botão Salvar lista, esse botão salva lista de URLs no arquivo de configuração do SanNFe (conf/san-nfe.conf);

- O botão Testa efetua o teste de conexão para todas as URLs incluídas na lista, um teste bem sucedido marca a URL com o ícone na cor verde, caso contrário, um ícone na cor vermelha é apresentada.

- A lista de URL é armazenada no arquivo de configuração do SanNFe por meio da propriedade: internet.test.urls=<lista de URLs>, onde cada URL é separada por virgula. Por exemplo:
internet.test.urls=http://www.sankhya.com.br,http://www.jiva.com.br

1. As URLs para execução serviços Web(webServices) executados pelo SanNFe diferem de estado para estado. Para não ter que liberar acesso completo da máquina basta liberar por meio de NAT(Network Address Translation) os endereços referentes ao estado que será emitido a NFe para a porta 443(HTTPS).

1. Como exemplo as URLs dos webservices para o estado de MG são:

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeRecepcao](https://nfe.fazenda.mg.gov.br/nfe/services/NfeRecepcao)

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeRetRecepcao](https://nfe.fazenda.mg.gov.br/nfe/services/NfeRetRecepcao)

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeCancelamento](https://nfe.fazenda.mg.gov.br/nfe/services/NfeCancelamento)

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeInutilizacao](https://nfe.fazenda.mg.gov.br/nfe/services/NfeInutilizacao)

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeConsulta](https://nfe.fazenda.mg.gov.br/nfe/services/NfeConsulta)

  - [https://nfe.fazenda.mg.gov.br/nfe/services/NfeStatusServico](https://nfe.fazenda.mg.gov.br/nfe/services/NfeStatusServico)

1. O endereço à liberar deve ser: nfe.fazenda.mg.gov.br para a porta 443.

1. A lista dos endereços para os outros estados podem ser encontradas no arquivo de urls conf/url-webservices.xml ou no site da [Receita Federal.](http://www.nfe.fazenda.gov.br/portal/Default.aspx)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458166125719)

 A Sankhya recomenda que sempre mantenha o SANNFE atualizado e compatível com a versão do **SankhyaW**. Esta compatibilidade pode ser consultada através do site [http://downloads.sankhya.com.br/](http://downloads.sankhya.com.br/) em **Requisitos** opção encontrada logo a frente de cada pacote disponível.


---

### 🔗 Links e Referências Internas:

- [http://www.sankhya.com.br](http://www.sankhya.com.br)
- [http://downloads.sankhya.com.br/](http://downloads.sankhya.com.br/)