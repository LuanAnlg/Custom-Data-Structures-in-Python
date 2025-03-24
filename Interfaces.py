class Fileable:
    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

class Randomizable:
    def generate(self) -> None:
        pass

class Interactable:
    def interact(self) -> None:
        pass
class Loadable:
    def from_string(self, string: str) -> None:
        pass