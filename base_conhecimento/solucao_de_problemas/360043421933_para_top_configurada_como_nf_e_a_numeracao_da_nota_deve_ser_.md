# Para TOP configurada como NF-e a numeração da nota deve ser automática

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043421933-Para-TOP-configurada-como-NF-e-a-numera%C3%A7%C3%A3o-da-nota-deve-ser-autom%C3%A1tica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043421933-Para-TOP-configurada-como-NF-e-a-numera%C3%A7%C3%A3o-da-nota-deve-ser-autom%C3%A1tica)  
> **ID:** `360043421933` | **Última Atualização:** 2026-07-22T16:04:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788777367)

 MENSAGEM:**

[CORE_E01858] Para TOP configurada como NF-e a numeração da nota deve ser automática.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117772165527)

 SOLUÇÃO:**

Considerando a emissão de nota fiscal eletrônica, na qual o número nota é gerado de forma sequencial pelo sistema, realize devidamente a marcação abaixo:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788782103)

 **Acesse a tela** "[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros).*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117772169111)

 Selecione a TOP utilizada no respectivo lançamento e na aba **"Impressão"**, marque o campo '**Numeração somente automática**';

 

****

| Após fazer o ajuste mencionado (conforme imagem abaixo), lembre-se de forçar a atualização dessa informação em seu lançamento. Sugerimos que troque a TOP do cabeçalho da nota, salve a alteração, em seguida volte para a TOP correta. |
| --- |

 

![697.png](https://ajuda.sankhya.com.br/hc/article_attachments/14610531126423)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788788119)

 Caso o procedimento de forçar a troca da TOP não solucione, refaça o lançamento/faturamento;

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17804097623319)

 IMPORTANTE:**

****************

| Caso esteja realizando o lançamento de uma nota emitida por Terceiros e a numeração de fato NÃO deva ser automática, será necessário ajustar a configuração do campo "NF-e" da aba "Impressão" para "Terceiros". |
| --- |

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788797463)

 OBSERVAÇÕES**:
 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788788119)

Se o parâmetro **"Valida config. de Nr automática** na **TOP-VALNRAUTTOP**" estiver ligado, ao criar ou alterar uma TOP de Venda ou Compra, com o campo NF-e diferente de Convencional (Não Usa NF-e), Import. Doc. (Emissão Própria) e Terceiros, na aba **"Impressão"** a marcação **"Numeração somente automática"** deverá estar selecionada e o campo **"Base de Numeração"** deverá indicar a opção **"Venda"** ou **"Devolução de venda"**.
 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788788119)

Caso não esteja marcada, ao tentar salvar a configuração o sistema apresentará a seguinte mensagem:
 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117788799639)

“Para TOP Configurada com Modelo de Documento 55 - Nota Fiscal Eletrônica e o campo NF-e diferente de ‘Convencional (Não Usa NF-e)', ‘Import. Doc.(Emissão Própria)' e 'Terceiros’ a numeração da Nota deve ser automática". Marque a opção **"Numeração somente automática"** e use a **"base de numeração"** Venda ou Devolução de venda".

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117772186135)

 CAUSA**:

Mensagem será apresentada ao realizar emissão de nota fiscal eletrônica, utilizando um tipo de operação com a configuração não definida com 'numeração somente automática';


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)