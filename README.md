EXECUTANDO O PROJETO

1. Crie um ambiente virtual e instale as dependências:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Inicialize o banco de dados:
python -c 'from app.utils.db import init_db; init_db()'

3. Inicie o servidor Flask:
python app/main.py

4. Utilize ferramentas como curl ou Postman para testar os endpoints:
Registrar lançamento:
curl -X POST http://127.0.0.1:5000/lancamento -H "Content-Type: application/json" -d '{"valor": 100, "tipo": "credito", "data": "2024-07-19"}'

Calcular saldo diário:
curl -X POST http://127.0.0.1:5000/consolidado/2024-07-19

Obter saldo diário:
curl http://127.0.0.1:5000/consolidado/2024-07-19




