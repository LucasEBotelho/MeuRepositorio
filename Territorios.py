import streamlit as st
import random

st.title("Gerador de Números Aleatórios 🎲")

min_val = st.number_input("Valor mínimo", value=1, step=1)
max_val = st.number_input("Valor máximo", value=100, step=1)

if st.button("Gerar Número"):
    if min_val < max_val:
        num = random.randint(min_val, max_val)
        st.success(f"Número sorteado: {num}")
    else:
        st.error("O valor mínimo deve ser menor que o máximo.")
