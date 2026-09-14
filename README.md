# Diário de Bordo — MDS

Template Docsify para o diário de bordo pessoal de estudantes da disciplina
**Métodos de Desenvolvimento de Software (MDS)** da UnB, usado como instrumento de uma pesquisa PIBIC sobre aprendizagem experiencial em
engenharia de software (orientação: Profa. Dra. Carla Rocha).

## Para estudantes

Leia **[docs/como-usar.md](docs/como-usar.md)**, passo a
passo de como criar seu próprio diário privado a partir deste template, com que
frequência escrever, como manter anonimato, e o que fazer com seus dados.

As perguntas orientadoras dissertativas, dividas por fase, estão em
[docs/perguntas.md](docs/perguntas.md) / [data/perguntas.json](data/perguntas.json).

## Estrutura

```text
index.html                Shell do site (Docsify, lido direto pelo navegador)
_sidebar.md               Navegação lateral do site
docs/como-usar.md         Passo a passo para o estudante
docs/como-escrever.md     Método para transformar uma pergunta em resposta concreta
docs/perguntas.md         As 15 perguntas dissertativas, por fase
data/perguntas.json       Mesma informação, em formato estruturado (fonte de verdade)
blog/_TEMPLATE.md         Modelo de entrada, duplicar 1x por fase
blog/*.md                 Entradas do diário (uma por fase, 5 no semestre)
scripts/export-entries.py  Gera um pacote anonimizado das entradas, para envio
                            voluntário quando a coleta for autorizada
```

## Para desenvolvimento local

Este site usa [Docsify](https://docsify.js.org/): é Markdown puro renderizado
pelo navegador, sem build. A única exigência é servir os arquivos por HTTP. Forma recomendada, com a CLI oficial do Docsify:

```bash
npm i -g docsify-cli
docsify serve .
```

Alternativas sem Node (Live Server do VS Code, ou
`python3 -m http.server 8080`) estão em
[docs/como-usar.md](docs/como-usar.md).

Para publicar (opcional), basta apontar o GitHub Pages do seu fork/template
pessoal para a branch `main`, raiz do repositório, sem build nem Actions,
já que não há nenhuma etapa de compilação.

O único script do template é `scripts/export-entries.py`, usado para gerar
o pacote de envio à pesquisa (veja [docs/como-usar.md](docs/como-usar.md)).
