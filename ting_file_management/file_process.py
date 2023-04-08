import sys
from .file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    if data is None:
        return

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    for item in instance.items:
        if item["nome_do_arquivo"] == path_file:
            print(f"File '{path_file}' already processed", file=sys.stdout)
            return

    instance.enqueue(file_info)
    print(file_info, file=sys.stdout)


def remove(instance):
    if not instance:
        print("Não há elementos", file=sys.stdout)
        return

    path_file = instance.items[0]["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
