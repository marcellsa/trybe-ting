import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return sys.stderr.write("Formato inválido")
    try:
        with open(path_file, 'r') as txt_file:
            data = txt_file.read().split('\n')
            return data
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    """Aqui irá sua implementação"""
