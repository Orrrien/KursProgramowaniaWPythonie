class Ułamek:

    def __init__(self, licznik, mianownik):
        assert mianownik != 0, "Mianownik nie może być równy 0"
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __repr__(self):
        return f"Ułamek({self.licznik}, {self.mianownik})"

    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __le__(self, other):
        return self.licznik * other.mianownik <= other.licznik * self.mianownik

    def __eq__(self, other):
        return (self.licznik == other.licznik and self.mianownik == other.mianownik) or (self.licznik % other.licznik == 0 and self.mianownik % other.mianownik == 0) or (other.licznik % self.licznik == 0 and other.mianownik % self.mianownik == 0)

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



u1 = Ułamek(2, 3)
u2 = Ułamek(6, 7)
u3 = Ułamek(4, 6)
u4 = Ułamek(0, 8)
print(str(u1), str(u2), str(u3), str(u4))
print(repr(u1), repr(u2), repr(u3), repr(u4))
print(f"{u1} < {u3}: {u1 < u3}")
print(f"{u1} <= {u3}: {u1 <= u3}")
print(f"{u1} == {u3}: {u1 == u3}")
print(f"{u1} != {u2}: {u1 != u2}")
print(f"{u1} != {u3}: {u1 != u3}")
print(f"{u1} * {u2} = {u1 * u2}")
print(f"{u1} / {u2} = {u1 / u2}")
print(f"{u1} ** {2} = {u1 ** 2}")
print(f"{u1} / {u4} = {u1 / u4}")

