import unittest, parameterized

from ..Konto import Konto

class TestKredyty(unittest.TestCase):

    def setUp(self):
        self.konto = Konto('darek', 'kowalski', '02271901334')
        self.kwota = 500

    @parameterized.expand([
        ([-100,100,100,100], 500, True, 500),
        ([-200,100,200,100,30], 600, True, 600)
    ])
    def test_udzielony_kredyt_ostatnie_3_transakcje(self, historia, kwota, oczekiwanyWynik, saldo):
        self.konto.historia = historia
        czyUdzielony = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czyUdzielony, oczekiwanyWynik)
        self.assertEqual(self.konto.saldo, saldo)

    def test_nieudzielony_kredyt_ostatnie_3_transakcje(self):
        self.konto.historia = [-100,100,-100,100]

        czyUdzielony = self.konto.zaciagnij_kredyt(self.kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(self.konto.saldo, 0)

    def test_udzielony_kredyt_ostatnie_5_transakcji(self):
        self.konto.historia = [-100,100,300,-100,200,200]

        czyUdzielony = self.konto.zaciagnij_kredyt(self.kwota)

        self.assertTrue(czyUdzielony)
        self.assertEqual(self.konto.saldo, self.kwota)

    def test_nieudzielony_kredyt_ostatnie_5_transakcji(self):
        self.konto.historia = [-100,100,200,100,-20]

        czyUdzielony = self.konto.zaciagnij_kredyt(self.kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(self.konto.saldo, 0)

    def test_nieudzielony_kredyt_za_malo_transakcji(self):
        self.konto.historia = [-100]

        czyUdzielony = self.konto.zaciagnij_kredyt(self.kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(self.konto.saldo, 0)


        