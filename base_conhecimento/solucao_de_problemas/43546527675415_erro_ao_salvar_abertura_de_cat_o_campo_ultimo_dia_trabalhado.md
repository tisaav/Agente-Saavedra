# Erro ao salvar abertura de CAT -  O campo Último dia Trabalhado não pode ser menor que a data de admissão.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546527675415-Erro-ao-salvar-abertura-de-CAT-O-campo-%C3%9Altimo-dia-Trabalhado-n%C3%A3o-pode-ser-menor-que-a-data-de-admiss%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546527675415-Erro-ao-salvar-abertura-de-CAT-O-campo-%C3%9Altimo-dia-Trabalhado-n%C3%A3o-pode-ser-menor-que-a-data-de-admiss%C3%A3o)  
> **ID:** `43546527675415` | **Última Atualização:** 2026-09-26T01:14:33Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/43546527649815)

 **MENSAGEM**

- O campo **"Último dia Trabalhado"** não pode ser menor que a data de admissão.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43546557800087)

 **SITUAÇÃO**

O erro ocorre ao tentar salvar o registro de uma CAT - Comunicação de Acidente de Trabalho na tela **"CAT - Comunicação de Acidente de Trabalho"** (Pessoal Rotinas SESMT CAT - Comunicação de Acidente de Trabalho), antes de preencher todas as informações obrigatórias nas abas **"Informações Gerais da CAT"** e **"Local do Acidente"**. O sistema valida os dados e impede o salvamento caso algum campo essencial, como o **"Último dia Trabalhado"**, esteja incoerente em relação à data de admissão do colaborador.
 

Esse erro ocorre ao tentar registrar uma CAT (Comunicação de Acidente de Trabalho) no Sankhya, quando o campo “Último dia Trabalhado” foi preenchido com uma data anterior à data de admissão do colaborador. O sistema faz essa validação para garantir a integridade dos dados, pois não é possível que o funcionário tenha trabalhado antes de ser admitido.

Além disso, para casos de reabertura de CAT, o campo “Último dia Trabalhado” deve ser posterior ao evento de origem, conforme as regras do sistema.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/43546557804183)

 **SOLUÇÃO**

Para solucionar o erro e conseguir salvar a abertura da CAT, siga o passo a passo abaixo:

1. 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43546557808279)

  Acesse a tela **"CAT - Comunicação de Acidente de Trabalho"** (Pessoal+ » Rotinas Folha » SESMT » CAT - Comunicação de Acidente de Trabalho).
 

1. 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43546557809303)

  Clique no botão **"Novo registro"** para iniciar o cadastro da CAT.
 

1. 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43546527657623)

  Preencha todos os campos obrigatórios na aba **"Informações Gerais da CAT"**, incluindo **"Empresa"**, **"Funcionário"**, **"Tipo de CAT"**, **"Emitente"**, **"Data da CAT"**, **"Data do Acidente"**, **"Hora do Acidente"**, **"Horas Trabalhadas"** e **"Último dia Trabalhado"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43561506506007)

 

1. 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43546557811863)

  Acesse a aba **"Local do Acidente"** e preencha todas as informações referentes ao local e ambiente de trabalho onde ocorreu o acidente.
 

1. 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43546557815191)

  Após preencher todas as abas obrigatórias, clique no botão **"Salvar"** para registrar a CAT.
 

Caso o erro persista, revise se a data informada no campo **"Último dia Trabalhado"** não é anterior à data de admissão do colaborador. Corrija, se necessário, para garantir a coerência das informações.

 

**Resumo dos Pontos de Atenção**

- O “Último dia Trabalhado” nunca pode ser anterior à data de admissão.

- Em reabertura de CAT, a data deve ser posterior à CAT de origem.

- Sempre valide as datas antes de finalizar qualquer movimentação.

- Manter a integridade das datas é fundamental para evitar rejeições no eSocial e inconsistências legais.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/43546527663767)

 **CAUSA**

A causa do erro está relacionada ao salvamento do registro da CAT antes do preenchimento completo das informações obrigatórias nas abas **"Informações Gerais da CAT"** e **"Local do Acidente"**. O sistema valida a consistência dos dados, especialmente datas, e impede o salvamento caso o **"Último dia Trabalhado"** seja anterior à data de admissão do funcionário, ou se algum campo obrigatório não for preenchido corretamente.