# Roteiro de aprendizagem — second brain
Proposta de estudo elaborada em 23/10/2026. **Não é uma lista operacional de tarefas** e não representa compromissos assumidos. A lista de execução do vault continua exclusivamente em `tarefas.md`.

## Etapa 1 — Entender o método (duas sessões de 45 minutos)
Ler S01 e S02 em [fontes.md](fontes.md). Explicar com suas palavras como uma captura vira uma entrega. Usar um exemplo de transformação de processos: uma observação de reunião vira evidência, decisão ou conhecimento reutilizável?

Resultado esperado: uma nota curta distinguindo informação de referência, ação e decisão. Evitar criar ações reais fora de `tarefas.md`.

## Etapa 2 — Aprender gestão de contexto (duas sessões de 45 minutos)
Ler S03 e S04. Produzir um pacote experimental com: contexto durável, estado de um projeto e informação temporária. Marcar origem, data e o que ainda precisa de confirmação.

Pergunta de controle: um agente que lesse só esse pacote conseguiria preparar um informe correto? Onde poderia confundir uma proposta com uma decisão?

## Etapa 3 — Experimentar recuperação (três sessões de uma hora)
Ler QMD (S07). Em uma cópia de teste, comparar perguntas exatas, paráfrases em português, siglas e perguntas sem resposta. Registrar consulta, fonte esperada, resultados encontrados e tempo.

Exemplos: “qual decisão vigente substituiu o prazo anterior?”, “que evidência sustenta esta conclusão?”, “o que ainda é hipótese?”. Usar cenários sintéticos se não quiser inserir documentos profissionais no ambiente de teste.

Resultado esperado: evidência de quando uma busca simples basta e quando a híbrida melhora a recuperação. Não há instalação ou execução concluída como parte desta pesquisa.

## Etapa 4 — Comparar experiências prontas (duas sessões de uma hora)
Explorar as documentações de Open Notebook, Khoj, Reor e Karakeep (S08–S11). Escolher apenas uma dor: capturar conteúdo, estudar PDFs ou responder sobre notas.

Usar o mesmo conjunto pequeno de documentos e as mesmas perguntas. Conferir citações, exportação, processamento externo e preservação do Markdown.

Resultado esperado: uma comparação baseada no seu fluxo, com um motivo claro para adotar ou rejeitar a ferramenta.

## Etapa 5 — Estudar memória e grafos (três sessões de uma hora)
Ler Mem0, Cognee, Microsoft GraphRAG e a introdução MCP (S12–S14, S16). Separar armazenamento, recuperação, geração e interface de integração.

Pergunta de controle: qual consulta importante exige relações explícitas que arquivos e busca não entregam bem? Sem um exemplo concreto, adiar a camada adicional.

## Vocabulário essencial
| Termo | Significado prático |
|---|---|
| PKM | Gestão pessoal do conhecimento |
| RAG | Recuperar evidências e fornecê-las à geração da resposta |
| Embedding | Representação numérica usada para comparar conteúdo |
| BM25 | Ranqueamento lexical baseado nos termos da consulta |
| Busca híbrida | Combinação de busca lexical e semântica |
| Reranking | Reordenar candidatos recuperados por relevância |
| Grafo de conhecimento | Entidades e relações explícitas |
| Memória de agente | Informação persistida e recuperada entre interações |
| MCP | Interface padronizada entre aplicação de IA e sistemas externos |
| Proveniência | Origem verificável de uma informação |
| Índice derivado | Estrutura reconstruível a partir dos registros originais |

## Prompt para aprender com o próprio vault
> Leia apenas os arquivos relevantes e informe o commit ou versão consultada. Responda à pergunta com links para os arquivos que sustentam cada fato. Separe fatos, inferências e lacunas. Quando houver decisões conflitantes, indique a sequência temporal e a vigente. Não invente prazos, responsáveis ou compromissos. Se propuser mudança, apresente-a como proposta; tarefas reais continuam em tarefas.md.

## Registro de um experimento
| Campo | Conteúdo a preencher |
|---|---|
| Hipótese | Qual melhoria espero? |
| Corpus e versão | Quais documentos e commit? |
| Configuração | Ferramenta, versão, modelo e processamento local/remoto |
| Perguntas | Conjunto fixo com respostas esperadas |
| Medidas | Fontes corretas, erros, abstenções, tempo e custo |
| Resultado | Evidência observada, incluindo falhas |
| Conclusão | Adotar, ajustar ou abandonar; motivo |

Para iniciar a leitura pelo panorama: [relatório](panorama-2026-10-23.md).
