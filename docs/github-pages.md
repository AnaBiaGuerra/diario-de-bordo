# GitHub Pages no projeto da disciplina

Esta página é sobre o **projeto de software da sua equipe** na disciplina MDS
(o sistema que vocês estão construindo), não sobre este diário de bordo. Se
você chegou aqui procurando como rodar ou publicar o diário, veja [Como usar
este diário](./como-usar.md).

Em algum momento da disciplina será preciso publicar a documentação do
projeto (manual de uso, decisões de arquitetura, guia de contribuição) como um
site, direto do repositório da equipe, usando o **GitHub Pages**. Duas
opções que recomendo são **Docsify** e **MkDocs**. Nenhuma das duas é obrigatória, use a que fizer mais sentido para a stack do seu projeto.

## Docsify

[Docsify](https://docsify.js.org/#/quickstart) renderiza Markdown puro direto no navegador, sem etapa de build. É a mesma ferramenta usada neste diário.

**Quando escolher:** projeto pequeno/médio, você quer só Markdown sem
configurar nada de build, ou busca maior facilidade.

### Instalação

```bash
npm i -g docsify-cli
```

### Uso local

Dentro da pasta de documentação do projeto:

```bash
docsify init ./docs
docsify serve ./docs
```

`docsify init` cria um `index.html` mínimo e um `README.md` de exemplo dentro
de `docs/`. Edite os arquivos `.md` e o navegador atualiza sozinho.

### Publicar no GitHub Pages

Como não há build, basta apontar o GitHub Pages para a pasta certa:

1. No GitHub, vá em **Settings → Pages**.
2. Em **Source**, selecione a branch `main` (ou a branch padrão do projeto) e
   a pasta `/docs` (ou `/root`, se o `index.html` estiver na raiz).
3. Salve. O site fica disponível em `https://<usuario-ou-org>.github.io/<repositorio>/`
   em alguns minutos.

Não é necessário nenhum workflow de Actions para o Docsify.

## MkDocs

[MkDocs](https://www.mkdocs.org/getting-started/) gera um site estático (HTML/CSS/JS) a partir de arquivos Markdown, com um passo de build. É comum em projetos Python e tem um tema popular, o
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

**Quando escolher:** projeto já usa Python/pip, ou você quer um tema mais
pronto (busca, navegação, dark mode) sem estilizar nada manualmente.

### Instalação

```bash
pip install mkdocs
# opcional, tema mais completo:
pip install mkdocs-material
```

### Uso local

Na raiz do projeto (ou em uma subpasta dedicada à documentação):

```bash
mkdocs new .
mkdocs serve
```

`mkdocs new .` cria `mkdocs.yml` (configuração) e `docs/index.md`. `mkdocs
serve` sobe um preview local, por padrão em `http://127.0.0.1:8000`, que
atualiza a cada arquivo salvo.

### Publicar no GitHub Pages

MkDocs tem um comando dedicado que builda o site e publica na branch
`gh-pages` automaticamente:

```bash
mkdocs gh-deploy
```

Depois, em **Settings → Pages** do repositório, confirme que a *Source* está
apontando para a branch `gh-pages`. Rode `mkdocs gh-deploy` de novo sempre que
quiser atualizar o site publicado (ele sobrescreve a branch `gh-pages` com o
build mais recente).

Alternativa mais automatizada: configurar uma GitHub Action que roda `mkdocs
build` (ou `mkdocs gh-deploy`) a cada push na branch principal, para não
depender de rodar o comando manualmente. Isso é opcional e só vale a pena se o
time já estiver confortável com Actions.

## Não confunda com o diário de bordo

Esta página é sobre a documentação **pública** do projeto de software da
equipe. O diário de bordo pessoal é outra coisa: é um instrumento de pesquisa
com regras próprias de anonimato e privacidade, publicado (se publicado) só
quando e como descrito em [Como usar este diário](./como-usar.md).
