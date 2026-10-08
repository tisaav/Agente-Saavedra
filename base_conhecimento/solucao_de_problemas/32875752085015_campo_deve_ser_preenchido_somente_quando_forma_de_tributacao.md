# Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32875752085015-Campo-deve-ser-preenchido-somente-quando-Forma-de-Tributa%C3%A7%C3%A3o-do-Lucro-abranger-o-Lucro-Presumido](https://ajuda.sankhya.com.br/hc/pt-br/articles/32875752085015-Campo-deve-ser-preenchido-somente-quando-Forma-de-Tributa%C3%A7%C3%A3o-do-Lucro-abranger-o-Lucro-Presumido)  
> **ID:** `32875752085015` | **Última Atualização:** 2026-07-25T16:29:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33153316441751)

 MENSAGEM**

Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido. Ou seja, o campo forma_trib deve ser igual a 3, 4, 5 ou 7

 

![506374713_1694747224513085_7359397908934389491_n.png](https://ajuda.sankhya.com.br/hc/article_attachments/33183390239511)

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33153322815895)

 **SITUAÇÃO**

O campo ''**TIP_ESC_PRE''** só deve ser preenchido se a empresa estiver **tributando pelo Lucro Presumido**. Os valores válidos para **forma_trib** são:

- 
**3** – Lucro Presumido

- 
**4** – Lucro Presumido – Imunes

- 
**5** – Lucro Presumido – Isentas

- 
**7** – Lucro Presumido – SCP

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33153316453527)

**SOLUÇÃO **

No Sankhya, acesse a tela ''**Empresa'' '**(Contabilidade'' > ''Preferências), aba **''ECF- Escrituração Contábil Fiscal**'' e sub-aba ''**Parâmetros de tributação**'':

- Quando o campo **''Forma de Tributação''** está Lucro Real, o Campo **''Escrituração'' **não deve ter configuração.

 

![image.png](https://ajuda.sankhya.com.br/hc/article_attachments/33153322826775)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33179173213591)

****AMBIENTE E CAUSA DO ERRO:** 

Se o campo ''**forma_trib''** estiver com um valor diferente, como, por exemplo, **1 –** Lucro Real**, **e ainda assim o campo ''**TIP_ESC_PRE'',** for preenchido, isso resultará no erro exibido. 

**Registro: **0010 – Parâmetros de Tributação

**Campo com erro:** TIP_ESC_PRE (Tipo de Escrituração do Lucro Presumido)