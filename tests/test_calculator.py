from calculator.__main__ import add, main, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_cli_add(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_subtract():
    assert subtract(5, 3) == 2


def test_cli_subtract(capsys):
    assert main(["subtract", "5", "3"]) == 0
    assert capsys.readouterr().out.strip() == "2.0"


def test_multiply():
    assert multiply(4, 3) == 12


def test_cli_multiply(capsys):
    assert main(["multiply", "4", "3"]) == 0
    assert capsys.readouterr().out.strip() == "12.0"
