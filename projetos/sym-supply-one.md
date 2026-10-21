# Sym Supply One

- **Slug:** #sym-supply-one
- **Outros nomes:** **Techsocial** (nome antigo, ainda usado no dia a dia — procurar por este termo em e-mail antigo), sistema da **Nashai**
- **Estado:** ativo — fase final de negociação
- **Pessoas:** a preencher (quem é o contato comercial da Nashai?)
- **Prazo-chave:** a definir
- **Último status ao Vinicius:** nunca
- **Atualizado:** 2026-10-21

## Para comunicar ao Vinicius

**Status: fase final de negociação da versão Standard.**

A negociação com a Nashai está avançada para contratar a versão **Standard** do Sym
Supply One (Techsocial) — ou seja, sem as modificações que fizemos ao longo do tempo.

**Risco que preciso registrar formalmente:** não temos levantamento de quais
modificações existem hoje nem de quais processos dependem delas. Cada modificação
foi feita porque alguma necessidade existia. Ir para Standard significa que esses
processos mudam, viram contorno manual ou desaparecem — e isso vai aparecer na
implantação, depois de assinado, não agora.

**Segundo risco, maior que o primeiro:** o Sym Supply One não é um sistema isolado.
Há frentes em paralelo integrando dados de fornecedores com **Prothera**, **FAS** e
**Protheus**. Se a versão Standard não expõe o que essas integrações consomem hoje,
o impacto não fica na ferramenta: ele chega nos sistemas de destino, e aparece na
implantação, depois de assinado.

**O que preciso de você:** ou autorização para levantar as modificações atuais, as
integrações e seus dependentes **antes** de fechar, ou ciência formal de que vamos
assinar sem esse levantamento e absorver o risco.

## Por que existe
Sistema fornecido pela **Nashai**. A decisão em curso é contratar a **versão
Standard** da ferramenta — isto é, abandonar as diversas modificações
(customizações) feitas ao longo do tempo.

## Estado atual
Fase final de negociação da versão Standard. Comercialmente avançado.

## Interfaces e integrações
Frentes em paralelo que o Bruno apoia e que trocam dados com o Sym Supply One.
Registrado em 21/10 a partir de conversa; **conteúdo ainda a detalhar** (ver tarefa
em `tarefas.md`).

| Sistema de destino | Natureza | Detalhe |
|---|---|---|
| **Prothera** | integração de dados de fornecedores | a detalhar |
| **FAS** | integração de dados de fornecedores | a detalhar |
| **Protheus** | integração de dados de fornecedores | a detalhar |

Cada uma dessas frentes pode virar um arquivo próprio em `projetos/` quando houver
fase, responsável e prazo. Até lá, ficam aqui.

## Próximo passo concreto
Fechar a negociação da versão Standard com a Nashai.

## Riscos / o que pode travar
- **O risco central é o abandono das customizações.** Houve "um monte de modificações" ao longo do tempo. Cada uma existe porque algum processo precisava dela. Ir para o Standard significa que esses processos mudam, ganham contorno manual ou somem — e isso aparece depois de assinado, não antes.
- Não há aqui um levantamento das modificações atuais nem de quem depende de cada uma.
- Usuários que hoje trabalham com os ajustes podem reagir na implantação, não na negociação.
- **O raio do risco é maior do que a ferramenta.** Existem integrações de dados de fornecedores com Prothera, FAS e Protheus. Se alguma delas consome campo, tabela ou extensão que só existe por causa de uma modificação, ir para Standard quebra a integração, e o estrago aparece no sistema de destino, não aqui.
- O levantamento das modificações, por si, não resolve: é preciso cruzar cada modificação com as integrações que a consomem.

## A confirmar
- Existe levantamento das modificações atuais e de quem depende de cada uma? (Se não existir, é o item mais urgente deste projeto.)
- **Prothera e Protheus são dois sistemas distintos, ou um deles é erro de grafia?** Os nomes são quase idênticos e errar isso aqui contamina tudo o que vier depois.
- **O que é FAS?** Nome completo, dono e o que consome do Sym Supply One.
- Cada integração consome só dado Standard, ou depende de customização?
- A decisão pelo Standard é financeira, de manutenção, ou imposta pela Nashai?
- Qual o impacto previsto para os usuários e quem precisa ser avisado?
- Tem data-limite da negociação ou de renovação do contrato atual?

## Histórico
- **2026-10-21** — registrado: existem frentes em paralelo integrando dados de fornecedores com Prothera, FAS e Protheus. Eleva o risco do Standard, que deixa de ser só perda de customização e passa a ser risco de quebra de integração. Detalhamento pendente.
- **2026-10-20** — registrado: fase final de negociação da versão Standard, sem as modificações históricas.
