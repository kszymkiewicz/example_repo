# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("Hello Kasia")
print ("{} {}".format(hello,student))


# zadanie 1.2

student = input("Wpisz swoje imie: ")

print(f"Hello {student}")

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print(f"Liczba studentow wynosi: {liczba_studentow}")


# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
for i in studenci:
    print("Hello {}".format(i))


# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: {}".format(wynik))


# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))


# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)


# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_split=[]
for student in studenci:
    student = student.split(" ")
    studenci_split.append(student)
studenci_split = sorted(studenci_split, key=lambda x: x[1])
# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci_split:
    print(student)



# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_split=[]
for student in studenci:
    student = student.split(" ")
    studenci_split.append(student)

liczba_n =0
for student in studenci_split:
    if student[1][0] == "N":
        liczba_n = liczba_n + 1

print("Liczba studentow na N wynosi: {}".format(liczba_n))


# zadanie 1.10

# zmienne poniezej preprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

wykres_1_funkcja_liniowa = False
wykres_2_funkcja_liniowa = False
wykres_3_funkcja_liniowa = False

if wykres_1[0][0]*(wykres_1[1][1]-wykres_1[2][1]) + wykres_1[1][0]*(wykres_1[2][1]-wykres_1[0][1]) + wykres_1[2][0]*(wykres_1[0][1]-wykres_1[1][1]) == 0:
    wykres_1_funkcja_liniowa = True

if wykres_2[0][0]*(wykres_2[1][1]-wykres_2[2][1]) + wykres_2[1][0]*(wykres_2[2][1]-wykres_2[0][1]) + wykres_2[2][0]*(wykres_2[0][1]-wykres_2[1][1]) == 0:
    wykres_2_funkcja_liniowa = True

if wykres_3[0][0]*(wykres_3[1][1]-wykres_3[2][1]) + wykres_3[1][0]*(wykres_3[2][1]-wykres_3[0][1]) + wykres_3[2][0]*(wykres_3[0][1]-wykres_3[1][1]) == 0:
    wykres_3_funkcja_liniowa = True


if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")

# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.
