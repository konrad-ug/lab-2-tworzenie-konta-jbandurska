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
        konto.imie = dane['imie'] or konto.imie
        konto.nazwisko = dane['nazwisko'] or konto.nazwisko
        konto.pesel = dane['pesel'] or konto.pesel

    @classmethod
    def usun_konto(cls, pesel):
        konto = cls.wyszukaj_konto_z_peselem(pesel)
        cls.lista.remove(konto)