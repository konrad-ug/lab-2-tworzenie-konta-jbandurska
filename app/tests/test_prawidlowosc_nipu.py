import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

class TestPrawidlowoscNipu(unittest.TestCase):
    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=True)
    def test_1_prawidlowy_nip(self, mock_konto_firmowe):
        konto_firmowe = KontoFirmowe("KONRAD SOŁTYS", "8461627563")
        self.assertEqual(konto_firmowe.nip, "8461627563")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=None)
    def test_2_nieprawidlowy_nip(self, mock_konto_firmowe):
        konto_firmowe = KontoFirmowe("gzegzolka", "0000000000")
        self.assertEqual(konto_firmowe.nip, "Pranie!")


