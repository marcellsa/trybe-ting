import pytest
from ting_file_management.priority_queue import PriorityQueue

stunt = [
    {
        "nome_do_arquivo": "arquivo_de_teste_1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linhas do arquivo 1"]
    },
    {
        "nome_do_arquivo": "arquivo_de_teste_2.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": ["linhas do arquivo 2"]
    },
    {
        "nome_do_arquivo": "arquivo_de_teste_3.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["linhas do arquivo 3"]
    }
]


def test_basic_priority_queueing():
    queue = PriorityQueue()
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(len(queue))

    assert queue.is_priority(stunt[0]) is True
    assert queue.is_priority(stunt[1]) is False
    assert queue.is_priority(stunt[2]) is False

    queue.enqueue(stunt[0])
    queue.enqueue(stunt[1])
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 1

    assert queue.search(0) == stunt[0]

    queue.dequeue()
    assert len(queue.high_priority) == 0
    """Aqui irá sua implementação"""
