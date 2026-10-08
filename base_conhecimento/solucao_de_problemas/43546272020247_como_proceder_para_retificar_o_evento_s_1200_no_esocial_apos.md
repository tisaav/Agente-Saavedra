# Como proceder para retificar o evento S-1200 no eSocial após realizar ajustes em rubricas?

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546272020247-Como-proceder-para-retificar-o-evento-S-1200-no-eSocial-ap%C3%B3s-realizar-ajustes-em-rubricas](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546272020247-Como-proceder-para-retificar-o-evento-S-1200-no-eSocial-ap%C3%B3s-realizar-ajustes-em-rubricas)  
> **ID:** `43546272020247` | **Última Atualização:** 2026-09-18T11:34:50Z

---

A retificação do evento S-1200 no eSocial é necessária sempre que houver ajustes em rubricas que impactam a remuneração dos colaboradores, como alteração de incidências, códigos ou valores. O procedimento correto garante que as informações transmitidas ao eSocial estejam alinhadas com a folha de pagamento e evita inconsistências fiscais e trabalhistas.
 

Após ajustar uma rubrica (por exemplo, corrigir incidência de INSS, IRRF ou natureza da rubrica), é fundamental realizar a retificação do S-1200 para que o eSocial reconheça a alteração. O processo envolve a exclusão dos eventos de pagamento vinculados (S-1210), a reabertura e recálculo da folha, e o reenvio dos eventos periódicos.

 

Isso garante que os valores de remuneração, descontos e bases estejam corretos tanto no sistema quanto no ambiente do Governo. A simples alteração da rubrica não gera automaticamente a retificação dos eventos 

S-1200 (Remuneração) e S-1210 (Pagamentos), sendo necessário um procedimento manual para garantir a consistência dos dados.
 

### **Quando retificar o S-1200**

A retificação do S-1200 deve ser realizada sempre que houver qualquer alteração em rubricas que afete o cálculo da remuneração, como:
 

- 

**"Correção de incidências"** (INSS, IRRF, FGTS) nas rubricas;

- 

**"Alteração de códigos"** ou descrições de rubricas no cadastro;

- 

**"Inclusão ou exclusão de eventos"** que impactam o valor da folha;

- 

**"Ajustes em fórmulas"** de cálculo das rubricas;

- 

**"Atualização de natureza da rubrica"** conforme nota técnica do eSocial.

**Envie o Evento S-1010 (Tabela de Rubricas)**

- Acesse:
`Pessoal+ » Rotinas Folha » Central do eSocial`

1. Gere e envie o evento S-1010 com a nova configuração da rubrica.

1. Certifique-se de informar a data de início de vigência correta (normalmente, o início do ano-calendário afetado, ex: 01/2025).

Essas situações exigem que o evento S-1200 seja reenviado para garantir a conformidade das informações transmitidas ao eSocial.
 

### **Passo a passo para retificar o S-1200**

Siga o passo a passo abaixo para realizar a retificação do S-1200 após ajuste de rubrica:
 

1. 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43546272010263)

 Acesse a tela **"Central do eSocial"** (Pessoal+ Rotinas Folha Central do eSocial) e verifique se há eventos S-1210 vinculados ao S-1200 que será retificado.
 

1. 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43546214078743)

 Se houver, exclua primeiro o evento S-1210 referente ao período desejado. Caso o sistema impeça a exclusão devido a eventos em competências posteriores, exclua os eventos dessas competências mais recentes antes.
 

1. 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43546214081175)

 Após excluir o S-1210, exclua também o evento S-1200 da competência que precisa ser retificada.
 

1. 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43546272016407)

 Reabra a folha de pagamento da competência, realize o recálculo para considerar o ajuste da rubrica e feche novamente a folha.
 

1. 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43546272017047)

 Libere a folha para o eSocial utilizando o botão **"Liberação para eSocial"** na tela do Gerenciador de Folhas (Pessoal+ Rotinas Folha Gerenciador de Folhas).
 

1. 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/43546272017687)

 Na **"Central do eSocial"**, gere e envie novamente os eventos S-1200 e S-1210 para a competência ajustada.
 

1. 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/43546272018071)

 Após o envio, confira o retorno do eSocial para garantir que os eventos foram recepcionados sem erros.
 

### **Pontos de atenção e dicas**

 

 

 

-Sempre confira se o evento S-1010 foi aceito antes de enviar os eventos de remuneração e pagamento.

- Sempre exclua os eventos S-1210 antes do S-1200, respeitando a ordem de competências.

- Caso o sistema apresente mensagem de impedimento para exclusão, verifique se há eventos em competências posteriores e exclua-os primeiro.

- Após o recálculo da folha, confira se o ajuste da rubrica foi corretamente considerado no cálculo.

- Utilize a **"Central do eSocial"** para acompanhar o status dos eventos enviados e garantir que não há pendências.

- Em caso de dúvidas sobre incidências ou parametrizações de rubricas, consulte a legislação vigente e as orientações do eSocial.

 

 

Seguindo essas orientações, a retificação do S-1200 será realizada de forma segura, evitando inconsistências e garantindo a conformidade das informações transmitidas ao eSocial.