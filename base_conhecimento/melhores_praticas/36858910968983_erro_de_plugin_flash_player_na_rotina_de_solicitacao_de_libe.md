# Erro de Plugin Flash Player na Rotina de Solicitação de Liberação de Computadores

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36858910968983-Erro-de-Plugin-Flash-Player-na-Rotina-de-Solicita%C3%A7%C3%A3o-de-Libera%C3%A7%C3%A3o-de-Computadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/36858910968983-Erro-de-Plugin-Flash-Player-na-Rotina-de-Solicita%C3%A7%C3%A3o-de-Libera%C3%A7%C3%A3o-de-Computadores)  
> **ID:** `36858910968983` | **Última Atualização:** 2026-07-22T14:22:22Z

---

Ao acessar a rotina de **Solicitação de Liberação de Computadores** pelos dos navegadores atuais (Chrome, Edge, etc.), o usuário se depara com erro relacionado ao **plugin**** do Flash Player**, ou percebe que a tela não abre em **HTML5**,** **exibindo apenas a versão em **Flex**.

Como o Flash Player foi descontinuado em 2021, qualquer rotina que ainda dependa desse recurso não será carregada corretamente nos navegadores, resultando nesse tipo de erro.

 

#### **Procedimento**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881449742743)

 Atualize o sistema para a versão 4.35 ou superior**

A rotina passa a funcionar em **HTML5** somente a partir da versão 4.35. Portanto, para utiliza-lá corretamente via navegador, é **obrigatória a atualização do ambiente**.

Se o sistema estiver em versão anterior, o acesso Web continuará tentando abrir a interface em **Flex**, o que resultará no erro mencionado.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36881465057687)

 Verifique se há argumento forçando a abertura em Flex**

No servidor de aplicação, revise os argumentos de inicialização da JVM.

Caso exista o argumento abaixo, ele deve ser removido para permitir a execução em HTML5:

 

```text
-Dskw.tela.identificacao.pc.flex=true
```

 

Após a remoção, reinicie o serviço do servidor de aplicação, WildFly ou Tomcat, conforme o ambiente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36858910958359)

CAUSA:**

A rotina de **Solicitação de Liberação de Computadores** passou a estar disponível em **HTML5** **somente a partir da versão 4.35** do sistema.

Em versões anteriores, ela continua funcionando apenas em **Flex**, o que faz com que, ao tentar acessá-la pelo navegador, ocorre o erro relacionado ao **plugin do Flex**, já que essa tecnologia não é mais compatível com os navegadores atuais.