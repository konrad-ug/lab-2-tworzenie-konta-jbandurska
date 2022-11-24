import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.konto = Konto('darek', 'kowalski', '02271901334')
        RejestrKont.dodaj_konto(cls.konto)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []


    def test_dodaj_drugie_konto(self):
        RejestrKont.dodaj_konto(self.konto)

        self.assertEqual(RejestrKont.lista[1], self.konto)

    def test_znajdz_konto(self):
        znalezione_konto = RejestrKont.wyszukaj_konto_z_peselem(self.konto.pesel)

        self.assertEqual(znalezione_konto, self.konto)

    def test_nieudane_znajdz_konto(self):
        znalezione_konto = RejestrKont.wyszukaj_konto_z_peselem('02271901335')

        self.assertIsNone(znalezione_konto)

    def test_ilosc_kont_w_rejestrze(self):
        RejestrKont.dodaj_konto(self.konto)

        self.assertEqual(RejestrKont.ile_kont(), 3)