import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    for i in instance._queue:
        if i["nome_do_arquivo"] != path_file:
            instance.enqueue(data)
    if len(instance._queue) == 0:
        instance.enqueue(data)
    print(data, file=sys.stdout)
    """Aqui irá sua implementação"""


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
