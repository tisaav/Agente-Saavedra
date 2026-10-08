# Cópia de personalização da tela Parceiros não replica campo da aba Crédito

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39380544306839-C%C3%B3pia-de-personaliza%C3%A7%C3%A3o-da-tela-Parceiros-n%C3%A3o-replica-campo-da-aba-Cr%C3%A9dito](https://ajuda.sankhya.com.br/hc/pt-br/articles/39380544306839-C%C3%B3pia-de-personaliza%C3%A7%C3%A3o-da-tela-Parceiros-n%C3%A3o-replica-campo-da-aba-Cr%C3%A9dito)  
> **ID:** `39380544306839` | **Última Atualização:** 2026-08-18T12:47:34Z

---

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39380544305303)

 SITUAÇÃO

Ao usar a funcionalidade de copiar personalização de tela (Configurações > Cadastros > Parceiros > Configuração da Tela > Copiar Personalização) de um usuário de origem para um usuário de destino, o sistema não replica todos os campos, em especial, da aba "Crédito", que não aparecem para o usuário de destino após a cópia.

 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39380557937687)

 SOLUÇÃO

Para que a cópia da personalização funcione corretamente e replique todos os campos, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380557937815)

 Acesse "Acessos" (Configurações > Segurança > Acessos).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380544306455)

 No campo de pesquisa, consulte a tela "Parceiros".

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380557937943)

 Localize o usuário destino (para quem a personalização será copiada) e habilite a marcação "Especiais" para ele.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39380557938199)

 Salve as alterações.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39380557938327)

 Peça para o usuário origem abrir a tela Parceiros e salvar a personalização novamente, agora incluindo os campos "Tabela de Preço" e aba "Crédito" (que passaram a ficar visíveis).

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39380557938455)

 Peça para o usuário destino abrir a tela Parceiros e confirmar que os campos aparecem corretamente.

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39380557939479)

 CAUSA

O acesso à tela Parceiros possui uma marcação chamada "Especiais" (Configurações > Segurança > Acessos), que controla a exibição de campos da aba "Crédito" (limite de crédito, prazo de pagamento, motivo de bloqueio, entre outros). Sem essa marcação habilitada, o sistema remove esses campos da tela do usuário, ele simplesmente não os vê.

Usuário de destino sem "Especiais": mesmo que a personalização copiada contenha configurações desses campos, eles continuam sendo removidos da tela do destino quando ele a abre. A marcação "Especiais" de cada usuário é checada individualmente.