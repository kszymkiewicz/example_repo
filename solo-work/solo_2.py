def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    print("Naleze do funkcji trojkat")
    return pole, obwod
    #return konczy funkcje, wiec wszystko co napiszemy po tym nie nalezy do funkji i jesli damy print po return to nie wyświetli się
    print("Jestem po return i się nie wyświetlę")

trojkat(1,2,3,4)
print("po wykonaniu funkcji")
print(trojkat(1,2,3,4)) #jeżeli chcemy wydrukować pole i obwód musimy wyprintować, bo return zwraca ale, nie printuje na konsoli

def trapez(podstawa_a, podstawa_b, bok_c, bok_d, h):
    pole = (podstawa_a+podstawa_b)*h/2
    obwod = podstawa_a + podstawa_b + bok_c + bok_d
    return pole, obwod

trapez(4,2,3,3,3.5)
print("pole i obwod trapezu wynosza: ", trapez(4,2,3,3,3.5))

def kolo(r):
    obwod = 2*3.314*r
    pole = 3.14*r**2
    return pole, obwod

print("pole i obwod kola wynosza: ", kolo(4))
