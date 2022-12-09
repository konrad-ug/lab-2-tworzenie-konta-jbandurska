from app.Konto import Konto
from datetime import date
import requests
import os

bank_api_mf_url = os.environ.get('BANK_APP_MF_URL')

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            if self.czy_nip_istnieje(nip) == None:
                self.nip = "Pranie!"
            else:     # Jeśli nip jest prawdziwy stwórz normalne konto
                self.nazwa_firmy = nazwa_firmy
                self.nip = nip
                self.saldo = 0
                self.oplata = 5
                self.historia = []

    def czy_nip_istnieje(self, nip):
        data = date.today()
        url = f"{bank_api_mf_url}{nip}?date={data}"
        get_resp = requests.get(url)
        resp_body = get_resp.json()

        return resp_body['result']['subject']

    def zaciagnij_kredyt(self, kwota):
        czySaldoDwaRazyWieksze = self.saldo >= kwota*2
        czyPrzelewDoZUS = -1775 in self.historia
        
        if czySaldoDwaRazyWieksze and czyPrzelewDoZUS:
            self.saldo += kwota
            return True
        else:
            return False