# GitHub Pages

Este repositório tem como propósito relatar a experiência de ensino e desenvolvimento de sistemas na matéria de MDS. Chamamos esse relato de **diário de bordo**, que deve ser escrito individualmente. Todos os relatos contidos nesse diário devem estar relacionados com a matéria de alguma forma (direta ou indiretamente). Para mais informações sobre como usar o diário, acesse [Como usar este diário](./como-usar.md).

Esta página descreve as etapas que você deve seguir para subir seu próprio diário de bordo. Recomendamos duas opções: **Docsify** e **MkDocs**. Nenhuma das duas é obrigatória, use a que fizer mais sentido para você.

## Docsify

[Docsify](https://docsify.js.org/#/quickstart) renderiza Markdown puro direto no navegador, sem etapa de build. É a mesma ferramenta usada neste diário.

**Quando escolher:** Você quer só Markdown sem configurar nada de build, ou busca maior facilidade.

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

**Quando escolher:** Você quer um tema mais
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
depender de rodar o comando manualmente.

