# Melhores práticas para ajuste dos impostos PIS/COFINS

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580134-Melhores-pr%C3%A1ticas-para-ajuste-dos-impostos-PIS-COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580134-Melhores-pr%C3%A1ticas-para-ajuste-dos-impostos-PIS-COFINS)  
> **ID:** `360044580134` | **Última Atualização:** 2026-07-22T15:51:15Z

---

Abaixo serão detalhadas as melhores práticas para correções no sistema, quando detectado uma quantidade considerável de lançamentos (Notas de Entrada/Saída) com informações de PIS/COFINS incorretas.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196064458135)

 A primeira etapa será uma sintonia com o Contador da empresa, esse será o responsável por identificar os registros incorretos, instruir sobre as configurações corretas, e autorizar os devidos ajustes retroativos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196049559447)

 É de suma importância que o Contador reporte se os ajustes poderão ser realizados também para ***Notas Fiscais Eletrônicas de emissão própria***, visto que se realizados ajustes no sistema, as informações ficarão incoerentes com as informações recebidas pela SEFAZ, e impactos fiscais poderão ocorrer.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196064468631)

 O implantador da empresa e/ou usuário com conhecimento/certificação nas configurações relacionadas ao Módulo Fiscal, deverá realizar os ajustes necessários, respeitando as devidas exceções nas telas:

- 
**Alíquotas de PIS ***(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS)*

- 
**Alíquotas de COFINS ***(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS)*

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196064473495)

 Desfazer as contabilizações existentes.

Esse procedimento é necessário, visto que podem existir fórmulas para contabilização de PIS/COFINS, dessa forma a contabilização precisa ser refeita após ajustes.

**Ajuste em lançamentos já realizados, como proceder ?**

- Possuímos uma ferramenta, que após ajustes/correções nas respectivas configurações, realiza o recálculo das informações de PIS/COFINS, ajustando conforme cenário atual os lançamentos filtrados no respectivo aplicativo.

- A utilização desse aplicativo, assim como o ajuste de configurações mencionado, é de responsabilidade do cliente. Caso esse não deseje validar tais ajustes, a sua Franquia/Filial poderá ser acionado para poio junto aos consultores.

- O 'SNK calcula PIS/COFINS' será disponibilizado pelo Service Desk somente nesses casos extremos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196049568407)

 Realizados os ajustes, necessário que os Livros sejam novamente gerados (Geração ICMS/IPI), contabilização refeita, para o envio correto do EFD Contribuições ao contador.