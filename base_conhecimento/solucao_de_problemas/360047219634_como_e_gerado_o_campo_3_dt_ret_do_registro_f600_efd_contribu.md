# Como é gerado o Campo 3 - DT_RET do Registro F600  - EFD Contribuições

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360047219634-Como-%C3%A9-gerado-o-Campo-3-DT-RET-do-Registro-F600-EFD-Contribui%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047219634-Como-%C3%A9-gerado-o-Campo-3-DT-RET-do-Registro-F600-EFD-Contribui%C3%A7%C3%B5es)  
> **ID:** `360047219634` | **Última Atualização:** 2026-07-22T15:31:58Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454040509335)

 Condições para preenchimento deste campo:

- 
**Se** os impostos forem retidos na nota, será considerada a data de negociação, para preenchimento do DT_RET;

- 
**Se** os impostos forem retidos no financeiro, sempre será considerada a data da baixa.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454040509335)

 Configurações dos impostos retidos:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532006422295)

 Na tela **"Impostos"** *(Caminho de acesso: Configurações » Cadastros » Impostos)*, configure cada imposto individualmente (não pode configurar o PCC como 'Outros', deve ser configurado PIS, depois COFINS, depois o CSLL);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532035509655)

 Para destaque na nota e retenção no financeiro, as abas** "Parceiro"**,** "TOP"** e **"Empresa"** da tela "**Impostos"**, devem estar da seguinte forma:

- Na Nota = Já Incluso

- No Financeiro Origem Financeiro = Nenhum

- No Financeiro Origem Estoque = Subtrair

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532006426903)

 Ligue o parâmetro **"DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15604131575575)