import streamlit as st

from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno
#python -m streamlit run app.py
st.set_page_config(page_title= "Gerenciamento de alunos", page_icon= "👩🏻")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.radio("Menu",["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("➕ Inserir alunos")
    nome = st.text_input("Nome", placeholder= "Seu nome")
    idade = st.number_input("Idade", min_value= 16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.seccess(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo não pode ser vazio.")
