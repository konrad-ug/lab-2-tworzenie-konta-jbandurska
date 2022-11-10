import unittest

from ..Konto import Konto

class TestKsiegowanie(unittest.TestCase):
    imie = 'darek'
    nazwisko = 'kowalski'
    pesel = '02271901334'

    def test_udzielony_kredyt_ostatnie_3_transakcje(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        kwota = 500

        konto.historia = [-100,100,100,100]

        czyUdzielony = konto.zaciagnij_kredyt(kwota)

        self.assertTrue(czyUdzielony)
        self.assertEqual(konto.saldo, kwota)

    def test_nieudzielony_kredyt_ostatnie_3_transakcje(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        kwota = 500

        konto.historia = [-100,100,-100,100]

        czyUdzielony = konto.zaciagnij_kredyt(kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(konto.saldo, 0)

    def test_udzielony_kredyt_ostatnie_5_transakcji(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        kwota = 500

        konto.historia = [-100,100,100,100,200,200]

        czyUdzielony = konto.zaciagnij_kredyt(kwota)

        self.assertTrue(czyUdzielony)
        self.assertEqual(konto.saldo, kwota)

    def test_nieudzielony_kredyt_ostatnie_5_transakcji(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        kwota = 500

        konto.historia = [-100,100,200,100,-20]

        czyUdzielony = konto.zaciagnij_kredyt(kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(konto.saldo, 0)

    def test_nieudzielony_kredyt_za_malo_transakcji(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        kwota = 500

        konto.historia = [-100]

        czyUdzielony = konto.zaciagnij_kredyt(kwota)

        self.assertTrue(not(czyUdzielony))
        self.assertEqual(konto.saldo, 0)


        