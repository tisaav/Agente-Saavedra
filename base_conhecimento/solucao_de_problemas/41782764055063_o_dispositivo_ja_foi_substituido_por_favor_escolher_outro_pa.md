# O dispositivo ' ' já foi substituido, por favor escolher outro para realizar a troca. Data para realizar a próxima troca XX/XX/XXXX. Código: SVC_E00916'

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41782764055063-O-dispositivo-j%C3%A1-foi-substituido-por-favor-escolher-outro-para-realizar-a-troca-Data-para-realizar-a-pr%C3%B3xima-troca-XX-XX-XXXX-C%C3%B3digo-SVC-E00916](https://ajuda.sankhya.com.br/hc/pt-br/articles/41782764055063-O-dispositivo-j%C3%A1-foi-substituido-por-favor-escolher-outro-para-realizar-a-troca-Data-para-realizar-a-pr%C3%B3xima-troca-XX-XX-XXXX-C%C3%B3digo-SVC-E00916)  
> **ID:** `41782764055063` | **Última Atualização:** 2026-08-13T12:04:24Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782809617687)

 **MENSAGEM**

O dispositivo ' ' já foi substituido, por favor escolher outro para realizar a troca. Data para realizar a próxima troca XX/XX/XXXX. Código: SVC_E00916'

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782764038039)

 **SITUAÇÃO**

Ao tentar substituir o registro de licença do Coletor WMS TotalCross, por meio da tela **''Administração de Licença'' **(Contratos e Serviços » Administração de licença) , na aba **''Solicitações Pendentes''**, utilizando o botão **''Substituir Dispositivo''**, foi selecionado um dispositivo cuja licença havia sido liberada há menos de 30 dias corridos.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782764039959)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782764050327)

 Ative o parâmetro **''PERMSUBSTDISP''** - **"Permite substituir dispositivos com menos de 30 dias"**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782809621911)

 Após a ativação, será possível realizar a substituição do dispositivo mesmo que o período mínimo de 30 dias ainda não tenha sido atingido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41782809623319)

 CAUSA**

Trata-se de comportamento sistêmico, pois, nativamente foi criado o produto, para ser possível substituir o uso da licença, somente 30 dias após a liberação do dispositivo.