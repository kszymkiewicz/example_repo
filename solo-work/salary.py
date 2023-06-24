class Pracownik:
    def __init__(self, imie, nazwisko, pensja_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja_brutto = pensja_brutto

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}"

    def oblicz_netto(self):
        skladka_emerytalna_pracownik = round(self.pensja_brutto * 0.0976, 2)
        skladka_rentowa_pracownik = round(self.pensja_brutto * 0.015,2)
        skladka_chorobowa = round(self.pensja_brutto * 0.0245,2)
        podstawa_wymiaru = round(self.pensja_brutto - skladka_chorobowa - skladka_rentowa_pracownik - skladka_emerytalna_pracownik,2)
        skladka_zdrowotna = round(podstawa_wymiaru * 0.09,2)
        podstawa_opodatkowania = podstawa_wymiaru - 250
        zaliczka_podatek = round(0.12 * podstawa_opodatkowania - 300,2)
        netto = podstawa_wymiaru - skladka_zdrowotna - zaliczka_podatek
        return round(netto, 2)

    def oblicz_koszty_pracodawcy(self):
        skladka_emerytalna = self.pensja_brutto * 0.0976
        skladka_rentowa = self.pensja_brutto * 0.065
        skladka_wypadkowa = self.pensja_brutto * 0.0167
        skladka_fundusz_pracy = self.pensja_brutto * 0.0245
        skladka_FGSP = self.pensja_brutto * 0.001
        skladki_razem = skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_fundusz_pracy + skladka_FGSP
        koszt_pracodawcy = self.pensja_brutto + skladki_razem
        return round(koszt_pracodawcy, 2)

    def wygeneruj_raport(self):
        dochod_netto = round(self.oblicz_netto(),2)
        koszt_pracodawcy = round(self.oblicz_koszty_pracodawcy(),2)
        skladka_emerytalna_pracownik = round(self.pensja_brutto * 0.0976,2)
        skladka_rentowa_pracownik = round(self.pensja_brutto * 0.015,2)
        skladka_chorobowa = round(self.pensja_brutto * 0.0245,2)
        podstawa_wymiaru = round(self.pensja_brutto - skladka_chorobowa - skladka_rentowa_pracownik - skladka_emerytalna_pracownik,2)
        skladka_zdrowotna = round(podstawa_wymiaru * 0.09,2)
        podstawa_opodatkowania = round(podstawa_wymiaru - 250,2)
        zaliczka_podatek = round(0.12 * podstawa_opodatkowania - 300,2)
        skladka_emerytalna = round(self.pensja_brutto * 0.0976,2)
        skladka_rentowa = round(self.pensja_brutto * 0.065,2)
        skladka_wypadkowa = round(self.pensja_brutto * 0.0167,2)
        skladka_fundusz_pracy = round(self.pensja_brutto * 0.0245,2)
        skladka_FGSP = round(self.pensja_brutto * 0.001,2)


        print(f"Wynagrodzenie brutto: {self.pensja_brutto}")
        print(f"Składka emerytalna: {skladka_emerytalna_pracownik}")
        print(f"Składka rentowa: {skladka_rentowa_pracownik}")
        print(f"Składka chorobowa: {skladka_chorobowa}")
        print(f"Składka zdrowotna: {skladka_zdrowotna}")
        print(f"Zaliczka na podatek dochodowy: {zaliczka_podatek}")
        print(f"Do wypłaty netto: {dochod_netto}")
        print(f"Wynagrodzenie brutto: {self.pensja_brutto}")
        print(f"Składka emerytalna: {skladka_emerytalna}")
        print(f"Składka rentowa: {skladka_rentowa}")
        print(f"Składka wypadkowa: {skladka_wypadkowa}")
        print(f"Składka na Fundusz Pracy: {skladka_fundusz_pracy}")
        print(f"Składka na FGSP: {skladka_FGSP}")
        print(f"Łączny kost pracodawcy: {koszt_pracodawcy}")

# test
pracownik_1 = Pracownik("Jan", "Kowalski", 3500)
print(pracownik_1)
# Pracownik: Jan Kowalski
print(pracownik_1.oblicz_netto())
# 2715.94
print(pracownik_1.oblicz_koszty_pracodawcy())
# 4216.80
pracownik_1.wygeneruj_raport()
# Wynagordzenie brutto: 3500
# Skladka emerytalna: 341.60
# Skladka rentowa: 52.5
# Skladka chrobowa: 85.75
# Skladka zdrowotna: 271.81
# Zaliczka na podatek: 32.4
# Do wyplaty: 2715.94
# Wynagordzenie brutto: 3500
# Skladka emerytalna: 341.60
# Skladka rentowa: 227.50
# Skladka wypadkowa: 58.45
# Skladka Fundusz Pracy: 85.75
# Skladka FGŚP: 3.50
# Całkowite koszty pracodawcy: 4216.80

import csv

def wczytaj_pracownikow(nazwa_pliku):
    pracownicy = []
    with open(nazwa_pliku) as plik:
        dane = csv.reader(plik)
        for wiersz in dane:
            imie = wiersz[0]
            nazwisko = wiersz[1]
            pensja_brutto = float(wiersz[2])
            pracownik = Pracownik(imie, nazwisko, pensja_brutto)
            pracownicy.append(pracownik)
    return pracownicy


pracownicy = wczytaj_pracownikow("pracownicy.csv")


for pracownik in pracownicy:
    print(str(pracownik))
    print(f"Do wypłaty netto: {pracownik.oblicz_netto():.2f}")
    print(f"Koszty pracodawcy: {pracownik.oblicz_koszty_pracodawcy():.2f}")
    pracownik.wygeneruj_raport()
    print('-' * 20)






