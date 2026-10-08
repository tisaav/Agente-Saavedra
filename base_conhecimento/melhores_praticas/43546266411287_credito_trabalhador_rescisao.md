# Crédito trabalhador - Rescisão

> **Módulo:** Melhores Praticas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546266411287-Cr%C3%A9dito-trabalhador-Rescis%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546266411287-Cr%C3%A9dito-trabalhador-Rescis%C3%A3o)  
> **ID:** `43546266411287` | **Última Atualização:** 2026-09-17T12:48:56Z

---

**"Rescisão não puxa parcela de crédito do trabalhador (Desconto Crédito Trabalhador não calculado na rescisão)"**

 

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43546266400151)

 SITUAÇÃO

Ao calcular a rescisão de um colaborador, o sistema não realiza o desconto referente à parcela do crédito do trabalhador (empréstimo consignado), mesmo havendo saldo devedor registrado para o funcionário.

 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/43546266400407)

 SOLUÇÃO

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43546266401047)

 No Site do empregador, confira o valor para desconto rescisório.  

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43546280204567)

 Na tela de "Lançamento de movimento" (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e realize a importação automática do crédito trabalhador. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43558788587031)

Lembrado de marcar a opção "**Rescisão**" 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43558788587927)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43546266402199)

 Confirme se o evento de **"Base Margem Crédito do Trabalhador"** está corretamente configurado e vinculado aos eventos de remuneração utilizados na rescisão.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43546280205975)

 Caso utilize eventos personalizados para remuneração, inclua-os manualmente na base de cálculo do evento de desconto do crédito do trabalhador. Tela "**Eventos**" (Pessoal+ » Cadastros » Eventos), aba de base de cálculo. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43558740647831)

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43546266403991)

 Após realizar os ajustes, recalcule a rescisão para que o desconto do crédito do trabalhador seja considerado corretamente.

 

**Observação:** os eventos padrão Sankhya já são automaticamente vinculados à base de cálculo. Eventos personalizados exigem vinculação manual.

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/43546266408471)

 CAUSA

A causa mais comum para o não desconto da parcela do crédito do trabalhador na rescisão é a ausência de vinculação dos eventos de remuneração disponíveis à base de cálculo do evento de desconto do crédito do trabalhador. Sem essa configuração, o sistema não identifica corretamente o valor a ser descontado, resultando na ausência do desconto na rescisão.

Além disso, se houver eventos personalizados de remuneração ou descontos não vinculados à base, o cálculo pode ser prejudicado. Sempre verifique a configuração das bases de cálculo e a correta parametrização dos eventos envolvidos no processo de rescisão.

Nos termos da regulamentação vigente, a realização de eventual desconto nas verbas rescisórias vinculadas à garantia da operação de crédito depende da prévia disponibilização, pela instituição consignatária, das seguintes informações: 

I – saldo devedor atualizado da operação de crédito; e 

II – percentual das verbas rescisórias oferecido em garantia pelo trabalhador no momento da contratação da operação. 

A ausência de qualquer dessas informações na data do desligamento do trabalhador inviabilizará a operacionalização do desconto sobre as verbas rescisórias. Nessa hipótese, o empregador não deverá efetuar qualquer retenção ou repasse relacionado à garantia da operação de crédito, por inexistirem os elementos necessários à apuração do valor passível de desconto.