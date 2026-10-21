#!/usr/bin/env python3
"""Gera painel/dados.json a partir de tarefas.md.

O markdown e a fonte da verdade. Este script apenas deriva. Nao escreva
nada de volta no markdown a partir do JSON.

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
SAIDA = RAIZ / "painel" / "dados.json"

ESTADOS = {" ": "aberto", "/": "andamento", "x": "concluido", "-": "cancelado"}
LINHA = re.compile(r"^\s*-\s*\[(.)\]\s*(.+)$")
CAMPO = re.compile(r"^(prazo|pri|prometi-a|aguardo|fonte)\s*:\s*(.*)$", re.I)


def parse_tarefa(texto, secao):
    partes = [p.strip() for p in texto.split("|")]
    tarefa = {
        "descricao": partes[0],
        "projeto": None,
        "prazo": None,
        "prioridade": None,
        "prometi_a": None,
        "aguardo": None,
        "fonte": None,
        "secao": secao,
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
        chave, valor = m.group(1).lower(), m.group(2).strip()
        if chave == "prazo":
            tarefa["prazo"] = valor
        elif chave == "pri":
            tarefa["prioridade"] = valor.lower()
        elif chave == "prometi-a":
            tarefa["prometi_a"] = valor
        elif chave == "aguardo":
            tarefa["aguardo"] = valor
        else:
            tarefa["fonte"] = valor
    # projeto tambem pode vir como #tag no meio da descricao
    if tarefa["projeto"] is None:
        m = re.search(r"#([\w\-/]+)", tarefa["descricao"])
        if m:
            tarefa["projeto"] = m.group(1)
    return tarefa


def dias_para(prazo, hoje):
    try:
        d = datetime.strptime(prazo, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None
    return (d - hoje).days


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

    projetos = {}
    for t in abertas:
        p = t["projeto"] or "sem-projeto"
        projetos[p] = projetos.get(p, 0) + 1

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
            "concluidas_no_arquivo": sum(1 for t in tarefas if t["estado"] == "concluido"),
        },
        "por_projeto": dict(sorted(projetos.items(), key=lambda kv: -kv[1])),
        "tarefas": tarefas,
    }

    SAIDA.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    r = dados["resumo"]
    print(f"{SAIDA.relative_to(RAIZ)} gerado")
    print(f"  {r['abertas']} abertas | {r['vencidas']} vencidas | "
          f"{r['promessas']} promessas | {r['travadas']} travadas")


if __name__ == "__main__":
    main()
