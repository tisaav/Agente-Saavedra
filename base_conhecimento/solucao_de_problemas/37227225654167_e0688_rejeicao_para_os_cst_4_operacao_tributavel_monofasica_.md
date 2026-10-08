# E0688 Rejeição: Para os CST "4 - Operação Tributável monofásica - Revenda a Alíquota Zero" ou "6 - Operação Tributável a Alíquota Zero", o valor das alíquotas para PIS e COFINS devem ser preenchidas com zero (0,00%).

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37227225654167-E0688-Rejei%C3%A7%C3%A3o-Para-os-CST-4-Opera%C3%A7%C3%A3o-Tribut%C3%A1vel-monof%C3%A1sica-Revenda-a-Al%C3%ADquota-Zero-ou-6-Opera%C3%A7%C3%A3o-Tribut%C3%A1vel-a-Al%C3%ADquota-Zero-o-valor-das-al%C3%ADquotas-para-PIS-e-COFINS-devem-ser-preenchidas-com-zero-0-00](https://ajuda.sankhya.com.br/hc/pt-br/articles/37227225654167-E0688-Rejei%C3%A7%C3%A3o-Para-os-CST-4-Opera%C3%A7%C3%A3o-Tribut%C3%A1vel-monof%C3%A1sica-Revenda-a-Al%C3%ADquota-Zero-ou-6-Opera%C3%A7%C3%A3o-Tribut%C3%A1vel-a-Al%C3%ADquota-Zero-o-valor-das-al%C3%ADquotas-para-PIS-e-COFINS-devem-ser-preenchidas-com-zero-0-00)  
> **ID:** `37227225654167` | **Última Atualização:** 2026-07-22T14:14:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225636759)

 **MENSAGEM**

E0688 Rejeição: Para os CST "4 - Operação Tributável monofásica - Revenda a Alíquota Zero" ou "6 - Operação Tributável a Alíquota Zero", o valor das alíquotas para PIS e COFINS devem ser preenchidas com zero (0,00%).

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227242396183)

 **SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e), o usuário configurou o **Código de Situação Tributária - CST** como **"04 - Operação Tributável Monofásica - Revenda a Alíquota Zero"** ou **"06 - Operação Tributável a Alíquota Zero"** para PIS e/ou COFINS, porém **manteve valores de alíquota diferentes de zero** (0,00%) cadastrados. Ao tentar transmitir o documento, a Sefaz rejeitou a operação com a mensagem acima, pois existe uma **inconsistência entre o CST informado e o valor da alíquota**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227242396695)

 **SOLUÇÃO**

Para resolver esta rejeição, ajuste as alíquotas de PIS e COFINS para **zero (0,00%)** quando utilizar os CST's 04 ou 06:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227242399255)

 Acesse a tela **"Alíquota de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225640983)

 Localize o grupo de produtos que está gerando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225642391)

 No campo **"Cód. sit. tributária"**, verifique se está selecionada a opção **"04 - Operação Tributável Monofásica - Revenda a Alíquota Zero"** ou **"06 - Operação Tributável a Alíquota Zero"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225643287)

 Certifique-se de que o campo **"Alíquota"** esteja preenchido com **0,00%** (zero).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225644183)

 Salve as alterações realizadas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225644439)

 Acesse a tela **"Alíquota de COFINS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e repita o mesmo procedimento:

- 

Localize o grupo de produtos correspondente.

- 

Verifique se o **"Cód. sit. tributária"** está como **"04"** ou **"06"**.

- 

Confirme que a **"Alíquota"** está em **0,00%**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227225644439)

 Salve as alterações.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227242405783)

 Após ajustar as alíquotas, retorne ao documento fiscal e **recalcule os impostos** ou **regere o documento** para que as novas configurações sejam aplicadas.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37616259088791)

 Transmita novamente o documento fiscal para a Sefaz.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227242407959)

 **CAUSA**

A rejeição E0688 ocorre porque a **Sefaz valida a consistência entre o CST informado e o valor da alíquota** de PIS e COFINS. Quando o **CST é "04 - Operação Tributável Monofásica - Revenda a Alíquota Zero"** ou **"06 - Operação Tributável a Alíquota Zero"**, a legislação determina que **não há incidência de PIS e COFINS na operação**, portanto, as alíquotas devem obrigatoriamente ser **zero (0,00%)**. Se houver qualquer valor diferente de zero cadastrado, o sistema identifica uma **incompatibilidade fiscal** e rejeita o documento para garantir a conformidade tributária.