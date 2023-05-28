class Student:
    def __init__(self, imie, nazwisko, nr_indeksu): #definijemy init w odniesieniu do siebie(init(self))
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.indeks = []

    def __str__(self):
        return self.imie + self.nazwisko + str(self.nr_indeksu)

    def dodaj_ocene(self,ocena):
        self.indeks.append(ocena)

    def oblicz_srednia(self):
        if len(self.indeks) == 0:
            srednia = 0
        else:
            srednia = sum(self.indeks) / len(self.indeks)
        return srednia


student_ola = Student("Aleksandra", "Wojewoda", 122345)
student_ola.dodaj_ocene(5.0)
student_ola.dodaj_ocene(4.5)
student_ola.dodaj_ocene(4.0)
student_ola.dodaj_ocene(5.0)
print(student_ola)
print(student_ola.indeks)

print(student_ola.oblicz_srednia())

class Mieszkanie:
    def __init__(self, ulica , nr_budynku, nr_mieszkania, kod_pocztowy, miasto, metraz, liczba_pokoi, rok_budowy):
        self.ulica = ulica
        self.nr_budynku = nr_budynku
        self.nr_mieszkania = nr_mieszkania
        self.kod_pocztkowy = kod_pocztowy
        self.miasto = miasto
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi
        self.rok_budowy = rok_budowy

    def __str__(self):
        return self.ulica +","+ str(self.nr_budynku) +"/"+ str(self.nr_mieszkania) +","+ self.miasto

    def dodaj_pokoj(self, liczba_nowych_pokoi):
        self.liczba_pokoi = self.liczba_pokoi + liczba_nowych_pokoi

    def wielkosc(self):
        print('Mieszkanie ma ' + str(self.metraz) + "m2, a liczba znajdujacych sie w nim pokoi to:  " + str(self.liczba_pokoi))

    def oblicz_wiek_mieszkania(self, rok_obecny):
        wiek = rok_obecny - self.rok_budowy
        return wiek


mieszkanie_1 = Mieszkanie('Grunwaldzka', 167, 4, "61-100", "Poznan", 74, 2, 2018)
print(mieszkanie_1)
print(mieszkanie_1.liczba_pokoi)
mieszkanie_1.dodaj_pokoj(2)
mieszkanie_1.wielkosc()
print(mieszkanie_1.oblicz_wiek_mieszkania(2023))



