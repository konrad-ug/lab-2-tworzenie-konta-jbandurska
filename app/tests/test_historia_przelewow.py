import unittest
from datetime import date
from unittest.mock import patch, MagicMock
from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from ..SMTPConnection import SMTPConnection

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
        
    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje')
    def test_historia_przelewow_firma(self, mock_konto_firmowe):
        mock_konto_firmowe.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 10000
        konto.zaksieguj_przelew_przychodzący(300)
        konto.zaksieguj_przelew_wychodzący(200)
        konto.przelew_ekspresowy(500)

        self.assertListEqual(konto.historia, [300,-200,-500,-5], "Niepoprawna historia")

    def test_wysyłanie_maila_z_historia(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzący(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("fakemail@mail.com", smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Twoja historia konta to: {konto.historia}","fakemail@mail.com")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=True)
    def test_wysyłanie_maila_z_historia_firma(self, mock_konto_firmowe):
        mock_konto_firmowe.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzący(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("fakemail@mail.com", smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Historia konta Twojej firmy to: {konto.historia}","fakemail@mail.com")

    def test_wysyłanie_maila_z_historia_nieudane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzący(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_maila("fakemail@mail.com", smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Twoja historia konta to: {konto.historia}","fakemail@mail.com")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=True)
    def test_wysyłanie_maila_z_historia_firma_nieudane(self, mock_konto_firmowe):
        mock_konto_firmowe.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzący(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_maila("fakemail@mail.com", smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today()}", f"Historia konta Twojej firmy to: {konto.historia}","fakemail@mail.com")