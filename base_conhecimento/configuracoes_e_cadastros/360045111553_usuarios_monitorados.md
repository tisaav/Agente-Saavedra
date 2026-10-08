# Usuários Monitorados

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111553-Usu%C3%A1rios-Monitorados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111553-Usu%C3%A1rios-Monitorados)  
> **ID:** `360045111553` | **Última Atualização:** 2026-07-29T13:57:59Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310970041879)

 Módulo:** Configurações > Avançado
```

Utiliza-se esta tela como uma ferramenta de acompanhamento das tarefas que forem executadas no Coletor WMS e no [Sankhya OK](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045229434). Estas tarefas passarão por uma análise de performance, que servirão para verificação de possíveis erros não casuais.

![usuarios_monitorados.png](https://ajuda.sankhya.com.br/hc/article_attachments/13349607555863)

Deve-se selecionar no campo **"Cód. Usuário" **o usuário que será monitorado e informar no campo **"Data da Expiração"** uma data superior a data atual, pois esta data determinará o término do período ao qual o usuário estará sendo monitorado.

Ao executar as tarefas pelo Coletor WMS ou Sankhya OK, o sistema irá gerar logs para análise de performance enquanto as tarefas estiverem sendo executadas, até a data informada.

**Observação:** no parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** é possível inserir o caminho da pasta destino dos logs gerados.

Serão gerados dois arquivos no diretório C:\Users\usuário do Windows\sw-logs\sqlmon, sendo eles:

- Um arquivo com as consultas executadas no banco de dados;

- Um arquivo contendo as funções que foram utilizadas no Sankhya Om.


---

### 🔗 Links e Referências Internas:

- [Sankhya OK](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045229434)