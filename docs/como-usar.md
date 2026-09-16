# Como usar este diário de bordo

Este repositório pode ser usado como **template** para o diário de bordo que você vai escrever ao longo da disciplina **Métodos de Desenvolvimento de Software (MDS)**. Esse diário (blog) tem como propósito coletar a experiência dos estudantes ao longo do semestre. Algumas perguntas foram desenvolvidas para ajudar a trazer insights sobre como e o que escrever no seu diário, acesse a página de [como escrever o meu diário](./como-escrever-o-meu-diario.md) e [perguntas](perguntas.md).

A importância desse diário vai além da disciplina. Compartilhar sua experiência de desenvolvimento com os outros alunos pode ajudar seus colegas e futuros alunos em MDS. Além disso, é possível ver o progresso ao longo do semestre e quais foram as decisões, impecilhos, sucessos e barreiras enfrentadas. Nesse sentido a visibilidade do repositório deve ser **pública**, para que seu diário possa ser acessado e consultado por outras pessoas.

## 1. Crie o seu próprio repositório a partir deste template

No GitHub, use o botão **"Fork"**, localizado na página inicial deste repositório, para criar uma "cópia" dele dentro da sua própria conta do GitHub. Em seguida, clone o seu repositório em sua máquina para iniciar a escrita do seu diário.


## 2. Rode o site localmente

Este site é feito com [Docsify](https://docsify.js.org/): é só Markdown lido direto pelo navegador, sem build. O navegador não deixa abrir o `index.html` direto (duplo clique), ele precisa vir de um servidor local. A forma recomendada é a ferramenta oficial do Docsify, `docsify-cli`, porque é a mesma que depois te ajuda a entender como o site é publicado no GitHub Pages. Rode o comando abaixo para instalar o docsify:

```bash
npm i -g docsify-cli/
```

E, a partir daí, sempre que quiser escrever, dentro da pasta do repositório:

```bash
docsify serve .
```

(Se preferir não instalar nada de forma permanente, `npx docsify-cli serve .` faz a mesma coisa, baixando a ferramenta na hora.)

Isso abre um preview local em `http://localhost:3000` e atualiza a página sozinho a cada vez que você salva um arquivo `.md`.

## 3. Hora de escrever no seu blog

Para adicionar uma nova postagem no seu diário copie `blog/_TEMPLATE.md` para um novo arquivo em `blog/`, com a data e o título (de sua escolha) para a entrega (ex: `blog/2026-03-10-título-de-sua-escolha.md`), e escreva seu relato sobre as últimas semanas de desenvolvimento do projeto. Um exemplo ilustrativo preenchido está em `blog/2026-03-10-título-de-sua-escolha.md`. Acesse a página [como escrever o meu diário](./como-escrever-o-meu-diario.md) para instruções de como escrever e se você quiser um pouco mais de direcionamento acesse a página de [Perguntas](perguntas.md), onde escrevemos algumas questões para fomentar uma melhor reflexão sobre o que escrever em seu blog.

