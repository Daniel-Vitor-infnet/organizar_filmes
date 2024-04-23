from function import extrair_filmes
import os
import glob

def main():
    # Limpar arquivos na pasta entrada
    files = glob.glob('entrada/*')
    for f in files:
        os.remove(f)
    
    print("Selecione a funcionalidade:")
    print("1. Extrair filmes")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        extrair_filmes()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
