"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Štěpán Fryšara
email: stepan.frysara@seznam.cz
discord: Štěpán F.
"""

TEXTS = ["Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.", "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.","The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."]


oddelovac = "-" * 50
uzivatele = {"bob":"123","ann":"pass123","mike":"password123", "liz":"pass123"}

uzivatel = input("username: ")
if not uzivatel in uzivatele.keys(): 
    print("Incorrect username.")
    quit()

heslo = input("password: ")
if heslo != uzivatele[uzivatel]: 
    print("Incorrect password.")
    quit()

print(oddelovac)
print(f"Welcome to the app, {uzivatel}")
print(f"We have 3 texts to be analyzed.")
print(oddelovac)

vybrany_text = input("Enter a number btw. 1 and 3 to select: ")
if not vybrany_text.isnumeric():
    print("Choose number between 1 and 3.")
    quit()
elif int(vybrany_text) > 3 or int(vybrany_text) < 1:
    print("Wrong number.")
    quit()
print(oddelovac)

text = TEXTS[int(vybrany_text) - 1].split(" ")
for poradi in range(len(text)): 
    text[poradi] = text[poradi].strip(",")
    text[poradi] = text[poradi].strip(".")

pocet_slov = len(text)
pocet_velke = 0
pocet_psane_velke = 0
pocet_psane_male = 0
pocet_cisel = 0
suma_cisel = 0
delka_nejdelsiho_slova = 1

for slovo in text: 
    if len(slovo) > delka_nejdelsiho_slova: delka_nejdelsiho_slova = len(slovo)
    if slovo[0].isupper(): pocet_velke = pocet_velke + 1
    if slovo.isupper(): pocet_psane_velke = pocet_psane_velke + 1
    if slovo.islower(): pocet_psane_male = pocet_psane_male + 1
    if slovo.isnumeric(): 
        pocet_cisel = pocet_cisel + 1
        suma_cisel = suma_cisel + int(slovo)

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_velke} titlecase words.")
print(f"There are {pocet_psane_velke} uppercase words.")
print(f"There are {pocet_psane_male} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")

graf = [0] * delka_nejdelsiho_slova
for slovo in text: graf[len(slovo.strip(",")) - 1] = graf[len(slovo) - 1] + 1

print(oddelovac)
print("LEN |","OCCURENCES".center(max(graf) + 2),"|NR")
print(oddelovac)
for poradi in range(delka_nejdelsiho_slova): 
    print(str(poradi + 1).rjust(len("LEN")) , "|","*"*graf[poradi]," "*(max(graf)+1-graf[poradi]), "|",graf[poradi]) 
