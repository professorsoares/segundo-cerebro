#!/usr/bin/env python3
"""Gera painel/dados.json e painel/painel.html a partir do markdown do vault.

O markdown e a fonte da verdade. Este script apenas deriva. Nao escreva
nada de volta no markdown a partir do JSON.

Le:   tarefas.md  +  projetos/*.md
Uso:  python painel/gerar.py
"""
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TAREFAS = RAIZ / "tarefas.md"
PROJETOS = RAIZ / "projetos"
SAIDA = RAIZ / "painel" / "dados.json"
TEMPLATE = RAIZ / "painel" / "template.html"
PAGINA = RAIZ / "painel" / "painel.html"
MARCADOR = "/*__DADOS__*/ {}"

# Para quem o status e devido. Comparado em minusculas, por substring.
ALVO_STATUS = "vinicius"

ESTADOS = {" ": "aberto", "/": "andamento", "x": "concluido", "-": "cancelado"}
LINHA = re.compile(r"^\s*-\s*\[(.)\]\s*(.+)$")
CAMPO = re.compile(
    r"^(prazo|hora|pri|prometi-a|aguardo|fonte|comunicar|comunicado|monday)"
    r"\s*:\s*(.*)$", re.I
)

# --- projetos/*.md ---
P_NOME = re.compile(r"^#\s+(.+)$", re.M)
P_SLUG = re.compile(r"\*\*Slug:\*\*\s*#?([\w\-/]+)")
P_ESTADO = re.compile(r"\*\*Estado:\*\*\s*(.+)")
P_STATUS = re.compile(r"\*\*[Úu]ltimo status ao Vinicius:\*\*\s*(.+)")
P_RASCUNHO = re.compile(
    r"^##\s*Para comunicar ao Vinicius\s*$\n(.*?)(?=^##\s|\Z)", re.M | re.S
)

CHAVES = {
    "prazo": "prazo", "hora": "hora", "pri": "prioridade",
    "prometi-a": "prometi_a", "aguardo": "aguardo", "fonte": "fonte",
    "comunicar": "comunicar", "comunicado": "comunicado", "monday": "monday",
}


def parse_tarefa(texto, secao):
    partes = [p.strip() for p in texto.split("|")]
    tarefa = {
        "descricao": partes[0], "projeto": None, "prazo": None, "hora": None,
        "prioridade": None, "prometi_a": None, "aguardo": None,
        "fonte": None, "comunicar": None, "comunicado": None,
        "monday": None, "secao": secao,
    }
    for parte in partes[1:]:
        if not parte:
            continue
        if parte.startswith("#"):
            tarefa["projeto"] = parte[1:]
            continue
        m = CAMPO.match(parte)
        if not m:
            continue
        chave = CHAVES[m.group(1).lower()]
        valor = m.group(2).strip()
        tarefa[chave] = valor.lower() if chave == "prioridade" else valor
    if tarefa["projeto"] is None:
        m = re.search(r"#([\w\-/]+)", tarefa["descricao"])
        if m:
            tarefa["projeto"] = m.group(1)
    return tarefa


def dias_para(prazo, hoje):
    """Dias entre hoje e a data dada. Negativo = passado. None se nao for data."""
    try:
        return (datetime.strptime(str(prazo), "%Y-%m-%d").date() - hoje).days
    except (ValueError, TypeError):
        return None


def precisa_comunicar(t):
    """Um problema que o Vinicius ainda nao sabe.

    Vale para: tarefa marcada com `comunicar:`, promessa feita *a ele*, ou
    qualquer tarefa vencida (atraso sempre interessa ao gerente). Promessa
    feita a outra pessoa nao e assunto dele. Deixa de valer com `comunicado:`.
    """
    if t["comunicado"]:
        return False
    if t["comunicar"]:
        return True
    if t["prometi_a"] and ALVO_STATUS in t["prometi_a"].lower():
        return True
    return t["dias"] is not None and t["dias"] < 0


def ler_projetos(hoje):
    projetos = {}
    if not PROJETOS.is_dir():
        return projetos
    for arq in sorted(PROJETOS.glob("*.md")):
        txt = arq.read_text(encoding="utf-8")
        m_nome = P_NOME.search(txt)
        m_slug = P_SLUG.search(txt)
        m_est = P_ESTADO.search(txt)
        m_st = P_STATUS.search(txt)
        m_ras = P_RASCUNHO.search(txt)

        slug = (m_slug.group(1) if m_slug else arq.stem).strip()
        bruto = m_st.group(1).strip() if m_st else ""
        dias = dias_para(bruto, hoje)

        projetos[slug] = {
            "slug": slug,
            "nome": m_nome.group(1).strip() if m_nome else arq.stem,
            "arquivo": f"projetos/{arq.name}",
            "estado": m_est.group(1).strip() if m_est else None,
            "ultimo_status": bruto or None,
            "dias_sem_status": -dias if dias is not None and dias <= 0 else None,
            "rascunho": m_ras.group(1).strip() if m_ras else None,
        }
    return projetos


