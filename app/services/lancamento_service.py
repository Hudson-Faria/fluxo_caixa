from datetime import datetime
from app.models.lancamento import Lancamento
from app.repositories.lancamento_repository import LancamentoRepository

class LancamentoService:
    def __init__(self, lancamento_repository: LancamentoRepository):
        self.lancamento_repository = lancamento_repository

    def registrar_lancamento(self, valor: float, tipo: str, data: datetime):
        lancamento = Lancamento(id=None, valor=valor, tipo=tipo, data=data)
        self.lancamento_repository.add_lancamento(lancamento)
