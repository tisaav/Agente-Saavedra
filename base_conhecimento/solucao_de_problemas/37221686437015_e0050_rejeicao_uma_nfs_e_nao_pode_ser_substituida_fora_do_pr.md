# E0050 Rejeição: Uma NFS-e não pode ser substituída fora do prazo estabelecido pelo município emissor da NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221686437015-E0050-Rejei%C3%A7%C3%A3o-Uma-NFS-e-n%C3%A3o-pode-ser-substitu%C3%ADda-fora-do-prazo-estabelecido-pelo-munic%C3%ADpio-emissor-da-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221686437015-E0050-Rejei%C3%A7%C3%A3o-Uma-NFS-e-n%C3%A3o-pode-ser-substitu%C3%ADda-fora-do-prazo-estabelecido-pelo-munic%C3%ADpio-emissor-da-NFS-e)  
> **ID:** `37221686437015` | **Última Atualização:** 2026-07-22T14:18:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38335462657559)

 MENSAGEM**

E0050 Rejeição: Uma NFS-e não pode ser substituída fora do prazo estabelecido pelo município emissor da NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221686432023)

 **SITUAÇÃO**

Ao tentar realizar a **substituição de uma NFS-e** através do Portal de Vendas, o sistema retorna a rejeição E0050, informando que **não é possível substituir a nota** porque o prazo estabelecido pela legislação municipal já foi ultrapassado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221686432535)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221686433175)

 Verifique junto ao **setor de NFS-e da Prefeitura** qual é o **prazo estabelecido para substituição** de NFS-e no município emissor da nota.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221689278871)

 Caso o prazo tenha sido ultrapassado, verifique se o município permite a **substituição através de solicitação de processo administrativo** diretamente no portal da Prefeitura.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221686434071)

 Se a solicitação for aceita e a substituição realizada pela Prefeitura, acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e na aba **"NFS-e"** verifique as seguintes configurações: 

- 

**"Tem substituição NFS-e":** certifique-se de que esta marcação esteja habilitada para o município em questão;

- 

**"Prazo para substituição de NFS-e":** confirme se o prazo em dias está configurado corretamente conforme a legislação municipal;

- 

**"Quantidade de substituições permitidas":** verifique se há limite de substituições dentro do mês.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221689279895)

 Caso não seja possível realizar a substituição, avalie a possibilidade de **cancelamento da nota** (se ainda estiver dentro do prazo) ou **emissão de uma nova NFS-e** com os dados corretos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221686435223)

 Para futuras emissões, certifique-se de realizar a **substituição dentro do prazo estabelecido** pelo município, acessando o **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas), localizando a NFS-e desejada e clicando no botão **"NFS-e"** e em seguida na opção **"Substituir nota"**. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221689280919)

 **CAUSA**

A rejeição ocorre porque a **tentativa de substituição da NFS-e foi realizada após o prazo estabelecido pela legislação municipal**. Cada município define um **período específico** em que é permitido substituir notas fiscais de serviço, geralmente contado em dias a partir da data de emissão. Quando este prazo é ultrapassado, o sistema da Prefeitura **bloqueia automaticamente** a operação de substituição via webservice, retornando a rejeição E0050. Esta validação visa garantir o **controle fiscal adequado** e evitar alterações em documentos fiscais fora do período permitido pela administração tributária municipal.