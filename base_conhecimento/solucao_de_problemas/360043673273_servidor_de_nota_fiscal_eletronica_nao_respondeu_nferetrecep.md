# Servidor de nota fiscal eletrônica não respondeu. "nfeRetRecepcao"

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673273-Servidor-de-nota-fiscal-eletr%C3%B4nica-n%C3%A3o-respondeu-nfeRetRecepcao](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673273-Servidor-de-nota-fiscal-eletr%C3%B4nica-n%C3%A3o-respondeu-nfeRetRecepcao)  
> **ID:** `360043673273` | **Última Atualização:** 2026-07-22T16:03:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453556597783)

 MENSAGEM:**

Servidor de Nota Fiscal eletrônica não respondeu. "nfeRetRecepcao".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453556604311)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453571570455)

 Verifique o IP de instalação do servidor de nota fiscal eletrônica:

**Mitra:**

- Acesse pelo usuário SUP e/ou usuário com acesso a rotina abaixo:

- Avançado >> Preferências >> Todas as Preferências >> CHAVE '**IPSERVNFE**'

- Botão Direito na Tela >> Expandir nível 3 >> Visualize o IP configurado.

**Fast Service:**

- Acesse o FAST pelo usuário SUP, busque pelo caminho Utilitários » DBEExplorer e execute o comando SELECT * FROM TSIPAR WHERE CHAVE = 'IPSERVNFE'

- O IP será apresentado com um duplo clique na coluna 'Texto'.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453556608919)

 Identifique para a máquina correspondente ao IP acima se a internet está funcionando normalmente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453556609943)

 Identifique se a SEFAZ do Estado está indisponível. É possível realizar essa consulta através da [Consulta Disponibilidade SEFAZ.](http://www.nfe.fazenda.gov.br/Portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY=)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453571581847)

 Mantenha a versão SANNFE atualizada conforme versão atual do banco. 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453571583639)

 Diante das situações acima, aguarde o retorno dos serviços de comunicação com a SEFAZ e para o item 2 regularizar o serviço de internet. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453571587863)

 CAUSA:**

Mensagem apresentada na emissão de documentos fiscais eletrônicos no sistema quando houver indisponibilidade na rede de internet e/ou nos serviços de recepção da SEFAZ.