# E0115 Rejeição: Valor 0 para o motivo da não informação do NIF do prestador não é permitido na Sefin do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222110155415-E0115-Rejei%C3%A7%C3%A3o-Valor-0-para-o-motivo-da-n%C3%A3o-informa%C3%A7%C3%A3o-do-NIF-do-prestador-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222110155415-E0115-Rejei%C3%A7%C3%A3o-Valor-0-para-o-motivo-da-n%C3%A3o-informa%C3%A7%C3%A3o-do-NIF-do-prestador-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e)  
> **ID:** `37222110155415` | **Última Atualização:** 2026-07-22T14:18:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222110139031)

 **MENSAGEM**

E0115 Rejeição: Valor 0 para o motivo da não informação do NIF do prestador não é permitido na Sefin do Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125982359)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** via **Sistema Nacional**, o usuário não informou corretamente o **NIF (Número de Identificação Fiscal)** do prestador de serviços ou selecionou o **valor "0" como motivo** para a não informação do NIF, o que não é permitido pela **Sefin** (Secretaria de Finanças) no padrão nacional de emissão de NFS-e.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125982871)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222110147351)

 Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros) e localize o **prestador de serviços** vinculado à NFS-e que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125983255)

 Na aba **''Fiscal''** verifique o campo **''Indicativo do NIF''** está preenchido corretamente com o Número de Identificação Fiscal do prestador.

- 

Caso o prestador não possua NIF, **não selecione o valor "0"** como motivo da não informação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222110148759)

 Caso o prestador não possua NIF, selecione um **motivo válido** para a não informação do NIF, conforme as opções disponibilizadas pelo **Sistema Nacional de NFS-e**.

- 

Os motivos válidos são aqueles diferentes de "0".

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222110149783)

 Salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125984791)

 Retorne à tela de **emissão da NFS-e** e tente emitir novamente a nota fiscal. Certifique-se de que as **credenciais de login da prefeitura** estejam configuradas corretamente, conforme orientado no artigo sobre **Emissão da Nota Fiscal de Serviço Eletrônica Padrão Nacional via Broker**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125987863)

 Caso não possua as credenciais ou informações sobre o NIF do prestador, **procure o contador da empresa** ou entre em contato com a **Prefeitura** responsável pela emissão da NFS-e. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222125991319)

 **CAUSA**

A rejeição ocorre porque o **Sistema Nacional de NFS-e** da **Sefin** não permite que o **valor "0"** seja utilizado como motivo para a não informação do **NIF do prestador** de serviços. Quando o NIF não é informado, é **obrigatório selecionar um motivo válido** diferente de "0", conforme as regras de validação estabelecidas pela Secretaria de Finanças. A ausência de um motivo válido ou a seleção incorreta resulta na **rejeição E0115** durante a transmissão da nota fiscal.