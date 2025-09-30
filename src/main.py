from database import *
from tabulate import tabulate
from os import system

system("cls")

# Mostrar tabela
def exibir_dados():
    exibição = (tabulate(listar_carros(), tablefmt='fancy_grid', headers=['ID', 'Modelo', 'Ano', 'Cor']))
    print(exibição)

# Pausar para visualização
def pausar():
    input("Pressione Enter... ")

criar_tabela()
inserir_carro('Fiat Uno', 2010, 'Prata'),
inserir_carro('Chevrolet Onix', 2022, 'Preto'),
inserir_carro('Volkswagen Gol', 2015, 'Branco'),
inserir_carro('Honda Civic', 2018, 'Azul'),
inserir_carro('Toyota Corolla', 2021, 'Cinza'),
inserir_carro('Ford Ka', 2017, 'Vermelho'),
inserir_carro('Renault Sandero', 2019, 'Verde'),
inserir_carro('Hyundai HB20', 2020, 'Branco'),
inserir_carro('Jeep Compass', 2023, 'Preto'),
inserir_carro('Nissan March', 2014, 'Amarelo');

exibir_dados()

pausar()

atualizar_carro(2, modelo="Toyota Corolla")
atualizar_carro(4, cor="Azul")
atualizar_carro(1, cor= 1234,ano="2023", modelo="Um modelo aí")

exibir_dados()
