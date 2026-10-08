# Nota 'X' DENEGADA não pode ser Cancelada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697993-Nota-X-DENEGADA-n%C3%A3o-pode-ser-Cancelada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697993-Nota-X-DENEGADA-n%C3%A3o-pode-ser-Cancelada)  
> **ID:** `360043697993` | **Última Atualização:** 2026-07-22T16:02:41Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16163259912983)

**MENSAGEM**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/16163259915287)

**SITUAÇÃO**

A Nota Fiscal Eletrônica foi **denegada pela ****SEFAZ** em razão de irregularidade fiscal do destinatário. No entanto, o sistema ainda apresenta o status como **“Enviada”**.

Ao tentar excluir, cancelar ou realizar qualquer alteração na nota, a ação é bloqueada pelo sistema, em função do status atual apresentado.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16163274096535)

**SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16163259918615)

 Certifique-se de que o sistema esteja atualizado para a versão **4.35b243** ou superior. Essa versão contempla a correção do problema em que notas denegadas permaneciam com status incorreto.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16163259919767)

 Além disso, acesse a tela **“Empresa”** (Comercial >> Preferências) e verifique se a **“NT 2024.001”** está devidamente ativa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39543455291543)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/16163259921687)

 Na tela **"Tipo de Operação - TOP"** (*Comercial >> Arquivo >> Cadastros*), localize a TOP utilizada na emissão da nota.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/16163274107031)

 Acesse a aba **"NF-e/NFC-e/CF-e"** e verifique o campo **"Tipo de operação NF-e Denegada". **Caso esteja preenchido remova a TOP Denegada, deixando em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39543455293079)

 Retorne à tela **"Portal de Vendas"** (*Comercial >> Consulta*) e utilize a opção "**NF-e**" >> **"Consulta situação atual da nota" **para que o sistema atualize corretamente o status conforme o retorno da SEFAZ.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39543455293591)

Execute as seguintes ações: notifique o parceiro sobre a irregularidade fiscal e, após a devida correção por parte dele, realize a transmissão da NF-e novamente. Caso não deseje prosseguir, é necessário inutilizar a numeração e excluir a nota. 

Ressaltamos que notas denegadas não devem ser canceladas. Após mudanças realizadas pela SEFAZ, a nota passará a ser retornada com rejeição, permitindo assim o seu reaproveitamento após a devida correção.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16163259927063)

**CAUSA**

Desde agosto de 2024, a SEFAZ alterou o tratamento das notas denegadas. Conforme o Ajuste SINIEF nº 43/2023, o evento de denegação de NF-e foi descontinuado.

Dessa forma, as irregularidades passaram a retornar como **Rejeição 307 – Emitente bloqueado pela UF de destino**, deixando o documento com status **“Aguardando Correção”**.