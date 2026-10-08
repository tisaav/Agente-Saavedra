# Erro no Cálculo de Décimo Terceiro para Contrato Suspenso

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39340252616855-Erro-no-C%C3%A1lculo-de-D%C3%A9cimo-Terceiro-para-Contrato-Suspenso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340252616855-Erro-no-C%C3%A1lculo-de-D%C3%A9cimo-Terceiro-para-Contrato-Suspenso)  
> **ID:** `39340252616855` | **Última Atualização:** 2026-08-10T15:12:01Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39340252597655)

 **MENSAGEM**

O sistema está calculando décimo terceiro salário para funcionário com contrato suspenso.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39340252598551)

 **SITUAÇÃO**

Ao processar o cálculo de décimo terceiro salário, o sistema está considerando funcionários que possuem **"contrato suspenso"**, gerando valores indevidos para colaboradores que não deveriam receber este benefício durante o período de suspensão.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39340236342551)

 **SOLUÇÃO**

Para corrigir o cálculo indevido do décimo terceiro salário, ajuste as configurações da ocorrência de afastamento:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39340236343319)

 Acesse a tela **"Código de Afastamento"** (Pessoal+ » Cadastros » Código de Afastamento).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41081432731799)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39340236344087)

 Localize a ocorrência de afastamento  (**Pessoal+ » Rotinas Folha » Ocorrências ) **que foi lançada para o funcionário com contrato suspenso.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39340252601751)

 Identifique as descrições informadas nos campos **"Descrição FGTS"** e **"Descrição RAIS"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41081432732695)

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39340252602263)

 Desmarque a opção **"Direito ao Décimo Terceiro"** para a ocorrência correspondente, na tela "Código de Afastamento"

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41081432733719)

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39340236346263)

 Salve as alterações e recalcule o décimo terceiro salário para validar que o valor não será mais gerado para o funcionário.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39340236347031)

 **CAUSA**

O erro ocorre porque a ocorrência de afastamento criada para o funcionário estava configurada com a opção **"Direito ao Décimo Terceiro"** marcada. Quando essa configuração está habilitada, o sistema interpreta que o colaborador mantém o direito ao benefício mesmo durante a suspensão do contrato, gerando o cálculo indevido do décimo terceiro salário.