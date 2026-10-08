# Campo "Atraso" incorreto na baixa de um título na Movimentação Financeira

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26948563024151-Campo-Atraso-incorreto-na-baixa-de-um-t%C3%ADtulo-na-Movimenta%C3%A7%C3%A3o-Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/26948563024151-Campo-Atraso-incorreto-na-baixa-de-um-t%C3%ADtulo-na-Movimenta%C3%A7%C3%A3o-Financeira)  
> **ID:** `26948563024151` | **Última Atualização:** 2026-07-22T14:40:31Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450188564631)

Quando o campo **"Atraso"** dentro da baixa de um título na movimentação financeira apresenta seu valor incorreto (**com um dia a mais ou um dia a menos**), é necessário analisar os Argumentos da VM.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26948563016343)

  Acesse a Administração do Servidor e verifique se no texto do campo** "Argumentos da VM"** possui o argumento abaixo, conforme cita no Help '[Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)'.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450188564631)

 **-JAVA_OPTS="$JAVA_OPTS -Duser.timezone=GMT-3"**

 

Esse argumento é responsável por ajustar o timezone do servidor de aplicação, que serve de referência para o campo Atraso. 

 

**Observação: **se seu servidor é Local, esse processo é realizado pelo time de Infraestrutura da empresa. Por outro lado, caso seja em Nuvem, entre em contato com os responsáveis pela hospedagem. Qualquer dúvida na execução do processo, acione a unidade responsável. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26948516842775)

CAUSA:**

Ocorre quando não existe o argumento de timezone, causando a divergência da data/hora do servidor.


---

### 🔗 Links e Referências Internas:

- [Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)