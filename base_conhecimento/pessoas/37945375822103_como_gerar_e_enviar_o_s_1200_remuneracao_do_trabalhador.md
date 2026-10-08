# Como gerar e enviar o S-1200 (Remuneração do trabalhador)?

> **Módulo:** Pessoas+ | **Subseção:** Eventos Periódicos e Fechamento do eSocial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37945375822103-Como-gerar-e-enviar-o-S-1200-Remunera%C3%A7%C3%A3o-do-trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37945375822103-Como-gerar-e-enviar-o-S-1200-Remunera%C3%A7%C3%A3o-do-trabalhador)  
> **ID:** `37945375822103` | **Última Atualização:** 2026-09-27T19:07:12Z

---

**Módulo: **Pessoal+
**Caminho de Acesso: **Pessoal+ > Rotinas Folha > Central do eSocial
**ID da Tela: **br.com.sankhya.CentraleSocial

 

O evento **S-1200 – Remuneração do Trabalhador** é utilizado para informar ao eSocial os **valores da remuneração de cada trabalhador** em um determinado período de apuração.

Nesse evento são enviados, por exemplo:

- Salário mensal;

- Horas extras e adicionais;

- Descontos;

- Outras verbas que compõem a folha de pagamento.

O S-1200 é um dos **principais eventos periódicos do eSocial**, pois é a base para o cálculo de encargos como **INSS, FGTS e IRRF**, além de servir de referência para benefícios previdenciários do trabalhador.

 

### **Quem está obrigado**

 

Devem enviar o evento **S-1200** todas as empresas e empregadores obrigados ao eSocial que possuam:

- Empregados com vínculo (CLT);

- Trabalhadores avulsos;

- Diretores com vínculo empregatício;

- Outros trabalhadores que recebem remuneração pela folha.

Sempre que houver pagamento ou crédito de remuneração ao trabalhador, o envio do S-1200 é obrigatório.

 

### **Prazo de envio**

 

O evento **S-1200 deve ser enviado mensalmente**, dentro do prazo legal do eSocial.

Atualmente, o envio deve ocorrer:

- 
**Até o dia 15 do mês seguinte** ao da competência da folha;

- Quando o dia 15 cair em fim de semana ou feriado, o prazo é antecipado para o **dia útil anterior**.

💡 O S-1200 deve ser enviado **antes** do envio do evento S-1210.

 

### **Pré-requisitos**

 

Antes de gerar e enviar o evento S-1200, é necessário que os seguintes eventos já tenham sido enviados e aceitos pelo eSocial:

- **S-1000 – Informações do Empregador**

- **S-1005 – Estabelecimentos**

- **S-1010 – Tabela de Rubricas**

- **S-1020 – Lotações Tributárias**

- **S-2200 ou S-2300 – Cadastro do Trabalhador**

Além disso, é necessário:

- Folha de pagamento calculada no sistema e liberada para o eSocial;

- Certificado digital válido;

- Ambiente do eSocial configurado (Produção).

 

### **Jornada de Uso**

 

![gerar-enviar1200.gif](https://ajuda.sankhya.com.br/hc/article_attachments/37960461768471)

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37945391471511)

 Gerar o evento S-1200**

1. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha).

1. Selecione a **Empresa** e a **Referência.**

1. Certifique de que o **Ambiente** esteja em** Produção.**

1. Clique em **Carregar**.

1. No menu lateral, clique em **Geração**.

1. Clique sobre o card **Selecionar Eventos** e em seguida no evento **S-1200 – Remuneração do Trabalhador.**

1. Clique em **Iniciar Geração**.

O sistema irá gerar um evento S-1200 para cada trabalhador com remuneração na competência.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37945391472151)

 Enviar o evento ao eSocial**

1. Após a conclusão da geração, o evento S-1200 será exibido no menu **Eventos Pendentes**.

1. Clique no botão **Habilitar/Desabilitar todos** para **desabilitar todos os eventos** gerados.

1. Habilite a opção **Enviar** no card do evento **S-1200 – Remuneração do Trabalhador**.

1. Ative a opção **Utilizar a data de início padrão do sistema** e clique em **Enviar Dados**.

1. Acompanhe o processo de envio no menu **Eventos na Fila**.

1. Após o envio, o evento passa para o menu **Acompanhamento**, onde é possível verificar:

  - 

status do envio;

  - 

retorno do eSocial;

  - 

mensagens de erro ou rejeição, se houver.

1. 

Clique sobre o card correspondente para ver os detalhes do retorno do eSocial.

  - Se o evento foi enviado com sucesso, será exibido o número do recibo.

  - Em caso de erro, o sistema exibirá a mensagem retornada pelo eSocial para ajuste da rubrica.

1. Para visualizar os XML de envio e retorno, poderá clicar em **Baixar Arquivos** ou em **Visualizar Dados**.

 

### **Pontos de Atenção**

- O S-1200 é gerado **por trabalhador e por competência**;

- Qualquer ajuste na folha exige o** reenvio do S-1200**;

- O evento S-1200 está diretamente ligado aos eventos:

  - 
**S-1210 – Pagamentos**;

  - 
**S-2299 – Rescisão** (quando aplicável).

- Para que a [folha de adiantamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967) seja corretamente gerada no evento S-1200 do eSocial, é necessário que exista ao menos** um evento** calculado que **não esteja configurado apenas como É base? na tela Eventos**. Quando a folha possuir somente eventos classificados como base, o sistema poderá não gerar o S-1200 da competência.

- Erros comuns no S-1200 estão geralmente relacionados a:

  - rubricas não enviadas no S-1010;

  - trabalhador sem cadastro válido no eSocial;

  - lotações tributárias incorretas;

  - folha não calculada ou com inconsistências.

Manter o S-1200 correto e dentro do prazo garante o **fechamento adequado da folha** e evita problemas com encargos, fiscalizações e obrigações legais.


---

### 🔗 Links e Referências Internas:

- [folha de adiantamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967)