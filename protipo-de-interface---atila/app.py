import streamlit as st
from controllers.sala_controller import SalaController
from controllers.agendamento_controller import AgendamentoController
from controllers.usuario_controller import UsuarioController
from controllers.disciplina_controller import DisciplinaController
from utils.ui import setup_page, header

setup_page()
header()

sala_controller = SalaController()
ag_controller = AgendamentoController()
usuario_controller = UsuarioController()
disc_controller = DisciplinaController()

st.sidebar.markdown("## ATILA")
st.sidebar.caption("Gestão e Agendamento de Salas")
menu = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "Salas", "Nova Reserva", "Agendamentos", "Usuários", "Disciplinas"]
)

if menu == "Dashboard":
    salas = sala_controller.listar()
    ags = ag_controller.listar()
    ativos = [a for a in ags if a["status"] == "Confirmado"]
    st.title("Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Salas", len(salas))
    c2.metric("Reservas", len(ags))
    c3.metric("Confirmadas", len(ativos))
    c4.metric("Usuários", len(usuario_controller.listar()))
    st.divider()
    st.subheader("Visão geral das salas")
    st.dataframe(salas, use_container_width=True, hide_index=True)

elif menu == "Salas":
    st.title("Cadastro e gerenciamento de salas")
    with st.form("nova_sala"):
        c1, c2 = st.columns(2)
        nome = c1.text_input("Nome da sala")
        capacidade = c2.number_input("Capacidade", min_value=1, value=30)
        tipo = c1.selectbox("Tipo de sala", ["Teórica", "Laboratório de Informática", "Odontologia", "Auditório", "Prática", "Outro"])
        campus = c2.text_input("Campus", "Campus Central")
        predio = c1.text_input("Prédio", "Prédio A")
        andar = c2.number_input("Andar", min_value=0, value=1)
        numero = c1.text_input("Número", "101")
        computadores = c2.number_input("Quantidade de computadores", min_value=0, value=0)
        projetor = c1.checkbox("Projetor")
        ar = c2.checkbox("Ar-condicionado")
        bancadas = c1.checkbox("Bancadas")
        if st.form_submit_button("Cadastrar sala", type="primary"):
            if not nome.strip():
                st.error("Informe o nome da sala.")
            else:
                sala_controller.criar(nome, capacidade, tipo, campus, predio, andar, numero, computadores, projetor, ar, bancadas)
                st.success("Sala cadastrada com sucesso.")
                st.rerun()

    st.subheader("Salas cadastradas")
    salas = sala_controller.listar()
    if salas:
        st.dataframe(salas, use_container_width=True, hide_index=True)
    else:
        st.info("Nenhuma sala cadastrada.")

elif menu == "Nova Reserva":
    st.title("Solicitação de reserva")
    usuarios = usuario_controller.listar()
    disciplinas = disc_controller.listar()
    salas = sala_controller.listar()

    if not usuarios or not disciplinas or not salas:
        st.warning("Cadastre usuários, disciplinas e salas antes de criar uma reserva.")
    else:
        with st.form("reserva"):
            professor = st.selectbox("Professor / solicitante", [u["nome"] for u in usuarios])
            disciplina = st.selectbox("Disciplina", [d["nome"] for d in disciplinas])
            tipo_aula = st.selectbox("Tipo de aula", ["Teórica", "Prática", "Laboratório de Informática", "Odontologia", "Auditório", "Outro"])
            alunos = st.number_input("Quantidade de alunos", min_value=1, value=30)
            data = st.date_input("Data")
            inicio = st.time_input("Horário inicial")
            fim = st.time_input("Horário final")
            sala_nomes = [s["nome"] for s in salas]
            sala_nome = st.selectbox("Sala", sala_nomes)

            selecionada = next(s for s in salas if s["nome"] == sala_nome)
            recomendada = sala_controller.recomendar(tipo_aula, alunos, selecionada)

            if recomendada:
                st.info(f"Recomendação: {recomendada['nome']} — {recomendada['tipo']} — capacidade {recomendada['capacidade']}")
            excepcional = recomendada is not None and sala_nome != recomendada["nome"]
            justificativa = ""
            if excepcional:
                justificativa = st.text_area("Justificativa obrigatória para reserva excepcional")

            if st.form_submit_button("Solicitar reserva", type="primary"):
                if fim <= inicio:
                    st.error("O horário final deve ser posterior ao horário inicial.")
                elif excepcional and not justificativa.strip():
                    st.error("Informe a justificativa para a reserva excepcional.")
                elif ag_controller.conflita(sala_nome, str(data), str(inicio), str(fim)):
                    st.error("Já existe uma reserva confirmada ou pendente para essa sala e período.")
                else:
                    ag_controller.criar(professor, disciplina, sala_nome, str(data), str(inicio), str(fim), alunos, justificativa)
                    st.success("Reserva registrada com sucesso.")
                    st.rerun()

elif menu == "Agendamentos":
    st.title("Agendamentos")
    ags = ag_controller.listar()
    if not ags:
        st.info("Nenhum agendamento registrado.")
    else:
        status = st.selectbox("Filtrar status", ["Todos", "Pendente", "Confirmado", "Cancelado"])
        filtrados = ags if status == "Todos" else [a for a in ags if a["status"] == status]
        st.dataframe(filtrados, use_container_width=True, hide_index=True)
        st.divider()
        st.subheader("Cancelar reserva")
        ids = [a["id"] for a in ags if a["status"] != "Cancelado"]
        if ids:
            rid = st.selectbox("ID da reserva", ids)
            if st.button("Cancelar reserva"):
                ag_controller.cancelar(rid)
                st.success("Reserva cancelada. O registro foi preservado no histórico.")
                st.rerun()

elif menu == "Usuários":
    st.title("Usuários")
    with st.form("usuario"):
        nome = st.text_input("Nome")
        perfil = st.selectbox("Perfil", ["Professor", "Coordenador", "Administrador"])
        if st.form_submit_button("Cadastrar usuário", type="primary"):
            if nome.strip():
                usuario_controller.criar(nome, perfil)
                st.success("Usuário cadastrado.")
                st.rerun()
    st.dataframe(usuario_controller.listar(), use_container_width=True, hide_index=True)

elif menu == "Disciplinas":
    st.title("Disciplinas")
    with st.form("disciplina"):
        nome = st.text_input("Nome da disciplina")
        curso = st.text_input("Curso")
        tipo = st.selectbox("Tipo de aula padrão", ["Teórica", "Prática", "Laboratório de Informática", "Odontologia", "Auditório", "Outro"])
        if st.form_submit_button("Cadastrar disciplina", type="primary"):
            if nome.strip() and curso.strip():
                disc_controller.criar(nome, curso, tipo)
                st.success("Disciplina cadastrada.")
                st.rerun()
    st.dataframe(disc_controller.listar(), use_container_width=True, hide_index=True)
