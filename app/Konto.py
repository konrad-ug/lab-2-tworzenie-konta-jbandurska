class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.historia = []
        self.oplata = 1

        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel

        if len(kod) == 8 and kod.startswith("PROM_") and (int(pesel[0:2]) > 60 or 2 <= (int(pesel[2:3])) <= 3):
            self.saldo = 50
        else:
            self.saldo = 0
    
    def zaksieguj_przelew_przychodzący(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def zaksieguj_przelew_wychodzący(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota
            self.historia.append(-kwota)


    def przelew_ekspresowy(self, kwota):
        saldoPrzed = self.saldo

        self.zaksieguj_przelew_wychodzący(kwota)
        
        if self.saldo != saldoPrzed:     # przelew dokonany
            self.saldo -= self.oplata
            self.historia.append(-self.oplata)

    def czy_ostatnie_3_wplywy(self):  
        czyDodatnie = True
        for el in self.historia[-3:]:
            if el <= 0:
                czyDodatnie = False 

        return len(self.historia) >= 3 and czyDodatnie     

    def czy_suma_5_ostatnich_wieksza_niz_kwota(self, kwota):
        return len(self.historia) >= 5 and sum(self.historia[-5:]) > kwota

    def zaciagnij_kredyt(self, kwota):
        if self.czy_ostatnie_3_wplywy() or self.czy_suma_5_ostatnich_wieksza_niz_kwota(kwota):
            self.saldo += kwota
            return True
        else: 
            return False
        
