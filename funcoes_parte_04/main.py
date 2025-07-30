from modulo import limpar_tela, velocidade_media, aceleracao_media

if __name__ == "__main__":
    while True:
        print("1 - Calcular velocidade média.")
        print("2 - Calcular aceleração média.")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()

        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade inicial: ").replace(",", "."))
                    vf = float(input("Informe a velocidade final: ").replace(",", "."))
                    v = velocidade_media(vi, vf)
                    print(f"Velocidade média: {v:.2f}")
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue

            case "2":
                try:
                    vm = float(input("Informe a velocidade média: ").replace(",", "."))
                    t = float(input("Informe o tempo: ").replace(",", "."))
                    if t != 0:
                        a = aceleracao_media(vm, t)
                        print(f"Aceleração média: {a:.2f}")
                    else:
                        print("Erro: o tempo não pode ser zero.")
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue

            case "3":
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida.")

