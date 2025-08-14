nomes = [
    "alex",
    "Joana",
    "joao",     
    "maria",
    "pedro",
    "luana",    
    "carlos",
    "ana",
    "fernando",
    "beatriz",
    "lucas",



]

for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}.")


try:
    i = int(input("Informe a posição do nome na lista : "))
    if i >= 0 and i < len(nomes):
         
                del(nomes[i])
                print("Nome excluido com sucesso!")
    else:
        print("Posição invalida.") 

except Exception as e:
    print(f"Não foi possível excluir o nome da lista. {e}.")


finally:
    for i in range(len(nomes)):
        print(f"{i}: {nomes[i]}.")

    ... 

