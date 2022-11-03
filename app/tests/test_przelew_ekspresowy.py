import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestPrzelewEkspresowy(unittest.TestCase):
    imie = 'darek'
    nazwisko = 'kowalski'
    pesel = '02271901334'

    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def test_udany_przelew_ekspresowy_firma(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        kontoFirmowe.saldo = 1000

        kontoFirmowe.przelew_ekspresowy(700)

        self.assertEqual(kontoFirmowe.saldo, 295, "Nieprawidłowe saldo po wykonaniu przelewu ekspresowego dla firmy!")

    def test_nieudany_przelew_ekspresowy_firma(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        kontoFirmowe.saldo = 100

        kontoFirmowe.przelew_ekspresowy(700)

        self.assertEqual(kontoFirmowe.saldo, 100)

    def test_udany_przelew_ekspresowy_firma_saldo_ponizej_0(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        kontoFirmowe.saldo = 700

        kontoFirmowe.przelew_ekspresowy(700)

        self.assertEqual(kontoFirmowe.saldo, -5)

    def test_udany_przelew_ekspresowy_zwykle_konto(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000

        konto.przelew_ekspresowy(700)

        self.assertEqual(konto.saldo, 299)