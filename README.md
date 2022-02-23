A Vough é uma empresa de marketing que está cada vez mais focada em atender empresas de tecnologia
de código aberto.

O objetivo desta API é auxiliar a empresa de marketing Vough a rankear seus atuais e potencias clientes e priorizar projetos
maiores e mais influentes de empresas de tecnologia que disponibilizam código aberto(open source).

O valor desse cálculo de prioridade na versão desta API é dado pela "quantidade de membros públicos da organização no Github + quantidade de repositórios públicos, fornecedo uma pontuação "score".

Para executar o projeto na sua IDE de preferência:

1 - Comece criando seu ambiente virtual para isolar seu projeto de qualquer outro projeto no seu computador.
Nomeei este ambiente virtual de "venv" utilizando o virtualenv.

```shell script
> virtualenv venv
```

2 - Ative o ambiente virtual no Windows da seguinte forma:

```shell script
> .\ven\scripts\activate
```

3 - Gere o arquivo de migrações para atualizar o banco de dados com o comando:

```shell script
> python manage.py makemigrations api
```

4 - Aplique as migrações no banco de dados com o comando migrate:

```shell script
> python manage.py migrate
```

5 - Execute o projeto com o comando:
```shell script
> python manage.py runserver
```