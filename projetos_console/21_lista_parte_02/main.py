nomes = [
    "alex",
    "Joana",
    "joao",
    "maria", 
      
]

for nome in nomes:
    print(nome)

novo_nome = input("Informe o nome: ").title().strip()

nomes.append(novo_nome)

for nome in nomes:
    print(nome)     


