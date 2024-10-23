import zipfile 
import pandas as pd

def unzip_quarterly_data(file_path, extract_to='../data/raw/'):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped '{file_path}' to '{extract_to}' successfully.")
    except zipfile.BadZipFile:
        print(f"Error: '{file_path}' is not a zip file or it is corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_data(file_path):
    return pd.read_csv(file_path)


