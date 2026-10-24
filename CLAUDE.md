# Manual de operação do segundo cérebro

Este repositório é o segundo cérebro do Bruno (professorsoares). Qualquer sessão
do Claude que abrir este repo — desktop, web ou celular — deve seguir este manual.

**A fonte da verdade é o markdown deste repositório. Nada mais.**
`painel/dados.json` é *gerado* a partir do markdown; nunca edite o JSON à mão e
nunca o trate como fonte de dados.

## Contexto do Bruno (leia antes de qualquer coisa)

- É **consultor**, alocado na **OceanPact** através da empresa **Capitani**.
- Seu gerente é **Vinicius Mattos** (colaborador OceanPact), o **principal afetado
  quando algo sai do esperado** — ver [[pessoas/vinicius-mattos]].
- Posição de consultor alocado significa que **comunicar problema a tempo vale
  tanto quanto entregar**. Atraso que o Vinicius descobre sozinho é o pior cenário.
- Por isso: sempre que uma captura revelar atraso, risco ou mudança de escopo,
  **crie a tarefa de comunicar ao Vinicius** junto com a tarefa de resolver.
  As duas, não só a segunda.
- Objetivo declarado do Bruno ao montar isto: acabar com a dificuldade de
  **comunicar os problemas**. O sistema tem que ser capaz de produzir, a qualquer
  momento, um relato claro de status e de problema por projeto.

## Regra zero: capturar é mais importante que organizar

Quando o Bruno despeja informação (texto ou áudio ditado), o trabalho é:

1. **Gravar primeiro.** Escreva em `inbox/AAAA-MM-DD-slug.md` imediatamente, cru,
   sem reescrever as palavras dele. Nunca perca a captura por estar organizando.
2. **Extrair.** Puxe dali: tarefas, decisões, pessoas, prazos, promessas.
3. **Arquivar.** Mande cada item para o arquivo certo (abaixo) e esvazie o item do inbox.
4. **Commitar e dar push.** Toda alteração termina em commit + push para `origin/main`.
   Sem push, a captura não existe no celular.

Se a captura for ambígua, grave do mesmo jeito e **pergunte depois**. Nunca
bloqueie a captura numa pergunta.

## Onde cada coisa mora

| Arquivo / pasta | O que guarda |
|---|---|
| `tarefas.md` | **Tudo** que está em aberto. Visão única. Nenhuma tarefa mora em outro lugar. |
| `decisoes.md` | O que foi combinado, com quem, quando e por quê. Imutável — nunca apague linha, só adicione. |
| `projetos/<slug>.md` | Um por frente de trabalho: contexto, estado, próximos passos, histórico. |
| `pessoas/<slug>.md` | Um por pessoa recorrente: o que ela te deve, o que você deve a ela, histórico de contato. |
| `reunioes/AAAA-MM-DD-slug.md` | Ata: quem estava, o que foi decidido, o que cada um levou. |
| `inbox/` | Captura crua, transitória. **Deve tender a zero.** |
| `templates/` | Modelos. Use-os ao criar arquivo novo. |

## Formato de tarefa (obrigatório, é o que o painel lê)

Uma tarefa é **uma linha** em `tarefas.md`:

```
- [ ] Descrição da tarefa | #projeto | prazo: 2026-10-24 | pri: alta | prometi-a: Fulano | fonte: <link ou arquivo>
```

- Campos separados por ` | `. Só a descrição é obrigatória.
- `#projeto` deve bater com o **Slug** declarado em `projetos/` (`#docket` → `projetos/docket.md`).
- `prazo:` sempre `AAAA-MM-DD`. Nunca "semana que vem" — converta para data.
- `hora: HH:MM` — quando o prazo é hora do dia, não o dia inteiro ("antes das 10h").
- `pri:` = `alta` | `media` | `baixa`.
- `prometi-a: Nome` — o Bruno se comprometeu com alguém. Dívida de reputação; prioridade.
- `aguardo: Nome (cobrado em AAAA-MM-DD)` — travado em terceiro. Registre quando foi cobrado.
- `comunicar: Nome` — **tem que ser comunicado a essa pessoa e ainda não foi.** Normalmente Vinicius Mattos.
- `comunicado: AAAA-MM-DD` — a data em que foi comunicado. Enquanto estiver ausente numa tarefa vencida, com `prometi-a:` ou com `comunicar:`, o painel trata como **problema que o Vinicius ainda não sabe**.
- `monday:` — id ou link do item correspondente no Monday, quando houver espelho.
- `fonte:` de onde veio (link de e-mail, `reunioes/...`, "call 20/10"). É o que permite cruzar depois.

Estados da caixa: `[ ]` aberto · `[/]` em andamento · `[x]` concluído · `[-]` cancelado

## Monday é o sistema oficial; este vault é a camada do Bruno

**Escopo vigente informado por Bruno em 23/10/2026:** por enquanto, somente o Projuris tem atividade a concluir que deve ser acompanhada/atualizada no Monday. DocuSign e Sym Supply serão tratados futuramente, sem prazo definido. Não criar ou cobrar atualização desses dois no Monday até Bruno ampliar o escopo. Esta orientação substitui a regra anterior de atualização automática para todos os projetos.

Dentro desse escopo:

- O Monday é o registro **oficial** — é onde a organização vê o andamento.
- Este vault é a camada **pessoal e de risco** do Bruno: o que ele precisa fazer,
  o que está travado, qual o risco e o que precisa ser comunicado. O Monday não
  guarda isso bem.
- **Quando algo muda de verdade, o Monday tem que ser atualizado.** Nos projetos incluídos no escopo vigente, depois de uma
  entrega, validação ou repactuação de prazo, a tarefa de atualizar o Monday é
  parte do trabalho, não um extra. Crie-a explicitamente.
- Exports do Monday entram em `importacoes/`. Ver o leia-me de lá antes de importar.

## Seção de comunicação em cada projeto

Todo arquivo em `projetos/` carrega:

- `- **Último status ao Vinicius:** AAAA-MM-DD` (ou `nunca`) — o painel calcula há
  quantos dias o projeto está sem status e cobra.
- `## Para comunicar ao Vinicius` — texto curto, honesto e **pronto para enviar**:
  status em uma linha, o que trava, e o que o Bruno precisa dele. O painel mostra
  esse texto com botão de copiar. Mantenha atualizado: texto velho aqui é pior que
  texto nenhum.

## Rotinas

**Brief diário (manhã, por e-mail)** — ler o repo e o Gmail/Calendar e entregar:
agenda do dia · tarefas com prazo hoje/vencidas · promessas pendentes ·
e-mails que exigem resposta e ainda não têm tarefa · o que está travado em terceiro.

**Revisão semanal (sexta e segunda, cedo)** — o que andou, o que não andou,
promessas feitas e não cumpridas, o que está parado há mais de 14 dias,
o que puxar. Grave o resultado em `reunioes/AAAA-MM-DD-revisao-semanal.md`.

## Regras de higiene

- **Nunca** crie uma segunda lista de tarefas. Se achar tarefa solta num projeto ou ata, mova para `tarefas.md` e deixe só o link.
- Converta data relativa em data absoluta sempre ("sexta" → `2026-10-23`).
- Ao concluir tarefa que veio de compromisso com alguém, registre em `decisoes.md` e na pessoa.
- Antes de afirmar que algo está feito, confira no arquivo. Não confie na memória da conversa.
- Mensagem de commit: o que mudou em uma linha, em português. Ex.: `captura: call OceanPact 20/10 + 3 tarefas`.
