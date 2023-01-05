from behave import *
# from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"

@when('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def utworz_konto(context, name, last_name, pesel):
    json_body = { "imie": name,
    "nazwisko": last_name,
    "pesel": pesel
    }
    print(json_body)
    create_resp = requests.post(URL + "/konta/stworz_konto", json = json_body)
    assert_equal(create_resp.status_code, 201)


@step('Number of accounts in registry equals: "{count}"')
def sprawdz_liczbe_kont_w_rejestrze(context, count):
    ile_kont = requests.get(URL + f"/konta/ile_kont")
    assert_equal(ile_kont.json()["ilosc_kont_w_rejestrze"], int(count))


@step('Account with pesel "{pesel}" exists in registry')
def sprawdz_czy_konto_z_pesel_istnieje(context, pesel):
    konto = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(konto.json()["msg"], "Konto jest w rejestrze")


@step('Account with pesel "{pesel}" does not exists in registry')
def sprawdz_czy_konto_z_pesel_nie_istnieje(context, pesel):
    konto = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(konto.json()["msg"], "Nie ma takiego konta")


@when('I delete account with pesel: "{pesel}"')
def usun_konto(context, pesel):
    delete_resp = requests.delete(URL + f"/konta/konto/{pesel}")
    assert_equal(delete_resp.status_code, 202)

@when('I edit account with pesel: "{pesel}" using last name: "{last_name}"')
def edytuj_nazwisko(context, pesel, last_name):
    put_resp = requests.put(URL + f"/konta/konto/{pesel}", json = {
            "nazwisko": last_name
        })
    assert_equal(put_resp.status_code, 202)

@step('Account with pesel "{pesel}" has last name: "{last_name}"')
def sprawdz_nazwisko(context, pesel, last_name):
    get_resp = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(get_resp.json()['nazwisko'], last_name)

@when('I clear the account registry')
def usun_wszystkie_konta(context):
    delete_resp = requests.delete(URL + "/konta/wyczysc_rejestr")
    assert_equal(delete_resp.status_code, 202)
