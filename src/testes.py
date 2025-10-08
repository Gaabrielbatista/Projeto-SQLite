from database import *
from tabulate import tabulate
from utils import limpar_terminal
# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Cria tabela
criar_tabela()
limpar_terminal()
# inserir_carro("  asdasdeq", 1900, "cor aleatória")
# exibir_dados()

atualizar_carro(1, cor="  ")

exibir_dados()
