import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKredyty(unittest.TestCase):

    def setUp(self):
        self.konto = Konto('darek', 'kowalski', '02271901334')

    @parameterized.expand([
        ([-100,100,100,100], 500, True, 500),
        ([-100,100,100,-100], 500, False, 0),
        ([-100,100,200,-100,500], 500, True, 500),
        ([-100,100,-100,100,-500], 500, False, 0),
        ([-100], 500, False, 0)
    ])
    def test_kredyt(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czyUdzielony = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czyUdzielony, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    @parameterized.expand([
        ([-100,-1775,100,100], 500, True, 2000, 2500), 
        ([200,30,900], 500, False, 2000, 2000),
        ([-1775,900,100], 500, False, 750, 750)
    ])
    def test_kredyt_konto_firmowe(self, historia, kwota, oczekiwany_wynik, początkowe_saldo, oczekiwane_saldo):
        konto_firmowe = KontoFirmowe("Januszex sp. z o.o", "8461627563")
        konto_firmowe.historia = historia
        konto_firmowe.saldo = początkowe_saldo

        czyUdzielony = konto_firmowe.zaciagnij_kredyt(kwota)
        self.assertEqual(czyUdzielony, oczekiwany_wynik)
        self.assertEqual(konto_firmowe.saldo, oczekiwane_saldo)
        