# Erro MS1441 - vlrBaseAgreg e Erro MS1449 - vlrAgreg - EFD Reinf

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26998637309463-Erro-MS1441-vlrBaseAgreg-e-Erro-MS1449-vlrAgreg-EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/26998637309463-Erro-MS1441-vlrBaseAgreg-e-Erro-MS1449-vlrAgreg-EFD-Reinf)  
> **ID:** `26998637309463` | **Última Atualização:** 2026-07-22T14:40:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27118915562135)

 ****MENSAGEM**

**Erro MS1441 - vlrBaseAgreg** - Informação permitida apenas se, para a natureza do rendimento informada em (natRend), houver 'Agregado' na coluna 'Tributo' da Tabela 1. Localiza??o: - Campo: vlrBaseAgreg - XPATH: /Reinf/evtRetPJ/ideEstab/ideBenef/idePgto/infoPgto/retencoes/vlrBaseAgreg

 

**Erro MS1449 - vlrAgreg** - Informação permitida apenas se, para a natureza do rendimento informada em (natRend), houver 'AGREGADO' na coluna 'Tributo' da Tabela 1. Localiza??o: - Campo: vlrAgreg - XPATH: /Reinf/evtRetPJ/ideEstab/ideBenef/idePgto/infoPgto/retencoes/vlrAgreg

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27118899046551)

SOLUÇÃO:**

Para corrigir os erros **MS1441** e **MS1449**, é necessário identificar as naturezas de rendimento associadas a tributos **agregados**. Essas informações são fundamentais para determinar quando os campos relacionados a agregados podem ser preenchidos.

**Tabela 1: **[http://sped.rfb.gov.br/arquivo/show/7134](http://sped.rfb.gov.br/arquivo/show/7134)

 

No link acima é possível baixar a tabela 1 que está disponível na extensão [xlsx](http://sped.rfb.gov.br/arquivo/download/7134), e na tabela tem uma coluna nomeada de tributo. Ao criar um filtro, pode-se filtrar nessa tabela as naturezas de rendimentos com tipo de tributo agregado.

 

![Erro MS1441 - vlrBaseAgreg e Erro MS1449 - vlrAgreg - EFD Reinf 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27116305636887)

 

Na tela **"Impostos",** sub-abas **"Parceiro"**,** "TOP", "Empresa", "Grupo de Produto", "Produto", "Serviço", **informe o Código da Receita no campo **"Cód.Receita"** que indica recolhimento com cálculo

 

![Erro MS1441 - vlrBaseAgreg e Erro MS1449 - vlrAgreg - EFD Reinf 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/27116305645591)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27118915570199)

CAUSA:**

Na **EFD-Reinf** as naturezas de rendimento e seus respectivos tributos (incluindo se são agregados ou não) estão listados na **Tabela 1** do manual da EFD-Reinf, que é essencial para definir corretamente os valores que podem ser informados nos campos como vlrBaseAgreg e vlrAgreg.