import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bd")

def get_file_path(filename: str):
    return os.path.join(DB_PATH, filename)