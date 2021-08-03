# Invoca Piroto Backend

Se baixar esse projeto no windows, uma opção é usar o Anaconda para gerenciar seus ambientes Python.

## Montando ambiente de desenvolvimento

Ao executar o projeto a primeira vez:

1. Clonar projeto no github

2. Instalar Python 3.9.2

3. Instalar Anaconda

4. Criar e ativar ambiente virtual

     ```shell
    > conda create  -p .venv python=3.9.2
    > conda activate ./.venv
    ```

5. Instalar Django

    ```shell
    > pip install -r requirements.txt
    ```

6. Criar super usuário

    Por padrão, sempre uso usuário `admin` e senha `123mudar`

    ``` shell
    > python manage.py createsuperuser
    ```

## Alterando projeto

Cada vez que for testar o projeto:

1. Ativar o ambiente virtual do conda

    ```shell
    > conda activate ./.venv
    ```

2. Executar o projeto localmente

    ```shell
    > python manage.py runserver
    ```

## Links funcionais

Os segunites links são funcionais, no aplicativo:

- [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
