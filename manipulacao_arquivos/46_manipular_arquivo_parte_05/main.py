try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()

    # Leitura do arquivo
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        print(f"Texto gravado:\n{texto}") 

    # Entrada de novo texto
    novo_texto = input("Digite o novo texto:\n: ")
    nova_gravacao = f"{texto}\n{novo_texto}"

    # Gravação no arquivo
    with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
        f.write(nova_gravacao)
    print("Gravação feita com sucesso!")

    # Leitura final do arquivo
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto_final = f.read()
    print(f"Texto final:\n{texto_final}")

except Exception as e:
    print(f"Não foi possível ler ou atualizar o conteúdo: {e}.")
