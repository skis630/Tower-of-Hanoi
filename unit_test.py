from home_task import read_input
from hanoi_class import Hanoi
from os import path

def test_program():
    game1 = Hanoi(path.join("moves which solve the problem","input1.txt"))
    assert game1.check_if_won() == "YES"

    game2 = Hanoi("input2.txt")
    assert game2.check_if_won() == "YES"

    game3 = Hanoi("input3.txt")
    assert game3.check_if_won() == "NO"

    game4 = Hanoi("input4.txt")
    assert game4.check_if_won() == "NO"

    game5 = Hanoi("input5.txt")
    assert game5.check_if_won() == "NO"

    game6 = Hanoi("input6.txt")
    assert game6.check_if_won() == "NO"

    game7 = Hanoi("input7.txt")
    assert game7.check_if_won() == "NO"

    game8 = Hanoi("input8.txt")
    assert game8.check_if_won() == "NO"

    game9 = Hanoi("input9.txt")
    assert game9.check_if_won() == "NO"

    game10 = Hanoi("no_moves.txt")
    assert game10.check_if_won() == "NO"

    game11 = 



