# Decisões e alinhamentos

Registro imutável do que foi combinado. **Nunca apague uma linha** — se mudou,
adicione uma entrada nova que revoga a anterior. É isto que te protege em
discussão de "mas a gente não tinha combinado que...".

Formato:

```
## AAAA-MM-DD — Título da decisão
- **Com quem:** Nome(s)
- **Contexto:** por que a decisão foi necessária
- **Decidido:** o que ficou valendo
- **Consequência:** o que muda / quem faz o quê
- **Fonte:** link de e-mail, ata em `reunioes/`, call
```

---

## 2026-10-20 — Arquitetura do segundo cérebro
- **Com quem:** Bruno (decisão própria)
- **Contexto:** volume de tarefas, comunicações e alinhamentos passou do que dá para guardar de cabeça.
- **Decidido:** markdown em git como fonte única da verdade; Claude como operador (captura, cruzamento e cobrança); Obsidian como leitor/editor humano; painel JSON apenas **derivado**, read-only.
- **Consequência:** nenhuma tarefa mora fora de `tarefas.md`. Nada de segunda base de dados.
- **Fonte:** conversa de montagem, 20/10/2026
