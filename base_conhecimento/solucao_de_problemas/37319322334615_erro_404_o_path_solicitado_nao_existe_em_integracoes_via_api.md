# Erro 404: "O path solicitado não existe" em integrações via API

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37319322334615-Erro-404-O-path-solicitado-n%C3%A3o-existe-em-integra%C3%A7%C3%B5es-via-API](https://ajuda.sankhya.com.br/hc/pt-br/articles/37319322334615-Erro-404-O-path-solicitado-n%C3%A3o-existe-em-integra%C3%A7%C3%B5es-via-API)  
> **ID:** `37319322334615` | **Última Atualização:** 2026-07-22T14:13:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37319322323223)

 **MENSAGEM:**

{ "statusCode": 404, "error": { "code": "NOT_FOUND", "message": "Item não encontrado!", "details": "O path solicitado não existe!" } }

 

![image.png](https://ajuda.sankhya.com.br/hc/article_attachments/37319322323863)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37319322325015)

SOLUÇÃO:**

##### **1. Verificação de Pré-Requisitos e Documentação**

##### Alguns recursos de integração possuem **requisitos específicos de sistema** para funcionarem corretamente. Dessa forma, recomenda-se seguir os passos abaixo:

- 

**Consulte a documentação do endpoint**

Antes de qualquer ação, verifique na documentação técnica se existe uma **versão mínima do sistema** exigida para utilização do serviço: ****[''Guia de Integração com o Sankhya OM''](https://developer.sankhya.com.br/reference/guia-integracao).

- 

**Valide o ambiente**

Confirme se a versão atual do seu sistema é compatível com os requisitos informados na documentação do endpoint utilizado.

- 

**Atualização do sistema**

Caso o recurso esteja disponível apenas em versões superiores à instalada, avalie a **atualização do sistema**, garantindo que todos os serviços e componentes de comunicação estejam disponíveis e atualizados.

 

**2. Limpeza e Reexecução de Módulos (Deploy)**

Caso a versão do sistema já seja compatível e o erro persista, pode haver um **problema no carregamento dos serviços** no servidor de aplicação.

Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37339203376535)

 Acesse o diretório de instalação do servidor de aplicação.

- 

(Exemplo: `/home/mgeweb/wildfly/standalone/deployments`).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37339211042199)

 Localize arquivos relacionados à API ou serviço em questão com a extensão `**.failed**`.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37339211042839)

 Exclua:

- 

Os arquivos `**.failed**`;

- 

Os arquivos `**.deployed**` correspondentes ao mesmo módulo.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37339211047447)

 Reinicie o servidor de aplicação para que o deploy seja executado novamente.

 

**3. Validação Técnica**

Após o reinício do servidor, realize as seguintes validações:

- 

Verifique se os arquivos na pasta **deployments** foram recriados com a extensão `**.deployed**`.

- 

Confirme se a **data e hora de modificação** desses arquivos correspondem ao momento do reinício do servidor.

- 

Caso o módulo volte a apresentar o estado `**.failed**`, será necessário analisar os **logs do servidor de aplicação** para identificar o erro técnico ocorrido durante o carregamento do serviço.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37319357106839)

CAUSA:**

Esse erro ocorre quando o **servidor de aplicação não consegue localizar o recurso ou serviço solicitado** na requisição. As principais causas são:

- 

**Versão do sistema**

O ambiente está em uma versão que ainda não contempla o recurso ou micromódulo utilizado na integração.

- 

**Falha no deploy**

O arquivo responsável por disponibilizar o serviço (extensão **.ear**) não foi carregado corretamente pelo servidor de aplicação.

- 

**Arquivos de falha no servidor**

A existência de arquivos com a extensão **.failed** na pasta de comunicações do servidor impede o carregamento correto do serviço, bloqueando o acesso ao recurso solicitado.


---

### 🔗 Links e Referências Internas:

- [''Guia de Integração com o Sankhya OM''](https://developer.sankhya.com.br/reference/guia-integracao)