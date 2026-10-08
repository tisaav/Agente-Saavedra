# Auditoria de Modificações

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es)  
> **ID:** `1500003568962` | **Última Atualização:** 2026-08-24T14:22:53Z

---

```text

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310464258455)

**Módulo:** Configurações>Controle de Acesso 

![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42310434566423)

**Versão disponível: **A partir da 4.6 
```

Através dessa tela é possível auditar tabelas e seus campos do sistema, mostrando quem fez uma determinada alteração na data/hora em que foi realizada.

Essa rotina é dividida em três partes, sendo elas:

[Filtros](#filtros)                                                                                  [Informações gerais das modificações](#informa%C3%A7%C3%B5esgeraisdasmodifica%C3%A7%C3%B5es)

[Detalhamento das modificações](#detalhamentodasmodifica%C3%A7%C3%B5es)

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418213367319)

[[voltar ao topo]](#top)

### 
Filtros

No Painel de Filtros, que está destacado na imagem abaixo, é possível que você pesquise pelo nome da **"Tabela"** ou da **"Instância"**, pelo nome do **"Campo"**, valor da **"Chave"** modificada, pelo **"Período"** (data inicial e data final), pelo nome ou código do **"Usuário"** que realizou a modificação ou ainda, pelo **"Tipo de Alteração"** feita, que pode ser de **"Edição"**,** "Remoção"** ou **"Inserção"**.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418213393047)

[[voltar ao topo]](#top)

### 
Informações gerais das modificações

Nessa grade serão exibidas as alterações realizadas nas tabelas previamente mapeadas como, por exemplo, o nome da Instância e o nome da Tabela, Data/hora, a Chave, o Tipo e o nome/código do Usuário Responsável.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418213435159)

[[voltar ao topo]](#top)

### 
Detalhamento das modificações

Por fim, quando você clicar em uma linha de alteração no guia geral de informações, essa grade será alterada, exibindo os campos que foram modificados, com o **"Nome do Campo"**, o **"Valor antes"** e o **"Valor depois"**.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418206285335)

**Observação:** caso o Valor antes esteja vazio, significa que foi um Tipo de Alteração de Inserção.

**Importante:** as tabelas abaixo são as que serão auditadas permanentemente pelo sistema e que sairão previamente configuradas:

- 
**TSIPAR -** Parâmetros

- 
**TGFPAR -** Parceiros

- 
**TGFPRO -** Produtos

- 
**TGFTPV -** Tipos de Negociação

- 
**TGFTOP -** Tipos de Operação

- 
**TGFEMP -** EmpresaFinanceiro

- 
**TSIEMP -** Empresas

- 
**TGFPPG -** Gestão Fiscal Parcelas de Pagamento

- 
**TGFCTB -** Parâmetros Contabilização

- 
**TSICTA -** Contas Bancárias (ignorar as alterações nas colunas: REMBCO, SALDOBCO, SALDOREAL, SEQREM e SEQREM2)

- 
**TCBEMP -** Empresas (contabilidade)

- 
**TFPEMP -** Empresa Pessoal

- 
**TFPFUN -** Funcionários

- 
**TFPEVE -** Eventos

- 
**TFPFOR -** FP Fórmulas de Cálculo

- 
**TGFMODTOP -** Modelos da TOP

- 
**TGFFOR -** Fórmulas de Precificação

- 
**TGWEND -** Endereço

- 
**TGWEAS -** EnderecoAreaSep

- 
**TGWEAC -** EnderecoAreaConf

- 
**TGWEXP -** ExplosaoLote

- 
**TGWARS -** AreaSeparacao

- 
**TGWDCA -** Doca

- 
**TGFPEM -** EmpresaProdutoImpostos

- 
**TGFVOA -** HistoricoUnidadeAlternativa

- 
**TGFGRU -** GrupoProduto

- 
**TGWEXG -** EnderecoGrupoProduto

- 
**TGWUAS -** Separador

- 
**TGWFEG -** FaixaEnderecosGrupo

- 
**TGWEGE -** ExecutanteGrupoEnderecos

- 
**TGWUTE -** TipoEquipamentoUnidade

- 
**TGWEQP -** EquipamentoWMS

- 
**TGWEXU -** EnderecoUnidade

- 
**TGWTEC -** TarefaExecucaoColetor

- 
**TGFICM -** AliquotaICMS

- 
**TGFIPI -** AliquotaIPI

- 
**TGFISS -** AliquotaISS

- 
**TGFIMA -** AliquotaImposto

- 
**TGFIMC -** Imposto

- 
**TFPSIN -** Sindicato

- 
**TFPCNV -** CNV

- 
**TFPPRE -** RegraCalculo

- 
**TFPFER -** ProgramacaoFerias

- 
**TSIUSU -** Usuario (ignorar a coluna DTULTACESSO)

**Importante:** a tela Auditoria de Modificações não permite a edição e nem inserção de novas tabelas.

[[voltar ao topo]](#top)