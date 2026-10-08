# Sessões de navegadores sendo finalizadas simultaneamente em múltiplos ambientes (Produção e Teste)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31288031947927-Sess%C3%B5es-de-navegadores-sendo-finalizadas-simultaneamente-em-m%C3%BAltiplos-ambientes-Produ%C3%A7%C3%A3o-e-Teste](https://ajuda.sankhya.com.br/hc/pt-br/articles/31288031947927-Sess%C3%B5es-de-navegadores-sendo-finalizadas-simultaneamente-em-m%C3%BAltiplos-ambientes-Produ%C3%A7%C3%A3o-e-Teste)  
> **ID:** `31288031947927` | **Última Atualização:** 2026-07-22T14:33:23Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32066474997015)

 **SITUAÇÃO:**

Sistema configurado para finalizar sessão a cada X minutos conforme configuração do parâmetro **SESSIONTIMEOUT**, porém, ao expirar a sessão de um ambiente (ex: Produção), o ambiente de Teste (Homologação) também é desconectado automaticamente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31288022174231)

SOLUÇÃO:**

Não se trata de um erro do sistema Sankhya, mas sim de uma limitação técnica imposta pelo navegador quando se utiliza domínios iguais diferenciando apenas a porta.

Considere configurar domínios diferentes para os ambientes:

1. 

  - 

Exemplo:

    - 

**Produção:** [empresax.sankhya.com.br:9921](http://empresax.sankhya.com.br)

    - 

**Teste:** [teste-empresax.sankhya.com.br:9922](http://teste-empresax.sankhya.com.br:9922)

Isso permitirá que o navegador trate os cookies de forma separada, evitando que a expiração de uma sessão afete a outra.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31288022175383)

CAUSA:**

O comportamento ocorre devido à forma como os navegadores lidam com cookies de sessão. Embora os ambientes de Produção e Teste estejam sendo acessados por portas diferentes, ambos compartilham o mesmo domínio: empresax.sankhya.com.br.

Os navegadores associam os cookies ao domínio principal, ignorando a porta da URL. Assim, quando a sessão de um ambiente expira (conforme o parâmetro SESSIONTIMEOUT), o cookie de sessão é invalidado e todos os acessos vinculados ao mesmo domínio são impactados.

Por se tratar de uma limitação do navegador, não há tratativa sistêmica que permita isolar sessões entre portas distintas dentro do mesmo domínio.


---

### 🔗 Links e Referências Internas:

- [empresax.sankhya.com.br:9921](http://empresax.sankhya.com.br)
- [teste-empresax.sankhya.com.br:9922](http://teste-empresax.sankhya.com.br:9922)