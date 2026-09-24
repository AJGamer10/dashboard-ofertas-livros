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
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num = float(preco_original_limpo)
        soma += preco_num
    return soma/len(livros)

def contar_cinco_estrelas(livros: list):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador += 1
    return contador
 
if __name__ == "__main__":
    livros = ler_livros()
    # print(f"A quantidade de livros da coleção é de {len(livros)} livros.")

    media = calcular_preco_medio(livros)
    print(round(media, 2))