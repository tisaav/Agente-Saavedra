# E0231 Rejeição: IM do emitente tomador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222832317463-E0231-Rejei%C3%A7%C3%A3o-IM-do-emitente-tomador-n%C3%A3o-est%C3%A1-autorizado-a-emitir-NFS-e-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222832317463-E0231-Rejei%C3%A7%C3%A3o-IM-do-emitente-tomador-n%C3%A3o-est%C3%A1-autorizado-a-emitir-NFS-e-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS)  
> **ID:** `37222832317463` | **Última Atualização:** 2026-07-22T14:17:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848311575)

 **MENSAGEM**

E0231 Rejeição: IM do emitente tomador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848313111)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e, o usuário recebe a rejeição E0231 informando que a **Inscrição Municipal (IM)** do emitente ou tomador **não está autorizada** a emitir notas fiscais de serviço eletrônicas no município.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832304407)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832305175)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o cadastro da empresa emitente da NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848317335)

 Na aba **"Geral"**, verifique se o campo **"Inscrição Municipal"** está preenchido corretamente, **sem caracteres especiais** (pontos, traços ou barras), apenas números.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832305559)

 Compare a Inscrição Municipal cadastrada no sistema com o **documento oficial fornecido pela Prefeitura** que valida o cadastro da empresa para emissão de NFS-e:

- 

Certifique-se de que **todos os dígitos estão corretos**, incluindo zeros à esquerda, se houver;

- 

Verifique se não há **dígitos faltando ou excedentes**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848318743)

 Caso a empresa seja **tomadora do serviço**, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do parceiro tomador.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848321815)

 Na aba **"Identificação"**, verifique se o campo **"Inscrição Municipal"** do tomador está preenchido corretamente, seguindo as mesmas orientações do passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832306199)

 Após corrigir as informações cadastrais, **salve as alterações** realizadas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832306455)

 Caso a empresa ainda não esteja autorizada junto à Prefeitura, **solicite a autorização** para emissão de NFS-e diretamente no portal da Prefeitura do município emissor.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222832307735)

 Após a confirmação da autorização pela Prefeitura e a correção dos dados cadastrais, **gere novamente o lote da NFS-e**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222848323991)

 **CAUSA**

Esta rejeição ocorre quando a **Inscrição Municipal cadastrada no sistema Sankhya** está divergente das informações registradas no **Cadastro Nacional de Contribuintes (CNC) da NFS-e** junto à Prefeitura do município emissor. Outra causa comum é quando o contribuinte **não está devidamente autorizado** pela Administração Tributária Municipal para emitir notas fiscais de serviço eletrônicas, seja por pendências cadastrais, documentação incompleta ou falta de solicitação formal de credenciamento junto ao município.