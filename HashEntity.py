from typing import TypeVar, Optional, Generic

T = TypeVar('T')

class HashEntity(Generic[T]):
    def __init__(self, key: Optional[str] = None, data: Optional[T] = None):
        self.key: Optional[str] = key
        self.data: Optional[T] = data


def hash_entity_test() -> None:
    # Test 1: Crear una instancia de HashEntity sin parámetros
    entity1 = HashEntity()
    print(f"Entity 1 - Key: {entity1.key}, Data: {entity1.data}")
    if entity1.key is not None:
        print("Error: key debería ser None por defecto")
    if entity1.data is not None:
        print("Error: data debería ser None por defecto")

    # Test 2: Crear una instancia de HashEntity con solo un key
    entity2 = HashEntity(key="myKey")
    print(f"Entity 2 - Key: {entity2.key}, Data: {entity2.data}")
    if entity2.key != "myKey":
        print("Error: key debería ser 'myKey'")
    if entity2.data is not None:
        print("Error: data debería ser None")

    # Test 3: Crear una instancia de HashEntity con key y data
    entity3 = HashEntity(key="key1", data=42)
    print(f"Entity 3 - Key: {entity3.key}, Data: {entity3.data}")
    if entity3.key != "key1":
        print("Error: key debería ser 'key1'")
    if entity3.data != 42:
        print("Error: data debería ser 42")

    # Test 4: Crear una instancia de HashEntity solo con data
    entity4 = HashEntity(data=100)
    print(f"Entity 4 - Key: {entity4.key}, Data: {entity4.data}")
    if entity4.key is not None:
        print("Error: key debería ser None")
    if entity4.data != 100:
        print("Error: data debería ser 100")

    # Test 5: Iterar sobre las instancias de HashEntity
    print("Iterar sobre las entidades creadas:")
    entities = [entity1, entity2, entity3, entity4]
    for entity in entities:
        print(f"Entity - Key: {entity.key}, Data: {entity.data}")

    print("Todos los tests de HashEntity pasaron correctamente.")  # Si no hubo errores

# hash_entity_test()
