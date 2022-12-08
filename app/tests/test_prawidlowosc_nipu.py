import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

class TestObslugaKont(unittest.TestCase):
    # @patch('module.KontoFirmowe')
    def test_1_prawidlowy_nip(self):
        konto_firmowe = KontoFirmowe("KONRAD SOŁTYS", "8461627563")
        self.assertEqual(konto_firmowe.nip, "8461627563")

    def test_2_nieprawidlowy_nip(self):
        konto_firmowe = KontoFirmowe("gzegzolka", "0000000000")
        self.assertEqual(konto_firmowe.nip, "Pranie!")


