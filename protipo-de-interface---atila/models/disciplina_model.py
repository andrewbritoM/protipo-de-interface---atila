from models.csv_model import CSVModel

class DisciplinaModel(CSVModel):
    def __init__(self):
        super().__init__("disciplinas.csv", ["id","nome","curso","tipo"])
