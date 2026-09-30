"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados


def main():
    st.set_page_config(layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.ler_livros()

    col1, col2, col3, col4 = st.columns(4)

    qte_livros = len(livros)
    col1.metric("Total de Livros", qte_livros,)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço Médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Total 5 estrelas", cinco_estrelas)

    titulo_livro_mais_caro, preco_livro_mais_caro = dados.livro_mais_caro(livros)
    col4.metric(f"Livro mais caro:", preco_livro_mais_caro, delta_description=f"{titulo_livro_mais_caro}")

    st.dataframe(livros)

if __name__ == "__main__":
    main()

