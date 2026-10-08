# ORA-20101: Lote deve ser informado

> **Módulo:** Solucao de Problemas | **Subseção:** Erros Internos  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15501207559959-ORA-20101-Lote-deve-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/15501207559959-ORA-20101-Lote-deve-ser-informado)  
> **ID:** `15501207559959` | **Última Atualização:** 2026-07-22T14:56:45Z

---

**

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/15501237487127)

 MENSAGEM:**

ORA-20101: Lote deve ser informado.

ORA-06512: em "SANKHYA.TRG_UPT_TGFITE", line 719

ORA-04088: erro durante a execução do gatilho. 

"SANKHYA.TRG_UPT_TGFITE"

 

**

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/15501270248343)

 CAUSA:**

O erro ocorre devido a validação de informações que a trigger TRG_UPT_TGFITE (bases SQL) faz. A trigger faz as seguintes validações 

SELECT
       1
     FROM INSERTED INS
     WHERE INS.ATUALESTOQUE <> 0 (se o campo ATUALESTOQUE for diferente de 0)
     AND INS.RESERVA <> 'S' (se estiver para reservar estoque igual a 'SIM')
     AND INS.CONTROLE = ' ' (se o campo Controle/Lote não estiver preenchido no cadastro do produto ou na central)
     AND INS.CODPROD = @CODPROD)
     AND @TIPCONTEST = 'L' 
     AND NOT UPDATE(QTDCONFERIDA)
     AND NOT UPDATE (QTDENTREGUE)
   BEGIN
     SET @ERRMSG = **'Lote deve ser informado.'**
     GOTO ERROR
   END

 

Sendo assim, ao tentar fazer o cálculo da comissão na tela 'Cálculo de Comissão por Fórmula (Comercial » Avançado)' o sistema apresentará erro se alguma das informações estiverem dentro das validações que trigger faz. 

**

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/15501242365591)

 SOLUÇÃO:**

Para solução é necessário identificar qual nota está sendo feita o cálculo da comissão (se for mais de uma será necessário identifica-la no Monitor de Consultas). Abrir a nota na Central e validar produto por produto se o campo 'Lote' está preenchido com o número do lote, se por acaso não estiver preenchido será necessário informa-lo e somente assim será possível calcular a comissão. 

Se não for viável a alteração das notas, ou se a mesma estiver aprovada a saída é desligar o parâmetro ATUALCOMITE para que os itens não sejam atualizados durante o cálculo de comissão. Desligando o parâmetro basta realizar o cálculo das comissões. **Após o cálculo deve-se ligar o parâmetro novamente! **

Quando parâmetro **ATUALCOMITE estiver ligado**, o cálculo de comissão altera os itens da nota gravando os valores da comissão.
Para essa atualização ser feita de maneira correta, **os itens devem estar lançados corretamente de acordo com as configurações atuais do produto. **

**O parâmetro ATUALCOMITE tem o seguinte comportamento; **
 
Quando habilitado, apresenta os campos Vlr.Com .Vendedor, %Com. Vendedor, Vlr.Com. Gerente e %Com. Gerente na TGFITE, . Estes campos são preenchidos quando for feito cálculo da comissão para esta nota. 

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18583844627735)

 ****OBSERVAÇÃO:  **

Caso a nota já esteja confirmada/aprovada, é de suma importância informar ao responsável que o estoque do mesmo pode estar irregular, uma vez que era para ter saído do estoque um produto com determinado lote e se a nota foi aprovada sem o produto ter o lote informado ou ter sofrido a devida alteração, possivelmente irá ocorre irregularidade na quantidade de estoque.