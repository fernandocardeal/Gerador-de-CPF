# API Django Rest Framework para Gerar CPFs

Esta é uma API simples construída com o Django Rest Framework que permite gerar CPFs formatados e não formatados, podendo ou não ter o estado como parâmetro

## Configuração do Ambiente
1. Clone este repositório:
    ```
    git clone https://github.com/fernandocardeal/Gerador-de-CPF.git
    ```

2. Acesse o diretório do projeto:
    ```
    cd Gerador-de-CPF
    ```

3. Tendo o Python em sua máquina, crie um ambiente virtual (use python3 no Linux ou Mac):
    ```
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

    ```
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```
    source venv/bin/activate
    ```

5. Instale as dependências do projeto:

    ```
    pip install django djangorestframework
    ```

## Executando o Projeto

1. Certifique-se de estar na pasta Gerador-de-CPF, com a seguinte organização de base:

    ```
    Gerador-de-CPF /
    | - cpf_app /
    | - doc_tools /
    | - venv /
    | - .gitignore
    | - manage.py
    | - README.md
    ```

2. Execute as migrações para criar o banco de dados:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Crie um superusuário para acessar a interface administrativa:

    ```
    python manage.py createsuperuser
    ```

4. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

A API estará disponível em `http://localhost:8000/api/cpf/`.

## Uso da API

### Gerando CPFs

Você pode usar esta API para gerar CPFs formatados e não formatados com base no estado. Acesse a seguinte URL em seu navegador ou use uma ferramenta como o Postman:

- Gerar um CPF padrão: `http://localhost:8000/cpf/gerar/`

- Gerar um CPF com base no estado: `http://localhost:8000/cpf/gerar/?estado=<estado>`

Certifique-se de fornecer o parâmetro `<estado>` na URL para gerar um CPF específico do estado desejado. Se o parâmetro `<estado>` não for fornecido, a API gerará um CPF padrão.

### Validando CPFs
Agora você usar a API para validar um CPF qualquer, passando-o como parâmetro via GET. Acesse a URL em seu navegador ou com ferramentas como o Postman:

- Valide um CPF: `http://localhost:8000/cpf/validar/?cpf=<cpf>`

Certifique-se de fornecer o parâmetro `<cpf>` na URL para que a validação seja bem sucedida.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, faça suas alterações e envie um pull request. Teremos prazer em analisar suas contribuições.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
