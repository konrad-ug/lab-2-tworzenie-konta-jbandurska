import unittest
from parameterized import parameterized

from ..Konto import Konto

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
        