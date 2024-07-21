from datetime import datetime
from app.models.consolidado import Consolidado
from app.repositories.consolidado_repository import ConsolidadoRepository
from app.repositories.lancamento_repository import LancamentoRepository

class ConsolidadoService:
    def __init__(self, consolidado_repository: ConsolidadoRepository, lancamento_repository: LancamentoRepository):
        self.consolidado_repository = consolidado_repository
        self.lancamento_repository = lancamento_repository

    def calcular_saldo_diario(self, data: datetime) -> Consolidado:
        lancamentos = self.lancamento_repository.get_lancamentos_por_data(data)
        saldo = sum(l.valor if l.tipo == 'credito' else -l.valor for l in lancamentos)
        consolidado = Consolidado(data=data, saldo=saldo)
        self.consolidado_repository.save_consolidado(consolidado)
        return consolidado

    def obter_saldo_diario(self, data: datetime) -> Consolidado:
        return self.consolidado_repository.get_consolidado_por_data(data)
