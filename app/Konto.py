class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oplata = 1

        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel

        if len(kod) == 8 and kod.startswith("PROM_") and (int(pesel[0:2]) > 60 or 2 <= (int(pesel[2:3])) <= 3):
            self.saldo = 50
        else:
            self.saldo = 0
    
    def zaksieguj_przelew(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota

    def przelew_ekspresowy(self, kwota):
        saldoPrzed = self.saldo

        self.zaksieguj_przelew(kwota)
        
        if self.saldo != saldoPrzed:     # przelew dokonany
            self.saldo -= self.oplata