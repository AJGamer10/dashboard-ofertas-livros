"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    """Lê o arquivo CSV de livros e retorna uma lista de direcionários.

    Returns:
        Lista contendo os dicionários com as informações de cada livro.
    """
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros

def calcular_preco_medio(livros: list):
    soma: float = 0
    for livro in livros:
        preco_num = _limpa_preco(livro["preco"])
        soma += preco_num
    return soma/len(livros)

def contar_cinco_estrelas(livros: list):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador += 1
    return contador

def livro_mais_caro(livros: list):
    titulo_mais_caro: str = ""
    preco_mais_caro: float = 0.0

    for livro in livros:
        preco = _limpa_preco(livro["preco"])
        if preco_mais_caro < preco:
            titulo_mais_caro = livro["titulo"]
            preco_mais_caro = preco

    return titulo_mais_caro, "£"+str(preco_mais_caro)

def _limpa_preco(preco_original: str):
    preco_original_limpo: str = preco_original.replace("£", "")
    return float(preco_original_limpo)

if __name__ == "__main__":
    livros = ler_livros()
    # print(f"A quantidade de livros da coleção é de {len(livros)} livros.")

    media = calcular_preco_medio(livros)
    print(round(media, 2))