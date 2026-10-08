# Entrega Automática de Mapas

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045159614-Entrega-Autom%C3%A1tica-de-Mapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045159614-Entrega-Autom%C3%A1tica-de-Mapas)  
> **ID:** `360045159614` | **Última Atualização:** 2026-07-29T14:16:23Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311584815383)

 Módulo: **WMS > Rotinas
```

Através desta rotina, será possível a configuração de uma sequência de atividades com suas devidas prioridades. A entrega do mapa está relacionada diretamente com a ordem de prioridade da tarefa e a permissão do usuário configurada anteriormente na tela [Configuração por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354-Configura%C3%A7%C3%B5es-por-Usu%C3%A1rio).

**Nota:** será possível efetuar a pega de um ou mais mapas, desde que sejam do tipo separação; estes mapas serão impressos automaticamente, de acordo com a sua necessidade no momento da impressão, sendo que, apenas o último ficará com a tarefa em aberto. Se dentre estes surgir um mapa do tipo Armazenamento, Reabastecimento e/ou Transferência, o sistema não permitirá, para este mesmo usuário, que seja impresso nenhum outro mapa na sequência, até que seja finalizado manualmente o mapa que está em andamento.

O fechamento de qualquer mapa ocorre no próprio local de impressão com a leitura do código de barras do crachá no totem, ou seja, manualmente através do Código do Token do Usuário. Caso hajam tarefas com status **"aberto"**, o sistema irá gerar um novo mapa e disponibilizará a impressão deste; do contrário, encerrará o mapa anterior (caso seja de separação) e informará que não há tarefas pendentes no momento para o usuário em questão.

**Observação:** outra forma de realizar o fechamento do mapa (apenas no processo de separação) será através da Conferência de Checkout. Este cenário específico, ocorrerá quando o usuário de separação não empenhar-se em dar início à uma nova atividade no totem, mas o mapa de separação (finalizado fisicamente) já encontra-se disponibilizado para conferência. Desta forma, ao acessar a opção **"Conferência por pedido"** no Coletor e informar o endereço do checkout, o sistema automaticamente encerrará o mapa, permitindo a conferência.

**Importante:** o parâmetro **"Associar checkout na geração do mapa de separação - CHECKMAPAWMS"** deverá estar habilitado para que o checkout seja vinculado ao mapa de separação.

Assim, com esta funcionalidade, as tarefas serão entregues automaticamente.

Primeiramente, habilite a marcação **"Entrega Automática de Mapas"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms):

![aaaa8.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083896074)

Além disto, na tela Configuração por Usuário, vincule **"Tarefas Permitidas"** ao usuário; sendo que será possível ordenar e cadastrar a sequência de prioridade de impressão dos mapas, através do campo **"Ordem"**:

![aaaa5.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083891194)

Ainda na tela acima mencionada, na aba **"Validações"**,** **vincule a Regra ao usuário que será bipado, exclusivo para a Empresa, sendo que a  mesma deverá estar ativa:

![aaaa6.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083895954)

**Nota:** a Regra incluída na aba Validações deve estar previamente cadastrada na [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es).

Após preencher a aba Validações, devemos gerar o Token para o usuário; observe como é feito:

![aaaa7.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083893474)

Realizadas as configurações acima, na tela **"Entrega Automática de Mapas"** será possível bipar o crachá com o Código do Token, gerado na aba **"Token"** da tela [Configuração por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354-Configura%C3%A7%C3%B5es-por-Usu%C3%A1rio) (conforme demonstramos acima) e, assim, o sistema te informará a tarefa gerada para ele:

![aaaa4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083886994)

**Observação:** após bipar o crachá com o Código do Token, o mapa será impresso (se configurada uma impressora).

**Nota:** bipando o token na tela novamente, a tarefa será finalizada e a próxima, caso exista, será apresentada.

Se você desejar encerrar o mapa, basta que você utilize a tecla de atalho (F9) ou acione o botão **"Encerrar Mapa (F9)"**, informando o Código do Token e o ID do mapa que deseja finalizar:

![aaaa2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360083887034)

No botão de 

![Botão Ações FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16844847288471)

 **"Ações"** localizado ao lado do botão Encerrar Mapa (F9), são apresentadas as ações que permitem a execução de tarefas específicas de forma rápida e descomplicada. No [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) e no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) através da aba** "Ações"** é possível definir a execução de uma Rotina no Banco de dados (Stored Procedure), execução de uma Rotina Java, execução de um Script (JavaScript) ou o Lançamento de uma tela do sistema.


---

### 🔗 Links e Referências Internas:

- [Configuração por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354-Configura%C3%A7%C3%B5es-por-Usu%C3%A1rio)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms)
- [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es)
- [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773)
- [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294)