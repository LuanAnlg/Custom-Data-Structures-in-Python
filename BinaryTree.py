from typing import TypeVar, Optional, Generic, Callable
from BinaryNode import BinaryNode

T = TypeVar('T')

class BinaryTree(Generic[T]):
    def __init__(self, process: Callable[[T], None], insert_mode: str = 'Duplicate'):
        self.root: Optional[BinaryNode[T]] = None
        self.process = process
        self.insert_mode = insert_mode

    def _empty(self, node: Optional[BinaryNode[T]]) -> bool:
        return node is None

    def _height(self, node: Optional[BinaryNode[T]]) -> int:
        return 0 if self._empty(node) else node.height

    def _insert(self, node: Optional[BinaryNode[T]], data: T) -> Optional[BinaryNode[T]]:
        if self._empty(node):
            return BinaryNode(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        else:
            if self.insert_mode == 'Duplicate':
                node.right = self._insert(node.right, data)
            else:
                return node
        return node

    def insert(self, data: T) -> None:
        self.root = self._insert(self.root, data)

    def _in_order(self, node: Optional[BinaryNode[T]]) -> None:
        if self._empty(node):
            return
        self._in_order(node.left)
        self.process(node.data)
        self._in_order(node.right)

    def in_order(self) -> None:
        self._in_order(self.root)

    def _pre_order(self, node: Optional[BinaryNode[T]]) -> None:
        if self._empty(node):
            return
        self.process(node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order(self) -> None:
        self._pre_order(self.root)

    def _post_order(self, node: Optional[BinaryNode[T]]) -> None:
        if self._empty(node):
            return
        self._post_order(node.left)
        self._post_order(node.right)
        self.process(node.data)

    def post_order(self) -> None:
        self._post_order(self.root)

    def _to_list(self, node: Optional[BinaryNode[T]], result: list) -> None:
        if self._empty(node):
            return
        self._to_list(node.left, result)
        result.append(node.data)
        self._to_list(node.right, result)

    def to_list(self) -> list:
        result = []
        self._to_list(self.root, result)
        return result

def process(element: int) -> None:
    print(element, end=" ")

def test_binary_tree() -> None:
    tree = BinaryTree(process)

    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(15)

    print("In-order traversal:")
    tree.in_order()  # Salida esperada: 5 10 15 20

    print("\nPre-order traversal:")
    tree.pre_order()  # Salida esperada: 10 5 20 15

    print("\nPost-order traversal:")
    tree.post_order()  # Salida esperada: 5 15 20 10

    print("In-order traversal:")
    print(tree.to_list())  # Salida esperada: [5, 10, 15, 20]

# test_binary_tree()