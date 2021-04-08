def saskaiti_skaitlus(sk1, sk2):
    #rez = sk1 + sk2
    return sk1 + sk2


rez1 = saskaiti_skaitlus(5, 11)
rez2 = saskaiti_skaitlus(2.5, 1.1)
rez3 = saskaiti_skaitlus(-2, -3.5)
print(rez1 * rez2 * rez3)


#noskaidro vai tas ir pāra skaitlis
def parbaudi_pari(skaitlis):
    return skaitlis % 2 == 0


print(parbaudi_pari(45))
print(parbaudi_pari(12))
print(parbaudi_pari(7))


#atgriež true, ja sarakstā ir kaut viens pāra skaitlis
def parbaudi_pari_list(saraksts):
    for skaitlis in saraksts:
        if skaitlis % 2 == 0:
            return True  #pēc return funkcijas darbība apstājas
        else:
            pass  #izlaiž
            return False  #darbosies pēc tam, kad būs izgājis viss cikls


print(parbaudi_pari_list([1, 2, 3, 7]))


#funkcija atgriež visus pāra skaitļus, kas atrodas sarakstā
def parbaudi_pari_list2(saraksts):
    para_skaitli = []
    for skaitlis in saraksts:
        if skaitlis % 2 == 0:
            para_skaitli.append(skaitlis)
        else:
            pass
        return para_skaitli


print(parbaudi_pari_list2([1, 2, 3, 4, 5, 6,8]))
print(parbaudi_pari_list2([1, 3, 5]))