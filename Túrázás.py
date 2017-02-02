#1. verzió
évszak = input('Nyár van, vagy ősz? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if évszak == 'ny' and szél == 'n':
    print('megyünk')
if évszak == 'ő' and esik == 'n' and szél == 'n':
    print('megyünk')
    
#2. verzió
évszak = input('Nyár van, vagy ősz? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if évszak == 'ny' and szél == 'n':
    print('megyünk')
elif évszak == 'ő' and esik == 'n' and szél == 'n':
    print('megyünk')
else:
    print('maradunk')

#3. verzió
évszak = input('Melyik évszak van? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if (évszak == 'ny' and szél == 'n') or (évszak == 'ő' and esik == 'n' \
                                        and szél == 'n'):
    print('megyünk')
else:
    print('maradunk')    

#4. verzió
évszak = input('Nyár van, vagy ősz? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if szél == 'n' and (évszak == 'ny' or (évszak == 'ő' and esik == 'n')):
    print('megyünk')
else:
    print('maradunk')

#1. feladat

szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot:"))
print(min(szam1,szam2))

#2. feladat
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot:"))
print(min(szam1,szam2))

#3. feladat
helyezes=int(input("Hányadik helyezést érted el? "))
if helyezes<=3:
    print("Dobogós!")
else:
    print(helyezes)

#4. feladat
eredmeny=int(input("Hanyadik helyezést érted el? "))
if eredmeny == 3:
    print("Bronz.")
elif eredmeny == 2:
    print("Ezüst.")
elif eredmeny == 1:
    print("Arany.")
else:
    print("Nem kaptám érmet.")

#5. feladat
a=int(input("Egyik oldal nagysága: "))
b=int(input("Másik oldal nagysága: "))
c=int(input("Harmadik oldal nagysága: "))
if a+b>c and a+c>b and b+c>a:
    print("A háromszög megszerkeszthető.")
else:
    print("A háromszög nem szerkeszthető meg.")

#6. feladat
"""
Ha darab > 500, akkor
    ki: ár * 0,7
Különben ha darab > 100, akkor
    ki: ár * 0,9
Elágazás vége
"""

#7. feladat
nev = input("Mi a neve? ")
nem = input("Lány, vagy fiú vagy? (l/f)")
if nem =="l":
    elotag = "Ms."
elif nem == "f":
    elotag == "Mr."
else:
    print("Elég furcsa szerzet vagy te.")
    elotag == "???"
napszak = input("Milyen napszak van? (r,du,e,é)")
if napszak == "r":
    angol = "morning"
elif napszak == "du":
    angol = "afternoon"
elif napszak == "e":
    angol = "evening"
elif napszak == "é":
    angol = "night"
else:
    print("Nem igazán ismerek ilyen napszakot, de te tudod.")
    angol = "I don\'t know"
print("Good ", angol, ", ", elotag, " ",nev, "!", sep="")


#8. feladat
gondolt=4
tipp=int(input("Mire gondolok 1 és 5 között? "))
if gondolt == tipp:
    print("Ez az.")
elif abs(tipp - gondolt) == 1:
    print("Majdnem...")
else:
    print("Nem sikerült")


#9. feladat
kor=int(input("Hány éves vagy? "))
if kor<6:
    print("Nézzél Piroska és a farkast!")
elif 6<= kor <=16:
    print("Nézzél Zootropoliszt!")
elif kor>16:
    print("Azt nézel, amit akarsz!")
