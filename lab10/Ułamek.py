import sys
import random

class Ułamek:
    # Wersja2 __slots__ = ('licznik', 'mianownik')

    def __init__(self, licznik, mianownik):
        assert mianownik != 0, "Mianownik nie może być równy 0"
        self.licznik = licznik
        self.mianownik = mianownik

    @classmethod
    def from_file(self, plik):
        u = open(plik, "r").readline()
        l, m = u.strip().split('/')
        return Ułamek(l, m)

    def save(self, plik):
        u = open(plik, 'w')
        u.write(str(self.licznik) + '/' + str(self.mianownik))

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __repr__(self):
        return f"Ułamek({self.licznik}, {self.mianownik})"

    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __le__(self, other):
        return self.licznik * other.mianownik <= other.licznik * self.mianownik

    def __eq__(self, other):
        return (self.licznik == other.licznik and self.mianownik == other.mianownik) or (int(self.licznik) % int(other.licznik) == 0 and int(self.mianownik) % int(other.mianownik) == 0) or (other.licznik % int(self.licznik) == 0 and int(other.mianownik) % int(self.mianownik) == 0)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.licznik * other.mianownik > other.licznik * self.mianownik

    def __ge__(self, other):
        return self.licznik * other.mianownik >= other.licznik * self.mianownik

    def __add__(self, other):
        return Ułamek(self.licznik * other.mianownik + other.licznik * self.mianownik, self.mianownik * other.mianownik)

    def __sub__(self, other):
        return Ułamek(self.licznik * other.mianownik - other.licznik * self.mianownik, self.mianownik * other.mianownik)

    def __mul__(self, other):
        return Ułamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        assert other.licznik != 0, "Niepoprawna operacja (dzielenie przez 0)"
        return Ułamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

    def __floordiv__(self, other):
        assert other.licznik != 0, "Niepoprawna operacja (dzielenie przez 0)"
        return (self.licznik * other.mianownik) // (self.mianownik * other.licznik)

    def __mod__(self, other):
        assert other.licznik != 0, "Niepoprawna operacja (dzielenie przez 0)"
        return (self.licznik * other.mianownik) % (self.mianownik * other.licznik)

    def __pow__(self, power):
        return Ułamek(self.licznik ** power, self.mianownik ** power)


