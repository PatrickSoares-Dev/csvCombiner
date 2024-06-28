import os
import pandas as pd
import chardet
from tqdm import tqdm

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def read_csv_files(folder_path, csv_files):
    data_frames = []
    for file in tqdm(csv_files, desc="Lendo arquivos CSV"):
        file_path = os.path.join(folder_path, file)
        encoding = detect_encoding(file_path)
        try:
            df = pd.read_csv(file_path, encoding=encoding)
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_path}: {e}")
            continue
        data_frames.append(df)
    return data_frames