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