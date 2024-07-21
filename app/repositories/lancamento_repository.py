from typing import List
from app.models.lancamento import Lancamento
from app.utils.db import get_db

class LancamentoRepository:
    def __init__(self):
        self.db = get_db()

    def add_lancamento(self, lancamento: Lancamento):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO lancamentos (valor, tipo, data) VALUES (?, ?, ?)",
                       (lancamento.valor, lancamento.tipo, lancamento.data))
        self.db.commit()

    def get_lancamentos_por_data(self, data) -> List[Lancamento]:
        cursor = self.db.cursor()
        cursor.execute("SELECT id, valor, tipo, data FROM lancamentos WHERE data = ?", (data,))
        rows = cursor.fetchall()
        return [Lancamento(id=row[0], valor=row[1], tipo=row[2], data=row[3]) for row in rows]
