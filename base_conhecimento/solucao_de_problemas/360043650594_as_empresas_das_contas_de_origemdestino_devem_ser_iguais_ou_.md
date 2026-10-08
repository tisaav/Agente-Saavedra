# As empresas das contas de origem/destino devem ser iguais ou uma das contas não pode ser exclusiva

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043650594-As-empresas-das-contas-de-origem-destino-devem-ser-iguais-ou-uma-das-contas-n%C3%A3o-pode-ser-exclusiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043650594-As-empresas-das-contas-de-origem-destino-devem-ser-iguais-ou-uma-das-contas-n%C3%A3o-pode-ser-exclusiva)  
> **ID:** `360043650594` | **Última Atualização:** 2026-08-22T19:15:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170334076183)

 MENSAGEM:**

[CORE_E04083] As empresas das contas de origem/destino devem ser iguais ou uma das contas não pode ser exclusiva.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170334082711)

 SOLUÇÃO:**

Quando o parâmetro **"Validar Empresa Exclusiva das Contas? - TRANSFMBEXC"** estiver habilitado, será permitido realizar a transferência e a conciliação entre contas exclusivas por meio de duas hipóteses:

- Se as empresas das contas de origem/destino forem iguais;

- Quando somente uma das contas for exclusiva.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170334090903)

 Dessa forma, acesse o cadastro das contas utilizadas durante o processo de transferência e certifique-se que a situação acima é respeitada:

Tela **"Contas"** (Caminho de acesso: *Configurações » Cadastros » Bancários » Contas*), aba **Cadastros**:

- Campo **"Empresa"**: Se a conta for para movimentação de empresa, informe o nome da empresa.

- Campo **'Exclusiva da Empresa':** Se esta opção for selecionada, a conta somente poderá ser utilizada pela empresa selecionada no campo acima. Ajuda a evitar lançamentos em contas erradas.

 

![contas3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14561226037015)

 

Se para as duas contas utilizadas, o campo **"Empresa"** for igual, a transferência será aceita.
Caso trate-se de empresas diferentes, uma delas não poderá ser exclusiva da empresa.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170334094487)

 De acordo com as validações acima e processo atual da empresa, realize os devidos ajustes e refaça a transferência.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170334100759)

 CAUSA:**

Quando as empresas das contas de origem/destino forem diferentes e ambas as contas forem "exclusivas da empresa", transferências entre essas contas não serão permitidas.