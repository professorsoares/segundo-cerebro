# Sym Supply One

- **Slug:** #sym-supply-one
- **Outros nomes:** **Sym Supply** (como o Bruno costuma chamar), **Techsocial** (nome antigo, ainda usado no dia a dia — procurar por este termo em e-mail antigo), sistema da **Nashai**
- **Estado:** ativo — contrato Standard assinado; integração Prothera aprovada para contratação separada; reunião técnica realizada
- **Pessoas:** a preencher (quem é o contato comercial da Nashai?)
- **Prazo-chave:** a definir
- **Último status ao Vinicius:** nunca
- **Atualizado:** 2026-10-23

## Para comunicar ao Vinicius

**Status: contrato Standard assinado; integração Prothera aprovada para contratação separada; reunião técnica realizada.**

Falta registrar as datas, os encaminhamentos da reunião e o cronograma vigente. A aprovação da proposta não confirma que a contratação da integração já foi formalizada. Também falta verificar se o contrato assinado contempla mapa das modificações, aceite das integrações e operação assistida.

**O que preciso de você:** alinhar próximos marcos e apoio em eventuais lacunas contratuais ou dependências de integração.

Rascunho atualizado; envio não confirmado.

## Por que existe
Sistema fornecido pela **Nashai**. A decisão em curso é contratar a **versão
Standard** da ferramenta — isto é, abandonar as diversas modificações
(customizações) feitas ao longo do tempo.

## Estado atual

Bruno confirmou contrato Standard assinado, proposta Prothera aprovada para contratação separada e reunião técnica Prothera × Nashai realizada. As datas efetivas e os encaminhamentos não foram informados.

A fase de redação do Standard foi superada. Conferir o contrato efetivamente assinado; eventuais ajustes dependerão dos instrumentos e acordos aplicáveis, sem presumir que já estejam previstos.

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

Registrar cronograma vigente e encaminhamentos da reunião; acompanhar a formalização separada da integração Prothera e conferir as proteções no contrato Standard assinado. Execução centralizada em [tarefas.md](../tarefas.md).

### Integração com o Prothera

Proposta aprovada para contratação separada, conforme Bruno. Não há confirmação de contrato da integração assinado, início de execução ou conclusão técnica.

### Reunião técnica Prothera × Nashai

Realizada, conforme Bruno. Data, participantes, decisões, responsáveis e prazos ainda precisam ser registrados; a sequência em relação à assinatura não foi informada.

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
- Existe levantamento das modificações atuais e de quem depende de cada uma? (Nunca foi confirmado. Com os termos fechados, a saída provável é obrigar a Nashai a entregá-lo por contrato, já que quem tem o mapa é o fornecedor.)
- O contrato assinado prevê prazo, aceite, mapa de modificações e operação assistida?
- Quem revisou o contrato assinado e onde está a versão final?
- **"Prothera" é também o nome do fornecedor, além do sistema?** A reunião é "Prothera com Nashai", o que indica fornecedor contra fornecedor. Confirmar o nome da empresa e quem é o contato.
- Quais encaminhamentos, responsáveis e prazos saíram da reunião Prothera × Nashai?
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
- **2026-10-21** — **Nashai apresentou proposta de integração com o Prothera**, em avaliação. Decisão em aberto: negociar junto do contrato Standard, que ainda está em redação, ou depois dele.
- **2026-10-21** — reunião **técnica** entre Nashai e Prothera **agendada**. Data a registrar; é o que define se as conclusões dela cabem no contrato em redação ou viram pedido de mudança.
- **2026-10-21** — registrada a necessidade de garantir reunião entre **Prothera e Nashai** na janela de 21 a 22/10. Amarrada à janela do contrato: vale muito mais antes da assinatura que depois.
- **2026-10-21** — termos da negociação fechados na reunião de **20/10**; Nashai redigindo o acordo, sem assinatura. Registrado em `decisoes.md`. A janela de influência deixa de ser escopo e passa a ser texto de contrato, com prazo curto. Cronograma do Sym Supply previsto para hoje.
- **2026-10-21** — "Sym Supply" registrado como nome usado pelo Bruno.
- **2026-10-21** — Protheus esclarecido: é só integração, sem processo próprio, e a frente está sequenciada para depois do término das atividades do Sym Supply One. Sai do rol de risco em paralelo e entra como dependente a jusante.
- **2026-10-21** — esclarecido que Prothera e Protheus são sistemas distintos. Prothera = permissão de terceiro para embarcar e prestar serviço no navio; FAS = agendamento do serviço com o fornecedor; Protheus = função ainda não descrita. Redação provisória, descrição formal pendente com o Bruno.
- **2026-10-21** — registrado: existem frentes em paralelo integrando dados de fornecedores com Prothera, FAS e Protheus. Eleva o risco do Standard, que deixa de ser só perda de customização e passa a ser risco de quebra de integração em cadeia operacional. Detalhamento pendente.
- **2026-10-20** — registrado: fase final de negociação da versão Standard, sem as modificações históricas.

- **2026-10-23** — Bruno confirmou contrato Standard assinado, proposta de integração Prothera aprovada para contratação separada e reunião técnica realizada. Datas efetivas não informadas. O histórico anterior descreve fases já superadas. Fonte: [formulário](../importacoes/2026-10-23-atualizacao-sym-supply.md).
