vards=input("Kā tevi sauc? ")
print(f"Tavs vārds ir {vards}.")

gadi=int(input("Cik tev gadu? "))
print(f"Tev ir {gadi} gadi.")
dzimsGads=2021-gadi
print(f"Tavs dzimšanas gads ir {dzimsGads}.")

celsij=int(input("Kāda ir temperatūra Celsija?" ))
faranheiti=celsij*9/5+32
print(f"Temperatūra {celsij} grādi pēc Celija skalas ir {faranheiti} pēc Faranheita skalas.")

platums=float(input("Platums: "))
garums=float(input("Garumss: "))
augstums=float(input("Augstums: "))
print(f"Tilpums ir {platums*garums*augstums}.")

#Strings (rakstzīmju virknes)
print("sveiki")
print("sveiki")
print(" I am going on a run")
print('Arī šis ir "risinājums"')
print("Sveika,\npasaule!") #izdrukā divās rindās
print("Sveika, \tpasaule") #izdrukā ar tabulācijas atkāpi

#String garums - len()
print(len("sveiki"))
print(len("Ko tu domā?"))

# {sākums:beigas:solis}
myString="Sveika, pasaule!"
print(myString)
print(myString[0]) #izdrukā pirmo rakstzīmi
print(myString[8]) #izdrukā 9. rakstzīmi
print(myString[13]) #izdrukā 14. rakstzīmi
print(myString[-3]) #izdrukā 14. rakstzīmi
print(myString[-1]) #izdrukā pēdejo rakstzīmi

myString="abcdefghijklmnoprstuvz"
print(myString)
print(myString[2]) #izdrukā c
print(myString[2:]) #izdrukā no c uz priekšu
print(myString[:3]) #izdrukā līdz 2. indeksam (neietver galapunktu)
print(myString[3:6]) #izdrukā no 4 līdz 6 
print(myString[::2]) #izdrukā katru otro jeb ar soli 2
print(myString[2:7:2]) #izdrukā n0 3. rakstzīmes (2.indekss) līdz 7. rakstzīmei katru otro
print(myString[::-1]) #izdrukā otrā virzienā

