# O servidor de nota fiscal eletrônica não está ativo 

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043154614-O-servidor-de-nota-fiscal-eletr%C3%B4nica-n%C3%A3o-est%C3%A1-ativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043154614-O-servidor-de-nota-fiscal-eletr%C3%B4nica-n%C3%A3o-est%C3%A1-ativo)  
> **ID:** `360043154614` | **Última Atualização:** 2026-07-22T16:03:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134463147031)

 MENSAGEM:**

O servidor de nota fiscal eletrônica não está ativo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499959959)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134463148567)

 Verifique o IP de instalação do servidor de nota fiscal eletrônica:

**Mitra:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Acesse o sistema pelo usuário SUP e/ou usuário com acesso a rotina abaixo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Avançado » Preferências » Todas as Preferências » CHAVE **"IPSERVNFE"**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Botão Direito na Tela » Expandir nível 3 » Visualize o IP configurado.

 

**Fast Service:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Acesse o FAST pelo usuário SUP, busque pelo caminho Utilitários » **DBEExplorer** e execute o comando SELECT * FROM TSIPAR WHERE CHAVE='IPSERVNFE'

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 O IP será apresentado com um duplo clique na coluna 'Texto'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134463150103)

 Localizado o IP acima, acesse a máquina correspondente ao mesmo para iniciar o Servidor de Nota Fiscal Eletrônica.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134463150743)

 Caso trate-se de um servidor de nota fiscal eletrônica **Windows**:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 No Menu Iniciar da máquina buscar por **"services.msc"**:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Aberto o services, busque do lado direito pelo serviço **"sannfe-service"**, conforme abaixo:

 

![2.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/14632966755479)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Possivelmente a coluna STATUS estará em branco e do lado direito estará habilitado a opção **"Inicia o serviço"**. Clique em Iniciar e aguarde que a inicialização seja concluída.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Atualize o services (botão atualizar na barra de ferramentas) e verifique se o STATUS passou a ser apresentado com a informação "Em execução".

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Em caso positivo, teste uma nova emissão.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499965591)

 Caso trate-se de um servidor de nota fiscal eletrônica **Linux**:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Através do aplicativo putty, acesse o IP do servidor de nota fiscal eletrônica pelo usuário mgeweb

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Localize a pasta do sannfe (normalmente na pasta home/mgeweb) e execute o comando: **./sannfe-service start**

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17803876062743)

 IMPORTANTE:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 Recomenda-se que o procedimento acima seja realizado por um usuário da empresa com conhecimento na infra/T.I. 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16134499961623)

 A princípio essa situação pode ocorrer apenas para sistema da Linha DELPH (Mitra), visto que para a Linha W esse serviço não precisa estar iniciado.