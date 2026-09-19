import streamlit as st

def setup_page():
    st.set_page_config(page_title="ATILA | Gestão de Salas", page_icon="🏫", layout="wide")
    st.markdown("""
    <style>
    .block-container {padding-top: 1.5rem;}
    .atilalogo {
        font-size: 2.2rem; font-weight: 900; letter-spacing: 4px;
        background: linear-gradient(90deg,#2563eb,#06b6d4);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }
    .subtitle {color:#64748b; margin-top:-14px;}
    </style>
    """, unsafe_allow_html=True)

def header():
    st.markdown('<div class="atilalogo">ATILA</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Sistema de Gestão e Agendamento de Salas</div>', unsafe_allow_html=True)
    st.divider()
