from models.sala_model import SalaModel

class SalaController:
    def __init__(self):
        self.model = SalaModel()

    def listar(self):
        return self.model.all().to_dict("records")

    def criar(self, nome, capacidade, tipo, campus, predio, andar, numero, computadores, projetor, ar, bancadas):
        df = self.model.all()
        new_id = str(len(df) + 1)
        row = {
            "id": new_id, "nome": nome, "capacidade": str(capacidade), "tipo": tipo,
            "campus": campus, "predio": predio, "andar": str(andar), "numero": numero,
            "computadores": str(computadores), "projetor": str(projetor),
            "ar_condicionado": str(ar), "bancadas": str(bancadas)
        }
        self.model.save(df._append(row, ignore_index=True) if hasattr(df, "_append") else __import__("pandas").concat([df, __import__("pandas").DataFrame([row])], ignore_index=True))

    def recomendar(self, tipo_aula, alunos, sala_escolhida=None):
        salas = self.listar()
        candidatos = [
            s for s in salas
            if int(s["capacidade"] or 0) >= int(alunos)
            and s["tipo"].lower() == tipo_aula.lower()
        ]
        return candidatos[0] if candidatos else None