def main():
    if not TAREFAS.exists():
        sys.exit(f"nao encontrei {TAREFAS}")

    hoje = date.today()
    secao = None
    tarefas = []

    for linha in TAREFAS.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            secao = linha[3:].strip()
            continue
        m = LINHA.match(linha)
        if not m:
            continue
        estado = ESTADOS.get(m.group(1).lower())
        if estado is None:
            continue
        t = parse_tarefa(m.group(2), secao)
        t["estado"] = estado
        t["dias"] = dias_para(t["prazo"], hoje)
        tarefas.append(t)

    abertas = [t for t in tarefas if t["estado"] in ("aberto", "andamento")]
    com_prazo = [t for t in abertas if t["dias"] is not None]
    for t in tarefas:
        t["precisa_comunicar"] = t in abertas and precisa_comunicar(t)

    projetos_meta = ler_projetos(hoje)

    # Agrupa o que precisa ser comunicado, por projeto.
    comunicar = []
    pendentes = [t for t in abertas if t["precisa_comunicar"]]
    slugs = sorted({t["projeto"] or "sem-projeto" for t in pendentes} |
                   {s for s, p in projetos_meta.items() if p["rascunho"]})
    for slug in slugs:
        meta = projetos_meta.get(slug, {})
        itens = [t for t in pendentes if (t["projeto"] or "sem-projeto") == slug]
        comunicar.append({
            "slug": slug,
            "nome": meta.get("nome") or slug,
            "arquivo": meta.get("arquivo"),
            "estado": meta.get("estado"),
            "ultimo_status": meta.get("ultimo_status"),
            "dias_sem_status": meta.get("dias_sem_status"),
            "rascunho": meta.get("rascunho"),
            "itens": itens,
        })
    # Projeto com mais pendencia primeiro; empate decide pelo mais atrasado.
    comunicar.sort(key=lambda c: (-len(c["itens"]), -(c["dias_sem_status"] or 0)))

    contagem = {}
    for t in abertas:
        p = t["projeto"] or "sem-projeto"
        contagem[p] = contagem.get(p, 0) + 1

    try:
        commit = subprocess.run(
            ["git", "-C", str(RAIZ), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip() or None
    except Exception:
        commit = None

    dados = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "commit": commit,
        "resumo": {
            "abertas": len(abertas),
            "vencidas": sum(1 for t in com_prazo if t["dias"] < 0),
            "hoje": sum(1 for t in com_prazo if t["dias"] == 0),
            "proximos_7_dias": sum(1 for t in com_prazo if 0 < t["dias"] <= 7),
            "sem_prazo": sum(1 for t in abertas if t["dias"] is None),
            "promessas": sum(1 for t in abertas if t["prometi_a"]),
            "travadas": sum(1 for t in abertas if t["aguardo"]),
            "a_comunicar": len(pendentes),
            "concluidas_no_arquivo": sum(1 for t in tarefas if t["estado"] == "concluido"),
        },
        "por_projeto": dict(sorted(contagem.items(), key=lambda kv: -kv[1])),
        "projetos": projetos_meta,
        "comunicar": comunicar,
        "tarefas": tarefas,
    }

    bruto = json.dumps(dados, ensure_ascii=False, indent=2)
    SAIDA.write_text(bruto + "\n", encoding="utf-8")
    print(f"{SAIDA.relative_to(RAIZ)} gerado")

    if TEMPLATE.exists():
        html = TEMPLATE.read_text(encoding="utf-8")
        if MARCADOR not in html:
            sys.exit(f"marcador {MARCADOR!r} nao encontrado em {TEMPLATE.name}")
        PAGINA.write_text(html.replace(MARCADOR, bruto, 1), encoding="utf-8")
        print(f"{PAGINA.relative_to(RAIZ)} gerado")

    r = dados["resumo"]
    print(f"  {r['abertas']} abertas | {r['vencidas']} vencidas | "
          f"{r['promessas']} promessas | {r['travadas']} travadas | "
          f"{r['a_comunicar']} a comunicar")


if __name__ == "__main__":
    main()
