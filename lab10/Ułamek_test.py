import pytest
from unittest.mock import mock_open

from Ułamek import Ułamek

@pytest.mark.parametrize("licznik, mianownik, ułamek", [[2, 3, Ułamek(2, 3)], [8, 10, Ułamek(8, 10)], [1, 1, Ułamek(1, 1)]])
def test_stwórz(licznik, mianownik, ułamek):
     assert Ułamek(licznik, mianownik) == ułamek

@pytest.fixture
def mock_answer():
    return Ułamek(2, 3)

def test_ulamek_wczyt(mock_answer):
        mock_data = '2/3'
        m = mock_open(read_data=mock_data)

        with pytest.MonkeyPatch.context() as mpatch:
            mpatch.setattr("builtins.open", m)
            result = Ułamek.from_file("dummy.txt")

        m.assert_called_once_with("dummy.txt", 'r')

        assert result == mock_answer

def test_ulamek_zap(mock_answer):
    mock_data = '2/3'
    m = mock_open()

    with pytest.MonkeyPatch.context() as mpatch:
        mpatch.setattr("builtins.open", m)
        u = Ułamek(2, 3)
        u.save("dummy.txt")
        result = m.read("dummy.txt")

    m.assert_called_once_with("dummy.txt", 'r+')

    assert result == mock_data