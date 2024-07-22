import unittest
from datetime import datetime
from app.models.lancamento import Lancamento
from app.repositories.lancamento_repository import LancamentoRepository
from app.services.lancamento_service import LancamentoService

class FakeLancamentoRepository(LancamentoRepository):
    def __init__(self):
        self.lancamentos = []

    def add_lancamento(self, lancamento: Lancamento):
        self.lancamentos.append(lancamento)

    def get_lancamentos_por_data(self, data):
        return [l for l in self.lancamentos if l.data == data]

class TestLancamentoService(unittest.TestCase):
    def setUp(self):
        self.lancamento_repository = FakeLancamentoRepository()
        self.lancamento_service = LancamentoService(self.lancamento_repository)

    def test_registrar_lancamento(self):
        data = datetime(2024, 7, 19)
        self.lancamento_service.registrar_lancamento(100.0, 'credito', data)
        lancamentos = self.lancamento_repository.get_lancamentos_por_data(data)
        self.assertEqual(len(lancamentos), 1)
        self.assertEqual(lancamentos[0].valor, 100.0)
        self.assertEqual(lancamentos[0].tipo, 'credito')
        self.assertEqual(lancamentos[0].data, data)

if __name__ == '__main__':
    unittest.main()
