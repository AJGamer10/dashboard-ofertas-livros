# Aula 4: Favoritos: escrita em arquivos e dicionários

## O que vimos hoje
- `st.tabs` para separar o app em abas e `st.button` para reagir a um clique
- Modos do `open`: `"w"` apaga e escreve, `"a"` acrescenta no fim
- `write` e `\n` para escrever em um arquivo de texto
- `csv.DictWriter`, `writeheader` e `writerow` para escrever um CSV
- `.keys()`, `.values()` e `.items()` para percorrer dicionários
- `d[chave] = valor`, `.update()` e `del` para alterar e apagar
- `copia = d` é o **mesmo** dicionário, e `d.copy()` é um dicionário **novo**
- Local × publicado: no Streamlit Cloud, o `favoritos.csv` some quando o app reinicia

## Como rodar
```powershell
.venv\Scripts\Activate.ps1
python aula04/teste_arquivos.py    # teste dos modos "w" e "a"
streamlit run aula04/app.py
```

## Atividade (feita em aula, sem nota)

**Reproduza o que fizemos em aula**
- [ ] Abas **Catálogo** e **Favoritos**, com `mostrar_catalogo` e `mostrar_favoritos`
- [ ] `teste_arquivos.py`: 2 linhas com `"w"`, mesmo rodando de novo, e 4 depois de trocar para `"a"`
- [ ] `salvar_favorito` e `carregar_favoritos` em `dados.py`
- [ ] Botão de adicionar, com aviso quando o livro já está nos favoritos
- [ ] `Sharp Objects` + `Harry Potter and the Deathly Hallows` → **2** favoritos, total de **£ 71.14**
- [ ] `gravar_favoritos` em `dados.py`, com os botões de salvar alterações e remover
- [ ] `aplicar_desconto` com `.copy()`: `Sharp Objects` → **£ 43.04**, e o total continua em **£ 71.14**

**Entrega:** `commit` + `push` com a mensagem `aula 4: favoritos`.
