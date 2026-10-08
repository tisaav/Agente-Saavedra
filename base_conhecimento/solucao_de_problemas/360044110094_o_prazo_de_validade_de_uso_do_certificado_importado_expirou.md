# O prazo de validade de uso do certificado importado expirou

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110094-O-prazo-de-validade-de-uso-do-certificado-importado-expirou](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110094-O-prazo-de-validade-de-uso-do-certificado-importado-expirou)  
> **ID:** `360044110094` | **Última Atualização:** 2026-07-22T15:53:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356658711)

 MENSAGEM:**

O prazo de validade de uso do certificado importado expirou.
**Observação**: esta data refere-se ao prazo permitido para utilização do certificado no SanNFE e não a data de expiração do certificado digital.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356663191)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

Tenha a seu acesso o **arquivo .pfx do certificado digital atual** da empresa e sua respectiva **senha**. 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356666007)

 Acesse  a tela** "Console NFe"*** (Caminho de acesso: Comercial » Configuração);*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356669591)

 Selecione o certificado referente ao CNPJ emissor o qual está ocorrendo o problema;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356672663)

 Clique em "Remover registro", depois em "Sim".

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458097435799)

 Para inserir o novo:

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618347522071)

 Clique em "Inserir registro";

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356680471)

 Procure o certificado no diretório do computador;

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618347526807)

 Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618347528087)

 Salve o registro.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458097435799)

 Depois de reinstalar o certificado é necessário testar a comunicação do serviço:

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618347534743)

 Acesse a aba Status Serviço;

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618347536279)

 Selecione o CNPJ que acabou de fornecer no novo certificado;

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356694167)

  Marque as Opções > Produção, 4.0 e SEFAZ;

![11 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356697495)

  Clique em "Testar". 

- Caso retorne **"Serviço em Operação"** é porque a troca foi efetuada com sucesso;

- Se retornar algum outro status, entre em contato com o Service Desk Sankhya Jiva;

- Acesse o Console NF-e, exclua o certificado anteriormente atualizado e insira novamente, via opção 'Inserir Registro' com o certificado Raiz;

- Salve o novo certificado.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618356699799)

 CAUSA:**

Ocorre pela expiração da data de utilização do certificado digital no SanNFE.

Geralmente quando se utiliza a opção de Exportar via aba: Administração, botão 'Importação/Exportação' e é inserido uma data menor que a data de validade do certificado, quando se exporta o certificado.