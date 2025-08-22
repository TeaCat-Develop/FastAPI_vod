# def add(a: int, b: int) -> int:
#     return a + b

# def mul(a: int, b: int) -> int:
#     return a * b


async def test_abc() -> None:
    print("abc")


def main() -> None:
    print("hihi")


def test_simple() -> None:
    print("abc")

from day1 import add
def test_add() -> None:
    # Given
    a, b = 1, 1

    # When
    result = test_add(a, b)

    # Then
    assert result == 2