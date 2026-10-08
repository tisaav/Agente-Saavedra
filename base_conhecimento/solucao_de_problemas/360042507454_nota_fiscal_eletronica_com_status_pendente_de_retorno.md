# Nota Fiscal Eletrônica com status 'Pendente de Retorno'

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454-Nota-Fiscal-Eletr%C3%B4nica-com-status-Pendente-de-Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454-Nota-Fiscal-Eletr%C3%B4nica-com-status-Pendente-de-Retorno)  
> **ID:** `360042507454` | **Última Atualização:** 2026-09-11T16:58:25Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779856535)

 SITUAÇÃO:**

Nota foi marcada como Pendente de retorno, como proceder, a partir de agora.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779858583)

 SOLUÇÃO:**

Quando utilizado este processo garanta a aprovação da nota pendente de retorno e, após a sua aprovação, faça o cancelamento dela.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779861783)

 Localize as duas notas envolvidas no processo (a nota pendente de retorno e a nota espelho gerada a partir desta nota). Pode-se filtrar a nota gerada pelo parceiro e data de negociação.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457795783191)

 Uma vez identificado ambas as notas, consulte suas respectivas chaves de acesso no site de consulta de NF-e da SEFAZ Nacional:

[http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779867159)

 **Repita a consulta através da opção 'Portais Estaduais da NF-e', selecionando o Estado da Empresa emissora e busque a opção de Consulta NF-e por chave de acesso.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779869207)

 Ao consultar as chaves na SEFAZ, pode-se deparar com algumas situações:

- 
**Ambas as chaves de acesso estão aprovadas na base da SEFAZ**: Consulte a situação atual da nota. Como consequência o Statusnfe da nota pendente de retorno será atualizado para APROVADA.

- 
**Nota Pendente de Retorno está inexistente na base da SEFAZ e a nota espelho aprovada na base da SEFAZ**/sistema: Busque a autorização da nota. Como consequência, o Statusnfe da nota será atualizada como APROVADA. Se o Statusnfe da nota for atualizada para algo diferente de APROVADA, como AGUARDANDO CORREÇÃO, identifique no Portal de Vendas, botão 'Outras Opçoes ...>>Ver acompanhamentos, a rejeição apresentada e busque na Central de Ajuda, um artigo referente ao problema apontado.

- 
**Nota Pendente de Retorno inexistente na base da SEFAZ 24 horas após a primeira emissão**: neste caso siga os passos previstos na documentação do StatusNfe '[Aguardando Autorização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)'.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779872663)

 CAUSA**

A marcação de Pendente de Retorno é usada quando uma nota é transmitida à SEFAZ, mas fica aguardando sua autorização por um tempo elevado. Neste caso, o processo de pendência de retorno é acionado, sendo criada uma nova nota com informações da antiga (numeração e chave nf-e). Esta nova nota, sob o ponto de vista da SEFAZ, estará aguardando sua autorização e a nota antiga tem os campos de NF-e limpos para que esta nota possa ser transmitida e aprovada pela SEFAZ.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457779877143)

 OBSERVAÇÃO:**

Uma vez que a nota que estava Pendente de Retorno estiver APROVADA, o cliente poderá então fazer o cancelamento ou a devolução desta NF-e conforme orientação dos responsáveis pela sua contabilidade.


---

### 🔗 Links e Referências Internas:

- [Aguardando Autorização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)