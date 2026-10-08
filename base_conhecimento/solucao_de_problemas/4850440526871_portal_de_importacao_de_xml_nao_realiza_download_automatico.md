# Portal de importação de XML não realiza download automático

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4850440526871-Portal-de-importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-realiza-download-autom%C3%A1tico](https://ajuda.sankhya.com.br/hc/pt-br/articles/4850440526871-Portal-de-importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-realiza-download-autom%C3%A1tico)  
> **ID:** `4850440526871` | **Última Atualização:** 2026-08-06T18:43:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731904151)

 MENSAGEM: **

Portal de importação de XML não realiza download automático / 656-Rejeição: Consumo Indevido

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344715319959)

 SOLUÇÃO: **

Com a nova norma da Sefaz, o tempo mínimo para consultar aos DF-e é de 60 minutos. Para realizar as configurações necessárias, siga o passo a passo mostrado abaixo: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731906711)

 Valide se a consulta está sendo realizada dentro do período indicado.

Tela: **"****Configuração MD-e/DF-e"**

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12555078252951)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731908247)

 OBSERVAÇÃO:**

Deixar no mínimo 60 minutos (recomendável 120 minutos) 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731910679)

 Outra norma informada pela Sefaz é que a busca por DF-e será apenas para as empresas que de fato utilizam DF-e e CT-e. **Caso utilize também a configuração de DF-e nas bases de teste e treina**, faça a remoção dessa configuração, mesmo se nestas bases não estiverem ocorrendo o erro, se estiver consumindo o mesmo serviço um vai interferir no outro.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731912215)

 Caso a empresa não utilize DF-e, altere o campo abaixo em todas as empresas que não vão utilizar o DF-e.

Tela: **"****Preferências » Empresa"**
Aba: **"NF-e/NFC-e -> Utiliza distribuição de DF-e?: Não utiliza"**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15776066323607)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344715332503)

  Também desmarque o campo.
Aba: **"CT-e -"**

Campo **"Utiliza distribuição de DF-e?"**: desmarcado

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15776054350231)

**

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731908247)

 OBSERVAÇÃO:**

Caso a contabilidade ou outra pessoa utilize a busca manual desses documentos, dentro do prazo de 60 minutos, nesse caso, o CNPJ **é bloqueado por 1 hora,** **sendo impedido de realizar novas consultas** nesse intervalo. Decorrido o intervalo de tempo, o desbloqueio será automático.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16344731915927)

 Causa:**

Os servidores da receita estão validando de forma mais precisa o consumo indevido. Antes quando ocorria um "bloqueio", após uma hora esse "bloqueio" era desfeito. Agora os servidores da receita mantém o "bloqueio" uma hora após a última tentativa fazendo com o bloqueio seja renovado a cada tentativa frustrada.
[https://www.nfe.fazenda.gov.br/portal/informe.aspx?ehCTG=false&Informe=0cu/yBLKrCs=](https://www.nfe.fazenda.gov.br/portal/informe.aspx?ehCTG=false&Informe=0cu/yBLKrCs=)