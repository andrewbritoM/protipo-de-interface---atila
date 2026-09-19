import pandas as pd
from models.usuario_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def listar(self):
        return self.model.all().to_dict("records")

    def criar(self, nome, perfil):
        df = self.model.all()
        row = {"id": str(len(df)+1), "nome": nome, "perfil": perfil}
        self.model.save(pd.concat([df, pd.DataFrame([row])], ignore_index=True))
