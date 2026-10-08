# NFS-e e Reforma Tributária: Configuração e Uso do IBS/CBS via Nota Gateway

> **Módulo:** Fiscal e Contábil | **Subseção:** Sistemas atendidos  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway)  
> **ID:** `36881907516567` | **Última Atualização:** 2026-07-29T13:39:51Z

---

**Você encontra neste artigo:**

[O que é e para que serve](#oque)
[1. Cadastro de Serviço](#cadastro-servico)
[Seção Geral](#secao-geral)
[Seção Reforma Tributária](#secao-reforma)
[2. Tipos de Operação (TOP)](#top)[3. Central de Vendas](#central-vendas)
[4. Regras de obrigatoriedade do IBS/CBS](#vigencia)
[5. Estrutura do XML](#xml)
[6. Persistência e rastreabilidade](#persistencia)
[7. Envio do Grupo de Benefício Municipal](#beneficio-municipal)

| ↳    ↳ |  |
| --- | --- |

## O que é e para que serve

Com a **Reforma Tributária (PEC 45/2019)** e a adoção do **Padrão Nacional da NFS-e**, o Sankhya OM e sua integração com o **Nota Gateway** foram atualizados para incluir os novos campos fiscais de **IBS (Imposto sobre Bens e Serviços)** e **CBS (Contribuição sobre Bens e Serviços)**. Este artigo detalha as configurações necessárias nos cadastros de Serviço, TOP e na Central de Vendas para garantir a conformidade legal na emissão da NFS-e. O artigo não cobre a configuração do IS (Imposto Seletivo) nem a parametrização de outros documentos fiscais.

## 1. Cadastro de Serviço

### Seção Geral

- 
**Código NBS** — registra o código da **Nomenclatura Brasileira de Serviços (NBS)**. O preenchimento é obrigatório para a padronização e a comunicação com o Ambiente Nacional da NFS-e na Reforma Tributária.

### Seção Reforma Tributária

- 
**Código Classificação Tributária Nacional** — registra a classificação tributária do serviço. Faz parte do grupo IBS/CBS e é necessário para o cálculo e a correta aplicação dos novos tributos.

## 2. Tipos de Operação (TOP)

- 
**Código Indicador Operação** — registra o código específico da operação de serviço utilizado para fins de cálculo e escrituração do IBS/CBS.

- 
**Consumidor Final** — define o padrão para a operação, indicando se a destinação é para o consumidor final. As opções são **Sim** ou **Não**.

## 3. Central de Vendas

- 
**Consumidor Final** — a marcação é herdada automaticamente da TOP configurada, mas permite ajuste manual no momento da emissão da nota, definindo se a destinação é para o consumidor final.

**Emissão para Consumidor Final / Auto-prestação (omissão do bloco Cliente)**

Em cenários de consumidor final não identificado ou auto-prestação, algumas prefeituras rejeitam a emissão quando o bloco do tomador é enviado sem CPF/CNPJ válido. Para atender essas prefeituras, o Sankhya OM omite automaticamente o bloco `cliente` do JSON enviado, quando o **Parceiro informado na nota possui o mesmo CNPJ e a mesma Inscrição Municipal da Empresa Emitente (prestadora)**.

O comportamento é automático — não há parâmetro ou marcação a ser habilitada. Quando o gatilho é atendido, os dados da própria empresa **não**** **são enviados como tomador do serviço, conforme permitido pela prefeitura.

## 4. Regras de obrigatoriedade do IBS/CBS

A obrigatoriedade do envio detalhado do grupo IBS/CBS é gradual, conforme o regime tributário da empresa:

************

****

****

****

| Período | Regime tributário | Regra |
| --- | --- | --- |
| A partir de 2026 | Lucro Real, Presumido e Simples Nacional acima do sublimite. | Envio das informações de IBS/CBS na NFS-e obrigatório. |
| A partir de 2026 | Simples Nacional e MEI. | IBS/CBS será ignorado ou enviado com alíquota zerada pelo Nota Gateway. |
| A partir de 2027 | Todas as empresas. | IBS/CBS obrigatório para todas as empresas. |

## 5. Estrutura do XML

O envio dos dados fiscais para o Nota Gateway pode ser feito de forma simplificada ou completa, dependendo do detalhamento fiscal configurado:

************

****````

****``````

| Tipo de envio | Dados enviados | Cálculo do imposto |
| --- | --- | --- |
| Simplificado (padrão) | Apenas classificacaoTributaria e codigoIndicadorOperacao. | O Nota Gateway realiza o cálculo automático do IBS/CBS. |
| Completo (cenários especiais) | Inclui situacaoTributaria, codigoTributacaoNacional e o grupo ibsCbs completo. | O Sankhya OM envia as informações detalhadas para validação. |

**ℹ️ Nota**

No envio simplificado, o Sankhya OM envia os dados preenchidos nos cadastros e o cálculo de IBS/CBS ocorre conforme o retorno da API do eNotas/Portal Nacional.

## 6. Persistência e rastreabilidade

O Sankhya OM armazena o retorno da NFS-e no histórico da nota e nas tabelas fiscais, garantindo a rastreabilidade dos dados e as informações de autorização. As seguintes informações são registradas:

- Protocolo

- Chave de Acesso

- URL do DANFSE

- Mensagens de erro

- Todas as informações detalhadas dos novos campos e do grupo IBS/CBS

## 7. Envio do Grupo de Benefício Municipal (BM) no DPS

A partir das versões **4.35b462**, **4.34b364** e **4.33b235**, o Sankhya OM passa a atender ao layout oficial do DPS (padrão nacional), permitindo o envio das informações de **Benefício Municipal**. Este grupo identifica reduções na base de cálculo do ISS — por valor ou percentual — na integração com o eNotas/Nota Gateway.

### Configuração necessária

Para utilizar esta funcionalidade, preencha o código do benefício conforme a legislação do seu município:

1. Acesse a aba [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) no [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o).

1. Preencha o campo **Número de identificação do Benefício Municipal** com o código numérico de até 14 posições.

**ℹ️ Nota**

O envio do Grupo BM no XML/JSON ocorre **apenas** se o campo **Número de identificação do Benefício Municipal** estiver preenchido.

### Regras de preenchimento e envio

O sistema define automaticamente como as informações serão enviadas ao Gateway (JSON) com base na configuração da redução de base de cálculo do ISS:

********

****
**``

****
**````

****
**````

| Cenário | Como será enviado no JSON |
| --- | --- |
| Apenas código do benefícioSem percentual ou tipo de dedução informados | Envia apenas o codigo. |
| Redução por percentualCampo "Perc. de dedução" preenchido + Tipo "Por percentual" na aba Alíquotas de ISS | Envia o codigo + percentualReducaoBaseCalculo. |
| Redução por valorCampo "Perc. de dedução" vazio + Tipo diferente de "Por percentual" na aba Alíquotas de ISS | Envia o codigo + valorReducaoBaseCalculo (valor efetivamente deduzido). |

### Exemplos técnicos (JSON)

Para conferência técnica ou depuração, veja como os dados são gerados na integração:

**Exemplo 1 — Apenas código:**

```text
"beneficioMunicipal": { "codigo": "32053090200007" }
```

**Exemplo 2 — Com percentual:**

```text
"beneficioMunicipal": { "codigo": "32053090200007", "percentualReducaoBaseCalculo": 5.00 }
```

**Exemplo 3 — Com valor:**

```text
"beneficioMunicipal": { "codigo": "32053090200007", "valorReducaoBaseCalculo": 146.00 }
```


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)
- [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)