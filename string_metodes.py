#string metodes
vards = "Man"  #ko darīt, lai nomainītu uz Gan?
ped_burti = vards[1:]
print("G" + ped_burti)  #string konkatinācija

x = "Sveika, pasaule, "
x = x + "kā klājas?"
print(x)

print(5 + 6)
print("5" + "6")

print(x.upper())  #uzraksta ar lielajiem burtiem
print(x.lower())  #uzraksta ar mazajiem burtiem
x2 = x.upper()
print(x2)

print(x.split())  #sadala visu pa daļam, izmantojot atstari
print(x.split("a")) #sadala visu pa daļam, izmantojot "a"
print(x2.split())
