from datetime import datetime
from dataclasses import dataclass

@dataclass
class Lancamento:
    id: int
    valor: float
    tipo: str  # 'debito' ou 'credito'
    data: datetime
