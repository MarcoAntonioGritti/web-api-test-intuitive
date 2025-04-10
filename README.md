
---

## Funcionalidades

- API leve e rápida construída com Flask.
- Gerenciamento de dependências e ambiente virtual com Poetry.

---

## Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:

- Python 3.13+
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

---

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/MarcoAntonioGritti/web-api-test-intuitive.git
    cd web-api-test-intuitive
    ```

2. Instale as dependências usando o Poetry:

    ```bash
    poetry install
    ```

3. Ative o ambiente virtual:

    ```bash
    ./.venv/Scripts/Activate
    ```

---

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento do Flask, execute:

```bash
poetry run flask --app src.backend.app run --debug
```

A API estará disponível na rota: [http://127.0.0.1:5000/api/consultar].

Certifique-se de ter a extensão Live Server instalada e ativada no seu editor para visualizar a interface da aplicação. Abra o arquivo `index.html` localizado em `src/frontend/` e inicie o Live Server para acessar a interface no navegador.

---

## Estrutura do Projeto

```plaintext
Web-Api-Test/
├── src/
│    │
│    ├─backend/
│    │   │
│    │   ├─controller/
│    │   │     │
│    │   │     ├── __init__.py          # Inicialização do módulo controller
│    │   │     ├── route.py             # Definição das rotas da API
│    │   │     ├── blueprint.py         # Configuração dos blueprints da API
│    │   │   
│    │   ├─data/
│    │   │  │
│    │   │  ├── Relatorio_cadop.csv     # Arquivo de dados utilizado pela aplicação
│    │   │   
│    │   ├── app.py                     # Ponto de entrada da aplicação Flask
│    │   ├── config.py                  # Configurações da aplicação
│    │   ├── exeception.py              # Tratamento de exceções personalizadas
│    │   └── utils.py                   # Funções utilitárias
│    │
│    ├─frontend/
│    │    │
│    │    ├── index.html                # Página inicial da aplicação
│
├── README.md                           # Documentação do projeto
├── pyproject.toml                      # Configuração do Poetry
```

---

