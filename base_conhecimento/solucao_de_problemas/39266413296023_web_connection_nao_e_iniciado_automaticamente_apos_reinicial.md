# Web Connection não é iniciado automaticamente após reinicialização do computador

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39266413296023-Web-Connection-n%C3%A3o-%C3%A9-iniciado-automaticamente-ap%C3%B3s-reinicializa%C3%A7%C3%A3o-do-computador](https://ajuda.sankhya.com.br/hc/pt-br/articles/39266413296023-Web-Connection-n%C3%A3o-%C3%A9-iniciado-automaticamente-ap%C3%B3s-reinicializa%C3%A7%C3%A3o-do-computador)  
> **ID:** `39266413296023` | **Última Atualização:** 2026-07-22T13:59:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39266385684759)

 **MENSAGEM:**

O Web Connection não é iniciado automaticamente após reinicialização do computador.

E todas as vezes tem que fazer o processo manual de iniciar o Web Connection.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39266413284247)

SOLUÇÃO:**

Validar se o arquivo de inicialização (.bat) existe na pasta:

```text
C:\Users\usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

ou acessando via "executar" digite:

```text
shell:startup
```

Caso o arquivo não exista:

1. 

Reinstalar o **Web Connection** com privilégios de administrador.
**ou**

1. 

Refazer o processo via login administrador e fazer a instalação.

 

1. 

Após a instalação validar a pasta abaixo onde o .bat aparecerá:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39266413285783)

Caso o arquivo exista, mas não execute:

- 

Verificar bloqueios de **antivírus** ou **firewall**

- 

Criar exceções para o Web Connection e para o script `.bat`

Reiniciar a máquina e validar se o serviço inicia automaticamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39266413286679)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39266385690007)

CAUSA:**

O problema pode ocorrer, principalmente, por dois motivos:

- 

O instalador do **Web Connection** não criou corretamente o arquivo de inicialização na pasta de startup do Windows:

- 

```text
C:\Users\usuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

ou

- 

Existência de **restrições de segurança**, como antivírus ou firewall ou ate mesmo acessos administradores, que impedem a execução automática do serviço.