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


def remove(instance):
    if len(instance._queue) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        delete = instance.dequeue()
        path_file = delete["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        data_info = instance.search(position)
        print(data_info, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
