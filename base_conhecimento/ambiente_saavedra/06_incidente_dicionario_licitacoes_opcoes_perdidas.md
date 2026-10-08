# 📋 Registro de Ocorrência: Opção "REVOGADO" sumiu no Portal de Licitações

> **Público:** Usuários, Gestores e Equipe de Suporte / TI  
> **Data:** 05/10/2026  
> **Status:** Resolvido em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

A equipe que opera o **Portal de Licitações** relatou que, ao acessar a aba **"Itens do Edital"** e tentar definir o resultado de um item licitado, a opção **`REVOGADO`** não aparecia mais na lista suspensa (caixinha de seleção da coluna *Resultado*). Só estavam visíveis as opções: *Cancelado*, *Fracassada*, *Ganha* e *Perdido*.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

Pense nas opções dessa caixinha como um **dicionário de palavras** que o Sankhya consulta para saber o que exibir na tela.

1. No dia **21/09/2026**, o sistema Sankhya passou por uma **atualização de versão de rotina**.
2. Quando essa atualização roda, ela vem com o "dicionário de fábrica" padrão da Sankhya.
3. No pacote padrão de fábrica, as opções que a Saavedra usava no dia a dia (**`Revogado`** e **`Desclassificado`**) não vinham cadastradas.
4. Por isso, a atualização acabou sobrescrevendo a lista da tela com a lista básica de fábrica, fazendo a opção "sumir" para os usuários.
5. **Importante:** Nenhum dado foi apagado. Os itens que já tinham sido marcados como revogados no passado continuavam salvos no sistema, apenas a opção visual para escolher novamente havia sumido.

---

## ✅ 3. O que fizemos para arrumar?

1. **Localizamos o backup automático:** Confirmamos nos backups gerados antes da atualização quais opções existiam exatamente e qual o código de cada uma.
2. **Reensinou o sistema:** Inserimos novamente as opções oficiais no "Dicionário de Dados" do Sankhya:
   * **`Revogado`** (Código `R`)
   * **`Desclassificado`** (Código `D`)
   * **`Suspenso`** (Código `11`, que também havia sumido do status do edital).
3. **Validação:** Verificamos que o sistema aceitou e gravou as opções com sucesso sem precisar reiniciar o servidor e sem afetar nenhum contrato ou edital.

---

## 👤 4. Como o usuário valida no dia a dia?

Para que o navegador do usuário carregue a lista atualizada:
1. Abra o Sankhya e acesse o **Portal de Licitações**.
2. Pressione as teclas **`Ctrl` + `F5`** juntas no teclado (ou feche a aba e abra novamente).
3. Na aba **Itens do Edital**, clique na coluna **Resultado**.
4. A opção **`Revogado`** (e também **`Desclassificado`**) já estará visível para seleção.

---

## 🔧 5. Detalhes Técnicos (Para TI e Administradores do Sistema)

* **Tela Sankhya:** Portal de Licitações (`LGH_LICITE`)
* **Tabela de Itens:** `LGH_LICITE`
  * **Campo:** `RESULTADO` (NUCAMPO: `185946`)
  * **Entidade Sankhya:** `OpcaoCampo` (Tabela `TDDOPC`)
  * **Opções reinseridas:**
    * `VALOR = 'R'`, `OPCAO = 'Revogado'`, `ORDEM = 6`, `PADRAO = 'S'`
    * `VALOR = 'D'`, `OPCAO = 'Desclassificado'`, `ORDEM = 5`, `PADRAO = 'S'`
* **Tabela de Cabeçalho:** `LGH_LICCAB`
  * **Campo:** `STATUS` (NUCAMPO: `185790`)
  * **Opção reinserida:**
    * `VALOR = '11'`, `OPCAO = 'Suspenso'`, `ORDEM = 11`, `PADRAO = 'S'`
* **Origem da Perda:** Substituição padrão do pacote *Release Package 4.36b* (backup localizado na tabela `TDDOPC_RP_4_36B114`).
* **Serviço de Execução Utilizado:** `CRUDServiceProvider.saveRecord` no Gateway Sankhya.
