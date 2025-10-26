import os
import pandas as pd
import requests

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_csv(data, filepath, sep=';'):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8-sig", sep=sep)

def download_file(url, path):
    resp = requests.get(url)
    with open(path, 'wb') as f:
        f.write(resp.content)
