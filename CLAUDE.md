# Manual de operação do segundo cérebro

Este repositório é o segundo cérebro do Bruno (professorsoares). Qualquer sessão
do Claude que abrir este repo — desktop, web ou celular — deve seguir este manual.

**A fonte da verdade é o markdown deste repositório. Nada mais.**
`painel/dados.json` é *gerado* a partir do markdown; nunca edite o JSON à mão e
nunca o trate como fonte de dados.

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
- `#projeto` deve bater com o nome de arquivo em `projetos/` (`#oceanpact-bid` → `projetos/oceanpact-bid.md`).
- `prazo:` sempre `AAAA-MM-DD`. Nunca "semana que vem" — converta para data.
- `pri:` = `alta` | `media` | `baixa`.
- `prometi-a: Nome` — o Bruno se comprometeu com alguém. Isto é dívida de reputação; trate como prioridade.
- `aguardo: Nome (cobrado em AAAA-MM-DD)` — está travado em terceiro. Registre quando foi cobrado.
- `fonte:` de onde veio (link de e-mail, `reunioes/...`, "call 20/10"). É o que permite cruzar depois.

Estados da caixa: `[ ]` aberto · `[/]` em andamento · `[x]` concluído · `[-]` cancelado

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
