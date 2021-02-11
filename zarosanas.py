#if, else, elif
"""
if nosacījums:
    izpildāmā darbība
elif cits nosacījums:
    izpildāmā darbība    
else:
    izpildāmā darbība (visos pārējos gadījumos)  
"""
#ja skaitlis ir lielāks par 5, izdrukā, ka lielāks par 5, citādi, ja skaitlis lielāks par 0, izdrukā, ka lielāks par 0. Citādi izdrukā, ka tas nav pozitīvs skaitlis.
a = 6
if a > 5:
    print("Skaitlis ir lielāks par 5.")
elif a > 0:
    print("Skaitlis ir lielāks par 0.")
else:
    print('Skaitlis nav pozitīvs')

if False:
    print("patiesi")

suns_grib_est = True
if suns_grib_est:
    print("Pabaro suni!")
else:
    print("Suns ir paēdis.")    