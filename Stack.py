from typing import TypeVar, Optional, Generic
from Node import Node

T = TypeVar('T')

class Stack(Generic[T]):
    # Clase interna para el iterador
    class Iterator:
        def __init__(self, stack_obj: 'Stack[T]') -> None:
            self.current = stack_obj.head  # Iniciar con el nodo cabeza de la pila

        def __iter__(self) -> 'Stack.Iterator':
            return self  # Retornar el iterador mismo

        def __next__(self) -> T:
            if self.current is None:  # Si no hay más elementos, lanza StopIteration
                raise StopIteration
            value = self.current.data  # Extraer el dato del nodo actual
            self.current = self.current.next  # Moverse al siguiente nodo
            return value

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.length: int = 0

    def empty(self) -> bool:
        return self.length == 0

    def size(self) -> int:
        return self.length

    def top(self) -> Optional[T]:
        if self.empty():
            print('You can\'t access from an empty stack')
            return None
        else:
            return self.head.data

    def push(self, data: T) -> None:
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self) -> None:
        if self.empty():
            print('You can\'t pop from an empty stack')
        else:
            self.head = self.head.next
            self.length -= 1

    def clear(self) -> None:
        while not self.empty():
            self.pop()

    def __iter__(self) -> 'Stack.Iterator':
        return Stack.Iterator(self)


# Test actualizado para Stack
def stack_test() -> None:
    stack = Stack[int]()

    # Insertar elementos en la pila
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Mostrar el top de la pila
    print(f"Top después de push: {stack.top()}")  # Salida: 3

    # Iterar sobre los elementos de la pila
    print("Iterar sobre la pila después de push:")
    for value in stack:  # Uso del iterador
        print(value)  # Salida: 3, 2, 1

    # Hacer pop y verificar el nuevo top
    stack.pop()
    print(f"Top después de pop: {stack.top()}")  # Salida: 2

    # Iterar después de pop
    print("Iterar sobre la pila después de pop:")
    for value in stack:  # Uso del iterador
        print(value)  # Salida: 2, 1

    # Limpiar la pila
    stack.clear()
    print(f"¿La pila está vacía después de clear? {stack.empty()}")  # Salida: True

    # Intentar iterar sobre una pila vacía
    print("Iterar sobre la pila después de clear:")
    for value in stack:  # No debe haber salida, la pila está vacía
        print(value)

# stack_test()
