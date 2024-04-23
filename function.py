import csv
import shutil
import os

def extrair_filmes():
    input_file = input("Digite o caminho completo do arquivo CSV: ")
    nome_saida = input("Digite o nome do arquivo de saída (sem extensão): ") + '.txt'
    output_file = f'saida/{nome_saida}'  # Arquivo de saída com nome customizado

    # Corrige o nome do arquivo de entrada para usar na cópia
    filename = os.path.basename(input_file)

    # Copiar o arquivo original para a pasta entrada
    shutil.copy(input_file, os.path.join('entrada', filename))

    # Processar o arquivo
    coluna = int(input("Digite o número da coluna para extrair (começando de 1): ")) - 1
    titulos = []
    with open(os.path.join('entrada', filename), 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pula a primeira linha
        for row in reader:
            if coluna < len(row):
                titulos.append(row[coluna].strip('"'))

    remover_duplicatas = input("Deseja remover nomes duplicados? (sim/não): ")
    if remover_duplicatas.lower() == 'sim':
        titulos = list(set(titulos))

    titulos.sort()

    numerar = input("Deseja numerar a lista? (sim/não): ")
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, title in enumerate(titulos, start=1):
            if numerar.lower() == 'sim':
                file.write(f"{i}. {title}\n")
            else:
                file.write(f"{title}\n")

    print(f"Arquivo processado com sucesso e salvo em '{output_file}'")
