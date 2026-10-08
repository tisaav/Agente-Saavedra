# Eventos importados não considerados no processamento da folha

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36025831436055-Eventos-importados-n%C3%A3o-considerados-no-processamento-da-folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/36025831436055-Eventos-importados-n%C3%A3o-considerados-no-processamento-da-folha)  
> **ID:** `36025831436055` | **Última Atualização:** 2026-08-27T18:35:51Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025831430807)

** SITUAÇÃO:**

Ao importar os eventos por meio de planilha, os valores são exibidos corretamente no movimento do funcionário. Entretanto, esses valores não estão sendo considerados no cálculo da folha de pagamento, o que indica que o evento, embora importado, não está sendo processado durante a apuração da folha.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025831431703)

** SOLUÇÃO:**

Para que o sistema identifique corretamente os eventos, é necessário observar o seguinte:

- 

**Desconto:** preencher a coluna com o valor -1.

- 

**Provento:** preencher a coluna com o valor 1.

Essa configuração é essencial, pois determina se o evento será tratado como desconto ou provento durante o cálculo da folha de pagamento.

**Exemplo:**

No lançamento de uma falta (evento 102), o campo **''TIPEVENTO''** deve ser preenchido com -1, por se tratar de um desconto. Já no lançamento de hora extra (evento 50), o campo TIPEVENTO deve ser preenchido com 1, por se tratar de um provento.

![image (42).png](https://ajuda.sankhya.com.br/hc/article_attachments/36132674133783)

- 

Antes de realizar a importação na tela '**'Lançamento de Movimento**'' (Pessoal+» Rotinas Folha), é necessário preencher corretamente a coluna TIPEVENTO na planilha, conforme o tipo de cada evento, seguindo o exemplo mencionado acima.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025822661399)

** CAUSA:**

O problema ocorreu porque o campo “TIPEVENTO” não foi configurado corretamente na planilha de importação, o que impediu o reconhecimento dos eventos no cálculo da folha de pagamento.