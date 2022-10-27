import unittest

from ..Konto import Konto

class TestKsiegowanie(unittest.TestCase):
    imie = 'darek'
    nazwisko = 'kowalski'
    pesel = '02271901334'

    def test_udany_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew(200)

        self.assertEqual(konto.saldo, 800, "Saldo po przelewie się nie zgadza")

    def test_niewystarczające_środki_przelew(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.zaksieguj_przelew(200)

        self.assertEqual(konto.saldo, 100, "Przelew został wykonany pomimo niewystarczających środków")