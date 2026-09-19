import pandas as pd
from models.disciplina_model import DisciplinaModel

class DisciplinaController:
    def __init__(self):
        self.model = DisciplinaModel()

    def listar(self):
        return self.model.all().to_dict("records")

    def criar(self, nome, curso, tipo):
        df = self.model.all()
        row = {"id": str(len(df)+1), "nome": nome, "curso": curso, "tipo": tipo}
        self.model.save(pd.concat([df, pd.DataFrame([row])], ignore_index=True))
