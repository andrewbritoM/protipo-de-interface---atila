from datetime import datetime
import pandas as pd
from models.agendamento_model import AgendamentoModel

class AgendamentoController:
    def __init__(self):
        self.model = AgendamentoModel()

    def listar(self):
        return self.model.all().to_dict("records")

    def _overlap(self, start1, end1, start2, end2):
        return start1 < end2 and start2 < end1

    def conflita(self, sala, data, inicio, fim):
        for a in self.listar():
            if a["sala"] != sala or a["data"] != data or a["status"] == "Cancelado":
                continue
            if self._overlap(inicio, fim, a["inicio"], a["fim"]):
                return True
        return False

    def criar(self, professor, disciplina, sala, data, inicio, fim, alunos, justificativa):
        df = self.model.all()
        row = {
            "id": str(len(df) + 1),
            "professor": professor, "disciplina": disciplina, "sala": sala,
            "data": data, "inicio": inicio, "fim": fim, "alunos": str(alunos),
            "justificativa": justificativa, "status": "Pendente"
        }
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        self.model.save(df)

    def cancelar(self, rid):
        df = self.model.all()
        df.loc[df["id"] == str(rid), "status"] = "Cancelado"
        self.model.save(df)
