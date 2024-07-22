import unittest
from datetime import datetime
from app.models.consolidado import Consolidado
from app.models.lancamento import Lancamento
from app.repositories.consolidado_repository import ConsolidadoRepository
from app.repositories.lancamento_repository import LancamentoRepository
from app.services.consolidado_service import ConsolidadoService

class FakeLancamentoRepository(LancamentoRepository):
    def __init__(self):
        self.lancamentos = []

    def add_lancamento(self, lancamento: Lancamento):
        self.lancamentos.append(lancamento)

    def get_lancamentos_por_data(self, data):
        return [l for l in self.lancamentos if l.data == data]

class FakeConsolidadoRepository(ConsolidadoRepository):
    def __init__(self):
        self.consolidados = {}

    def get_consolidado_por_data(self, data):
        return self.consolidados.get(data, None)

    def save_consolidado(self, consolidado: Consolidado):
        self.consolidados[consolidado.data] = consolidado

class TestConsolidadoService(unittest.TestCase):
    def setUp(self):
        self.lancamento_repository = FakeLancamentoRepository()
        self.consolidado_repository = FakeConsolidadoRepository()
        self.consolidado_service = ConsolidadoService(self.consolidado_repository, self.lancamento_repository)

    def test_calcular_saldo_diario(self):
        data = datetime(2024, 7, 19)
        self.lancamento_repository.add_lancamento(Lancamento(id=1, valor=100.0, tipo='credito', data=data))
        self.lancamento_repository.add_lancamento(Lancamento(id=2, valor=50.0, tipo='debito', data=data))

        consolidado = self.consolidado_service.calcular_saldo_diario(data)
        self.assertEqual(consolidado.saldo, 50.0)
        self.assertEqual(consolidado.data, data)

    def test_obter_saldo_diario(self):
        data = datetime(2024, 7, 19)
        self.consolidado_repository.save_consolidado(Consolidado(data=data, saldo=50.0))

        consolidado = self.consolidado_service.obter_saldo_diario(data)
        self.assertIsNotNone(consolidado)
        self.assertEqual(consolidado.saldo, 50.0)
        self.assertEqual(consolidado.data, data)

if __name__ == '__main__':
    unittest.main()
