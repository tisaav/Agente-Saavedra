# O parâmetro CODOBSDIFICMS está sem o código de observação para a Dif.Alíq.ICMS

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9192188846871-O-par%C3%A2metro-CODOBSDIFICMS-est%C3%A1-sem-o-c%C3%B3digo-de-observa%C3%A7%C3%A3o-para-a-Dif-Al%C3%ADq-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/9192188846871-O-par%C3%A2metro-CODOBSDIFICMS-est%C3%A1-sem-o-c%C3%B3digo-de-observa%C3%A7%C3%A3o-para-a-Dif-Al%C3%ADq-ICMS)  
> **ID:** `9192188846871` | **Última Atualização:** 2026-07-22T15:09:27Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15138514990359)

 MENSAGEM:**

[LIV_E00141]  O parâmetro CODOBSDIFICMS está sem o código de observação para a Dif.Alíq.ICMS.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15138514994455)

 CAUSA:**

Quando deseja gerar Diferencial de Alíquota mas as configurações não estão devidamente configuradas.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15138514997271)

SOLUÇÃO:**

Essa mensagem é apresentada quando o campo **Gerar Dif.Alíq.ICMS em Observação **é selecionado na tela **Registro de apuração de ICMS ***(Livros Fiscais » Relatórios » Registro de Apuração do ICMS).*

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15138450348951)

Independente da forma que a empresa trabalhe, utilizando o botão mencionado deverá configurar o parâmetro "Código da Observação para Diferença de ICMS-**CODOBSDIFICMS**" na tela **Preferências** *(Configurações » Avançado » Preferências)*, em que será informado o código referente a observação para diferença de alíquota de ICMS. Não sendo realizada a configuração mencionada, será apresentada a  mensagem citada acima.

Essa Observação é cadastrada na tela de** Observações para Notas** *(Comercial » Arquivo » Cadastros » Observações para Notas)* e  após criar a mesma deve-se acessar a tela **Preferências ***(Configurações » Avançado » Preferências)* e colocar o código da observação no parâmetro **CODOBSDIFICMS**.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9191926582423)

É importante ressaltar que, no parâmetro "Código da Observação para ICMS Complementar - **CODOBSICMSCOMP**"  na tela **Preferências ***(Configurações » Avançado » Preferências) *informe o código relacionado a observação para ICMS Complementar.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/9192091908503)

Este parâmetro não pode ser preenchido com o mesmo código informado no parâmetro citado anteriormente; caso isso ocorra, será exibida a mensagem abaixo:

** **O parâmetro **CODOBSDIFICMS** de 'Dif.Alíq.ICMS' não pode ser igual ao parâmetro **CODOBSICMSCOMP** de 'ICMS Complementar'.

Além disso, quando a geração for realizada, o sistema exibirá uma mensagem informando a quantidade de registros que foram gerados.
Caso não tenha que gerar o Diferencial de Alíquota basta não flegar o campo.