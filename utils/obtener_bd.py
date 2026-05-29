import os


# os.path.dirname -> devuelve el directorio padre del archivo actual
# os.path.abspath(__file__) -> devuelve la ruta absoluta del archivo actual
# os.path.join -> une partes de una ruta de manera segura, teniendo en cuenta el sistema operativo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bd")

def get_file_path(filename: str):
    return os.path.join(DB_PATH, filename)