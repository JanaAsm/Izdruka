#tupes - līdzīgi list, bet nav maināmi, izmanto (iekavas)
#sakārtoti
my_tup = (1, 2, 3)
my_list = [1, 2, 3]
print(type(my_tup))
print(type(my_list))
print(len(my_tup))

#var saturēt dažādus datu tipus
my_tup = ("es", 6, 6, 2.35)
print(my_tup)

#var indeksēt
print(my_tup[0])
print(my_tup[-1])

#metodes
print(my_tup.count(6))  #saskaita cik reizes atkārtojas konkrētais elements
print(my_tup.index(
    6))  #parāda indeksu, kur pirmo reizi parādās norādītais elements

#nav maināms
my_list[0] = "viens"
print(my_list)
#my_tup[0] = "tu"
print(my_tup)

#sets - nesakārtota unikālu elementu kopa; izmanto figūriekavas
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(2.59)
print(my_set)
my_set.add(2)
print(my_set)
my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 333, 3]
print(set(my_list))

#piemērs
s = "Salaspils"
my_set = set(s)
print(my_set)

#booleans - True or False - izmanto loģiskajiem operatoriem
print(True)
print(type(False))

#Piemēri
print(1 > 2)
print(1 == 1)
