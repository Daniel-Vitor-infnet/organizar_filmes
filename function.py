import csv
import shutil
import os

def extrair_filmes():
    input_file = input("Digite o caminho completo do arquivo CSV: ")
    nome_saida = input("Digite o nome do arquivo de saída (sem extensão): ") + '.txt'
    output_file = f'saida/{nome_saida}'

    filename = os.path.basename(input_file)
    shutil.copy(input_file, os.path.join('entrada', filename))

    escolha_coluna = input("Digite o número da coluna ou o nome dela para extrair: ")
    coluna = None

    # Processar o arquivo
    titulos = []
    with open(os.path.join('entrada', filename), 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        if escolha_coluna.isdigit():
            coluna = int(escolha_coluna) - 1
        else:
            if escolha_coluna in cabecalho:
                coluna = cabecalho.index(escolha_coluna)
        
        if coluna is None or coluna >= len(cabecalho):
            print("Coluna inválida.")
            return

        for row in reader:
            if coluna < len(row):
                titulos.append(row[coluna].strip('"'))

    count_total = len(titulos)
    titulos = list(set(titulos))
    count_duplicadas = count_total - len(titulos)

    titulos.sort()

    numerar = input("Deseja numerar a lista? (sim/não): ")
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, title in enumerate(titulos, start=1):
            if numerar.lower() == 'sim':
                file.write(f"{i}. {title}\n")
            else:
                file.write(f"{title}\n")

    print(f"Arquivo processado com sucesso e salvo em '{output_file}'")
    print(f"Inicialmente tinha {count_total} filmes/séries.")
    print(f"Foram removidos {count_duplicadas} filmes/séries duplicados.")
    print(f"Agora o total de filmes/séries é {len(titulos)}.")

def combinar_arquivos():
    # Solicita ao usuário os nomes dos arquivos
    file1_path = input("Digite o caminho do primeiro arquivo .txt: ")
    file2_path = input("Digite o caminho do segundo arquivo .txt: ")
    output_filename = input("Digite o nome do arquivo de saída (sem extensão): ") + '.txt'
    output_file = f'saida/{output_filename}'

    # Lê os arquivos e combina as listas
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        list1 = file1.read().splitlines()
        list2 = file2.read().splitlines()

    # Combina e remove duplicatas usando conjuntos
    combined_list = sorted(set(list1 + list2))

    # Escreve o resultado no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in combined_list:
            file.write(f"{item}\n")

    print(f"Arquivos combinados com sucesso. O arquivo resultante '{output_filename}' foi salvo em 'saida/'.")

