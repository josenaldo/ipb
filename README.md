# Invoca Piroto Backend

## Sobre o Projeto

O invoca Piroto é um [pet project](https://medium.com/@gabilapus1989/to-all-software-developers-do-have-a-pet-project-b7de8d51f244) que tenho para testar novas tecnologias que estou estudando. Nesta versão, vamos brincar com Django, no backend, e React, no frontend.

### Status do projeto

Projeto em desenvolvimento. Provavelmente, estará assim pelo resto da vida dele. Ele é feito pra isso e serve enquanto eu estiver estudando. Mas, se vocês querem apenas invocar os nomes do Capeta, usem sem moderação.

### Licença

![License Badge](https://img.shields.io/github/license/josenaldo/ipb?style=for-the-badge)

## Funcionalidades

- [x] Gestão da lista de Nomes do Capeta
- [x] Invocação de nome do capeta
- [ ] Jogo da forca de nome do capeta
- [ ] Lista de últimos nomes adicionados
- [ ] Cada nome adicionado é postado no Twitter
- [ ] Votação de nomes do capeta
- [ ] Lista dos nomes mais populares

## Demonstração

[https://invoca-piroto-backend.herokuapp.com/](https://invoca-piroto-backend.herokuapp.com/)

## Colaborando

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com).
- [Python 3.9.2](https://www.python.org/downloads/).
- [PostgreSQL 13.3](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [VSCode](https://code.visualstudio.com/) ou outro editor de código.
- [Anaconda](https://www.anaconda.com/) ou outro gerenciador de ambientes.

Não são obrigatórios, mas podem ajudar:

- [Sourcetree](https://www.sourcetreeapp.com/) ou outra GUI para o Git.

### Montando ambiente de desenvolvimento

Ao executar o projeto a primeira vez:

1. Clonar projeto no github

2. Instalar Python 3.9.2

3. Instalar Anaconda

4. Criar e ativar ambiente virtual
   - É muito importante que o ambiente virtual seja salvo em uma pasta com um nome DIFERENTE de `.env`. Uma sugestção é `.venv`.

    ```shell
    conda create  -p .venv python=3.9.2
    conda activate ./.venv
    ```

5. Instalar os pré-requisitos do projeto

    ```shell
    pip install -r requirements.txt
    ```

6. Configurar o acesso ao banco de dados
   - No arquivo `settings.py`, configurar a variável DATABASES['default']

    ```python
    DATABASES['default'] = dj_database_url.config(default='postgres://USER:PASS@HOST/DATABASE_NAME')
    ```

7. Executar os migrations

   ```shell
   python manage.py migrate
   ```

8. Criar super usuário
   - Por padrão, sempre uso usuário `admin` e senha `123mudar`
   - Pode ser usado qualquer email

   ``` shell
   python manage.py createsuperuser
   ```

9. Executar o projeto pela primeira vez, conforme descrito no item 'Executar o projeto localmente'

10. Configurar usuários padrão
    - Entrar no [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
    - Logar com super usuário
    - Adicionar grupo sumonadores
    - Dar, ao grupo sumonadores, as seguintes permissões
      - "namelist | Nome | Can add Nome do Capeta"
      - "namelist | Nome | Can change Nome do Capeta"
      - "namelist | Nome | Can delete Nome do Capeta"
      - "namelist | Nome | Can view Nome do Capeta"
    - Adicionar usuário `sumonador`
      - senha `123mudar@` ou outra qualquer
      - email qualquer (mas diferente do super usuário admin)
      - adicionar grupo sumonadores
      - NÃO marcar como super usuário
    - Se quiser, adicione outro usuário, mas sem grupo

### Alterando projeto

Cada vez que for testar o projeto:

1. Ativar o ambiente virtual do conda, no terminal da IDE a ser usado.

    ```shell
    conda activate ./.venv
    ```

2. Executar o projeto localmente
    - Com o Django:

    ```shell
    python manage.py runserver
    ```

    - Com o Heroku, no Windows:

    ```shell
    heroku local web -f Procfile.windows
    ```

    - Com o Heroku, no Linux:

    ```shell
    heroku local web
    ```

### Comandos úteis

#### Heroku

- Abre, no navegador, a aplicação rodando no heroku

  ```shell
  heroku open --app invoca-piroto-backend
  ```

- Mostra os logs da aplicação

  ```shell
  heroku logs --tail --app invoca-piroto-backend
  ```

- Roda o bash no Heroku

  ```shell
  heroku run bash --app invoca-piroto-backend
  ```

- Configurar variáveis de configuração no heroku

  ```shell
  heroku config:set --app invoca-piroto-backend NOME=VALOR
  ```

- Ver as configurações do Heroku

  ```shell
  heroku config --app invoca-piroto-backend
  ```

- Ver a lista de addons usados no Heroku

  ```shell
  heroku addons
  ```

- Ver dados sobre o banco de dados usado pelo app, no Heroku

  ```shell
  heroku pg --app invoca-piroto-backend
  ```

- Roda o migrate do Django no Heroku

  ```shell
  heroku run python manage.py migrate --app invoca-piroto-backend
  ```

- Configurar super usuário no Heroku

  ```shell
  heroku run python manage.py createsuperuser --app invoca-piroto-backend
  ```

- Abre o shell do Postgres, no Heroku

  ```shell
  heroku pg:psql --app invoca-piroto-backend
  ```

#### Django

- Depurar a pesquisa por arquivos estáticos, para ver em quais diretórios o Django está buscando esses arquivos

    ```shell
    python manage.py findstatic --verbosity 2 assets/js/modules/PageNomes.js
    ```

- Ver, no terminal, as configurações do Django

    ```shell
    python manage.py diffsettings --all
    ```

## Tecnologias utilizadas

Neste projeto, utilizei as seguintes tecnologias:

- [Python](https://www.python.org)
- [DJango](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [dj-database-url](https://github.com/jacobian/dj-database-url)
- [Bootstrap 4.6.0](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

## Links funcionais

Acessando as funcionalidades do aplicativo

### Local

- Qualquer usuário
  - [Home](http://127.0.0.1:8000/)
  - [Django Admin Site](http://127.0.0.1:8000/admin)
  - [Incocação do Nome do Capeta](http://127.0.0.1:8000/invocacao)
- Autenticados
  - [Lista de Nomes do Capeta](http://127.0.0.1:8000/nomes/)
  - [Detalhes do Nome do Capeta 1](http://127.0.0.1:8000/nomes/1)
  - [Editar Nome do Capeta 1](http://127.0.0.1:8000/nomes/1/editar/)
  - [Remover Nome do Capeta 1](http://127.0.0.1:8000/nomes/1/remover/)

### Em produção

-

## Autor

[![Profile Pic](https://avatars.githubusercontent.com/u/359860?s=100&v=4)](https://hithub.com/josenaldo)

Criado por [Josenaldo de Oliveira Matos Filho](https://hithub.com/josenaldo)

Contatos: [![Twitter Badge](https://img.shields.io/badge/-@vudureverso-1ca0f1?style=for-the-badge&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/vudureverso)](https://twitter.com/vudureverso) [![Linkedin Badge](https://img.shields.io/badge/-Josenaldo-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/josenaldo/)](https://www.linkedin.com/in/josenaldo/) [![Gmail Badge](https://img.shields.io/badge/-josenaldo@gmail.com-c14438?style=for-the-badge&logo=Gmail&logoColor=white&link=mailto:josenaldo@gmail.com)](mailto:josenaldo@gmail.com)
