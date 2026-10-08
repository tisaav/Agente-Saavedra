# A data de lançamento deve respeitar os parâmetros de Dias para Retroação e Dias para lançamentos futuros

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9329869905943-A-data-de-lan%C3%A7amento-deve-respeitar-os-par%C3%A2metros-de-Dias-para-Retroa%C3%A7%C3%A3o-e-Dias-para-lan%C3%A7amentos-futuros](https://ajuda.sankhya.com.br/hc/pt-br/articles/9329869905943-A-data-de-lan%C3%A7amento-deve-respeitar-os-par%C3%A2metros-de-Dias-para-Retroa%C3%A7%C3%A3o-e-Dias-para-lan%C3%A7amentos-futuros)  
> **ID:** `9329869905943` | **Última Atualização:** 2026-07-22T15:08:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701430184727)

 MENSAGEM:**

[CORE_E04090]: A data de lançamento deve respeitar os parâmetros de Dias para Retroação e Dias para lançamentos futuros.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701430190743)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701430195351)

 A data limite para retroação da baixa de títulos e lançamentos futuros, podem ser definidas no campo **"Dias para retroação da baixa"** e **"Dias para lançamentos futuros"**, localizados na tela ****["Cadastro de Usuário"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), botão ****["Outras Opções"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Configurações do Usuário".**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14495156772631)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701437504535)

 Ou ainda por meio dos parâmetros **"Dias para retroação da Baixa - DIASRETROACAO" **na tela **"Preferências" ***(Caminho de acesso: Configurações » Avançado » Preferências).*

Dias para retroação da Baixa - DIASRETROACAO: defina a data limite para retroação da baixa de títulos por meio deste parâmetro.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14495159750679)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701437509271)

 "Dias para lançamentos futuros (ref. data hoje)-DIASFUTURO": **este parâmetro é definido a partir do cadastro de usuários, campo "Dias para lançamentos futuros". Utilizado para informar o número máximo de dias em que será permitido ao usuário lançar baixas futuras. Para cada usuário será criado um parâmetro quando for informado um valor qualquer neste campo.

 

**Exemplo: **

Usuário baixando um título no dia 01/06/2004 e no campo **"Data da baixa"** informando 23/06/2004. Se os dias para lançamentos futuros forem menor que 24, o sistema não permitirá a confirmação da baixa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14495213214999)

 

**Observações: ****é fundamental a configuração dos valores padrões dos parâmetros DIASFUTURO e DIASRETROACAO no usuário SUP**, definindo uma configuração geral que atenda a todos os usuários responsáveis pelas baixas, com as permissões mínimas necessárias. **Usuários gestores, que podem precisar de limites mais amplos e personalizados, devem ter suas configurações ajustadas de forma individual.**

Os referidos parâmetros estão associados ao usuário SUP. Portanto, o valor configurado será aplicado como padrão geral para todos os usuários que realizam baixas, exceto para aqueles com configurações personalizadas.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16701430211095)

 CAUSA:**

Quando usuário logado não possui permissão para fazer lançamentos com data retroativa ou baixa futura.


---

### 🔗 Links e Referências Internas:

- ["Cadastro de Usuário"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- ["Outras Opções"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es)