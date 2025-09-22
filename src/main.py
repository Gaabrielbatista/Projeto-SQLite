from database import *
from tabulate import tabulate
from os import system

system("cls")

# Mostrar tabela
def exibir():
    exibir_dados = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibir_dados)


criar_tabela()
inserir_carro("Honda Civic", 2020, "Prata")
inserir_carro("Audi A6", 2022, "Preto")

exibir()

atualizar_carro(2, modelo="Toyota Corolla")
atualizar_carro(4, cor="Azul")
atualizar_carro(6, ano="2023")

exibir()
