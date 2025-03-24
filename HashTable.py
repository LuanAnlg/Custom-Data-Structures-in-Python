from typing import TypeVar, Optional, Generic
from HashEntity import HashEntity

T = TypeVar('T')

class HashTable(Generic[T]):
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.length: int = 0
        self.table: list[Optional[HashEntity[T]]] = [None] * self.capacity

    def empty(self) -> bool:
        return self.length == 0

    def hash(self, key: str) -> int:
        hash_value: int = 0
        for c in key:
            hash_value = hash_value * 41 + ord(c)
        return hash_value % self.capacity

    def expand(self) -> None:
        self.capacity *= 2
        new_table: list[Optional[HashEntity[T]]] = [None] * self.capacity
        for entity in self.table:
            if entity is not None:
                index: int = self.hash(entity.key)
                new_table[index] = entity
        self.table = new_table

    def push(self, key: str, data: T) -> None:
        if self.length >= self.capacity * 0.7:
            self.expand()
        index: int = self.hash(key)
        self.table[index] = HashEntity(key, data)
        self.length += 1

    def at(self, key: str) -> Optional[HashEntity[T]]:
        index: int = self.hash(key)
        if self.table[index] is None:
            print(f'This data doesn\'t exist [{key}]')
            return None
        return self.table[index]

    def clear(self) -> None:
        self.table = [None] * self.capacity
        self.length = 0

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        while self._current_index < self.capacity:
            entity = self.table[self._current_index]
            self._current_index += 1
            if entity is not None:
                return entity
        raise StopIteration

def hash_table_test() -> None:
    hash_table = HashTable(10)

    hash_table.push("12345678A", "Juan Pérez")
    hash_table.push("87654321B", "Ana López")
    hash_table.push("11223344C", "Pedro García")

    juan_entity = hash_table.at("12345678A")
    ana_entity = hash_table.at("87654321B")
    non_existent = hash_table.at("00000000Z")

    print(f"Juan Pérez: {juan_entity.data if juan_entity else 'Not found'}")  # Salida: Juan Pérez
    print(f"Ana López: {ana_entity.data if ana_entity else 'Not found'}")  # Salida: Ana López
    print(f"Non-existent: {non_existent}")  # Salida: This data doesn't exist

    hash_table.push("33445566D", "María Sánchez")
    print(f"María Sánchez: {hash_table.at('33445566D').data}")  # Verificar si María Sánchez se insertó correctamente

    print("\nIterando sobre los elementos de la tabla hash:")
    for entity in hash_table:
        print(f"DNI: {entity.key}, Nombre: {entity.data}")

    hash_table.clear()
    print(f"Is table empty after clear? {'Yes' if hash_table.empty() else 'No'}")  # Salida: Yes

# Ejecutar el test
hash_table_test()
