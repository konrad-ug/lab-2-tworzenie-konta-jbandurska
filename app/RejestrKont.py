class RejestrKont:
    lista = []
    
    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)

    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def zaktualizuj_konto(cls, pesel, dane):
        konto = cls.wyszukaj_konto_z_peselem(pesel)

        if konto != None:
            for key in dane:
                if key == "imie":
                    konto.imie = dane["imie"]
                elif key == "nazwisko":
                    konto.nazwisko = dane["nazwisko"]


    @classmethod
    def usun_konto(cls, pesel):
        konto = cls.wyszukaj_konto_z_peselem(pesel)
        cls.lista.remove(konto)

    @classmethod
    def wyczysc_rejestr(cls):
        cls.lista = []
        return cls.lista