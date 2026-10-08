# Empréstimo consignado em duplicidade na contabilização

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39378065192727-Empr%C3%A9stimo-consignado-em-duplicidade-na-contabiliza%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/39378065192727-Empr%C3%A9stimo-consignado-em-duplicidade-na-contabiliza%C3%A7%C3%A3o)  
> **ID:** `39378065192727` | **Última Atualização:** 2026-07-29T13:23:23Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378019199383)

 **MENSAGEM**

Duplicidade de valores na contabilização referente ao crédito consignado do trabalhador.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39378019199511)

 **SITUAÇÃO**

Ao realizar a **Integração contábil **pela tela **"Gerenciador de folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) dos eventos de folha de pagamento, o sistema apresenta **"Duplicidade de valores"** relacionados ao empréstimo consignado. Isso ocorre quando há duas contas contábeis cadastradas para eventos distintos de crédito do trabalhador, resultando em lançamentos duplicados na contabilização.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39378065191063)

 **SOLUÇÃO**

Para corrigir a duplicidade na contabilização, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39378065191447)

 Acesse a tela de **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento **" CRED. DO TRABALHADOR"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39378065191703)

 Verifique se este evento possui conta contábil vinculada. Como o evento "CRED. DO TRABALHADOR" possui caráter meramente demonstrativo e apresenta o valor total do crédito sem considerar a margem consignável, sua integração contábil não é necessária.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39378019200919)

 Realize uma das seguintes ações para regularização:

- 

Exclua a conta contábil vinculada ao no evento** CRED. DO TRABALHADOR** na rotina **Configuração de Integração Contábil** (Pessoal+ » Cadastros » Configuração de Integração Contábil); ou

- 

Acesse a rotina **Eventos** (Pessoal+ » Cadastros » Eventos) e desmarque a opção **"Integra a Contabilidade"** no cadastro do Evento **CRED. DO TRABALHADOR**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41173995054999)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39378065191959)

 Mantenha apenas o **"Desconto Crédito Trabalhador"** com integração contábil ativa, pois este é o evento que deve gerar os lançamentos contábeis.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41173995057559)

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39378065192087)

 Para os valores já integrados incorretamente, escolha uma das opções:

- 

Retire a integração realizada e efetue nova integração com as configurações ajustadas; ou 

- 

Proceda com o ajuste manual diretamente no módulo contábil.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39378019201047)

 **CAUSA**

A duplicidade ocorre porque existem duas configurações de integração contábil relacionadas ao crédito do trabalhador. O "Evento 10108 – CRED. DO TRABALHADOR" possui caráter meramente demonstrativo e não deve ter integração contábil configurada, pois apresenta o valor total do crédito sem considerar a margem consignável. Quando os eventos "10105 – Desconto Crédito Trabalhador" e "10108 – CRED. DO TRABALHADOR" possuem contas contábeis vinculadas, o sistema gera lançamentos duplicados, comprometendo a precisão da contabilização.