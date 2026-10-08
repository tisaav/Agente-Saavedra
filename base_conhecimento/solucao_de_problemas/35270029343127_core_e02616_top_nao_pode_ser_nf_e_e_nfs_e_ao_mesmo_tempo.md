# CORE_E02616: TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35270029343127-CORE-E02616-TOP-n%C3%A3o-pode-ser-NF-e-e-NFS-e-ao-mesmo-tempo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35270029343127-CORE-E02616-TOP-n%C3%A3o-pode-ser-NF-e-e-NFS-e-ao-mesmo-tempo)  
> **ID:** `35270029343127` | **Última Atualização:** 2026-07-22T14:25:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35270029328279)

 **MENSAGEM**

[CORE_E02616] TOP não pode ser 'NF-e' e 'NFS-e' ao mesmo tempo.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490113491095)

 **SITUAÇÃO**

A mensagem aparece quando o usuário tenta configurar uma **"TOP"** (Configurações » Fiscal » TOP) com os campos **"NF-e"** e **"NFS-e"** habilitados simultaneamente. O sistema identifica este conflito durante a validação e impede o salvamento da configuração.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35269985448343)

 **SOLUÇÃO**

#### **Configure o campo NFS-e:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490113492375)

 Acesse a tela **"TOP"** (Configurações » Fiscal » TOP) e localize a TOP que apresentou o erro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490113493399)

 Clique na aba **"NFS-e"** da TOP.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490113496215)

 No campo **"NFS-e"**, selecione a opção **"Convencional (Não usa NFS-e)" **e salve a alteração.
 

#### **Configure o campo NF-e:**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490124970903)

  Em seguida, ainda TOP que apresentou o erro, acesse a aba **"NF-e/NFC-e/CF-e".**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490124975511)

 Configure o campo **"NF-e"** conforme desejado (Normal, Complementar, Anulação ou Devolução) e salve.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35490113500695)

 **Importante:**** sempre configure primeiro o campo NFS-e como "Convencional" antes de alterar o campo NF-e para evitar este erro de validação.**

 

#### **Observações:**

**Quando há uma configuração legada,** na qual não existe licença de emissão de NFS-e, o campo NFS-e pode ficar com valor padrão e não permitir alteração através da interface. Nestes casos:

- O valor do campo NFS-e no banco de dados pode estar diferente de "M" (Convencional)

- É necessário que seu DBA execute um comando SQL para alterar o valor para (M - Convencional)

Após a alteração pelo DBA, será possível configurar o campo NF-e normalmente

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35270029334295)

 **CAUSA**

O erro ocorre porque o sistema não permite que uma TOP seja configurada para emitir **NF-e** (Nota Fiscal Eletrônica) e **NFS-e** (Nota Fiscal de Serviços Eletrônica) simultaneamente. A validação identifica quando o campo **"NF-e"** está configurado com valores diferentes de "Não emite" enquanto o campo **"NFS-e"** não está como "Convencional (Não usa NFS-e)".