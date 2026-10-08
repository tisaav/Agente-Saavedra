# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Mato Grosso do Sul

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/22599828778263-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Mato-Grosso-do-Sul](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599828778263-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Mato-Grosso-do-Sul)  
> **ID:** `22599828778263` | **Última Atualização:** 2026-07-29T13:42:16Z

---

Nesse artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Mato Grosso do Sul, para conhecê-las acesse os links abaixo:

****

[Batayporã/MS](#bataypor%C3%A3/ms)[Dourados/MS](#dourados/ms)

[Camapuã/MS](#camapua/ms)[Rio Brilhante/MS](#riobrilhante/ms)

[Campo Grande/MS](#campogrande/ms)[São Gabriel do Oeste/MS](#saogabrieldooeste)

[Chapadão do Sul/MS](#chapadaodosulms)[Três Lagoas/MS](#tr%C3%AAslagoas/ms)

| Cidades |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

 

### **Batayporã/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Batayporã.

**Observação:** a cidade não suporta o cancelamento de nota de serviço via webservice, este deverá ser feito diretamente na prefeitura.

[[voltar ao topo]](#top)

### **Camapuã/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Camapuã.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **Campo Grande/MS**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23966535223063)

 Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Campo Grande, sendo este 2701506 e o **"Cód. município SIAFI"** 2729.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23966510713367)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| A | Sem dedução |
| B | Com dedução/Materiais |
| C | Imune/Isenta ISSQN |
| D | Devolução/Simples remessa |
| J | Intermediação |

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29304552771607)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)  e  defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas: 

********

| Código | Descrição |
| --- | --- |
| C | Isenta de ISS |
| E | Não Incidência no Município |
| F | Imune |
| K | Exigibilidade Susp. Dec. J/Proc.A |
| N | Não Tributável |
| T | Tributável |
| G | Tributável Fixo H |
| H | Tributável S. N. |

####  

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

**

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29303892851863)

 Informação sobre personalizar a tag <DescricaoRPS> ao emitir NFS-e em Campo Grande/MS: {disponível na versão ≥ 4.34}**

Se o parâmetro **"Cód. IBGE mun. enviam retenções discriminação serviços DSF - MUNENVRETDISCR"** estiver configurado com o código do município de Campo Grande/MS (5002704), o sistema deve adicionar os dados sobre retenção de impostos na tag **<DescricaoRPS>** do arquivo XML.

Isso garante que as informações sobre os impostos retidos sejam incluídas corretamente na discriminação dos serviços, para que isso não ocorra será necessário remover o código do município do campo **"Texto"** do parâmetro.

[[voltar ao topo]](#top)

### **Chapadão do Sul/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Chapadão do Sul.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **Dourados/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Dourados.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **Rio Brilhante/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Rio Brilhante.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)

### **São Gabriel do Oeste/MS**

Os seguintes cadastros estão envolvidos:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23966535223063)

 Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

********

| Código | Descrição |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 4 | Exportação |
| 5 | Imunidade |
| 6 | Exigibilidade Suspensa por Decisão Judicial |
| 7 | Exigibilidade Suspensa por Processo Administrativo |

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23966510713367)

 Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e defina no campo **"Regime esp. trib. ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

********

| Código | Descrição |
| --- | --- |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual (MEI) |
| 6 | Microempresário e empresa de pequeno porte (ME EPP) |

####  

#### **Cancelamento**

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

********

| Código | Descrição |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade da nota |

 

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

**Nota:** esta prefeitura não suporta a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

[[voltar ao topo]](#top)

### **Três Lagoas/MS**

O sistema encontra-se apto para emitir NFS-e para o município de Três Lagoas.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)
- [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e)