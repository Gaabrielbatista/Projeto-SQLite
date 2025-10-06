from database import *
from tabulate import tabulate
from os import system

system("cls")

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...\n ")

# Cria tabela
criar_tabela()

inserir_carro(' a', 1901, "    asdfsda")

exibir_dados()