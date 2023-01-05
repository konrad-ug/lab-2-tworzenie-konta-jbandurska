from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    if RejestrKont.wyszukaj_konto_z_peselem(dane["pesel"]) == None:
        konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
        RejestrKont.dodaj_konto(konto)
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Konto z takim peselem już istnieje"), 400

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return {"ilosc_kont_w_rejestrze": RejestrKont.ile_kont()}, 200

@app.route("/konta/konto/<pesel>", methods=['GET', 'PUT', 'DELETE'])
def wyszukaj_konto_z_peselem(pesel):
    if request.method == "GET":
        konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
        if konto != None:
            return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo, msg="Konto jest w rejestrze"), 200
        else:
            return jsonify(msg="Nie ma takiego konta"), 200
    elif request.method == "PUT":
        dane = request.get_json()
        print(f"Update konta z peselem {pesel}")
        RejestrKont.zaktualizuj_konto(pesel, dane)
        return jsonify("Konto zaktualizowane"), 202
    else:
        RejestrKont.usun_konto(pesel)
        return jsonify("Konto usunięte D:"), 202


@app.route("/konta/wyczysc_rejestr", methods=['DELETE'])
def wyczysc_rejestr():
    RejestrKont.wyczysc_rejestr()
    return "Rejestr wyczyszczony", 202