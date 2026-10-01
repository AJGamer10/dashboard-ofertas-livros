"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados


def montar_tabela(livros: list):
    tabela = []
    for livro in livros:
        linha = {
            "Titulo": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": livro["nota"] * "⭐️",
            "Preço": f"£{livro["preco"]:.2f}",
            "Faixa": classificar_preco(livro["preco"])
        }
        tabela.append(linha)

    return tabela

def classificar_preco(preco):
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa_dict(livros):
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        contagem[faixa] = contagem[faixa] + 1 if faixa in contagem else 1

    return contagem

def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    # livros_originais = ler_livros()
    livros = dados.carregar_livros()
    tabela = montar_tabela(livros)

    col1, col2, col3, col4, col5 = st.columns(5)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", f"£{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])

    col5.metric(contar_por_faixa_dict["Barato"])

    st.dataframe(tabela)


if __name__ == "__main__":
    main()
