from flask import Flask, request, jsonify
from app.services.consolidado_service import ConsolidadoService
from app.repositories.consolidado_repository import ConsolidadoRepository
from app.repositories.lancamento_repository import LancamentoRepository

app = Flask(__name__)

consolidado_service = ConsolidadoService(ConsolidadoRepository(), LancamentoRepository())

@app.route('/consolidado/<data>', methods=['GET'])
def obter_saldo_diario(data):
    consolidado = consolidado_service.obter_saldo_diario(data)
    if consolidado:
        return jsonify({'data': consolidado.data, 'saldo': consolidado.saldo}), 200
    return jsonify({'message': 'Consolidado não encontrado'}), 404

@app.route('/consolidado/<data>', methods=['POST'])
def calcular_saldo_diario(data):
    consolidado = consolidado_service.calcular_saldo_diario(data)
    return jsonify({'data': consolidado.data, 'saldo': consolidado.saldo}), 200
