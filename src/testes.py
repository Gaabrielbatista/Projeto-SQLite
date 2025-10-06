from database import *
from utils import pausar
from tabulate import tabulate

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

pausar()

# Mostra tabela
exibir_dados()

# Pausa para visualização
def pausar():
    input("\nPressione Enter para continuar...\n ")


# Cria tabela
criar_tabela()

inserir_carro("carro_teste", 2024, "")

exibir_dados()
pausar()

atualizar_carro(1, modelo="outro aí")