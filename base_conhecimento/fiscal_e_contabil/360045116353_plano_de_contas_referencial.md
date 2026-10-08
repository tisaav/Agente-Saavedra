# Plano de Contas Referencial

> **Módulo:** Fiscal e Contábil | **Subseção:** Contabilidade  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353-Plano-de-Contas-Referencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353-Plano-de-Contas-Referencial)  
> **ID:** `360045116353` | **Última Atualização:** 2026-07-29T16:02:14Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42314991343767)

 **Módulo:** Contabilidade > Conexão > ECF > Configuração P/ ECF
```

Por meio desta tela é realizada a importação dos Planos de Conta salvos pelo PVA do ECF para o sistema, visando facilitar a atualização das informações pertinentes ao [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234874-Plano-de-Contas) da Empresa.

![Importar.png](https://ajuda.sankhya.com.br/hc/article_attachments/33532280538519)

Para o uso da tela, primeiramente defina o **"Tipo"** de Plano de Contas a ser trabalhado; assim, temos as seguintes opções:

- 1 - PJ em Geral (L100_A + L300_A);

- 2 - PJ em Geral - Lucro Presumido ( P100 + P150 );

- 3 - Financeiras ( L100_B + L300_B );

- 4 - Seguradoras ou Entidades Abertas de Previdência Complementar ( L100_C + L300_C );

- 5 - Imunes e Isentas em Geral ( U100_A + U150_A );

- 6 - Financeiras - Imunes e Isentas ( U100_B + U150_B );

- 7 - Seguradoras - Imunes e Isentas ( U100_C + U150_C );

- 8 - Entidades Fechadas de Previdência Complementar ( U100_D + U150_D );

- 9 - Partidos Políticos ( U100_E + U150_E );

- 10 - Financeiras - Lucro Presumido ( P100B + P150B ).

Uma vez definido o Tipo de Plano de Contas, o sistema automaticamente filtra e carrega na grade predominante da tela, os Planos de Conta Referenciais correspondentes.

O botão **"Importar Plano ECF 2025" **permite que o usuário importe o plano de contas referencial exigido pelo ECF 2025, utilizando um arquivo no formato .xlsx conforme padrão oficial disponibilizado pelo governo. Ao clicar no botão, é aberto um pop-up para seleção do arquivo. O sistema processa todas as abas presentes no .xlsx e grava as informações do plano de contas referencial nas tabelas correspondentes, permitindo que as contas importadas tenham o mesmo comportamento das importações anteriores. Esta opção é exclusiva para a rotina de importação do plano de contas ECF 2025, sem interferência nas demais funcionalidades da tela.

Ao clicar no botão **"Atualizações Sped ECF"**, o sistema verifica se existe algum arquivo pertinente às Tabelas Dinâmicas para ser importado e/ou atualizado; caso afirmativo, tem-se a importação/atualização das Tabelas Dinâmicas do ECF correspondentes ao Tipo de Plano de Contas inicialmente definido.

**Observação:** a verificação da necessidade e a consequente importação/atualização das Tabelas Dinâmicas, é feita através da aplicação [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394) e Jiva Web Connection, que irá executar localmente na máquina de cada usuário. Assim, observe o caminho da Importação/Atualização:

1.Uma atualização das Tabelas Dinâmicas através do aplicativo da Receita, o Sped ECF. Este aplicativo pode ser obtido através do link [SPED ECF](http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/sped-sistema-publico-de-escrituracao-digital/escrituracao-contabil-fiscal-ecf/programa-sped-contabil-fiscal-para-windows);

2.O Sankhya Web Connection/Jiva Web Connection irá compactar esses arquivos e enviar para o Repositório de Arquivos (servidor) do Sankhya Om/Jiva Evo;

3.O Sankhya Om/Jiva Evo irá descompactar o arquivo que está no Repositório de Arquivos e proceder com a atualização das tabelas dinâmicas.


---

### 🔗 Links e Referências Internas:

- [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234874-Plano-de-Contas)
- [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394)