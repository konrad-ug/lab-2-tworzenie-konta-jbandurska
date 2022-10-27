import unittest

from ..KontoFirmowe import KontoFirmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def test_tworzenie_konta(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, self.nip)

        self.assertEqual(kontoFirmowe.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie została zapisana!")
        self.assertEqual(kontoFirmowe.nip, self.nip, "Nip nie został zapisany!")
        self.assertEqual(kontoFirmowe.saldo, 0, "Saldo nie jest zerowe!")

    def test_zbyt_dlugi_nip(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, self.nip + "0")

        self.assertEqual(kontoFirmowe.nip, "Niepoprawny NIP!", "Niepoprawny NIP!")


    def test_zbyt_krotki_nip(self):
        kontoFirmowe = KontoFirmowe(self.nazwa_firmy, "0")

        self.assertEqual(kontoFirmowe.nip, "Niepoprawny NIP!", "Niepoprawny NIP!")