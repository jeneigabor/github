gondolt_szám = 4
tipp = input('Szerinted melyik számra gondolok 1 és 5 között? ')
tipp = int(tipp)
if gondolt_szám == tipp: # a gondolt szám egyenlő a tippel?
    print('Eltaláltad!')
    print('Kis ügyes!')
else: #különben
    print('Ez most sajnos nem sikerült...')
    print('De majd legközelebb... talán... ha nagyobb szerencséd lesz...')
print('Pápá!')


#1 feladat
print("Megoldás linkje: https://pythonidomar.wordpress.com/2016/09/15/gondoltam-egy-szamra/")

#2. feladat
jelszo="valami"
tipp=input("Írja be a jelszót:")
if tipp==jelszo:
    print("Jelszó elfogadva.")
else:
    print("Belépés megtagadva.")

#3. feladat
a=10
b=3
osszeg=a+b
tipp=int(input("Mennyi " + str(a) + " + " + str(b) + " ? "))
if tipp == osszeg:
    print("Helyes megoldás")
else:
    print("Ülj le, egyes!")

#4. feladat
a=int(input("Írj be egy egész számot: "))
if a >= 0:
    print("A", a, "természetes szám.")
else:
    print("A", a, "negatív egész szám.")
