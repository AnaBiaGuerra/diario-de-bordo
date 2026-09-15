# Como usar este diário de bordo

Este repositório é um **template** para o diário de bordo pessoal que você vai
escrever ao longo da disciplina **Métodos de Desenvolvimento de Software (MDS)**,
como parte de uma pesquisa PIBIC sobre aprendizagem experiencial em engenharia de
software.

## 1. Crie o seu próprio repositório a partir deste template

No GitHub, use o botão **"Use this template"**. "Use this template" cria um repositório independente, sem o vínculo ativo com o repositório que acontece no fork.

## 2. Privacidade do Repositório

A escolha de marcar o novo repositório como privado é totalmente sua. Este é o
seu diário, ele só precisa ser compartilhado quando for
enviar seus dados para a pesquisa, no momento certo (veja o passo 6).

## 3. Rode o site localmente para escrever com preview

Este site é feito com [Docsify](https://docsify.js.org/): é só Markdown lido
direto pelo navegador, sem build. O navegador não
deixa abrir o `index.html` direto (duplo clique), ele precisa vir de um
servidor local. A forma recomendada é a ferramenta oficial do Docsify,
`docsify-cli`, porque é a mesma que depois te ajuda a entender como o site é
publicado no GitHub Pages. Instale uma vez:

```bash
npm i -g docsify-cli/
```

E, a partir daí, sempre que quiser escrever, dentro da pasta do repositório:

```bash
docsify serve .
```

(Se preferir não instalar nada de forma permanente, `npx docsify-cli serve .`
faz a mesma coisa, baixando a ferramenta na hora.)

Isso abre um preview local em `http://localhost:3000` e atualiza a página
sozinho a cada vez que você salva um arquivo `.md`. Não precisa publicar
este site em lugar nenhum, pode escrever só para você.

Outras opções, caso não tenha Node instalado:

- **VS Code:** instale a extensão "Live Server" e clique em "Go Live" no
  canto inferior direito.
- **Python:**
  ```bash
  python3 -m http.server 8080
  ```

Qualquer uma delas serve, o resultado é o mesmo: você pode ler as perguntas
de cada fase e visualizar seus posts formatados enquanto escreve.

## 4. Escolha um pseudônimo e reutilize-o sempre

Escolha um codinome (ex: `hitman`, `james-bond`) e anote-o em algum lugar
seu. Use **sempre o mesmo pseudônimo** nas 5 entregas do semestre, isso é o que
permite, depois, acompanhar a evolução da mesma pessoa ao longo das fases sem
saber quem ela é.

## 5. Escreva uma entrada por fase

A cada fase da disciplina (veja a lista completa em [Perguntas por
fase](./perguntas.md)), copie `blog/_TEMPLATE.md` para um novo arquivo em
`blog/`, com a data e um slug da fase no nome (ex:
`blog/2027-03-10-formacao-de-equipe.md`), e responda de forma dissertativa às 3
perguntas daquela fase. Um exemplo ilustrativo preenchido está em
`blog/2027-03-10-formacao-de-equipe-exemplo.md`. Veja [Como escrever uma
entrada](./como-escrever.md) para um método simples de transformar cada
pergunta em uma resposta concreta.

Ao todo, são **5 entradas no semestre**, uma por fase:

1. Formação de equipe
2. Pré-release 1
3. Entre releases
4. Pré-release 2
5. Pós-entrega

## 6. Quando isso vira dado de pesquisa

Em cada etapa do desenvolvimento da matéria/ao fim da matéria, para fazer o envio do .json, rode:

```bash
python3 scripts/export-entries.py
```

Esse script lê os seus posts em `blog/`, monta um pacote só com pseudônimo, fase,
data e o texto das respostas, sem dado de autor/commit do Git, e salva em
`export/diario-<seu-pseudonimo>.json`. O canal exato para enviar esse arquivo será informado no momento do envio.

## Resumo dos cuidados éticos

- Participação voluntária, pode parar a qualquer momento.
- Sem uso em avaliação acadêmica individual.
- Anonimato por pseudônimo autoescolhido + repositório privado.
