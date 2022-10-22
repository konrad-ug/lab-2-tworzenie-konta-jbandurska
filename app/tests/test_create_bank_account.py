import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "12345678910"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "brak peselu")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_niepoprawny_pesel(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "123456789"

        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Podano nieprawidłowy pesel i został on zaakceptowany")

    def test_poprawny_kod(self):
        kod = "PROM_123"

        pierwsze_konto = Konto('imie', 'nazwisko', '90115678910', kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Poprawny kod nie dał promocji")

    def test_niepoprawny_kod(self):
        kod = "POM_123"

        pierwsze_konto = Konto('imie', 'nazwisko', '12345678910', kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Niepoprawny kod dał promocję")

    def test_brak_kodu(self):
        pierwsze_konto = Konto('imie', 'nazwisko', '12345678910')
        self.assertEqual(pierwsze_konto.saldo, 0, "Brak kodu dał promocję")

    def test_niesenior_promocja(self):
        pesel = '02272378910'
        konto = Konto('imie', 'nazwisko', pesel, 'PROM_KGV')

        self.assertEqual(konto.saldo, 50, "Niesenior nie dostał promocji")

    def test_senior_promocja(self):
        pesel = '59042378910'
        konto = Konto('imie', 'nazwisko', pesel, 'PROM_KGV')

        self.assertEqual(konto.saldo, 0, "Senior dostał promocję")