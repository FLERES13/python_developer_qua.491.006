cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte", 
    "Curitiba",
    "Porto Alegre",
    "Salvador",

]

for i in range(len(cidades)):
    print(f"Indice: {i} - Cidade: {cidades[i]}.")


try: 

    nova_cidade = input("Informe o nome da cidade: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir: "))

    if i >0 and i <= len(cidades):

        cidades.insert(i,nova_cidade)
        print("Cidade inserida com sucesso!")


        
    else:
        print("indice incorreto.")
            
except Exception as e:
    print(f"Nome foi possivel inserir item na lista. {e}.")

finally:
    for i in range(len(cidades)):
        print(f"Indice: {i} - Cidade: {cidades[i]}.")
    ...


