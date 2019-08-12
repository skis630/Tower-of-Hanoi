from hanoi_class import Hanoi
from os import path, listdir

def test_program():
    for file in listdir("moves which solve the problem"):
        game = Hanoi(path.join("moves which solve the problem", file))
        assert game.check_if_won() == "YES"

    for file in listdir("invalid input"):
        game = Hanoi(path.join("invalid input", file))
        assert game.check_if_won() == "NO"

    for file in listdir("illegal moves"):
        game = Hanoi(path.join("illegal moves", file))
        assert game.check_if_won() == "NO"

    game = Hanoi("input9.txt")
    assert game.check_if_won() == "NO"

    

