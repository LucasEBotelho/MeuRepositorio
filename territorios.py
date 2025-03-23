import streamlit as st
import pandas as pd

df = pd.read_excel("dados.xlsx")  # Pandas usará openpyxl automaticamente

st.title("Seleção de Territórios 📍")

bairro = st.selectbox("Escolha um Bairro:", df["Bairro"].unique())
territorio = st.selectbox("Escolha um Território:", df["Territorio"].unique())
quadra = st.selectbox("Escolha uma Quadra:", df["Quadras"].unique())

st.write(f"📌 Você selecionou: **{bairro}**, **{territorio}**, **{quadra}**")
