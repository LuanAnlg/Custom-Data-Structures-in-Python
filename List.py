from typing import TypeVar, Optional, Generic
from Node import Node

T = TypeVar('T')

class List(Generic[T]):
    # Clase interna para el iterador
    class Iterator:
        def __init__(self, list_obj: 'List[T]') -> None:
            self.current = list_obj.head  # Iniciar con el nodo cabeza de la lista

        def __iter__(self) -> 'List.Iterator':
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

    def push_front(self, data: T) -> None:
        node: Node[T] = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.length += 1

    def push_back(self, data: T) -> None:
        node: Node[T] = Node(data)
        if self.empty():
            self.head = self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop_front(self) -> None:
        if self.empty():
            print('You can\'t pop from an empty list')
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1

    def pop_back(self) -> None:
        if self.empty():
            print('You can\'t pop from an empty list')
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            self.tail.next = None
        self.length -= 1

    def front(self) -> Optional[T]:
        if self.empty():
            print('You can\'t access an empty list')
            return None
        return self.head.data

    def back(self) -> Optional[T]:
        if self.empty():
            print('You can\'t access an empty list')
            return None
        return self.tail.data

    def at(self, index: int) -> Optional[T]:
        if self.empty():
            print('You can\'t access an empty list')
            return None
        if index >= self.length:
            print(f'You can\'t access out of bounds [{index}]')
            return None
        if index == 0:
            return self.head.data
        if index == self.length - 1:
            return self.tail.data
        current: Node[T] = self.head
        for i in range(index):
            current = current.next
        return current.data

    def clear(self) -> None:
        while not self.empty():
            self.pop_front()

    def __iter__(self) -> 'List.Iterator':
        return List.Iterator(self)

def list_test() -> None:
    l = List[int]()

    l.push_back(10)
    l.push_back(20)
    l.push_back(30)

    print("Iterar sobre la lista:")
    for value in l:  # Uso del iterador
        print(value)  # Salida: 10, 20, 30

    print(f"Front después de push_back: {l.front()}")  # Salida: 10
    print(f"Back después de push_back: {l.back()}")  # Salida: 30
    print(f"Elemento en índice 0: {l.at(0)}")  # Salida: 10
    print(f"Elemento en índice 2: {l.at(2)}")  # Salida: 30
    print(f"Elemento en índice 3: {l.at(3)}")  # Salida: None (índice fuera de rango)

    l.push_front(5)
    print("Iterar después de push_front:")
    for value in l:  # Uso del iterador
        print(value)  # Salida: 5, 10, 20, 30

    print(f"Front después de push_front: {l.front()}")  # Salida: 5
    print(f"Back después de push_front: {l.back()}")  # Salida: 30

    # Acceso con at
    print(f"Elemento en índice 0: {l.at(0)}")  # Salida: 5
    print(f"Elemento en índice 1: {l.at(1)}")  # Salida: 10
    print(f"Elemento en índice 4: {l.at(4)}")  # Salida: None (índice fuera de rango)

    l.pop_front()
    print("Iterar después de pop_front:")
    for value in l:  # Uso del iterador
        print(value)  # Salida: 10, 20, 30

    print(f"Front después de pop_front: {l.front()}")  # Salida: 10
    print(f"Back después de pop_front: {l.back()}")  # Salida: 30

    l.pop_back()
    print("Iterar después de pop_back:")
    for value in l:  # Uso del iterador
        print(value)  # Salida: 10, 20

    print(f"Back después de pop_back: {l.back()}")  # Salida: 20

    l.clear()
    print("Iterar después de limpiar la lista:")
    for value in l:
        print(value)  # No hay salida porque la lista está vacía

    print(f"¿Lista vacía después de clear? {l.empty()}")  # Salida: True

# list_test()
