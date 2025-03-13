# Manual de Uso da API Flask

## Introdução
Esta API foi desenvolvida utilizando Flask e SQLAlchemy para gerenciar clientes, produtos, pedidos e itens de pedidos. Ela roda localmente no computador do usuário e permite interação através de requisições HTTP.

## Requisitos
Antes de iniciar a API, certifique-se de ter os seguintes requisitos instalados:

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (banco padrão)
- Insomnia, Thunder Client ou Postman (para testar as requisições)

Se ainda não instalou as dependências, execute:
```bash
pip install flask flask-sqlalchemy flask-migrate
```

## Configuração e Inicialização
1. Clone o repositório do GitHub:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Configure e inicialize o banco de dados:
   ```bash
   flask db init
   flask db migrate -m "Inicialização do banco"
   flask db upgrade
   ```

3. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
   A API estará rodando localmente em: `http://127.0.0.1:5000/`

## Endpoints Disponíveis
A API possui os seguintes endpoints:

### 1. Clientes
#### a) Listar todos os clientes
- **GET** `/clientes/`
- **Resposta Exemplo:**
```json
[
  {
    "id": 1,
    "nome": "João da Silva",
    "endereco": "Rua das Flores, 123",
    "numero": "456",
    "complemento": "Apto 101",
    "bairro": "Centro",
    "cep": "12345-678",
    "cidade": "São Paulo",
    "estado": "SP"
  }
]
```

#### b) Criar um novo cliente
- **POST** `/clientes/`
- **Corpo da requisição (JSON):**
```json
{
  "nome": "Maria Oliveira",
  "endereco": "Avenida Paulista, 1000",
  "numero": "1000",
  "complemento": "Sala 101",
  "bairro": "Bela Vista",
  "cep": "01310-100",
  "cidade": "São Paulo",
  "estado": "SP"
}
```
- **Resposta:**
```json
{"message": "Cliente criado com sucesso!"}
```

### 2. Produtos
#### a) Listar todos os produtos
- **GET** `/produtos/`

#### b) Criar um novo produto
- **POST** `/produtos/`
```json
{
  "nome": "Notebook Dell XPS",
  "preco": 7500.00
}
```

### 3. Pedidos
#### a) Listar todos os pedidos
- **GET** `/pedidos/`

#### b) Criar um novo pedido
- **POST** `/pedidos/`
```json
{
  "cliente_id": 1
}
```

### 4. Itens do Pedido
#### a) Adicionar um item ao pedido
- **POST** `/itens_pedido/`
```json
{
  "pedido_id": 1,
  "produto_id": 2,
  "quantidade": 3
}
```

## Testando a API
Você pode usar o Thunder Client, Insomnia ou Postman para testar as requisições. Basta configurar as requisições conforme os endpoints mencionados.

Caso queira testar via terminal, use o `curl` para um GET:
```bash
curl -X GET http://127.0.0.1:5000/clientes/
```
E para um POST:
```bash
curl -X POST http://127.0.0.1:5000/clientes/ \
-H "Content-Type: application/json" \
-d '{"nome": "Maria Oliveira", "endereco": "Av. Paulista, 1000", "cidade": "São Paulo", "estado": "SP"}'
```

## Conclusão
Agora você tem a API rodando localmente e pronta para uso. Para qualquer problema, verifique se o Flask está rodando e se as dependências estão instaladas corretamente.

