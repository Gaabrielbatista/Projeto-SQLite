from database import criar_tabela, inserir_carro, listar_carros
from tabulate import tabulate
from os import system

system("cls")

criar_tabela()
inserir_carro("Honda Civic", 2020, "Prata")
inserir_carro("Audi A6", 2022, "Preto")

exibir_dados = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
print(exibir_dados)
