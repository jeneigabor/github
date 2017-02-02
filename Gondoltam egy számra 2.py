gondolt_szám = 4
 
kitalálta = False 
 
while not kitalálta:
    tipp = input('Melyik számra gondoltam 1 és 5 között? ')
    tipp = int(tipp)
    if tipp == gondolt_szám:
        kitalálta = True
print('Pápá!')


#1. feladat
szam = 1
while szam <= 100:
    print(szam**2)
    szam += 1

#2. feladat
szam=0
while szam<100:
    print(szam)
    szam +=2

#3. feladat
szam=101
while szam <= 999:
    print(szam)
    szam+=2

#4. feladat
valasz = None    
while valasz != "Szeretlek":
    valasz = input("De ugye szeretsz? ")

#5. feladat
kezdet=int(input("Hánytól írjam? "))
veg=int(input("Meddig írjam? "))
while kezdet<=veg:
    print(kezdet)
    kezdet+=1

#6. feladat
kezdet=int(input("Hánytól írjam? "))
veg=int(input("Meddig írjam? "))
hanyasaval=int(input("Hányasával számoljak? "))
while kezdet<=veg:
    print(kezdet)
    kezdet+=hanyasaval

#7. feladat
mettől = input('Honnan kezdve írjam ki a számokat? ')
meddig = input('Meddig írjam ki a számokat? ')
hányasával = input('Hányasával írjam ki a számokat? ')
hatványkitevő = input('Hányadik hatványukat írjam a számok mellé? ')
 
mettől = int(mettől)
meddig = int(meddig)
hányasával = int(hányasával)
hatványkitevő = int(hatványkitevő)
 
szám = mettől 
 
while szám <= meddig:
    print(szám, szám**hatványkitevő)
    szám = szám + hányasával

