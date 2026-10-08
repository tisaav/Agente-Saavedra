# ORA-01400: não é possível inserir NULL em ("SANKHYA"."TGWITT"."CODENDDESTINO")

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20342186373911-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGWITT-CODENDDESTINO](https://ajuda.sankhya.com.br/hc/pt-br/articles/20342186373911-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGWITT-CODENDDESTINO)  
> **ID:** `20342186373911` | **Última Atualização:** 2026-07-22T14:51:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20342201201943)

 **MENSAGEM:**

ORA-01400: não é possível inserir NULL em ("SANKHYA"."TGWITT"."CODENDDESTINO").

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20342201206295)

CAUSA:**

Ao cancelar uma expedição pela rotina de expedição de mercadorias - botão outras opções 'Cancelar separação' ou quando a expedição já está cancelada, mas, no coletor de dados é necessário gerar a tarefa de retorno das mercadorias, através da tarefa subsequente ao momento que foi cancelada a expedição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20342186369815)

SOLUÇÃO:**

Quando o parâmetro** "Utiliza lote único por endereço? - LOTEUNICOXEND" **está habilitado, é necessário configurar nas[preferências da empresa no](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) campo **"Cód. End. Armazenamento Indefinido" **indique um endereço de armazenamento indefinido que é utilizado durante a geração de tarefas de armazenagem, quando nenhuma regra de armazenagem é satisfeita. Deste modo, é gerada tarefa com a quantidade restante a armazenar para o endereço definido neste campo.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20440559830039)


---

### 🔗 Links e Referências Internas:

- [preferências da empresa no](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)