import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowanie(unittest.TestCase):
    imie = 'darek'
    nazwisko = 'kowalski'
    pesel = '02271901334'
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def test_historia_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 10000
        konto.zaksieguj_przelew_przychodzący(300)
        konto.zaksieguj_przelew_wychodzący(200)
        konto.przelew_ekspresowy(500)

        self.assertListEqual(konto.historia, [300,-200,-500,-1], "Niepoprawna historia")
        
    def test_historia_przelewow_firma(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 10000
        konto.zaksieguj_przelew_przychodzący(300)
        konto.zaksieguj_przelew_wychodzący(200)
        konto.przelew_ekspresowy(500)

        self.assertListEqual(konto.historia, [300,-200,-500,-5], "Niepoprawna historia")