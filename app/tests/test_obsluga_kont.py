import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "Nick",
        "nazwisko": "Cave",
        "pesel": "01292909876"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body['nazwisko'], self.body['nazwisko'])
        self.assertEqual(resp_body['imie'], self.body['imie'])
        self.assertEqual(resp_body['saldo'], 0)
