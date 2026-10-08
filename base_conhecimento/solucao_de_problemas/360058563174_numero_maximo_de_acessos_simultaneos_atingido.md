# Número máximo de acessos simultâneos atingido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360058563174-N%C3%BAmero-m%C3%A1ximo-de-acessos-simult%C3%A2neos-atingido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058563174-N%C3%BAmero-m%C3%A1ximo-de-acessos-simult%C3%A2neos-atingido)  
> **ID:** `360058563174` | **Última Atualização:** 2026-07-22T15:26:26Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273328083223)

 MENSAGEM:**

[CORE_E01435] Número máximo de acessos simultâneos atingido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273318627991)

 SOLUÇÃO:
**

Para correção, siga os passos abaixo:

**
**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273318630807)

 Acesse o cadastro de usuários em: *Configurações » Controle de Acesso » Usuários*
Aba: **"Identificação"**
Campo **"Empresa"**: verifique o código da empresa vinculado ao usuário

![N_mero_m_ximo_de_acessos_simult_neos_atingido_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14660830848407)

**
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273318631959)

 Acesse a tela ****["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas) (Caminho de acesso: *Configurações » Cadastros » Empresas*):

No campo **"Quantidade de usuários logados simultaneamente"**, realize a limitação do número de conexões **"por empresa"** no SankhyaOM. 
Depois de configurado este campo, sendo feita a tentativa de acesso ao sistema com um número de usuários (conforme a empresa do usuário logado) que seja superior ao aqui estipulado, será apresentada a mensagem.

 

![N_mero_m_ximo_de_acessos_simult_neos_atingido_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14660950393623)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273318633751)

 CAUSA:**

Essa mensagem é resultante da Quantidade de Acessos Simultâneos configurada no Cadastro de Empresas (*Configurações » Cadastros » Empresas*), campo: Quantidade de usuários logados simultaneamente, de acordo com a empresa vinculada ao cadastro do usuário.


---

### 🔗 Links e Referências Internas:

- ["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)