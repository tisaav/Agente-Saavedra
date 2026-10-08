# Uso do local "Em Trânsito" em transferências de imobilizado entre empresas

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35644814485783-Uso-do-local-Em-Tr%C3%A2nsito-em-transfer%C3%AAncias-de-imobilizado-entre-empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/35644814485783-Uso-do-local-Em-Tr%C3%A2nsito-em-transfer%C3%AAncias-de-imobilizado-entre-empresas)  
> **ID:** `35644814485783` | **Última Atualização:** 2026-09-15T17:55:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019769810711)

 **MENSAGEM:**

Recomenda-se utilizar o local “Em Trânsito” nas transferências de imobilizado entre empresas para evitar que o bem seja considerado disponível antes da chegada física.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019769811991)

 **SITUAÇÃO:**

Ao registrar a nota de transferência diretamente para o local de destino, o sistema passa a considerar o bem como disponível na empresa de destino antes da chegada física, gerando inconsistência entre o controle físico e o controle fiscal.

Utilize o local **"Em Trânsito"** como etapa intermediária para representar o período de transporte e evitar que o bem seja usado ou localizado incorretamente.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019765581975)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019769815191)

 Registre a remessa entre empresas:

- 

Abra o documento de transferência; 

- 

Informe o **"Local de Origem"** com o local atual do bem;

- 

Informe o **"Local de Destino"** como **"Em Trânsito"; **

- 

Selecione a TOP com **"Atualização do Bem"** adequada (ex.: *Transf. Saída/Remessa*) e preencher as configurações fiscais conforme a operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019769816855)

 Registre a chegada física (transferência de local):

- 

Abra o documento de transferência de local; 

- 

Informe o **"Local de Origem"** como **"Em Trânsito"; **

- 

Informe o **"Local de Destino"** como o local definitivo na empresa de destino; 

- 

Use a TOP que atualize o local do bem sem efeito fiscal, se aplicável.
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019769818263)

 Valide o processo:

- 

Confirme que a nota de remessa representa a saída fiscal e que o bem ficou com local “Em Trânsito”; 

- 

Confirme que a nota de chegada atualiza o local físico do bem para o destino definitivo; 

- 

Confira a ficha patrimonial e os registros fiscais para garantir consistência.

 

#### **Exemplo: Nota de Transferência**

![image (30).png](https://ajuda.sankhya.com.br/hc/article_attachments/36020358617623)

 

#### **Exemplo: Nota de Movimentação de Local **

![image (31).png](https://ajuda.sankhya.com.br/hc/article_attachments/36020358621463)

 

#### **Exemplo: Ficha Patrimonial **

![image (32).png](https://ajuda.sankhya.com.br/hc/article_attachments/36020358623639)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36019765593623)

 **CAUSA:**

O lançamento direto para o local de destino faz com que o sistema interprete que o bem já está fisicamente disponível na empresa de destino. Isso ocorre por ausência da etapa intermediária que represente o transporte físico, gerando divergência entre disponibilidade física e controle fiscal.