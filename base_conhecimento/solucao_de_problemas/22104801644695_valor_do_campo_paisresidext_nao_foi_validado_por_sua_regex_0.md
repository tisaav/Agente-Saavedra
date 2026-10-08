# Valor do campo paisResidExt nÃo foi validado por sua regex [0-9]{3}. [60]

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/22104801644695-Valor-do-campo-paisResidExt-n%C3%83o-foi-validado-por-sua-regex-0-9-3-60](https://ajuda.sankhya.com.br/hc/pt-br/articles/22104801644695-Valor-do-campo-paisResidExt-n%C3%83o-foi-validado-por-sua-regex-0-9-3-60)  
> **ID:** `22104801644695` | **Última Atualização:** 2026-07-22T14:49:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22104785048727)

 **MENSAGEM:**

Valor do campo paisResidExt nÃo foi validado por sua regex [0-9]{3}. [60].

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/22104801637015)

SOLUÇÃO:**

O código do cadastro do país, informando na tela PAÍSES, campo "País Domicílio Fiscal", tem que estar configurado com um código de acordo com a [tabela 7](http://sped.rfb.gov.br/estatico/AE/C60E9D9BF5128AA07A232DAA39A6A42F8D7724/Leiautes%20da%20EFD-Reinf%20v1.1%20-%20Anexo%20I%20-%20Tabelas.pdf) do REINF, para que no momento da geração dos registros do grupo 4000 puxe a informação correta para a tag paisResidExt.