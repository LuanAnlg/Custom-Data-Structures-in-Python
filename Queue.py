from typing import TypeVar, Optional, Generic
from Node import Node

T = TypeVar('T')

class Queue(Generic[T]):
    # Clase interna para el iterador
    class Iterator:
        def __init__(self, queue_obj: 'Queue[T]') -> None:
            self.current = queue_obj.head  # Iniciar con el nodo cabeza de la cola

        def __iter__(self) -> 'Queue.Iterator':
            return self  # Retornar el iterador mismo

        def __next__(self) -> T:
            if self.current is None:  # Si no hay más elementos, lanza StopIteration
                raise StopIteration
            value = self.current.data  # Extraer el dato del nodo actual
            self.current = self.current.next  # Moverse al siguiente nodo
            return value

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.length: int = 0

    def empty(self) -> bool:
        return self.length == 0

    def size(self) -> int:
        return self.length

    def front(self) -> Optional[T]:
        if self.empty():
            print('You can\'t access from an empty queue')
            return None
        else:
            return self.head.data

    def back(self) -> Optional[T]:
        if self.empty():
            print('You can\'t access from an empty queue')
            return None
        else:
            return self.tail.data

    def push(self, data: T) -> None:
        node: Node[T] = Node(data, None)
        if self.empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self) -> None:
        if self.empty():
            print('You can\'t pop from an empty queue')
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1

    def clear(self) -> None:
        while not self.empty():
            self.pop()

    def __iter__(self) -> 'Queue.Iterator':
        return Queue.Iterator(self)


# Test actualizado para Queue
def queue_test() -> None:
    q = Queue[int]()

    # Insertar elementos en la cola
    q.push(1)
    q.push(2)
    q.push(3)

    # Mostrar el frente y el fondo de la cola
    print(f"Front después de push: {q.front()}")  # Salida: 1
    print(f"Back después de push: {q.back()}")  # Salida: 3

    # Iterar sobre los elementos de la cola
    print("Iterar sobre la cola después de push:")
    for value in q:  # Uso del iterador
        print(value)  # Salida: 1, 2, 3

    # Hacer pop y verificar el nuevo frente
    q.pop()
    print(f"Front después de pop: {q.front()}")  # Salida: 2

    # Iterar después de pop
    print("Iterar sobre la cola después de pop:")
    for value in q:  # Uso del iterador
        print(value)  # Salida: 2, 3

    # Limpiar la cola
    q.clear()
    print(f"¿La cola está vacía después de clear? {q.empty()}")  # Salida: True

    # Intentar iterar sobre una cola vacía
    print("Iterar sobre la cola después de clear:")
    for value in q:  # No debe haber salida, la cola está vacía
        print(value)

queue_test()
