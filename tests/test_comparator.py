from src.core.comparator import ResponseComparator


def test_display_does_not_crash(capsys):
    results = {
        "ModelA": "Hello",
        "ModelB": "World"
    }

    ResponseComparator.display(results)

    captured = capsys.readouterr()
    assert "ModelA" in captured.out
    assert "ModelB" in captured.out
