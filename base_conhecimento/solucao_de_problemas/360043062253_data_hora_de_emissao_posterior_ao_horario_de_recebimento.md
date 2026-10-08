# Data-Hora de Emissão posterior ao horário de recebimento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062253-Data-Hora-de-Emiss%C3%A3o-posterior-ao-hor%C3%A1rio-de-recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062253-Data-Hora-de-Emiss%C3%A3o-posterior-ao-hor%C3%A1rio-de-recebimento)  
> **ID:** `360043062253` | **Última Atualização:** 2026-07-22T16:09:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473951668119)

 MENSAGEM:**

[703-Rejeição]: Data-Hora de Emissão posterior ao horário de recebimento.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473936110487)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473936111767)

 Verifique, com a área de TI da empresa, se o horário do servidor do Banco de Dados está com a hora adiantada. Verifique o fuso horário local e ajuste a Data/Hora do servidor.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473951673239)

 Acesse a NF-e e verifique os campos de "**Data do Cabeçalho"**, "**Data de Negociação"**, "**Data de Ent./Saída"**, "**Data de Movimento"** e "**Data de Faturamento"**.

Verifique se a Data de Movimento está com a mesma data, das Data de Negociação e Data de Faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473951678615)

 CAUSAS:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473936111767)

 Quando uma NF-e/NFC-e é emitida com Data/Hora de Emissão 2018-05-19T08:30:00-03:00  e na SEFAZ quando recebeu o documento era  2018-05-19T08:00:00-03:00, então ocorre a rejeição.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473951673239)

 Quando emite uma NF-e/NFC-e durante o horário de verão, para Sefaz SP (São Paulo), que sofreu mudança em seu horário. Na NF-e/NFC-e, foi informada data-hora de emissão igual a "2018-10-17T10:00:00-03:00" e na Sefaz, com o horário de verão, o GMT passa de "-03:00" para "-02:00". No momento da recepção da NF-e/NFC-e, a data-hora da Sefaz era igual a "2018-10-17T10:00:00-02:00". 

Pela diferença entre o GMT informado na NF-e/NFC-e e o servidor da Sefaz, o documento será rejeitado.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473951683351)

 OBSERVAÇÕES:**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458226887959)

 É comum durante o horário de Verão Brasileiro² esta rejeição ocorrer com maior frequência, pois ocorre ajustes nos horários dos Servidores da SEFAZ, porém os clientes se esquecem de ajustar o horário do Servidor de Banco de Dados.

 

*

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458226887959)

 *O horário de verão foi aplicado por decreto nas regiões Sul, Sudeste e Centro-Oeste, desta forma os estados afetados serão: Distrito Federal, Espírito Santo, Goiás, Minas Gerais, Mato Grosso, Mato Grosso do Sul, Paraná, Rio de Janeiro, Rio Grande do Sul, Santa Catarina e São Paulo.