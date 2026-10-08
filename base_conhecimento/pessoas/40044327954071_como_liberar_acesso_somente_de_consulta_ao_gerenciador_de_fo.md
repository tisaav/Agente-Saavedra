# Como liberar acesso somente de consulta ao Gerenciador de Folhas?

> **Módulo:** Pessoas+ | **Subseção:** Usuários e Permissões do Pessoas+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/40044327954071-Como-liberar-acesso-somente-de-consulta-ao-Gerenciador-de-Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40044327954071-Como-liberar-acesso-somente-de-consulta-ao-Gerenciador-de-Folhas)  
> **ID:** `40044327954071` | **Última Atualização:** 2026-09-27T14:04:05Z

---

**Módulo: **Pessoal+
**Versão Mínima: **5.96.0 
**Caminho de Acesso: **Pessoal+ > Configurações > Painel de Configurações
**ID da Tela: **br.com.sankhya.rh.ConfiguracoesDaFolha

 

### **Descrição e Usabilidade**

A permissão **Apenas Consulta** garante maior controle e segurança no acesso ao **Gerenciador de Folhas**, permitindo que determinados usuários visualizem as informações da folha de pagamento **sem possibilidade de alteração ou execução de rotinas**.

Essa funcionalidade é especialmente útil em cenários como:

- Auditorias internas ou externas;

- Acompanhamento gerencial;

- Consulta por áreas que não executam cálculos (ex: financeiro, controladoria).

⚠️ Quando ativada, essa permissão transforma o **Gerenciador de Folhas** e a tela de **Cálculos** em **modo somente leitura**, impedindo qualquer ação operacional.

Com a opção **Apenas Consulta** habilitada no **Painel de Configurações**:

- O usuário terá acesso **exclusivo para consulta** no Gerenciador de Folhas e tela Cálculos;

- Todas as ações operacionais serão bloqueadas, mesmo que existam permissões liberadas em outros menus;

- A permissão passa a atuar como **restritiva global**, ou seja, **tem prioridade sobre permissões de cálculo e folha.**

### **Pré-requisitos**

- Possuir acesso ao sistema com usuário ativo;

- Ter permissão de acesso às telas **Gerenciador de Folhas** e **Cálculos**;

- 

Estar vinculado a um grupo de usuários que tenha permissão de **Apenas Consulta** configurado no **Painel de Configurações**.

⚠️ Lembre-se que você está dando permissão a um grupo, não a um usuário individual. Se você adicionar um novo usuário a um grupo, ele automaticamente herdará todas as permissões daquele grupo.

Para saber como realizar essas liberações e criar um novo grupo de decisores, acesse o artigo: ****[Liberação de acesso às telas do módulo Pessoal+ para novos colaboradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/38583858942743).

### **Jornada de Uso**

 

![permissaoconsultagerenciadorfolhas.gif](https://ajuda.sankhya.com.br/hc/article_attachments/40274147046039)

1. Acesse a tela **Painel de Configurações** (Pessoal+ > Configurações);

1. Clique em **Configuração de permissões** e, em seguida, no card **Gerenciador de Folhas**;

1. Selecione o** Grupo de acessos** e os **usuários**;

1. Marque a opção **Apenas Consulta**;

1. 

Clique em **Confirmar alterações** para salvar a configuração.

A partir desse momento, os usuários vinculados terão acesso restrito ao **Gerenciador de Folhas**.

#### 
**🔹****Regras de funcionamento**

Ao marcar **Apenas Consulta**:

As opções abaixo serão automaticamente desmarcadas:

- Integrar com o Financeiro;

- Excluir Folhas;

- Integrar com a Contabilidade;

- Fechar/Reabrir folhas;

Caso alguma dessas opções seja marcada, a opção **Apenas Consulta **será desmarcada automaticamente.

✔️ Podem ser utilizadas junto com **Apenas Consulta** as opções:

- Aba **Análises**;

- 
**Resumo da Folha**.

#### 
**🔹****Ações bloqueadas**

Quando a permissão estiver marcada, o usuário **não poderá executar**:

- Reprocessar plano de saúde;

- Atualizar dados de plano de saúde;

- Fechar ou reabrir folhas;

- Excluir folhas;

- Alterar status de conferência;

- Realizar integrações (contábil, financeira, eSocial);

- Liberar holerites no Portal RH;

- Calcular provisões (férias e 13º).

⚠️ Os botões dessas ações ficam desabilitados e exibem a mensagem:

***"Acesso somente de consulta. Para alterar: Painel de Configurações > Configuração de Permissões > Gerenciador de Folhas."***

#### 
**🔹****Ações permitidas**

Mesmo com a restrição, o usuário poderá:

- Consultar informações no Gerenciador de Folhas;

- Acessar cálculos já realizados (modo leitura);

- Gerar relatórios de:

  - Décimo terceiro;

  - Férias.

- Gerar **Resumo da Folha** (se habilitado);

- Fazer download/envio de holerites;

- Gerar arquivo de seguro-desemprego;

- Acessar abas:

  - Análises;

  - Provisões.

### **Pontos de Atenção**

- A opção **Apenas Consulta** é **desmarcada** por padrão no **Painel de Configurações**, não impactando usuários já existentes;

- Essa permissão **não exige configuração adicional** nas permissões de cálculo;

- Mesmo com permissões liberadas em outros menus, o usuário continuará com acesso restrito;

- O usuário ainda poderá abrir cálculos, porém **somente para visualização**.

### **Dicas de Usabilidade**

- Utilize essa permissão para perfis que não devem executar rotinas críticas;

- Evite combinar com permissões operacionais — elas serão ignoradas;

- Ideal para ambientes com segregação de funções (ex: auditoria, conferência);

- Sempre valide o comportamento após ativar a configuração.

### **Perguntas Frequentes (FAQ)**

**1. O usuário consegue acessar a tela de Cálculos com essa permissão?**

Sim, mas apenas para consulta. Nenhuma ação poderá ser executada.

**2. Preciso configurar permissões de cálculo junto com a opção Apenas Consulta?**

Não. Essa permissão sobrepõe qualquer configuração de cálculo.

**3. O usuário consegue calcular ou excluir folhas?**

Não. Todas as ações operacionais ficam bloqueadas.

**4. O usuário pode usar junto com outras permissões?**

Sim, mas elas serão ignoradas enquanto o **Apenas Consulta** estiver ativo.

**5. Essa configuração afeta usuários já existentes?**

Não. A opção é desmarcada por padrão.

**6. O usuário consegue escolher um tipo de folha específico que deseja consultar?**

Não, a consulta é para todos os tipos de folha.  

 

### **Artigos Relacionados**

- 

[Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)

- 

[Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)


---

### 🔗 Links e Referências Internas:

- [Liberação de acesso às telas do módulo Pessoal+ para novos colaboradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/38583858942743)
- [Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)