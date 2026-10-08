# Menu do Checkout

> **Módulo:** Comercial e Vendas | **Subseção:** Sankhya Checkout  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001985901-Menu-do-Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001985901-Menu-do-Checkout)  
> **ID:** `1500001985901` | **Última Atualização:** 2026-07-29T16:02:52Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315007499799)

 Módulo:** Configurações > Sankhya Checkout 
```

Ao clicar no botão 

![menu.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500001895742)

 você terá acesso às funcionalidades disponíveis no Sankhya Checkout. Assim, teremos:

[SAT](#sat)                                                                            [Cadastros](#cadastros) 

[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout)                                                            [Configurar LOG](#configurarlog)

[Central de Sincronização](#centraldesincroniza%C3%A7%C3%A3o)

![gif_do_menu_2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500001946681)

## 
SAT

Nesse menu, você pode consultar as configurações do SAT que você utiliza nas suas vendas, além de conseguir **"Ativar"** o SAT e vincular uma **"Assinatura"** à ele. 

![gif_sat.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500005211221)

**Observação:** Este menu estará disponível apenas se o **"Tipo de ambiente usado"** estiver definido como **"SAT"**.

[[voltar ao topo]](#top)

## 
Cadastros

[Impressora](#impressora)                                                   [Equipamento SAT](#equipamentosat)                                                [Perfis](#perfis)

## 
Impressora  

No menu Cadastros do Checkout, teremos algumas opções, dentre elas o cadastro de Impressoras. Através desta opção você irá cadastrar aquelas que serão utilizadas na impressão das notas fiscais das vendas:

![impressoras.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/1500002139202)

Ao habilitar a marcação **"Utilizar impressora instalada"**, o campo **"Porta"** será alterado para **"Impressora"** para que você possa selecionar a Impressora já instalada de sua preferência.

[[voltar ao subtítulo]](#cadastros)

## 
Equipamento SAT

Nesse menu, você pode editar as configurações de um SAT já configurado, adicionar outro SAT ou exclui-lo.

![registro_de_sat.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500005216501)

**Observação:** Este menu estará disponível apenas se o **"Tipo de ambiente usado" **(localizado no Cadastro de Checkout) estiver definido como **"SAT"**.

[[voltar ao subtítulo]](#cadastros)

## 
Configurar LOG

Por meio desta opção, você poderá realizar as configurações para o armazenamento de logs:

![CONFIGURAR_LOG.gif](https://ajuda.sankhya.com.br/hc/article_attachments/16806163258775)

A marcação **"Apresentar todas as informações no LOG" **fará com que o checkout grave todas as movimentações executadas. Observe que quando a marcação estiver selecionada, as opções abaixo desta, também serão automaticamente marcadas. Assim, tem-se as opções mais específicas de gravações de LOG, são elas:

- Processos de banco de dados;

- Inicialização e entrada de dados;

- Processos da aplicação;

- Integração com portais fiscais;

- Recursos compartilhados;

- Comunicação com a impressora;

- Integração com o ERP;

- Recebimentos com cartão.

Ao passar o cursor do mouse por cada uma destas opções, o sistema disponibilizará uma descrição sobre cada uma. Abaixo destas marcações, temos a linha de rastreamento, onde será configurado um número máximo de 10 arquivos do log geral; sendo assim, após atingir esse limite, o décimo primeiro subscreverá o primeiro. 

**Observação:** Cada arquivo terá no máximo 100MB.

Ao selecionar a opção** "Extrair LOG do sistema"** no menu superior direito **"Sair/Trocar de Usuário"**, o sistema gerará um arquivo zip contendo os logs no caminho em que você informar.

**Nota:** Cada tipo de log será gravado em um arquivo diferente.

[[voltar ao subtítulo]](#cadastros)

## 
Perfis

Nesse menu, temos diversas abas com diferentes funcionalidades. Observe:

## 

![checkout.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42314997070615)

Dentre estes, no pop-up **"Cadastro de Perfil"** (**"Perfil e Acessos"** > Selecione um perfil > aba **"Venda"**), temos as marcações:

**Pode alterar DAV com financeiros:** Quando desabilitada, ao utilizar dois Tipos de Negociações diferentes em uma venda no perfil do usuário que executá-la, o sistema exigirá as credenciais de um usuário que autorize a referida ação. Caso esteja habilitada, a venda será executada normalmente.

**Exigir Dav/Pré-venda na venda:** Ao efetuar esta marcação, só será possível realizar uma venda direta no caixa se no Sankhya Om estiver cadastrado um pedido de venda. Caso tente efetuar a venda sem informar este pedido/pré-venda, o sistema apresentará a mensagem abaixo:

***"Atenção! Proibido fazer venda sem Dav/Pré-venda, para prosseguir faça a liberação."***

Ao clicar em **"OK"**, será exibido um pop-up solicitando a liberação do gerente para continuação da venda direta. Já com a opção desmarcada, a venda direta no caixa será executada normalmente.

 

[[voltar ao subtítulo]](#cadastros)[[voltar ao topo]](#top)

## 
Central de Sincronização

Por meio desta opção, você poderá consultar impeditivos durante as sincronizações realizadas no sistema.

Assim, teremos o botão **"Gerenciar sincronizações"** sendo que ao clicar neste, você poderá selecionar os serviços dentro da central que gostaria de sincronizar:

![sincronizao_menor.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500001946841)

Ao clicar em **"Validar checkout"**, o sistema validará o(s) serviço(s) selecionado(s) no pop-up **"Gerenciamento de Sincronizações"**, e exibirá a mensagem:

***"Este Checkout foi validado com sucesso!***
***Todos os serviços essenciais foram inicializados"***

No quadro **"Dados da última sincronização"**, podemos consultar os dados provindos da última sincronização realizada, como a **"Data/hora"**, o **"Usuário"** que efetuou a sincronização, a **"URL do servidor"** e a **"Versão do ERP"**. Além disso, ao clicar no botão 

![image__288_.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500001947541)

 as informações de sincronizações realizadas serão atualizadas.

Ao clicar no quadro **"Movimentações que estão pendentes de exportação"**, as movimentações pendentes serão apresentadas e, ao selecionar um dos itens, o resumo deste será exibido. Caso não haja, o sistema emitirá uma mensagem o informando da ausência das exportações.

Além disso, você poderá verificar se o hardware do seu computador atende os requisitos do Checkout. Assim, caso o seu computador atenda aos requisitos necessários, o ícone 

![icone-positivo.png](https://ajuda.sankhya.com.br/hc/article_attachments/11121338440983)

 será exibido e se estes não forem cumpridos, o ícone 

![icone-negativo.png](https://ajuda.sankhya.com.br/hc/article_attachments/11121230158231)

 será apresentado. Essas informações também poderão ser consultadas na sub-aba [Informações de Hardware](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053#abavis%C3%A3ogeral) da tela [Menu do Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053):

![painel-informacoes-de-hardware.png](https://ajuda.sankhya.com.br/hc/article_attachments/11121218980887)

As falhas que poderão ocorrer durante as instalações e/ou sincronizações do Checkout, serão mostradas na grade abaixo junto aos seus motivos:

![grade_do_checkout__1_.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/360102956793)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout)
- [Informações de Hardware](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053#abavis%C3%A3ogeral)
- [Menu do Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053)