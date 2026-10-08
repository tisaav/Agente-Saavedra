# Para NF-e (emissão própria) informar somente os registros C100 e C190

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111014-Para-NF-e-emiss%C3%A3o-pr%C3%B3pria-informar-somente-os-registros-C100-e-C190](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111014-Para-NF-e-emiss%C3%A3o-pr%C3%B3pria-informar-somente-os-registros-C100-e-C190)  
> **ID:** `360044111014` | **Última Atualização:** 2026-08-10T20:52:29Z

---

### **Erros no Registro C170 - EFD ICMS/IPI**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18664212223255)

**MENSAGEM:**
Para NF-e (emissão própria) informar somente os registros C100 e C190 e se for o caso, os regs. C105, C110 e filhos, C120, C170 e C176, ou C195 ou C195 e C197.
 

**Principais causas dos erros no C170:**
 

- 

Opção de geração do registro C170 marcada indevidamente para NF-e de emissão própria.

- 

Campo **"Referência"** do produto está em branco no cadastro.

- 

Notas fiscais de serviço sendo geradas incorretamente no livro de ICMS/IPI.

- 

Produtos sem código devidamente cadastrado.

- 

Configurações incorretas dos parâmetros de geração do EFD.

**Como resolver erros no C170:**
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18664212237975)

 Se a mensagem indicar erro em NF-e de emissão própria, acesse **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (Livros Fiscais >> Conexão >> EFD - Escrituração Fiscal Digital - ICMS/IPI) e na aba **"Opções"**, **desmarque** a opção **"Gerar Registro C170/C173/C176 para NF-e de emissão própria"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/18664212245399)

 Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos) e verifique se todos os produtos possuem o campo **"Referência"** preenchido na aba **"Geral"**. Este campo é obrigatório para a geração do código do item no registro C170.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42618733154839)

 Verifique se as notas fiscais de serviço estão sendo geradas no livro correto. Notas de serviço devem ser escrituradas no livro de ISS, não no livro de ICMS/IPI. Para corrigir, acesse o **"Tipo de Operação (TOP)"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) e configure para não atualizar o livro de ICMS/IPI e atualizar o livro de ISS para aquisições de serviços.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42618743031447)

 Verifique os parâmetros **"Usa Unidade padrão do produto no R.0200 - EFD (USAUNIPADR0200)"** e **"Usar cód. de barras da unidade alternativa no SPED (LIVUSACODBARALT)"** em **"Preferências"** (Configurações >> Avançado >> Preferências).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42618733155735)

 Após realizar as correções, gere novamente o arquivo TXT e valide no Programa Validador e Assinador (PVA) da Receita Federal.
 

###