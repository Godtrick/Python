#while <podmínka/test/výraz>:
    #<kód/ohlášení>



n = 5

while n != 10:
    n += 1
    print(n)

auta = ["Skoda", "Audi", "Opel", "Mercedes"]

while auta:
    auta.pop(-1)
    print(auta)

muj_string = "while smyčky muzou byt nekonecne"

while muj_string:
    muj_string = muj_string[1:]
    print(muj_string)

n = 5

while n > 0:
    n -= 1
    if n == 3:
        break
    print(n)

    index = 10

    while index < 20:
        if len(str(index)) == 2:
            index += 1
        print(f"{index}")


n = 5 

while n > 0:
    n -= 1
    print(n)
else:
    print("smycka skoncila")


switch = True

while switch:
    vstupni_hodnota = input("zadej pismeno: ")

    if vstupni_hodnota.isalpha():
        print(f"{vstupni_hodnota} je opravdu pismeno.")
    else:
        print(f"{vstupni_hodnota} neni pismeno, konec.")
        switch = False
    

barvy = [ 'zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena' ]

pocet_barev = {}

while barvy:
    barva = barvy.pop()

    if barva not in pocet_barev:
        pocet_barev[barva] = 0
    
    pocet_barev[barva] += 1

    print(pocet_barev)




    

