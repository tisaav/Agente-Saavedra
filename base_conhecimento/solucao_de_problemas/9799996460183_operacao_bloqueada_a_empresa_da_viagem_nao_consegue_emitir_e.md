# Operação Bloqueada A empresa da viagem não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9799996460183-Opera%C3%A7%C3%A3o-Bloqueada-A-empresa-da-viagem-n%C3%A3o-consegue-emitir-esse-documento-por-estar-configurada-com-ambiente-produ%C3%A7%C3%A3o-em-uma-base-de-teste](https://ajuda.sankhya.com.br/hc/pt-br/articles/9799996460183-Opera%C3%A7%C3%A3o-Bloqueada-A-empresa-da-viagem-n%C3%A3o-consegue-emitir-esse-documento-por-estar-configurada-com-ambiente-produ%C3%A7%C3%A3o-em-uma-base-de-teste)  
> **ID:** `9799996460183` | **Última Atualização:** 2026-07-22T15:06:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19480724557591)

 MENSAGEM:**

[CORE_E05565] Operação Bloqueada: A empresa da viagem não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste. Avise o administrador para que o mesmo ajuste o registro da base na tela de Administração do servidor.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19480711594775)

 SITUAÇÃO:**

Ao gerar o lote das notas a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19480711596951)

 CAUSA:**

Quando a base está registrada como teste incorretamente.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19480724574231)

 SOLUÇÃO:**

Acesse a tela **Administração do Servidor** *(Caminho de acesso à tela: Configurações » Avançado » Administração do Servidor),* vá até aba 'Registro de Base de Dados' e verifique se a base está registrada como "Teste", sendo assim, é necessário que seja alterada para "Produção"

![adm do servidor 01-12.png](https://ajuda.sankhya.com.br/hc/article_attachments/19480711610647)

![Aviso_importante.gif](https://ajuda.sankhya.com.br/hc/article_attachments/9799994226967)

 Cuidado ao alterar o tipo da base pois cada tipo tem suas restrições.