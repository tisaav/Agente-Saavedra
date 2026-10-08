# Número da parcela inválido ou não informado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487093-N%C3%BAmero-da-parcela-inv%C3%A1lido-ou-n%C3%A3o-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048487093-N%C3%BAmero-da-parcela-inv%C3%A1lido-ou-n%C3%A3o-informado)  
> **ID:** `360048487093` | **Última Atualização:** 2026-07-22T15:31:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311421628439)

 MENSAGEM:**

[852 - Rejeição]: Número da parcela inválido ou não informado

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311410094743)

** **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311410111511)

 Certifique-se que a UF emissora da nota não consta no parâmetro abaixo:

- Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** *(Caminho para acesso: Configurações » Avançado » Preferências), parâmetro *Chave **"UFNFEOMITV160B - UFs que omitem o schema NFe 4.0 v1.60B"**:

 

*

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14439243628823)

*

 

Foi criado o parâmetro UFNFEOMITV160B com default vazio. Essa criação ocorreu quando algumas UFs ainda estavam com sua SEFAZ sem implementar esse schema.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311410114327)

 Após retirar a UF do parâmetro, refaça o faturamento. Gere o XML em conferência e certifique-se que a tag **<nDup>** foi gerada seguindo as regras da SEFAZ:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311421641495)

 O número de parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Exemplo: **"001", "002", "003"**

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311421643671)

****OBSERVAÇÃO:** 

Nota Técnica (**NT-2016.002 - v 1.60**):

**[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311410122135)

 CAUSA:**

Se informado o Grupo de Parcelas de cobrança (tag <dup>), Número da parcela (<nDup>) não informado ou inválido.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311421643671)

****OBSERVAÇÃO:** 
O número de parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Exemplo: "001", "002", "003", ...


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)