cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",       
    "Curitiba",
    "Porto Alegre",
    "Salvador",
    "Brasília",
    "Fortaleza",
    "São Paulo",
    "Rio de Janeiro",
    "Curitiba",
    "Brasília",
]

cidade_pesquisada = input("Infome o nome da cidade: ").title().strip()

quantidade = cidades.count(cidade_pesquisada)

print(f"{cidade_pesquisada} foi encontrada {quantidade} vezes na lista :")


