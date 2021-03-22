n = int(input('Ievadi veselu skaitli: '))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

a = int(input("Pirmais skaitlis: "))
b = int(input("Otrais skaitlis: "))

if a < b:
    for i in range(a, b + 1):
        print(i)  
else:
    for i in range(a,b-1,-1): #skaita atpakaļ
        print(i)        

n = int(input("Ievadi veselu skaitli: "))
for i in range(n, 0 - 1, -1):
    if i % 2 == 0:
        print(i)     


mylist = []
for i in range(10):
    n = float(input(f"Ievadi {i+1}. skaitli: "))
    mylist.append(n)

#mylist.sort()
print(mylist)


sk = 1
n = int(input("Ievadi veselu skaitli: "))
while sk*sk <= n:
    print(sk**2)
    sk+= 1


n=0
while n<2:
    n = int(input("Ievadi veselu skaitli: "))

dalitajs = 2
while True:
    if n%dalitajs==0:
        print(f"Mazākais skaitlis, ar ko {n} dalās bez atlikuma, ir {dalitajs} .")
        break
    else:
        dalitajs += 1


sk = 1
a = ""
for sk in range(sk, 5):
    a = a + str(sk)
    print(a)




