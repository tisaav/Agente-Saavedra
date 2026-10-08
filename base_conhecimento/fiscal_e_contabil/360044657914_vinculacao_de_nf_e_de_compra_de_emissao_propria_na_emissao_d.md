# Vinculação de NF-e de Compra de Emissão Própria na emissão do MDF-e

> **Módulo:** Fiscal e Contábil | **Subseção:** MDF-e  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044657914-Vincula%C3%A7%C3%A3o-de-NF-e-de-Compra-de-Emiss%C3%A3o-Pr%C3%B3pria-na-emiss%C3%A3o-do-MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044657914-Vincula%C3%A7%C3%A3o-de-NF-e-de-Compra-de-Emiss%C3%A3o-Pr%C3%B3pria-na-emiss%C3%A3o-do-MDF-e)  
> **ID:** `360044657914` | **Última Atualização:** 2026-09-15T16:56:54Z

---

Através de nosso sistema, será possível realizar a inclusão de NF-e de Compra de Emissão Própria na emissão do MDF-e. Desta forma, as tag's de UF de Início e Município de Carregamento utilizarão os dados do **"Parceiro Remetente"**, informado na Central de Compras (grade **"Rodapé"**, aba **"Transporte"**) e a UF Fim e o Município de Descarregamento utilizarão os dados da Empresa da NF-e vinculada ao MDF-e.

**Observação:** para que o MDF-e seja emitido nas condições acima, é necessário que a NF-e vinculada ao MDF-e tenha o Tipo de Movimento igual à Compra que o Parceiro Remetente tenha sido informado. Quando o campo Parceiro Remetente não for informado e o parâmetro **"Considerar UF Coleta XML MDF-e Envolve Mov Compra? - UFCOLCOMPMDFE"** estiver ligado, o sistema considerará como UF inicial no XML a UF de Coleta da Aba Geral do MDF-e.

Considere ainda que, ao habilitar o parâmetro **"UF Coleta e UF Descarregamento manualmente - UFCOLDESCMANUAL" **será possível indicar manualmente a **"UF de Coleta"** e o **"Município de Coleta"**, bem como, a **"UF de Descarregamento"** e o **"Município de Descarregamento"** diretamente na sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral), aba [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) da tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514).

Este parâmetro será priorizado sempre que no MDF-e houver apenas documentos de emissão própria, ou seja, se a marcação **"Contém documentos de terceiros?"** estiver desativada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abageral) da tela Viagens de Transporte (MDF-e). Do contrário, a funcionalidade do parâmetro UFCOLCOMPMDFE será executada prioritariamente.


---

### 🔗 Links e Referências Internas:

- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral)
- [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e)
- [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abageral)