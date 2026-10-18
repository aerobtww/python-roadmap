def add(a: int, b: int) -> int:
    return a + b

def test_add() -> None:
    assert add(2, 3) == 5

def test_add_negative() -> None:
    assert add(-1, 1) == 0


