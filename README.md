# Invoca Piroto Backend

## Sobre o Projeto

O invoca Piroto é um [pet project](https://medium.com/@gabilapus1989/to-all-software-developers-do-have-a-pet-project-b7de8d51f244) que tenho para testar novas tecnologias que estou estudando. Nesta versão, vamos brincar com Django, no backend, e React, no frontend.

## Status do projeto

Em desenvolvimento.

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
- [VSCode](https://code.visualstudio.com/) ou outro editor de código.
- [Python 3.9.2](https://www.python.org/downloads/).
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

5. Instalar Django

    ```shell
    pip install -r requirements.txt
    ```

6. Criar super usuário
    - Por padrão, sempre uso usuário `admin` e senha `123mudar`

    ``` shell
    python manage.py createsuperuser
    ```

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
heroku config:set VAR=VALUE
```

- Ver as configurações do Heroku

```shell
heroku config
```

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

- [Python]()
- [DJango]()
- [Django Rest Framework]()

## Links funcionais

Acessando as funcionalidades do aplicativo

- [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Autor

[![Profile Pic](https://avatars.githubusercontent.com/u/359860?s=100&v=4)](https://hithub.com/josenaldo)

Criado por [Josenaldo de Oliveira Matos Filho](https://hithub.com/josenaldo)

Contatos: [![Twitter Badge](https://img.shields.io/badge/-@vudureverso-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/vudureverso)](https://twitter.com/vudureverso) [![Linkedin Badge](https://img.shields.io/badge/-Josenaldo-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/josenaldo/)](https://www.linkedin.com/in/josenaldo/) [![Gmail Badge](https://img.shields.io/badge/-josenaldo@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:josenaldo@gmail.com)](mailto:josenaldo@gmail.com)