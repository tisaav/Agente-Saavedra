# Não foi possível conectar ao servidor de acessos (SAS), isso pode limitar telas e funcionalidades

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110174-N%C3%A3o-foi-poss%C3%ADvel-conectar-ao-servidor-de-acessos-SAS-isso-pode-limitar-telas-e-funcionalidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110174-N%C3%A3o-foi-poss%C3%ADvel-conectar-ao-servidor-de-acessos-SAS-isso-pode-limitar-telas-e-funcionalidades)  
> **ID:** `360044110174` | **Última Atualização:** 2026-07-22T15:53:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522695069847)

 MENSAGEM:**

Não foi possível conectar ao servidor de acessos (SAS), isso pode limitar telas e funcionalidades. Por favor comunique o administrador do sistema para que sejam verificados os parâmetros e configurações de acesso.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708462231)

 SITUAÇÃO:**

Ao acessar o sistema ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522695082519)

 SOLUÇÃO:**

Para correção seguir os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708469911)

 Acesse com um usuário que tenha permissão para copiar a Chave de Licença o Place Sankhya

Informações Cadastrais>>Chave do Cliente.
Copie o código e insira no campo: Chave de cliente na aba Licença do Administrador do Servidor e clique em Aplicar depois 'Recarregar Licença'

Se NÃO resolver seguir os passos abaixo:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708473495)

 Primeiro identifique se o IP do Servidor onde está instalado o serviço SAS, está informado no Parâmetro **IP do servidor de acessos -IPSERVACESS.**

2.1-Configurações » Avançado » Preferências

Pesquise pelo parâmetro **IP do servidor de acessos -IPSERVACESS.**

No campo TEXTO, verifique se tem o IP informado, se está correto e se é o IP onde está instalado o Serviço do SAS. Se não estiver informado, deve-se informar apenas o IP no formato(Exemplo: 192.168.1.1). 

2.2- Configurações » Avançado » Administração do Servidor

Aba: Licença

Clique na opção 'Recarregar Licença' ou considere reiniciar o serviço do SankhyaW.

Para identificar se o serviço do SAS está Iniciado, considere o processo abaixo:

**Para ambiente [WINDOWS](http://downloads.sankhya.com.br/docs/MAN_TI_Instala%C3%A7%C3%A3o_SAS_2_3_Windows.pdf).**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708469911)

 Acesse o Servidor onde está instalado o SAS

Painel de Controle>>Ferramentas Administrativas>>Serviços

Pesquise pelo serviço do SAS (Nome: SAS3.0bxx), clique no botao direito do mouse em INICIAR).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708473495)

 Reiniciar o serviço do SankhyaW

**Para ambiente [LINUX](http://downloads.sankhya.com.br/docs/MAN_TI_Instala%C3%A7%C3%A3o_SAS_2_3_Linux.pdf)**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708469911)

 Acesse o Servidor onde está instalado o SAS, com o usuario MGEWEB

Execute a linha de comando

[mgeweb@teste ~]#** /opt/./protstart.sh**

Apresentando a mensagem abaixo, significa que o SAS foi iniciado, caso não ocorra nenhum problema, que pode ser analisado pelo LOG. 

Preparing JRE ...
testing JVM in /opt/SASX.XXX/jre ...
Starting sasrun
[mgeweb@teste ~]$ **nohup: appending output to `nohup.out'**
Obs. Ao aparecer a msg nohup: appending output to `nohup.out' (Tecle Enter)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708473495)

 Reiniciar o serviço do SankhyaW.

 

 

**CONSIDERAÇÕES**** PARA BANCO DE DADOS EXTERNO:**

Quando o ambiente de acesso ao banco de dados fica fora de sua empresa, deverá ser criado um redirecionamento de comunicação do serviço do SAS, que está instalado no host indicado no parâmetro **IP do servidor de acessos -IPSERVACESS** e por padrão usa a porta 10050.

Logo em seguida deverá ser ajustado o parâmetro **IP do servidor de acessos -IPSERVACESS**, adicionando uma segunda opção de conexão com o SAS.

A configuração para o parâmetro deverá ser conforme exemplos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708469911)

 Porta padrão:
- IP na rede local: 10.1.0.20, porta 10050
- IP público: 200.232.243.254, porta 10050

-> O IPSERVACESS deverá ser ajustado para: 10.1.0.20;200.232.243.254

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708473495)

 Caso a porta do SAS seja diferente de 10050, deve ser colocada logo a frente do IP desta forma:

- IP na rede local: 10.1.0.20, porta 10060
- IP público: 200.232.243.254, porta 10060

-> O IPSERVACESS deverá ser ajustado para: 10.1.0.20:10060;200.232.243.254:10060

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18522708475031)

 CAUSA:**

Significa que o parâmetro **IP do servidor de acessos -IPSERVACESS** está com o IP que não tem o SAS, ou o SAS não está inicializado.

**VÍDEO TUTORIAL DE LICENCIAMENTO ONLINE**

****


---

### 🔗 Links e Referências Internas:

- [WINDOWS](http://downloads.sankhya.com.br/docs/MAN_TI_Instala%C3%A7%C3%A3o_SAS_2_3_Windows.pdf)
- [LINUX](http://downloads.sankhya.com.br/docs/MAN_TI_Instala%C3%A7%C3%A3o_SAS_2_3_Linux.pdf)