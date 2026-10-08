# S-1200 Erro 8 - Grupo 'Remuneração no período de apuração' deve ser preenchido. Verifique as condições de preenchimento no leiaute. Elemento: /eSocial/evtRemun/dmDev

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/5127698536471-S-1200-Erro-8-Grupo-Remunera%C3%A7%C3%A3o-no-per%C3%ADodo-de-apura%C3%A7%C3%A3o-deve-ser-preenchido-Verifique-as-condi%C3%A7%C3%B5es-de-preenchimento-no-leiaute-Elemento-eSocial-evtRemun-dmDev](https://ajuda.sankhya.com.br/hc/pt-br/articles/5127698536471-S-1200-Erro-8-Grupo-Remunera%C3%A7%C3%A3o-no-per%C3%ADodo-de-apura%C3%A7%C3%A3o-deve-ser-preenchido-Verifique-as-condi%C3%A7%C3%B5es-de-preenchimento-no-leiaute-Elemento-eSocial-evtRemun-dmDev)  
> **ID:** `5127698536471` | **Última Atualização:** 2026-07-29T13:23:52Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/40923924025239)

**MENSAGEM**

Erro 8 - Grupo 'Remuneração no período de apuração' deve ser preenchido. Verifique as condições de preenchimento no leiaute. Elemento: /eSocial/evtRemun/dmDev [].

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/40923952808087)

**SITUAÇÃO**

Este erro ocorre ao tentar enviar o evento **"S-1200 (Remuneração de Trabalhador)"** para o eSocial. O sistema identifica que há informações de remuneração que precisam ser enviadas, porém o grupo de dados obrigatório não está devidamente preenchido ou estruturado na folha de pagamento.

**REAJUSTE CCT–** campo para informar se aquela folha refere-se a uma folha complementar decorrente de um reajuste sindical ou não. Se for um dissídio, marcar a opção, se não for deixar sem marcação.

**PROCESSO–** Têm que trazer a informação do processo cadastrado na tela do sindicato.

**DSC–** É um campo texto, que carrega a informação do campo 'Descrição Origem do Pagamento' da tela de cálculo de rescisão complementar 'Cálculos >> Individuais >> Complementar para Desligados (exceto sindical)'.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/40923924026391)

**SOLUÇÃO**

### **Folha complementar por reajuste sindical (dissídio) - Pessoal G:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250397719)

 Acesse o cadastro do sindicato:

 

**

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/5128328511639)

**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250399639)

 Realize o cadastro da CCT a qual deseja realizar o cálculo, se atentando sempre a preencher os campos obrigatórios para o eSocial: nº do Processo, Reaj. Sindical e Descrição.

 

![Erro 8 - Grupo 'Remuneração no período de apuração' deve ser 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250406935)

 

### **Folha complementar por reajuste sindical (dissídio) - Pessoal +:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250397719)

 Acesse o cadastro do sindicato: Pessoal+ » Cadastros » Sindicato

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250399639)

 Realize o cadastro da CCT a qual deseja realizar o cálculo, se atentando sempre a preencher os campos obrigatórios para o eSocial: nº do Processo, Reaj. Sindical e Característica.

 

![Erro 8 - Grupo 'Remuneração no período de apuração' deve ser 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349267372567)

 

### **Folha complementar por outros motivos que não seja sindical - Pessoal G:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250397719)

 Acesse a tela: Cálculos > Individuais > Complementar p/ Desligados (exceto sindical):

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/5149857492631)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250399639)

 Preencha o campo **"Descrição"**, pois este campo é obrigatório para o eSocial. Caso ele não esteja preenchido acontece o erro.

 

![Erro 8 - Grupo 'Remuneração no período de apuração' deve ser 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250410391)

 

### **Rescisão complementar por outros motivos que não seja sindical - Pessoal +:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250397719)

 Acesse a tela: Pessoal+ » Rotinas Folha » Cálculos, escolha individual e, em seguida, **"Rescisão Complementar".**

 

![Erro 8 - Grupo 'Remuneração no período de apuração' deve ser 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349267381655)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349250399639)

 Preencha o campo Descrição, pois este campo é obrigatório para o eSocial. Caso ele não esteja preenchido acontece o erro.

 

![Erro 8 - Grupo 'Remuneração no período de apuração' deve ser 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/16349267383575)

 

**Observação:** Após verificar que todo o processo foi realizado de forma correta e, ainda assim, o erro persiste, entre em contato com o Service Desk para análise mais detalhada do caso concreto, pois erros parecidos podem ocorrer para outras situações.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/40923924026647)

**CAUSA**

O sistema não localiza informações de remuneração estruturadas corretamente. Como os dados obrigatórios (Processo, Descrição) ausentes em folhas complementares ou dissídios;