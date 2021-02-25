#iterācija - kādas darbības atkārtota izpildīšana
mainigais = [1, 2, 3, 4]
for elements in mainigais:
    print(elements)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for x in mylist:
    print(x)

for _ in mylist:  #var nerakstīt cikla mainīgo
    print("Sveiki!")

#atrast pāra skaitļus
for skaitlis in mylist:
    if skaitlis % 2 == 0:
        print(skaitlis)
    else:
        print(f"Nepāra skaitlis: {skaitlis}")

#aprēķina summu
summa = 0

for sk in mylist:
    summa = summa + sk
    print(f"Pēc {sk} skaitļu saskaitīšanas summa ir {summa}")

print(summa)

#drukā tekstu
mystring = "Sveika, pasaule!"
for burts in mystring:
    print(burts)

for burts in "programma":
    print(burts, end=" ")

#drukā tuple
tup = (1, 2, 3, 4)
for elements in tup:
    print(elements)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mylist))

for elements in mylist:
    print(elements)

for (a, b) in mylist:  #atpako - tuple unpacking
    print(a)
    print(b)

for viens, otrs in mylist:
    print(otrs)

mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for a, b, c in mylist:
    print(c)
    print(a)

#vārdsnīcas
d = {"k1": 11, "k2": 12, "k3": 13}
for elements in d:
    print(elements)  #izdrukā tikai atslēgas

for elements in d.items():
    print(elements)  #izdrukā atslēgu/vērtību pārus

for atslega, vertiba in d.items():
    print(vertiba)

#izdrukā skaitļus ar range()
for skaitlis in range(15):  #intervāls [0;15)
    print(skaitlis + 1)


for skaitlis in range(4, 15): #intervāls [4;15)
    print(skaitlis)

