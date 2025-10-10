from database import listar_carros, criar_tabela
from tabulate import tabulate
from interface import interface_menu

# Mostra tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Cria tabela
criar_tabela()

if __name__ == "__main__":
    interface_menu()
