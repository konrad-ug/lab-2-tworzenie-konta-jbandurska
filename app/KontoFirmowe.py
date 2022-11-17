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

    def zaciagnij_kredyt(self, kwota):
        czySaldoDwaRazyWieksze = self.saldo >= kwota*2
        czyPrzelewDoZUS = -1775 in self.historia
        
        if czySaldoDwaRazyWieksze and czyPrzelewDoZUS:
            self.saldo += kwota
            return True
        else:
            return False