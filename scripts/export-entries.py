#!/usr/bin/env python3
"""
Exporta as entradas do diário de bordo (blog/*.md) para um pacote único,
anonimizado, pronto para envio voluntário à pesquisa. Veja docs/como-usar.md.

O que este script faz:
  - Lê cada arquivo .md em blog/, exceto os que começam com "_"
    (como blog/_TEMPLATE.md).
  - Extrai APENAS o front matter (title, authors, tags, date) e o corpo do
    texto de cada post.
  - Não lê metadado de commit/autor do Git, só o conteúdo dos arquivos
    no disco.
  - Escreve export/diario-<pseudonimo>.json com o pacote consolidado.

Uso:
  python3 scripts/export-entries.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = REPO_ROOT / "blog"
EXPORT_DIR = REPO_ROOT / "export"

FRONT_MATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.DOTALL)
LIST_ITEM_RE = re.compile(r"^\s*-\s*(.*)$")
OBJECT_FIELD_RE = re.compile(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$")
KEY_RE = re.compile(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$")


def unquote(value):
    """Remove aspas simples/duplas envolvendo uma string, se houver."""
    trimmed = value.strip()
    if len(trimmed) >= 2 and (
        (trimmed[0] == '"' and trimmed[-1] == '"')
        or (trimmed[0] == "'" and trimmed[-1] == "'")
    ):
        return trimmed[1:-1]
    return trimmed


def parse_inline_list(value):
    """Parseia uma lista inline no estilo YAML flow: [a, "b c", 'd']."""
    inner = value.strip()[1:-1]
    if not inner.strip():
        return []
    return [unquote(item) for item in inner.split(",")]


def parse_front_matter(block):
    """
    Parser mínimo de front matter YAML, o suficiente para o formato fixo
    usado em blog/_TEMPLATE.md: chaves escalares (title, date) e chaves com
    valor em lista, seja inline ([a, b]) seja em linhas "- item" logo abaixo
    da chave (usado por "authors" quando declarado como lista de objetos
    {name: ...}).
    """
    data = {}
    current_key = None
    current_list = None

    def flush_list():
        nonlocal current_key, current_list
        if current_key:
            data[current_key] = current_list
        current_key = None
        current_list = None

    for raw_line in block.splitlines():
        if not raw_line.strip():
            continue

        list_item_match = LIST_ITEM_RE.match(raw_line)
        if list_item_match and current_key:
            rest = list_item_match.group(1)
            object_field_match = OBJECT_FIELD_RE.match(rest)
            if object_field_match:
                # Lista de objetos, ex.: "- name: exemplo-lobo-42"
                current_list.append(
                    {object_field_match.group(1): unquote(object_field_match.group(2))}
                )
            else:
                current_list.append(unquote(rest))
            continue

        flush_list()

        key_match = KEY_RE.match(raw_line)
        if not key_match:
            continue
        key, raw_value = key_match.group(1), key_match.group(2)
        value = raw_value.strip()

        if value == "":
            # Valor virá nas próximas linhas como lista "- item".
            current_key = key
            current_list = []
        elif value.startswith("[") and value.endswith("]"):
            data[key] = parse_inline_list(value)
        else:
            data[key] = unquote(value)

    flush_list()
    return data


def extract_author_pseudonym(authors):
    if not authors:
        return None
    first = authors[0] if isinstance(authors, list) else authors
    if isinstance(first, str):
        return first
    if isinstance(first, dict):
        return first.get("name") or first.get("key")
    return None


def list_post_files():
    return sorted(
        path
        for path in BLOG_DIR.iterdir()
        if path.is_file() and path.suffix == ".md" and not path.name.startswith("_")
    )


def format_date(value):
    if not value:
        return None
    return str(value)


def strip_truncate_marker(content):
    return re.sub(r"^\s*<!--\s*truncate\s*-->\s*$", "", content, flags=re.MULTILINE).strip()


def read_entry(file_path):
    raw = file_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(raw)
    data = parse_front_matter(match.group(1)) if match else {}
    content = match.group(2) if match else raw
    tags = data.get("tags")
    return {
        "fase": tags[0] if isinstance(tags, list) else tags,
        "titulo": data.get("title"),
        "data": format_date(data.get("date")),
        "pseudonimo": extract_author_pseudonym(data.get("authors")),
        "conteudo": strip_truncate_marker(content),
    }


def main():
    files = list_post_files()

    if not files:
        print(
            "Nenhuma entrada encontrada em blog/ (além do template). Nada para exportar.",
            file=sys.stderr,
        )
        sys.exit(1)

    entradas = [read_entry(f) for f in files]

    pseudonimos = {e["pseudonimo"] for e in entradas if e["pseudonimo"]}
    if not pseudonimos:
        print(
            'Nenhum pseudônimo encontrado no front matter "authors" das entradas.',
            file=sys.stderr,
        )
        sys.exit(1)
    if len(pseudonimos) > 1:
        print(
            f"Aviso: encontrei mais de um pseudônimo ({', '.join(sorted(pseudonimos))}). "
            "Confirme que você usou sempre o mesmo em todas as entradas.",
            file=sys.stderr,
        )
    pseudonimo = next(iter(pseudonimos))

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = EXPORT_DIR / f"diario-{pseudonimo}.json"
    out_path.write_text(
        json.dumps({"pseudonimo": pseudonimo, "entradas": entradas}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Exportadas {len(entradas)} entrada(s) para {out_path}")
    print(
        "Veja docs/como-usar.md."
    )


if __name__ == "__main__":
    main()
