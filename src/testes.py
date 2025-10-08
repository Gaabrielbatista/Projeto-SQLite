from database import *
from tabulate import tabulate

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Cria tabela
criar_tabela()

inserir_carro("  asdasdeq", 1900, "cor aleatória")
exibir_dados()

atualizar_carro(2, cor="cor aí")

exibir_dados()
