#uzd1
#Lietotājs ievada divus skaitļus, Izdrukāt visus intervāla skaitļus. Abus galapunktus ieskaitot.abs
a =int(input("Pirmais skaitlis: "))
b = int(input("Otrais skaitlis: "))
for i in range(a,b+1):
    print(i)

#uzd2
#Aprēķini skaitļa faktoriālu izmantojot ciklu. Lietotājs ievada veselu skaitļi.
#faktoriāls = 1*2*3...*n
n = int(input("Ievadi veselu skaitli: "))
faktorials = 1
for i in range(1,a+1):
    faktorials = faktorials*i
print(f"Skaitļa {a} faktoriāls ir {faktorials}.")

#uzd3
#No lietotāja ievadīta intervāla, izvadi visus veselos skaitļus,
#kas dalās ar konkrētu skaitli (arī to norāda lietotājs)
a =int(input("Pirmais skaitlis: "))
b = int(input("Otrais skaitlis: "))
dalitajs =int(input("Ievadi skaitli, ar kuru dalīt: "))
for i in range(a,b+1):
    if i%dalitajs==0:
        print(i)

#Lietotājs ievada divus veselos skaitļus A un B. Izdrukā visus skaitļus no A līdz B augošā secībā,ja A<B, bet dilstošā secībā, ja A>=B.
a =int(input("Pirmais skaitlis: "))
b = int(input("Otrais skaitlis: "))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

#Lietotājs ievada veselu skaitli N. Izdrukā visus nepāra skaitļus no 1 līdz N augošā secībā. Piemēram, ja N = 9, tad izdrukā 1, 3, 5, 7, 9
N = int(input('Ievadi veselu skaitli: '))
for i in range(1, N + 1):
    if i % 2 == 1:
        print(i)


