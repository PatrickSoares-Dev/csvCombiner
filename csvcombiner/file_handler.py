import os

def list_csv_files(folder_path):
    """
    Lista todos os arquivos CSV no diretório especificado.

    Args:
        folder_path (str): Caminho para o diretório contendo arquivos CSV.

    Returns:
        list: Lista de nomes de arquivos CSV.
    """
    return [f for f in os.listdir(folder_path) if f.endswith('.csv')]