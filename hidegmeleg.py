
from random import randint
szam = randint(0,100)
bekeres = 0
masikszam = szam
while bekeres != szam:
    bekeres = int(input("Talald ki a szamot: "))
    if bekeres < szam:
        if masikszam - 10 < bekeres:
            print("meleg")
        elif masikszam - 10 > bekeres:
            print("hideg")
    if bekeres > szam:
        if masikszam + 10 > bekeres:
            print("meleg")
        elif masikszam + 10 < bekeres:
            print("hideg")
    if szam == bekeres:
        print("Eltalalt")
    
