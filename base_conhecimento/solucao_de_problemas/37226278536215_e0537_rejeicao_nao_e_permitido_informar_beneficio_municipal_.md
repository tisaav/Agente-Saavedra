# E0537 Rejeição: Não é permitido informar benefício municipal (BM deve ser nulo) quando o município de incidência do ISSQN não está "Ativo" no Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226278536215-E0537-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-benef%C3%ADcio-municipal-BM-deve-ser-nulo-quando-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-n%C3%A3o-est%C3%A1-Ativo-no-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226278536215-E0537-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-benef%C3%ADcio-municipal-BM-deve-ser-nulo-quando-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-n%C3%A3o-est%C3%A1-Ativo-no-Sistema-Nacional-NFS-e)  
> **ID:** `37226278536215` | **Última Atualização:** 2026-09-11T14:39:35Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/37226262838551)

**Mensagem**

E0537 Rejeição: Não é permitido informar benefício municipal (BM deve ser nulo) quando o município de incidência do ISSQN não está "Ativo" no Sistema Nacional NFS-e.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37226262841623)

**Situação**

Ao tentar emitir uma NFS-e, o sistema apresenta a mensagem de rejeição E0537, indicando que foi informado um **benefício fiscal municipal** para um município que **não está ativo no Sistema Nacional NFS-e**.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37226278527639)

**Solução**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226262843415)

 Confirme o status do município de incidência do ISSQN:

- 

Verifique se o município informado na nota fiscal está ativo no **Sistema Nacional NFS-e**.

- 

Para isso, acesse o portal da prefeitura ou consulte a documentação oficial.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37639336822935)

 Caso o município informado na nota não esteja ativo no **Sistema Nacional NFS-e**, siga os passos abaixo para remover o benefício fiscal municipal:

- 

Acesse a tela** "Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação – TOP).

- 

Localize o tipo de operação utilizado na emissão da NFS-e.

- 

Na aba **“NFS-e”**, verifique se há algum **benefício fiscal municipal** configurado.

- 

Se houver, remova-o, deixando o campo **em branco ou nulo**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37639336823703)

 Se o município estiver ativo no **Sistema Nacional NFS-e**, mas a rejeição continuar, verifique:

- 

Se o **código do benefício fiscal** informado está correto;

- 

Se ele é **válido para o município** em questão.

Para confirmar, consulte o **manual da prefeitura** com os códigos de benefícios aceitos.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226262846615)

 Após realizar todos os ajustes necessários, emita novamente a NFS-e para validar se a rejeição foi solucionada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226278532759)

 **CAUSA**

A rejeição ocorre porque foi informado um **benefício fiscal municipal** na NFS-e, porém o **município de incidência do ISSQN** não está cadastrado como ativo no Sistema Nacional NFS-e. Segundo as regras de validação da Sefaz, **somente municípios ativos** no sistema podem ter benefícios fiscais municipais informados nas notas fiscais de serviço eletrônicas.