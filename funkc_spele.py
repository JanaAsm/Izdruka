#piemers = [1,2,3,4,5,6,7]
from random import shuffle

#rezult = shuffle(piemers) #shuffle funkcija neatgriež rezultātu
#print(piemers)

#izveido savu shuffle funkciju, kas atgriež rezultātu
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#rezult = shuffle_list([1,2,3,4,5])    
#print(rezult)

#izveido 3 "glāzītes", kur vienā ir bumbiņa
#mylist = [" ", "o", " "]
#print(shuffle_list(mylist))

#izveido funkciju, kur spēlētājs norāda savu minējumu
def mans_minejums():
    minejums = ""
    while minejums not in ["0", "1", "2"]:
        minejums = input("Izvēlies skaitli - 0, 1 vai 2: ")
    return int(minejums)
#indekss = mans_minejums() 

#izveido funkciju, kas pārbauda vai minējums sakrīt
def parbaudi_minejumu(mylist,minejums):
    if mylist[minejums] == "o":
        print("Uzminēji!")
    else:
        print("Neuzminēji...") 
        print(mylist)
#parbaudi_minejumu(mylist,indekss)    

#pa soļiem izsauc visas funkcijas
#norāda sarakstu
mylist = [" ", "o", " "]

#sajauc sarakstu
sajaukts_saraksts = shuffle_list(mylist)

#spēlētāja minējums
spelet_minejums = mans_minejums()

#pārbauda spēlētaja minējumu
parbaudi_minejumu(sajaukts_saraksts,spelet_minejums)