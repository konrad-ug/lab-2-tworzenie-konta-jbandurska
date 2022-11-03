from app.Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip
        self.saldo = 0
        self.oplata = 5
        self.historia = []

        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"