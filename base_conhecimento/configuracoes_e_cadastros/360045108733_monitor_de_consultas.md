# Monitor de Consultas

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas)  
> **ID:** `360045108733` | **Última Atualização:** 2026-09-20T03:46:38Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310884956439)

 **Módulo:** Configurações > Avançado   
```

O Monitor de Consultas permitirá que você realize a geração de arquivos de log das querys e stacktraces (processos) das telas e também, faça o download dos mesmos. Essa funcionalidade é equivalente ao SQLMon, utilizado para gerar log do MGE/Jiva G1.

Essa tela não possui controle de acessos, ou seja, todos que utilizam nosso sistema poderão utilizá-la.

Para se trabalhar com essa tela é bem simples, basta dar apenas um clique no botão 

![botao-iniciar-movimento.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/15632916385047)

 **"Iniciar monitoramento"**, para que o monitoramento seja iniciado.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360075371914)

Finalizada a navegação nas rotinas desejadas, para interromper o monitoramento, clique no botão 

![botao-parar-monitoramento.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/15632976623127)

 **"Parar monitoramento"**.

Quando desejar obter os arquivos de log gerados, basta paralisar a gravação e clicar no botão **"Baixar arquivos de Log"**:

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360076541053)

Só é possível Baixar o arquivo de Log se o monitoramento estiver Parado.

 

**Dados informados nos arquivos**

Log do SQL

**##ID_x##**: É um identificador para relacionar a query com o seu respectivo stackTrace;

**Tempo**: É o tempo de execução da query;

**Query**: Query executada no sistema;

**Params**: Os parâmetros que a query está utilizando.

Abaixo, trouxemos um exemplo de logs de queries gerados:

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/360076541133)

 

Log do stackTrace

**##ID_x##**: Identificador que relaciona o stackTrace com a sua respectiva query.

Agora um exemplo de logs de stackTraces gerados:

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/360076541173)

Os nomes dos arquivos serão: 

- 
Do arquivo zip será Monitoramento.zip;

- 
O arquivo com as querys efetuadas pelo sistema terá o nome de Monitor_Consultas.log;

- 
Staktraces (processos) será denominado Monitor_Processos.log.

 

**Mensagens de erro**

As mensagens de erro estarão presentes no arquivo Monitor_Processos; no arquivo Monitor_Consultas serão somente informações do Banco de Dados.

**Observação:** o arquivo Monitor_Consultas.log trará os dados utilizados para efetuar a query. Exemplo: *SELECT * FROM TGFPAR WHERE CODPARC=?*; posteriormente, trará o argumento 1=10, ou seja, o código do parceiro informado para fazer o select é o número 10.