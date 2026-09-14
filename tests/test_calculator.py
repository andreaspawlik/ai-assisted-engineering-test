from calculator.__main__ import add, main


def test_add():
    assert add(2, 3) == 5


def test_cli_add(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"
