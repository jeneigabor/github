név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = 2016 - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

#Feladatok:
#1. feladat megoldása:
név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = input('Melyik évben járunk?')
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

#2. feladat megoldása:
név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = input('Melyik évben járunk? ')
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
érettségi_év = születési_év + 18
print(név, ', kend ', érettségi_év, '-ban érettségizik.', sep='')

#3. feladat megoldása:
a = int(input("Egyik szám:"))
b = int(input("Másik szám"))
c = a*b
print(c)

#4. feladat megoldása:
magyar_merfold = input("Hány magyar mérföldre van a sárkány barlangja? ")
magyar_merfold = int(magyar_merfold)
km = magyar_merfold * 8.3536
tengeri_merfold = km / 1.852
print("Ez a táv", km, "kilométert és", tengeri_merfold, "tengeri mérföldet jelent.")
