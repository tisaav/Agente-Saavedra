# ORA-20101: Para salvar um funcionário novo com vínculo de prazo indeterminado selecione a opção *Dispensado do período de experiência

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35314856211479-ORA-20101-Para-salvar-um-funcion%C3%A1rio-novo-com-v%C3%ADnculo-de-prazo-indeterminado-selecione-a-op%C3%A7%C3%A3o-Dispensado-do-per%C3%ADodo-de-experi%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/35314856211479-ORA-20101-Para-salvar-um-funcion%C3%A1rio-novo-com-v%C3%ADnculo-de-prazo-indeterminado-selecione-a-op%C3%A7%C3%A3o-Dispensado-do-per%C3%ADodo-de-experi%C3%AAncia)  
> **ID:** `35314856211479` | **Última Atualização:** 2026-07-29T13:20:51Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628382480535)

 **MENSAGEM**

ORA-20101: Para salvar um funcionário novo com vínculo de prazo indeterminado selecione a opção *Dispensado do período de experiência*
ORA-06512: em "SANKHYA.TRG_VINCULOS_TFPFUN", line 18
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_VINCULOS_TFPFUN'

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628382481815)

 **SITUAÇÃO**

Durante a **admissão de um novo colaborador** no sistema, ao tentar salvar o cadastro do funcionário, a mensagem de erro é apresentada. Isso ocorre quando o usuário seleciona um **tipo de vínculo inadequado** para a situação do funcionário que está sendo cadastrado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628353266583)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628353268119)

 Acesse o cadastro do funcionário e verifique o **tipo de vínculo** selecionado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628382489239)

 Se o funcionário está entrando em **contrato de experiência**, selecione o vínculo de **prazo determinado**.

 

![ORA-20101 Para salvar um funcionário novo com vínculo de prazo indeterminado.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628382494743)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628353274519)

 Utilize a opção **"Dispensado do período de experiência"** apenas quando:
• O colaborador já tiver cumprido os 90 dias de experiência em contrato anterior
• For contratado diretamente em prazo indeterminado (casos específicos permitidos pela CLT)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628382498199)

 Salve o cadastro após realizar os ajustes necessários.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628353284887)

 **CAUSA**

O erro ocorre porque foi selecionada a opção de vínculo **"10 – Prazo indeterminado pessoa jurídica"** para um funcionário **pessoa física**, cuja contratação deve obedecer às regras da **CLT**. Segundo a legislação trabalhista, novos colaboradores contratados sob o regime da CLT devem inicialmente passar pelo **contrato de experiência** de até **90 dias**, configurando vínculo **por prazo determinado**. Somente após a conclusão do período de experiência é que o vínculo pode ser efetivado como **prazo indeterminado**.