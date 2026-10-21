# Sym Supply One

- **Slug:** #sym-supply-one
- **Outros nomes:** **Sym Supply** (como o Bruno costuma chamar), **Techsocial** (nome antigo, ainda usado no dia a dia — procurar por este termo em e-mail antigo), sistema da **Nashai**
- **Estado:** ativo — **termos fechados em 20/10; contrato em redação pela Nashai, não assinado**
- **Pessoas:** a preencher (quem é o contato comercial da Nashai?)
- **Prazo-chave:** a definir
- **Último status ao Vinicius:** nunca
- **Atualizado:** 2026-10-21

## Para comunicar ao Vinicius

**Status: termos fechados ontem (20/10). A Nashai está redigindo o contrato.**

Fechamos na reunião de ontem os termos para contratar a versão **Standard** do Sym
Supply One (Techsocial), ou seja, sem as modificações que fizemos ao longo do tempo.
O acordo está sendo escrito pela Nashai e ainda não foi assinado.

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

**Decisão que preciso tomar hoje, e que te afeta:** a Nashai apresentou proposta para
a integração com o **Prothera**. Como o contrato do Standard está em redação, dá para
negociar as duas coisas no mesmo pacote, com alavanca, ou deixar a integração para
depois, sem alavanca nenhuma. Minha leitura é que vale juntar.

**Dependência que vale registrar:** a integração com o **Protheus** está sequenciada
para depois do término das atividades do Sym Supply One. Todo atraso aqui empurra o
Protheus junto.

**O que preciso de você, e o prazo é agora:** como os termos já estão fechados, não
estou pedindo para mexer em escopo nem em preço. O que ainda dá para mudar é o
**texto do contrato**, enquanto a Nashai o está escrevendo. Três coisas que, se
entrarem no documento, custam zero agora e valem muito na implantação:

1. **Obrigação da Nashai de entregar o mapa do que muda** — inventário das
   modificações hoje existentes e das diferenças de modelo de dados em relação ao
   Standard. Hoje nós não temos isso; quem tem é o fornecedor.
2. **Critério de aceite amarrado às integrações** — a implantação só é aceita com
   **Prothera** e **FAS** funcionando. Sem isso, "entregue" significa a ferramenta de
   pé e o processo parado.
3. **Período de operação assistida ou paralelo** para absorver o que aparecer depois.

Se a tua leitura for que não vale reabrir o documento, me diz e eu registro a ciência
formal de que assinamos sem o levantamento e absorvemos o risco. Qualquer das duas
serve; o que não serve é assinar sem essa conversa ter acontecido.

## Por que existe
Sistema fornecido pela **Nashai**. A decisão em curso é contratar a **versão
Standard** da ferramenta — isto é, abandonar as diversas modificações
(customizações) feitas ao longo do tempo.

## Estado atual
Termos fechados com a Nashai em reunião de **20/10**. O acordo está sendo **redigido
pela Nashai** e ainda não foi assinado. Cronograma do Sym Supply previsto para
**21/10**, decorrente desse fechamento.

**A janela mudou de natureza.** Até ontem o que estava em jogo era escopo. Com os
termos fechados, escopo e preço saíram da mesa; o que ainda está aberto é o **texto
do contrato**, e só enquanto ele está sendo escrito. Depois da assinatura não há mais
alavanca nenhuma.

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
Levar ao Vinicius, hoje, o pedido de cláusulas de proteção antes da assinatura (ver
`## Para comunicar ao Vinicius`), garantir a reunião Prothera × Nashai na janela de
hoje a amanhã, e registrar o cronograma quando chegar.

### Proposta da Nashai para a integração com o Prothera
Registrado em 21/10: a **Nashai apresentou proposta** para a integração com o
Prothera, e ela está para avaliação.

**A questão não é só se a proposta é boa, é quando ela é negociada.** O contrato do
Standard está em redação agora. Avaliar a proposta de integração como item separado
significa negociar duas vezes com o mesmo fornecedor, sendo que na segunda vez o
Standard já está assinado e a alavanca acabou. Se a integração entra no mesmo pacote,
ela é moeda de troca; se sai depois, é pedido de mudança com preço de pedido de
mudança.

Vale também conferir se a proposta já cobre, de graça, o que eu sugeri pedir por
cláusula: expor o dado que o Prothera consome e amarrar aceite ao funcionamento da
integração.

### Reunião técnica Prothera × Nashai — agendada
**Agendamento concluído em 21/10.** É reunião **técnica** entre os dois fornecedores.
A data ainda não está registrada aqui, e é ela que decide se a reunião serve de
insumo para o contrato ou chega tarde.

O prazo real dessa reunião não é "amanhã", é **antes de o contrato da Nashai ser
assinado**. Se os dois fornecedores se falarem enquanto o acordo está em redação,
tudo o que a reunião concluir sobre a integração ainda cabe no documento: campo que
o Prothera precisa, obrigação de expor dado, prazo, aceite. Se a reunião acontecer
depois da assinatura, as conclusões não têm onde morar e viram pedido de mudança,
que se paga.

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
- O contrato em redação já prevê prazo, aceite e operação assistida, ou vem só com licença e valor?
- Quem revisa o contrato do nosso lado antes da assinatura, e qual o prazo que temos para comentar?
- **"Prothera" é também o nome do fornecedor, além do sistema?** A reunião é "Prothera com Nashai", o que indica fornecedor contra fornecedor. Confirmar o nome da empresa e quem é o contato.
- A reunião Prothera × Nashai tem pauta definida? Se o objetivo é a integração, quem do nosso lado leva a lista do que o Prothera precisa receber?
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
