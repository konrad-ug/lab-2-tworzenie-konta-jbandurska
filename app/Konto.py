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

    def zaciagnij_kredyt(self, kwota):
        length = len(self.historia)

        # Czy 3 ostatnie przelewy są wpływami - warunek 1
        czyDodatnie = True
        for el in self.historia[-3:]:
            if el <= 0:
                czyDodatnie = False

        # Czy długość historii przynajmniej 5 i czy suma 5 ostanich większa niż kwota - warunek 2
        suma = (length >= 5 and sum(self.historia[-5:]) > kwota)

        # Jeśli warunek 1 lub 2 spełniony zwiększ saldo
        if length >= 3 and (czyDodatnie or suma):
            self.saldo += kwota
            return True
        else:
            return False
        
