"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")

livros = dados.ler_livros()

col1, col2, col3 = st.columns(3)

qte_livros = len(livros)
col1.metric("Total de Livros", qte_livros,)

preco_medio = dados.calcular_preco_medio(livros)
col2.metric("Preço Médio", f"£{preco_medio:.2f}")

cinco_estrelas = dados.contar_cinco_estrelas(livros)
col3.metric("Total 5 estrelas", cinco_estrelas)

st.dataframe(livros)

