from os.path import exists, getsize
from what_to_eat import get_choice, get_food, save_food


def test_get_choice(monkeypatch):
    # monkeypatch the "input" function, so that it returns what I want.
    monkeypatch.setattr('builtins.input', lambda _: "add")
    assert get_choice() == "add"

    monkeypatch.setattr('builtins.input', lambda _: "eat")
    assert get_choice() == "eat"

    monkeypatch.setattr('builtins.input', lambda _: "del")
    assert get_choice() == "del"

    # not sure how to test timeout of the loop when the input is something else


def test_get_food():
    # if file exists and is not empty, make sure something is returned
    if exists("foodlist.txt") and getsize("foodlist.txt") > 0:
        assert get_food() != None


def test_save_food(tmpdir):
    # create temporary file
    file = tmpdir.mkdir("sub").join("output.txt")
    save_food(file, "Pasta")
    assert file.read() == "Pasta\n"

  