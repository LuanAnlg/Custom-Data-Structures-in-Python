from typing import TypeVar, Optional, Generic

T = TypeVar('T')

class BinaryNode(Generic[T]):
    def __init__(self, data: T, left: Optional['BinaryNode[T]'] = None, right: Optional['BinaryNode[T]'] = None, height: int = 0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height
