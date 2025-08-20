import os 
import datetime
from datetime import date

data = date.today().strftime("%d/$m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

# Lista de filmes com suas classificações e salas
filmes = {
    1: {"nome": "A Roda Quadrada", "classificacao": 0},
    2: {"nome": "A Volta dos Que Não Foram", "classificacao": 12},
    3: {"nome": "Poeira em Alto Mar", "classificacao": 14},
    4: {"nome": "As Tranças do Rei Careca", "classificacao": 16},
    5: {"nome": "A Vingança do Peixe Frito", "classificacao": 18}
}

# Entrada do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Loop para exibir o menu até que o usuário escolha um filme adequado
while True:
    print("\n=== MENU DE FILMES ===")
    for sala, info in filmes.items():
        classificacao = "Livre" if info["classificacao"] == 0 else f"{info['classificacao']} anos"
        print(f"Sala {sala}: {info['nome']} - {classificacao}")

    try:
        escolha = int(input("\nDigite o número da sala do filme que deseja assistir: "))
        if escolha not in filmes:
            print("Sala inválida. Escolha uma sala entre 1 e 5.")
            continue
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    filme_escolhido = filmes[escolha]
    if idade >= filme_escolhido["classificacao"]:
        agora = datetime.datetime.now()
        print("\n=== INGRESSO ===")
        print(f"Nome: {nome}")
        print(f"Filme: {filme_escolhido['nome']}")
        print(f"Sala: {escolha}")
        print(f"Data e hora da compra: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
        print("Bom filme!😁")
        break
    else:
        print("\nVocê não tem idade suficiente para assistir a este filme.")
        print("Por favor, escolha outro filme.")






