# Importações

Exports crus de ferramentas externas, principalmente do **Monday**. Um arquivo por
export: `monday-<projeto>-AAAA-MM-DD.csv` (ou `.xlsx`).

## Como importar um export do Monday

A regra que evita o descontrole: **não copie o Monday inteiro para `tarefas.md`.**
O Monday tem o plano do projeto; `tarefas.md` tem o que o Bruno precisa fazer. São
coisas diferentes, e misturar as duas é o caminho mais rápido para ter duas listas
desatualizadas em vez de uma confiável.

Ao receber um export:

1. **Guarde o arquivo cru aqui**, sem editar, e commite. É a prova do que o Monday
   dizia naquela data.
2. **Faça o snapshot legível** em `projetos/<slug>-monday.md`: tabela com item,
   responsável, status e prazo, mais a data do export no topo. É material de
   consulta e de análise de risco, não lista de tarefas.
3. **Leve para `tarefas.md` só o que é ação do Bruno** — o que ele mesmo executa,
   cobra ou comunica. Marque com `monday:` o id/link do item espelhado.
4. **Reconcilie nos dois sentidos** e relate o que achou:
   - item do Monday atrasado que não tem tarefa aqui → criar
   - tarefa aqui que não existe no Monday → o Monday está desatualizado, criar tarefa de atualizar
   - prazo diferente entre os dois → **sempre apontar**; não escolher sozinho qual vale
5. **Avalie risco** e escreva no projeto: o que não vai caber no prazo, o que está
   travado em terceiro, o que ninguém está olhando.
6. **Atualize `## Para comunicar ao Vinicius`** no arquivo do projeto se a leitura
   mudou. Importação que não resulta em comunicação atualizada foi importação perdida.

## Se o conector do Monday estiver autorizado

Com o conector do Monday ligado, nada disso precisa de export manual: dá para ler
os quadros direto. Até lá, export é o caminho.
