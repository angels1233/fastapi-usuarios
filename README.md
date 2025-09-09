# Leitura de Usuários - FastAPI

API simples para leitura de usuários baseada em um arquivo mock `mock-users.json`.  
Permite listar usuários com filtros, paginação e consultar por ID. Inclui CORS habilitado.

---

## Tecnologias

- Python 3.12+
- FastAPI
- Uvicorn
- Poetry
- Pydantic (modelos de validação)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/leitura-usuario.git
cd leitura-usuario
pip install poetry
poetry install
poetry shell
```
## Rodando a aplicação:

```bash
uvicorn src.main:app --reload
```
1. Testando no navegador

abra o Swagger UI em: 

http://127.0.0.1:8000/docs

por lá você terá acesso a todos o endpoints.

2. Testando usando curl

Lista usuários(pagina1, tamanho 10):
```bash
curl "http://127.0.0.1:8000/users?page=1&page_size=10"
```
Filtra por e-mail:
```bash
curl "http://127.0.0.1:8000/users?q=felipe"
```
Filtra por role:
```bash
curl "http://127.0.0.1:8000/users?role=manager&is_active=true"
curl "http://127.0.0.1:8000/users?role=manager&is_active=false"
```
Filtra por ID de usuário:
```bash
curl "http://127.0.0.1:8000/users/16"
```