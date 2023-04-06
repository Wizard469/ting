import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r") as f:
            if path_file.endswith(".txt"):
                lines = f.read().splitlines()
                return lines
            else:
                print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
