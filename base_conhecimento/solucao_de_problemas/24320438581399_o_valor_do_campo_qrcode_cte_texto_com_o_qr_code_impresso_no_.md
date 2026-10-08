# O valor do campo QRcode CTe Texto com o QR-Code impresso no DACTE) Informado não é valido

> **Módulo:** Solucao de Problemas | **Subseção:** Distribuição  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24320438581399-O-valor-do-campo-QRcode-CTe-Texto-com-o-QR-Code-impresso-no-DACTE-Informado-n%C3%A3o-%C3%A9-valido](https://ajuda.sankhya.com.br/hc/pt-br/articles/24320438581399-O-valor-do-campo-QRcode-CTe-Texto-com-o-QR-Code-impresso-no-DACTE-Informado-n%C3%A3o-%C3%A9-valido)  
> **ID:** `24320438581399` | **Última Atualização:** 2026-07-22T14:46:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24320438566423)

 **MENSAGEM:**

[CORE E03981] O valor do campo QRcode CTe Texto com o QR-Code impresso no DACTE) Informado não é valido

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24320438569239)

 **SOLUÇÃO:**

Para solucionar o erro, primeiramente é preciso que a base esteja na versão 4.23b166 ou superior. Após verificação e adequação da versão da base, faça as seguintes configurações:

 

Acesse a tela **"Preferências"**, busque pelo parâmetro **"DATINICTEQRCOD (Data Início QR Code no CT-e)** "e nele adicione a UF da empresa e a data igual ou inferior ao dia atual (exemplo: XX:21/06/2024); 

OBS: Caso tenha mais de uma UF emitente de CTe, deve inserir as demais UF separado por ponto e vírgula: ";" 

 

![O valor do campo QRcode CTe Texto com o QR-Code impresso no DACTE) 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/24339909564951)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24339909577495)

**CAUSA:**

O erro aparece ao tentar emitir CT-e de transportes sem possuir as devidas configurações no sistema.