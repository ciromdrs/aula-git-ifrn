# App exemplo para aula de Git
Este é um aplicativo exemplo para a aula de Git.
Está escrito em Flask, mas isto não importa tanto para a aula.

# Como executar

1. Escolha uma pasta para trabalhar e abra o terminal nela.


2. Crie um ambiente virtual python:

    ```
    python -m venv envaula
    ```


3. Vá para dentro do novo ambiente virtual e ative-o:
   
    No Linux:
    ```
    cd envaula
    source bin/activate
    ```

    No Windows:
    ```
    cd envaula
    .\Scripts\activate.bat
    ```

    Perceba o `(envaula)` adicionado ao início da linha no terminal.

5. Clone o repositório:

    ```
    git clone https://github.com/ciromdrs/aula-git-ifrn
    ```

6. Vá para dentro da pasta da aplicação Flask:

    ```
    cd aula-git-ifrn/flask-app
    ```

7. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

8. Execute o projeto Flask no modo depuração:

    ```
    flask --app aula_git.py run --debug
    ```

9. Acesse `localhost:5000` no navegador. Você deve ver uma página web.
