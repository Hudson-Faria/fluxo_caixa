from typing import List
from app.models.consolidado import Consolidado
from app.utils.db import get_db

class ConsolidadoRepository:
    def __init__(self):
        self.db = get_db()

    def get_consolidado_por_data(self, data) -> Consolidado:
        cursor = self.db.cursor()
        cursor.execute("SELECT data, saldo FROM consolidados WHERE data = ?", (data,))
        row = cursor.fetchone()
        if row:
            return Consolidado(data=row[0], saldo=row[1])
        return None

    def save_consolidado(self, consolidado: Consolidado):
        cursor = self.db.cursor()
        cursor.execute("INSERT OR REPLACE INTO consolidados (data, saldo) VALUES (?, ?)",
                       (consolidado.data, consolidado.saldo))
        self.db.commit()
