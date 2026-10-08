# Código de Terceiros incompatível com o FPAS informado

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043730174-C%C3%B3digo-de-Terceiros-incompat%C3%ADvel-com-o-FPAS-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043730174-C%C3%B3digo-de-Terceiros-incompat%C3%ADvel-com-o-FPAS-informado)  
> **ID:** `360043730174` | **Última Atualização:** 2026-07-29T13:21:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198855965463)

 MENSAGEM:**

Erro 247 - Código de Terceiros incompatível com o FPAS informado.
Ação Sugerida: Para classificação tributária igual a [01, 02, 03, 04], informar 0000. Nos demais casos, o valor informado no campo deverá ser compatível com o código FPAS que consta na Tabela 4 (Códigos e Alíquotas de FPAS/Terceiros).
Elemento: /eSocial/evtTabLotacao/infoLotacao/inclusao/dadosLotacao/fpasLotacao/codTercs [0000]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198855966743)

 SOLUÇÃO**:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198840987159)

 Para correção, siga os passos abaixo de acordo com produto utilizado:

#### 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309886595991)

 PESSOAL + / W **

Acesse Pessoal+ » Cadastros » Registro Fiscal >> aba **"Geral" **campo **"Códigos INSS Terceiros".**

Verifique o valor informado no campo INSS Terceiros, que dever ser compatível com o campo **"Cód. FPAS"**, também informado nessa tela. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/25777127357719)

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309886595991)

 MGE Pessoal **

Acesse *MGEPessoal » Avançado » Registro Fiscal*, aba **"****Informações", **campo **"Códigos INSS Terceiros".**

Verifique o valor informado no campo INSS Terceiros, que dever ser compatível com o campo **"Cód. FPAS"**, também informado nessa tela. 

 

![INSS_TERCEIROS.png](https://ajuda.sankhya.com.br/hc/article_attachments/14466902036247)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198855970839)

 No Anexo I dos Leiautes do eSocial versão S-1.2 Tabela 04 - Códigos e Alíquotas de FPAS/Terceiros consta as compatibilidades entre os códigos de terceiros e FPAS;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198855970839)

 Para o preenchimento correto, busque orientações com Contador/Jurídico validando inclusive a classificação tributária da empresa.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198855972631)

 Após os ajustes, gere os eventos e libere o S-1200.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198840994711)

 CAUSA**:

Ocorre devido à falta de compatibilidade entre o código INSS Terceiros com o código FPAS do Registro Fiscal da Respectiva empresa do arquivo. Incidente ao tentar enviar o S-1020.