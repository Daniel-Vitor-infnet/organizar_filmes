from function import extrair_filmes, combinar_arquivos

import os
import glob
def main():
    # Limpar arquivos na pasta entrada
    files = glob.glob('entrada/*')
    for f in files:
        os.remove(f)
    
    print("Selecione a funcionalidade:")
    print("1. Extrair filmes")
    print("2. Combinar arquivos")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        extrair_filmes()
    elif opcao == '2':
        combinar_arquivos()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
