from datetime import datetime
from dataclasses import dataclass

@dataclass
class Consolidado:
    data: datetime
    saldo: float
