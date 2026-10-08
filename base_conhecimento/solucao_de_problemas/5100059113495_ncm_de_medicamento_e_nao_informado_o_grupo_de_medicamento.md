# NCM de medicamento e não informado o grupo de medicamento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/5100059113495-NCM-de-medicamento-e-n%C3%A3o-informado-o-grupo-de-medicamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/5100059113495-NCM-de-medicamento-e-n%C3%A3o-informado-o-grupo-de-medicamento)  
> **ID:** `5100059113495` | **Última Atualização:** 2026-07-22T15:18:11Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16348381432215)

 MENSAGEM:** 

Rejeição 840 - NCM de medicamento e não informado o grupo de medicamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16348397643159)

 CAUSA: **

Este erro ocorre devido as novas regras de validação da Nota Técnica 2021.004, que é a validação sobre o  GRUPO MED, ou seja, grupo de medicamento no XML.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16348397645463)

 SOLUÇÃO: **

Os medicamentos são classificados nos NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15776088610711)

 

Para gerar as tags de Medicamento no XML, consulte o artigo: 

- [Quais as configurações para gerar as TAG de Medicamento no XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000927421-Quais-as-configura%C3%A7%C3%B5es-para-gerar-as-TAG-de-Medicamento-no-XML-)

O texto da NT traz a seguinte instrução: 

2.2.1. Criação da Regra de Validação K01-10 Regra de validação para obrigar o preenchimento do grupo de medicamento (campo: med.) quando o código NCM do produto for de medicamento (NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006).

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16348397649047)

 OBSERVAÇÃO: **

Se o produto não for medicamente altere o NCM para diferente de 3001, 3002, 3003, 3004, 3005 e 3006.


---

### 🔗 Links e Referências Internas:

- [Quais as configurações para gerar as TAG de Medicamento no XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000927421-Quais-as-configura%C3%A7%C3%B5es-para-gerar-as-TAG-de-Medicamento-no-XML-)