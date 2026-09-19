from models.csv_model import CSVModel

class AgendamentoModel(CSVModel):
    def __init__(self):
        super().__init__("agendamentos.csv", [
            "id","professor","disciplina","sala","data","inicio","fim",
            "alunos","justificativa","status"
        ])
