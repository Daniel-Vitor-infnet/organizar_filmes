from function import extrair_filmes

def main():
    print("Selecione a funcionalidade:")
    print("1. Extrair filmes")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        extrair_filmes()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
