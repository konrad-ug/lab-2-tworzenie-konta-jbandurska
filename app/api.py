from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f"Ilość kont w rejestrze {RejestrKont.ile_kont()}", 200

@app.route("/konta/konto/<pesel>", methods=['GET', 'PUT', 'DELETE'])
def wyszukaj_konto_z_peselem(pesel):
    if request.method == "GET":
        konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
        return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200
    elif request.method == "PUT":
        dane = request.get_json()
        print(f"Update konta z peselem {pesel}")
        RejestrKont.zaktualizuj_konto(pesel, dane)
        return jsonify("Konto zaktualizowane"), 202
    else:
        RejestrKont.usun_konto(pesel)
        return jsonify("Konto usunięte D:"), 202