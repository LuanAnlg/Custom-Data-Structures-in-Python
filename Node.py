from typing import TypeVar, Optional, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T, next: Optional['Node[T]'] = None):
        self.data = data
        self.next = next

def snode_test() -> None:
    # Crear nodos de tipo entero
    nodo3 = Node(3)
    nodo2 = Node(2, nodo3)
    nodo1 = Node(1, nodo2)

    # Mostrar la lista
    actual = nodo1
    while actual:
        print(actual.data, end=" -> ")
        actual = actual.next
    print("None")

# snode_test()
