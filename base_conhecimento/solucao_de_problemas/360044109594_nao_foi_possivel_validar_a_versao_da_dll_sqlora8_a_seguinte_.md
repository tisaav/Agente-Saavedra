# Não foi possível validar a versão da dll sqlora8. A seguinte pasta não foi encontrada: C:\Program Files\Borland\Borland Shared\BDE;\ 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109594-N%C3%A3o-foi-poss%C3%ADvel-validar-a-vers%C3%A3o-da-dll-sqlora8-A-seguinte-pasta-n%C3%A3o-foi-encontrada-C-Program-Files-Borland-Borland-Shared-BDE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109594-N%C3%A3o-foi-poss%C3%ADvel-validar-a-vers%C3%A3o-da-dll-sqlora8-A-seguinte-pasta-n%C3%A3o-foi-encontrada-C-Program-Files-Borland-Borland-Shared-BDE)  
> **ID:** `360044109594` | **Última Atualização:** 2026-07-22T15:54:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613025282839)

 MENSAGEM**:

Não foi possível validar a versão da dll sqlora8. A seguinte pasta não foi encontrada: C:\Program Files\Borland\Borland Shared\BDE;\

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613025287063)

 CAUSA**:

Ocorre quando ao final do diretório de instalação do BDE, existe o carácter ;(ponto-e-virgula), se faz necessário retirar através do Regedit.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613000478103)

 SOLUÇÃO**:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613025293847)

 Acesse o Editor de Registro do Windows, digite 'Regedit' na barra de pesquisa.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360063059033)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613025299479)

 Acesse o caminho:
\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Borland\Database Engine

Nome do Valor:** DLLPATH**
Dados do Valor:  **DE**: C:\Program Files\Borland\Borland Shared\BDE;\
**                            Para:** C:\Program Files\Borland\Borland Shared\BDE\

Ou seja retire o caracter ; (ponto-e-virgula).

![2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360063059053)

-Caso o caminho seja outro e mesmo assim ao final tenha o carácter ';' faça o procedimento retirando o carácter apenas.

-Este processo deve ser feito em cada Computador, que ocorrer o incidente