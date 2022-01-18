'''
2. Feladat
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket!
'''
def szumma(listacska):
    osszeg = 0
    for i  in listacska:
        osszeg += i
    return osszeg


lista = []

while True:
    bekert = int(input("Kérem adjon mege egy számot -5 és 5 között!"))
    if 5 < bekert or bekert < -5:
        break
    lista.append(bekert)

print(lista)
print(szumma(lista))

