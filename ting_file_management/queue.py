from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = list()

    def __len__(self):
        # quando pedido o tamanho do array
        # retonar o tamanho da fila
        return len(self._queue)

    def enqueue(self, value):
        return self._queue.append(value)

    def dequeue(self):
        # se não houver mais itens na fila, o método retornará None
        if len(self._queue) == 0:
            return None
        # o método pop removerá e retornará o valor do índice fornecido
        return self._queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]
