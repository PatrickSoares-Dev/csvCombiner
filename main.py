import os
import pandas as pd
from csvcombiner.csv_processor import read_csv_files
from tqdm import tqdm

def main():
    folder_path = r'C:\Users\patrick.oliveira\Desktop\BD Ported_Number2'
    output_file = 'unified_ported_numbers.csv'

    # Listar todos os arquivos CSV na pasta
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    print(f"Encontrados {len(csv_files)} arquivos CSV para processar.")

    # Ler os arquivos CSV
    data_frames = read_csv_files(folder_path, csv_files)

    print("Concatenando DataFrames...")

    # Concatenar todos os DataFrames em um único DataFrame
    unified_df = pd.concat(data_frames, ignore_index=True)

    print("Salvando o DataFrame unificado em um novo arquivo CSV...")

    # Salvar o DataFrame unificado em um novo arquivo CSV
    unified_df.to_csv(os.path.join(folder_path, output_file), index=False)

    print(f'Arquivo unificado salvo em: {os.path.join(folder_path, output_file)}')

if __name__ == "__main__":
    main()