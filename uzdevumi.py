# 1.uzdevums
a = 15
b = 2.5
c = 4.78
if c < a  and a > b:
    print("4.78 ir mazāk nekā 15, bet 15 ir lielāks nekā 2.5!")
if c > b:
    print("4.78 ir vairāk nekā 2.5")


# 2.uzdevums
temper = float(input("Ievadi savu temperatūru! "))
if temper < 35:
    print("Vai nav par aukstu?")
elif temper < 38:
    print("Viss kārtībā.")
else:
    print("Iespējams drudzis.")

#stundas uzdevums
atr = "banka"
#banka (te ir daudz naudas), veikals (Jānopērk āboli), aptieka (man ir iesnas), visur citur - āboli nav
if atr == "banka":
    print("Te ir daudz naudas")
elif atr=="veikals":
    print("Jānopērk āboli")
elif atr=="aptieka":  
    print("Man ir iesnas")
else:
    print("Ābolu nav")    


