
nomes = []

while True:
    print("MENU DE CADASTRO DE NOMES")
    print("1. Cadastrar nome")
    print("2. liste todos os nomes na lista")           
    print("3. Pesquise por um nome na lista")
    print("4. Altere um nome na lista")
    print("5. Exclua um nome da lista")
    print("6. Sair do programa")


    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        novo_nome = input("Informe o nome: ").title().strip()
        nomes.append(novo_nome)
        print(f"{novo_nome} foi adicionado à lista.")
    elif opcao == "2":
        print("Lista de nomes:")
        for nome in nomes:
            print(nome)
    elif opcao == "3":
        nome_pesquisa = input("Informe o nome a pesquisar: ").title().strip()
        if nome_pesquisa in nomes:
            print(f"{nome_pesquisa} está na lista.")
        else:
            print(f"{nome_pesquisa} não foi encontrado na lista.")
    elif opcao == "4":
        nome_antigo = input("Informe o nome a alterar: ").title().strip()
        if nome_antigo in nomes:
            novo_nome = input("Informe o novo nome: ").title().strip()
            index = nomes.index(nome_antigo)
            nomes[index] = novo_nome
            print(f"{nome_antigo} foi alterado para {novo_nome}.")
        else:
            print(f"{nome_antigo} não foi encontrado na lista.")
    elif opcao == "5":
        nome_excluir = input("Informe o nome a excluir: ").title().strip()
        if nome_excluir in nomes:
            nomes.remove(nome_excluir)
            print(f"{nome_excluir} foi excluído da lista.")
        else:
            print(f"{nome_excluir} não foi encontrado na lista.")
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")