# Documento XXXXX: No space Left on device

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32396794581143-Documento-XXXXX-No-space-Left-on-device](https://ajuda.sankhya.com.br/hc/pt-br/articles/32396794581143-Documento-XXXXX-No-space-Left-on-device)  
> **ID:** `32396794581143` | **Última Atualização:** 2026-07-22T14:31:32Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32396781317271)

 **MENSAGEM:**

Documento XXXXX: No space Left on device.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32396794571927)

SOLUÇÃO:**

Libere** espaço em disco** no servidor onde o sistema está instalado.

**Recomendado:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33013999903383)

 Acione o DBA ou administrador de infraestrutura**, que poderá:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33013975586839)

 Verificar o volume afetado (geralmente `/tmp`, `/var`, `C:\Temp` ou diretórios específicos).

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33013975586839)

 Realizar a **limpeza de arquivos temporários antigos ou não utilizados**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33013975586839)

 Avaliar e, se possível, redimensionar o volume ou mover dados antigos para armazenamento externo.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33013975587863)

 Caso a empresa **não tenha DBA, equipe de infraestrutura ou ****hospedagem de servidor** é recomendável acionar a unidade de negocio. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32396794573079)

CAUSA:**

Esse erro ocorre devido à **falta de espaço livre em disco no servidor de aplicação**.

No momento da geração do PDF (ou outro tipo de saída de impressão), o sistema Sankhya precisa alocar espaço em disco para criar arquivos temporários. Caso o volume de armazenamento onde esses arquivos são gravados esteja cheio, o sistema operacional retorna o erro `"No space left on device"`, impedindo a conclusão da tarefa.