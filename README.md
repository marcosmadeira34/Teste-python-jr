# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

Neste repositório você encontra o enunciado do teste técnico para a vaga de Desenvolvedor(a) Python Júnior [REMOTO].

## PROBLEMA

A companhia de marketing Vough tem trabalhado cada vez mais para empresas de tecnologia que disponibilizam código aberto.

Com o aumento das demandas surgiu a necessidade de rankear seus atuais e potenciais clientes por um nível de prioridade, de modo a dar preferência a projetos de empresas maiores e mais influentes no meio open source.

## SOLUÇÃO

Para auxiliar a Vough, você deve desenvolver uma API que calcula o valor de prioridade de cada cliente e retorna uma lista de clientes ordenandos por prioridade.

Na versão inicial da API, o valor de prioridade é calculado com base em dados encontrados no Github, através da seguinte fórmula:

`prioridade = <quantidade de membros públicos da organização no Github> + <quantidade de repositórios públicos da organização no Github>`

Na raiz deste repositório você encontra uma base para o projeto na pasta `vough_backend`. A API foi desenvolvida em Django/Python e seu dever é completar este projeto com as funcionalidades que estão faltando.

Para isso, foram passados alguns requisitos técnicos:

- Deve utilizar a [API Rest do Github](https://docs.github.com/pt/free-pro-team@latest/rest) para coletar as informações referentes às organizações.

- Deve possuir um endpoint para consultar uma organização específica através do nome (`login`):

```
GET /api/orgs/<login>/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```
{
    "login": "string",
    "name": "string",
    "score": int
}
```

Onde o `score` é o nível de prioridade da organização.
Em caso de sucesso, o status `200` deverá ser retornado.
Caso a empresa não seja encontrada, deve retornar o status `404`.

- Deve possuir um endpoint para a listagem de todas as organizações já consultadas através da API:

```
GET /api/orgs/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```
[
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  {
    "login": "string",
    "name": "string",
    "score": int
  },
  ...
]
```

As organizações listadas aqui devem estar ordenadas pela prioridade (`score`), da maior para a menor.

- Deve possuir um endpoint para a remoção de organizações da listagem:

```
DELETE /api/orgs/<login>/
```

Em caso de sucesso, o status `204` deverá ser retornado.
Caso a empresa não seja encontrada, deve retornar o status `404`.

## AVALIAÇÃO

Iremos avalias não só se a aplicação funciona, mas também a organização e a forma de codificar e resolver o problema. Após terminar a implementação, suba o teste no seu git e avise-nos.

## RECOMENDAÇÕES

- Use Python >= 3.7
- Siga a PEP-8.
- Use Git.
- [Escreva mensagens claras no Git](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices).
- Escreva testes unitários!
- Modele o banco de dados com cautela e procure representar as entidades corretamente.
- Siga as [boas práticas](https://swagger.io/resources/articles/best-practices-in-api-design/) para o desenvolvimento de APIs RESTful.
- Documente sua aplicação:
  - Descreva sua aplicação e os problemas que ela resolve.
  - Dê instruções de como executar os testes e a sua aplicação.
  - Documente os endpoints da API (ex.: Swagger).



Este teste foi originalmente desenvolvido pela [Instruct](https://instruct.com.br/)