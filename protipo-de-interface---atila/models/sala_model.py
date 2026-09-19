from models.csv_model import CSVModel

class SalaModel(CSVModel):
    def __init__(self):
        super().__init__("salas.csv", [
            "id","nome","capacidade","tipo","campus","predio","andar","numero",
            "computadores","projetor","ar_condicionado","bancadas"
        ])
