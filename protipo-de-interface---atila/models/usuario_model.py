from models.csv_model import CSVModel

class UsuarioModel(CSVModel):
    def __init__(self):
        super().__init__("usuarios.csv", ["id","nome","perfil"])
