# Não é permitido excluir/alterar custo com data anterior a DD/MM/AA

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088833-N%C3%A3o-%C3%A9-permitido-excluir-alterar-custo-com-data-anterior-a-DD-MM-AA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088833-N%C3%A3o-%C3%A9-permitido-excluir-alterar-custo-com-data-anterior-a-DD-MM-AA)  
> **ID:** `360044088833` | **Última Atualização:** 2026-07-22T16:01:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108127681303)

 MENSAGEM:**

Não é permitido excluir/alterar custo com data anterior a dd/mm/aa.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108160169623)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108160171287)

 Acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"*** (Configurações » Avançado).*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108127689111)

 No campo de busca ao lado esquerdo da tela, busque pela Chave **"DIASLIMALTCUSTO - Dias limite para excluir custos"**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108127690135)

 Verifique o valor informado no campo **"Inteiro"**:

 

![DIASLIMALTCUSTO.png](https://ajuda.sankhya.com.br/hc/article_attachments/12300118547863)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108127691543)

 Este valor é o limite de dias retroativos para que essa exclusão/alteração seja permitida. Exemplo: Se estiver como 180, o sistema só deixará você fazer a exclusão de notas que atualizam custo lançadas até 180 dias anteriores a data de hoje;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108160182679)

 Para conseguir prosseguir com a operação, altere o parâmetro informando no mesmo uma quantidade de dias suficientes para realizar o ajuste desejado.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108160182679)

 Lembrando que tal alteração deve ser realizada de forma consciente, visto que informações de Custo e a permissão de exclusão desses de forma retroativa trata-se de uma decisão de suma importância em sua empresa.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108127695383)

 Após alteração do parâmetro, recomendável fechar as telas do sistema ou acessar novamente o sistema para realizar a operação desejada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108160185495)

 CAUSA:**

Quando houver a tentativa de alteração/exclusão de pedidos/notas no sistema em que houve atualização de Custos, ocorre a mensagem. Essa será ocasionada quando a quantidade de dias entre a data de atualização desse custo e a data de alteração/exclusão for superior ao informado no parâmetro DIASLIMALTCUSTO.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)