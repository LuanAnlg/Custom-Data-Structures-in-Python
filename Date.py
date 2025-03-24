from Interfaces import Randomizable, Loadable
import random
from datetime import  datetime

class Date(Loadable, Randomizable):
    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        self.year = year
        self.month = month
        self.day = day

    def is_valid(self) -> bool:
        try:
            datetime(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        return f'{self.year}-{self.month:02d}-{self.day:02d}'

    def __repr__(self) -> str:
        return f'Date(year={self.year}, month={self.month}, day={self.day})'

    def __format__(self, format_spec: str) -> str:
        if format_spec == 'save':
            return f'{self.year}-{self.month:02d}-{self.day:02d}'
        if format_spec == 'cvv':
            return f'{self.year}-{self.month:02d}'
        else:
            return f'{self.year}/{self.month:02d}/{self.day:02d}'

    def from_string(self, string: str) -> None:
        try:
            data = string.split('-')
            if len(data) == 3:
                self.year = int(data[0])
                self.month = int(data[1])
                self.day = int(data[2])
                if not self.is_valid():
                    print(f'Invalid date: {string}')
                return
            print(f'The format is incorrect: {string}')
        except ValueError:
            print(f'Error parsing date from string: {string}')

    def generate(self) -> None:
        while not self.is_valid():
            self.year = random.randint(1960, 2006)
            self.month = random.randint(1, 12)
            self.day = random.randint(1, 31)

    def __lt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) < (other.year, other.month, other.day)
        print('Cannot compare Date with non-Date object')

    def __gt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) > (other.year, other.month, other.day)
        print('Cannot compare Date with non-Date object')

def test_date():
    d1 = Date(2020, 5, 10)
    d2 = Date(2021, 6, 15)

    d3 = Date()
    d3.generate()

    print(f'Date 1: {repr(d1)} -> {str(d1)}')
    print(f'Date 2: {repr(d2)} -> {str(d2)}')
    print(f'Random Date 3: {repr(d3)} -> {str(d3)}')
    print(f'Comparison d1 < d2: {d1 < d2}')
    print(f'Comparison d2 > d1: {d2 > d1}')

test_date()