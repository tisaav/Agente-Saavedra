# Gestão de Inconsistências para Integrações HCM

> **Módulo:** Pessoas+ | **Subseção:** Inconsistências das Integrações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35434005265047-Gest%C3%A3o-de-Inconsist%C3%AAncias-para-Integra%C3%A7%C3%B5es-HCM](https://ajuda.sankhya.com.br/hc/pt-br/articles/35434005265047-Gest%C3%A3o-de-Inconsist%C3%AAncias-para-Integra%C3%A7%C3%B5es-HCM)  
> **ID:** `35434005265047` | **Última Atualização:** 2026-09-26T01:40:07Z

---

**Módulo**: Pessoal+
**Versão Mínima**: 5.56.0
**Caminho de Acesso**: Pessoal+ > Consultas

## **Sumário**

[Descrição e Usabilidade](#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](#1-descri%C3%A7%C3%A3o-da-funcionalidade)

- [2. Pré-requisitos](#2-pr%C3%A9-requisitos)

- [3. Jornada de Uso](#4-jornada-de-uso)

- [4. Pontos de Atenção](#5-pontos-de-aten%C3%A7%C3%A3o)

- [5. Dicas de Usabilidade](#6-dicas-de-usabilidade)

- [6. Casos de Uso](#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](#faq--d%C3%BAvidas-frequentes)

[Artigos Relacionados](#artigos-relacionados)

## **Descrição e Usabilidade**

 

### **1. Descrição da Funcionalidade**

 

A tela **Gestão de Inconsistências para Integrações HCM** é uma ferramenta preventiva que permite identificar e ajustar cadastros de colaboradores que possam causar falhas nas integrações com outros sistemas, como Vixting, Pontotel e Mindsight. 

Atualmente, a tela possui duas abas principais, que, identifica colaboradores com múltiplos líderes e usuários ativos; situação que, embora permitida, pode comprometer a integridade dos dados e o funcionamento correto das integrações:

- **Liderança;**

- **Usuários**.

O objetivo da funcionalidade é garantir a consistência das informações e um fluxo de integração estável e confiável entre o sistema Sankhya e os sistemas integrados.

 

### **2. Pré-requisitos**

 

**Permissões necessárias**

- 
Acesso à tela liberado por meio da rotina de **Acessos**.

**Parâmetros essenciais**

- Integração HCM habilitada.

- Módulo Pessoal+ atualizado na versão 5.56.0 ou superior.

**Configurações relacionadas**

- Cadastro de colaboradores, líderes e usuários devidamente atualizados.

 

### **3. Jornada de Uso**

 

- Acesse a tela **Gestão de Inconsistências para Integrações HCM **(Pessoal+ > Consultas > Gestão de Inconsistências para Integrações HCM).

- Utilize os filtros (Cód. Empresa, Cód. Funcionário, Matrícula, CPF, Nome do Colaborador) para localizar colaboradores.

#### 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309792223255)

 **Aba Liderança**

| Versão 5.56 |
| --- |

1. 

Caso não haja inconsistências, a tela exibe a seguinte mensagem: ***"Nenhum colaborador com mais de uma liderança foi encontrado"***.

![gstão-de-inconsistencia-limpa.png](https://ajuda.sankhya.com.br/hc/article_attachments/35459772861335)

Todavia, quando existem colaboradores com mais de um líder, a lista é apresentada na grade principal.

![gestao-inconsistencia-lider.png](https://ajuda.sankhya.com.br/hc/article_attachments/35460465591063)

1. Analise a lista e clique na linha do colaborador desejado para abrir o pop-up de ajuste.

1. 

Defina um líder único, removendo a liderança incorreta.

![remover-lider-inconsistente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35460613732375)

1. Confirme a alteração e uma mensagem de sucesso será exibida.

 

#### 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309792223255)

 **Aba Usuários**

| Versão 5.57 |
| --- |

Essa aba identifica colaboradores com mais de um usuário do sistema vinculado.

1. 

Quando houver múltiplos usuários por colaborador, a grade exibe as principais informações do colaborador.

![aba-usuarios-inconsistencias-integracao.png](https://ajuda.sankhya.com.br/hc/article_attachments/35916837354519)

1. 

Para ajustar, selecione a linha do colaborador e dê um duplo clique. No pop-up de **Ajuste de Usuário **apresentado, defina somente um usuário e exclua os demais. Confirme a ação para atualizar o cadastro.

![ajuste-usuario-inconsistencia-integracao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35916950126743)

Caso não haja funcionários com múltiplos usuários, ao acessar a aba será exibida a seguinte mensagem:

***"Nenhuma inconsistência foi encontrada."***

 

#### 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309792223255)

 **Gerenciar notificações de inconsistências**

 

É possível ativar as notificações proativas para alertar sobre inconsistências de múltiplos usuários ou lideranças; quando habilitada, o sistema notifica o usuário e direciona automaticamente para a tela de **Gestão de Inconsistências**, e essa opção pode ser ativada ou desativada a qualquer momento por meio do botão **Outras Opções...**, opção **Gerenciar notificações de inconsistências**. 

![ATIVAR-NOTIFIC-INCONSISTENCIAS.gif](https://ajuda.sankhya.com.br/hc/article_attachments/37192855872791)

 

### **4. Pontos de Atenção**

- O ajuste deve garantir apenas uma liderança ativa por colaborador.

- Embora o sistema permita múltiplos usuários, mantenha apenas um ativo por colaborador para evitar falhas de integração.

- Todas as alterações de usuários e líderes impactam diretamente nas integrações.

### **5. Dicas de Usabilidade**

- Utilize filtros para agilizar a busca em grandes bases de dados.

- Sempre revise as lideranças e usuários vinculados antes de confirmar a alteração.

### **6. Casos de Uso**

 

✅ **Exemplo Real:** 

Usuário identifica colaborador com dois líderes, remove um e confirma o ajuste.

❌ **Erro Comum:** 

Usuário tenta confirmar ajuste sem definir um líder único.

 

## **FAQ – Dúvidas Frequentes**

 

1. 

**O que acontece se não corrigir as lideranças ou usuários duplicados?**

Pode haver falhas nas integrações com sistemas externos (Vixting, Pontotel, Mindsight).

1. 

**Posso ajustar outros tipos de inconsistências cadastrais?**

Não. Essa tela foca apenas em múltiplas lideranças e múltiplos usuários. 

1. 

**Como saber se um colaborador está com inconsistência?**

Ele aparecerá na lista da tela, com a mensagem de inconsistência; múltiplos líderes ou usuários.

1. 

**O ajuste altera dados do colaborador?**

Não. A ação apenas redefine vínculos de liderança e usuário, mantendo as demais informações inalteradas.

 

## **Artigos Relacionados**

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- [Gestão de Liderança](https://ajuda.sankhya.com.br/hc/pt-br/articles/32988307114903)


---

### 🔗 Links e Referências Internas:

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Gestão de Liderança](https://ajuda.sankhya.com.br/hc/pt-br/articles/32988307114903)