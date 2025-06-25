import os

nomes = ["Fulano", "Ciclano", "Beltrano", "João", "Maria", "Ana", "Pedro"]

# Exibe os nomes com seus índices
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("-" * 60)

try:
    # Entrada do índice a ser separado
    i = int(input("Informe o índice que deseja separar: "))
    
    if i >= 0 and i < len(nomes):
        # Remove o nome da lista e limpa a tela
        nome_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_isolado} separado com sucesso!\n")

        # Exibe a lista atualizada
        for j in range(len(nomes)):
            print(f"{j}: {nomes[j]}")
        print("-" * 60)
    else:
        print("Índice inválido!")

except Exception as e:
    print(f"Não foi possível executar a operação: {e}")


