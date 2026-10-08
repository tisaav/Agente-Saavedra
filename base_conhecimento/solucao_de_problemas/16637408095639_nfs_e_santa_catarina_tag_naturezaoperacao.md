# NFS-e Santa Catarina - Tag <NaturezaOperacao>

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16637408095639-NFS-e-Santa-Catarina-Tag-NaturezaOperacao](https://ajuda.sankhya.com.br/hc/pt-br/articles/16637408095639-NFS-e-Santa-Catarina-Tag-NaturezaOperacao)  
> **ID:** `16637408095639` | **Última Atualização:** 2026-07-22T14:54:56Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16691685387927)

  SITUAÇÃO:**

Ao gerar NFS-e a tag <NaturezaOperacao> é apresentada diferente da impressão do documento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16637424763543)

 CAUSA:**

Santa Cataria possui algumas validações internas para que seja atribuída a natureza conforme operação da NFS-e. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16637399224599)

 SOLUÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450516206743)

Parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"** = Ligado.
Na tabela: TGFNAS são gravadas as Naturezas conforme código de Município Fiscal com suas respectivas regras. 
 

![Imagem](/attachments/token/VEzwDTQ1Z6ou1XrkgW76M7KqB/?name=image.png)

 
No exemplo acima, se trata de uma NFS-e de Serviço onde o Tomador é de outro município, e para que a NFS-e fosse aprovada na prefeitura deveria gerar no XML na TAG Natureza o Código 501, porém o sistema estava gerando o Código 111.

Nesse caso, para Gerar o código Natureza 501, na Operação o ISS Retido tem que ser Devido para Itajaí (Simples Nacional), que no caso é a cidade do Prestador, no entanto foi necessário realizar as seguintes configurações abaixo: 
 
Parâmetro **"Cidade do ISS conforme CNAE empresa? – CIDISSCNAEEMP"** = Ligado.
 
Nas preferências da **Empresa** *(Comercial » Preferências » Empresa)* aba: CNAE Empresa, deve-se informar o código do CNAE que consta na aba imposto do cadastro do Serviço, e definido o Local de Tributação de ISS = Cidade do Prestador. 
 

![Imagem](/attachments/token/993vaif4hSwmRFxco1axst5BF/?name=image.png)

 
Feito isso ao gerar uma nova NFS-e a mesma foi emitida com a Natureza 501, e aprovada com sucesso na Prefeitura.