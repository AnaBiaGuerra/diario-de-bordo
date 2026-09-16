# Diário de Bordo — MDS

O diário de bordo é um registro pessoal e dissertativo, escrito por cada estudante ao longo do semestre, sobre a própria experiência de cursar MDS decisões da equipe, dificuldades técnicas, aprendizados, mudanças de rumo. Cada estudante mantém o seu diário em um repositório público próprio (fork deste template).Usado como instrumento de avaliação da disciplina e, também, como instrumento sobre aprendizagem experiencial em engenharia de software.
 Veja [docs/avaliacao.md](docs/avaliacao.md) para a especificação de como o diário é avaliado.

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


