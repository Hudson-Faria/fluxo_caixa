from flask import Flask, request, jsonify
from app.services.lancamento_service import LancamentoService
from app.repositories.lancamento_repository import LancamentoRepository

app = Flask(__name__)

lancamento_service = LancamentoService(LancamentoRepository())

@app.route('/lancamento', methods=['POST'])
def registrar_lancamento():
    dados = request.get_json()
    lancamento_service.registrar_lancamento(dados['valor'], dados['tipo'], dados['data'])
    return jsonify({'message': 'Lançamento registrado com sucesso!'}), 201
