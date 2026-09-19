# ATILA — Sistema de Gestão e Agendamento de Salas

Protótipo acadêmico desenvolvido em Python + Streamlit + Pandas + CSV, organizado em MVC.

## Estrutura

- `app.py` — interface principal
- `models/` — acesso aos dados
- `controllers/` — regras de negócio
- `data/` — arquivos CSV
- `utils/` — componentes de interface
- `requirements.txt` — dependências

## Executar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Funcionalidades

- cadastro de salas;
- localização por campus, prédio, andar e número;
- cadastro de usuários;
- cadastro de disciplinas;
- classificação por tipo de aula;
- recomendação de sala por tipo e capacidade;
- solicitação de reserva;
- verificação de conflito de horário;
- justificativa para reserva excepcional;
- cancelamento sem apagar histórico;
- filtros de agendamentos;
- dashboard;
- comprovante em tela por meio do registro da reserva.

> O CSV é utilizado apenas como persistência inicial do protótipo. Para produção, recomenda-se migrar para SQLite/PostgreSQL e implementar autenticação e permissões.
