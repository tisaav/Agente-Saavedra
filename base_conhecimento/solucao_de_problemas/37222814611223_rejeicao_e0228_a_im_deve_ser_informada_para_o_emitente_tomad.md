# REJEIÇÃO E0228: A IM deve ser informada para o emitente tomador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222814611223-REJEI%C3%87%C3%83O-E0228-A-IM-deve-ser-informada-para-o-emitente-tomador-do-servi%C3%A7o-na-DPS-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222814611223-REJEI%C3%87%C3%83O-E0228-A-IM-deve-ser-informada-para-o-emitente-tomador-do-servi%C3%A7o-na-DPS-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS)  
> **ID:** `37222814611223` | **Última Atualização:** 2026-07-22T14:17:24Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799468567)

 **MENSAGEM**

E0228 Rejeição: A IM deve ser informada para o emitente tomador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799469463)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços eletrônica)** em que o **emitente é também o tomador do serviço**, o sistema rejeitou o documento porque a **Inscrição Municipal (IM)** do emitente não foi informada corretamente na DPS (Declaração de Prestação de Serviços), conforme exigido pelo **Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799469847)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222814600343)

 Acesse a tela **"Empresa"** (Configurações » Cadastros » Empresa) e localize o cadastro da empresa emitente da NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799471767)

 Verifique se o campo **"Inscrição Municipal (IM)"** está preenchido corretamente com o número de inscrição municipal da empresa no município emissor.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799472663)

 Caso a **Inscrição Municipal** não esteja cadastrada ou esteja incorreta, atualize o campo com as informações corretas fornecidas pela prefeitura do município.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222814603671)

 Confirme que o campo **"Código do contribuinte da NFS-e"** também está preenchido, pois este código é necessário para a emissão de NFS-e e deve estar de acordo com o cadastro no CNC do município.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222814606103)

 Salve as alterações realizadas no cadastro da empresa.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222814606871)

 Retorne ao ''**Portal de Vendas'' **(Comercial » Consulta » Portal de Vendas)** **e gere novamente a NFS-e, garantindo que todas as informações do emitente tomador estejam corretas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222799474455)

 **CAUSA**

A rejeição ocorre porque, quando o **emitente é também o tomador do serviço** na DPS, a legislação municipal exige que a **Inscrição Municipal (IM)** seja obrigatoriamente informada no documento fiscal. Esta informação deve estar **registrada no Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município emissor. A ausência ou incorreção da IM no cadastro da empresa impede a validação do documento pela Sefaz municipal, resultando na rejeição E0228.