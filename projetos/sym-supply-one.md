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

**Segundo risco, maior que o primeiro:** o Sym Supply One é o cadastro mestre de
fornecedor de uma cadeia operacional. O **FAS** agenda o serviço com o fornecedor e o
**Prothera** autoriza o pessoal dele a embarcar no navio. Se a versão Standard não expõe o que essas integrações consomem hoje, o
impacto não fica na ferramenta nem no relatório: terceiro não liberado para embarcar
é serviço não executado e navio esperando. E isso aparece na implantação, depois de
assinado.

**Dependência que vale registrar:** a integração com o **Protheus** está sequenciada
para depois do término das atividades do Sym Supply One. Todo atraso aqui empurra o
Protheus junto.

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
Frentes em paralelo que o Bruno apoia e que consomem dados de fornecedores do Sym
Supply One. **Prothera e Protheus são sistemas distintos** — nomes parecidos, funções
diferentes. Confirmado em 21/10.

> **Redação provisória.** As descrições abaixo vieram de conversa rápida em 21/10. O
> Bruno vai trazer a descrição formal de cada sistema. Não citar este texto em
> documento oficial antes disso.

| Sistema | Para que serve | O que consome daqui |
|---|---|---|
| **Prothera** | permissão de terceiros para embarcar no navio e prestar serviço. A OceanPact é empresa de navegação e serviços ligados ao oceano; o braço de navegação precisa desse controle de acesso. | dados do fornecedor e do seu pessoal, para autorizar o embarque |
| **FAS** | agendamento dos serviços com os fornecedores | dados do fornecedor, para marcar o serviço |
| **Protheus** | só integração, sem processo próprio descrito | a detalhar — **frente sequenciada para depois** do término das atividades do Sym Supply One |

### A cadeia, na ordem em que acontece
O Sym Supply One é, na prática, o **cadastro mestre de fornecedor** dessa cadeia:

1. o fornecedor existe e está qualificado no **Sym Supply One**;
2. o **FAS** agenda o serviço com esse fornecedor;
3. o **Prothera** autoriza o pessoal dele a embarcar para executar o serviço.

Quebrar o elo 1 não para só o cadastro: para o agendamento e para o embarque.

O **Protheus não está nessa cadeia operacional**: é integração pura, e a frente está
sequenciada para **depois** que as atividades do Sym Supply One terminarem. Ou seja,
não é risco em paralelo, é dependente a jusante.

Cada frente pode virar arquivo próprio em `projetos/` quando houver fase, responsável
e prazo. Até lá, ficam aqui.

## Próximo passo concreto
Fechar a negociação da versão Standard com a Nashai.

## Riscos / o que pode travar
- **O risco central é o abandono das customizações.** Houve "um monte de modificações" ao longo do tempo. Cada uma existe porque algum processo precisava dela. Ir para o Standard significa que esses processos mudam, ganham contorno manual ou somem — e isso aparece depois de assinado, não antes.
- Não há aqui um levantamento das modificações atuais nem de quem depende de cada uma.
- Usuários que hoje trabalham com os ajustes podem reagir na implantação, não na negociação.
- **O raio do risco é maior do que a ferramenta.** Existem integrações de dados de fornecedores com Prothera, FAS e Protheus. Se alguma delas consome campo, tabela ou extensão que só existe por causa de uma modificação, ir para Standard quebra a integração, e o estrago aparece no sistema de destino, não aqui.
- **O pior caminho de falha é o do Prothera, e ele é operacional, não administrativo.** Prothera autoriza terceiro a embarcar. Se o dado que ele consome deixar de existir no Standard, a consequência não é relatório errado: é pessoa não liberada para embarcar, serviço não executado e navio esperando. *(Leitura minha a partir da função descrita, não afirmação do fornecedor — confirmar.)*
- **O FAS falha antes:** sem dado de fornecedor, não há agendamento. Serviço que não é agendado também não acontece.
- O levantamento das modificações, por si, não resolve: é preciso cruzar cada modificação com as integrações que a consomem.
- **O Protheus herda o atraso.** A frente está sequenciada para depois do término do Sym Supply One. Todo dia que o Sym Supply One atrasa empurra o Protheus junto, e isso provavelmente não está visível no cronograma de quem cobra o Protheus.
- **Risco de retrabalho se o Protheus for especificado antes da decisão do Standard.** Especificação feita contra o modelo de dados atual (customizado) não vale para o Standard. O sequenciamento protege disso, mas só enquanto ninguém adiantar a especificação.

## A confirmar
- Existe levantamento das modificações atuais e de quem depende de cada uma? (Se não existir, é o item mais urgente deste projeto.)
- **Descrição formal de Prothera, FAS e Protheus** — o Bruno vai trazer. Até então a tabela acima é redação provisória.
- **O que exatamente a integração com o Protheus vai trocar, e em que direção?** Hoje só se sabe que é integração e que vem depois.
- **"Término das atividades do Sym Supply One" é o quê, concretamente?** Assinatura do Standard, implantação concluída, ou estabilização? A data do Protheus depende dessa definição.
- Quem cobra o prazo do Protheus sabe que ele está amarrado ao Sym Supply One?
- Cada integração consome só dado Standard, ou depende de customização?
- Quem é o responsável por cada frente (Prothera, FAS, Protheus) e em que fase cada uma está?
- O Prothera trata documentação de pessoal de terceiro para embarque (aptidão, treinamento, certificação)? Se sim, há peso regulatório, e o campo que falta vira impedimento legal de embarque, não inconveniência.
- A decisão pelo Standard é financeira, de manutenção, ou imposta pela Nashai?
- Qual o impacto previsto para os usuários e quem precisa ser avisado?
- Tem data-limite da negociação ou de renovação do contrato atual?

## Histórico
- **2026-10-21** — Protheus esclarecido: é só integração, sem processo próprio, e a frente está sequenciada para depois do término das atividades do Sym Supply One. Sai do rol de risco em paralelo e entra como dependente a jusante.
- **2026-10-21** — esclarecido que Prothera e Protheus são sistemas distintos. Prothera = permissão de terceiro para embarcar e prestar serviço no navio; FAS = agendamento do serviço com o fornecedor; Protheus = função ainda não descrita. Redação provisória, descrição formal pendente com o Bruno.
- **2026-10-21** — registrado: existem frentes em paralelo integrando dados de fornecedores com Prothera, FAS e Protheus. Eleva o risco do Standard, que deixa de ser só perda de customização e passa a ser risco de quebra de integração em cadeia operacional. Detalhamento pendente.
- **2026-10-20** — registrado: fase final de negociação da versão Standard, sem as modificações históricas.
