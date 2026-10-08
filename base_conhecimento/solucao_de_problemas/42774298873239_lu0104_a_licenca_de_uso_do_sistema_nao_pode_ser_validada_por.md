# LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/42774298873239-LU0104-A-licen%C3%A7a-de-uso-do-sistema-n%C3%A3o-p%C3%B4de-ser-validada-por-falha-na-conex%C3%A3o-com-o-servi%C3%A7o-de-valida%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/42774298873239-LU0104-A-licen%C3%A7a-de-uso-do-sistema-n%C3%A3o-p%C3%B4de-ser-validada-por-falha-na-conex%C3%A3o-com-o-servi%C3%A7o-de-valida%C3%A7%C3%A3o)  
> **ID:** `42774298873239` | **Última Atualização:** 2026-08-26T18:44:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774298856471)

 **MENSAGEM:**

LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação. Por favor, comunique o administrador do sistema para que seja verificada a conexão com a internet do servidor (SAS) e possíveis bloqueios nos endereços de acesso.

Permanecendo a falha na conexão, algumas telas e recursos do sistema poderão ficar indisponíveis daqui a X dias e X horas.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774291656215)

SOLUÇÃO:**

**Cenários de correção da falha de validação da cadeia de certificados pelo SAS3 Linux:**

- 

**Alternativa 1: Ativar o INITSASONLINE (Somente Cliente que NÃO usa o MGE / DELPHI)**

Ativar o parâmetro ''**INITSASONLINE''** para casos em que o cliente esteja em versões que já tenham esta possibilidade e não tenham módulos MGE (Delphi)

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774688531991)

****

| Caso o parâmetro não exista, crie-o com as seguintes configurações: Chave: "INITSASONLINE" | Descrição: Ativa a nova versão do SAS | Módulos: Configurações | Menu: Diversas | Aba: Diversas | Tipo: Lógico | Status: Ligado. |
| --- |

 

![INITSASONLINE.png](https://ajuda.sankhya.com.br/hc/article_attachments/42818507385751)

 Após Criar/habilitar o parâmetro, realize o recarregamento das licenças do sistema na tela **"Administração do servidor ** (Configurações » Avançado » Administração do Servidor), aba Licença e selecione a opção **Recarregar Licença**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42775117971479)

- 

**Alternativa 2: Utilizar uma JRE instalada no ambiente**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576779927)

 Verificar se há uma JRE instalada no servidor onde roda o SAS: 

- 

java -version

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965207)

 Caso seja uma JRE mais recente que 1.7.0_80, já poderá ser suficiente para ajustar.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576783511)

 Parar o SAS

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965335)

 Renomear a pasta <PASTA_DO_SAS>/jre para <PASTA_DO_SAS>/jre_old: 

- 

mv <PASTA_DO_SAS>/jre <PASTA_DO_SAS>/jre_old

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576784151)

 Iniciar o SAS

 

- 

**Alternativa 3: Atualizar manualmente a JRE do SAS**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576779927)

 **Parar o SAS

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965207)

 Fazer download do arquivo para a pasta do SAS:

- 

cd <PASTA_DO_SAS>
 wget https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/grfetvhg7pdl/b/ti-files/o/jre1.8.tar.gz
 mv jre jre_old
 tar -xzvf jre1.8.tar.gz

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576783511)

 Iniciar o SAS

 

- 

**Alternativa 4: Atualizar o SAS**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576779927)

 **Parar o SAS.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965207)

 Baixar o SAS do site de Downloads:

- 

cd /opt
 wget <LINK_DO_SAS>

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576783511)

 Renomear a pasta do SAS antigo

- 

mv <PASTA_DO_SAS> <PASTA_DO_SAS_old>

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965335)

 Descompactar o novo SAS

- 

tar -xzvf SAS_3_1b26_Sankhya_unixx64.tar.gz

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774576784151)

 Copiar os arquivos de configuração da pasta antiga para o novo:

- 

cp <PASTA_DO_SAS_old>/conf/sas.cfg <PASTA_DO_SAS>/conf/sas.cfg

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595965719)

 Ajustar os arquivos protstart.sh e protstop.sh, apontando para a nova pasta do SAS.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774595966103)

 Iniciar o SAS.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42774298857623)

CAUSA:**

Foi feito uma migração da cadeia de certificados, sendo necessário atualização da JRE do SAS.