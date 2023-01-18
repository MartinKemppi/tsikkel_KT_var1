from math import *
from random import *
#Variant_1
#Ü1
try:
    n=int(input("vali 1-9 palju tahad näha kuuske? "))
    if n<1 or n>9:
        print("Vale vahemik")
except:
    print("Vale andmetüüp")
x=0
for x in range(4):
    for e in range(n):
        if x == 0:
            print("     /V\     ", end="")
            
        elif x == 1:
            print("    / V \    ", end="")
        
        elif x == 2:
            print("   / V V \   ", end="")      
        
        elif x == 3:
            print("  /VV V VV\  ", end="")
    print("")
  
#Ü2
try:
    def korda_paaritu(R):
        i = 1
        result = 1
        while i <= R:
            if i % 2 != 0:
                result *= i
            i += 1
        return result
    R = int(input("Sisesta arv: "))
    print(korda_paaritu(R))

except:
    print("Vale andmetüüp")

#Ü3
try:
    N=randint(1,100)
except:
    print("Vale andmetüüp")
paaris = 0
paaritu = 0
try:
    while N > 0: 
        if N % 2 == 0:
            paaris += 1
            break
        else:
            paaritu += 1
            break
    print("Paarisarvu on:",paaris)
except:
    print("Vale andmetüüp")

#Ü4
try:
    N=randint(1,100000)
    paaris = 0
    paaritu = 0
    while N > 0:
        number = N % 10
        if number % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        N = N // 10
    print(N)
    print("Paaris arvu on:", paaris)
    print("Paaritu arvu on:", paaris)
except:
    print("Vale andmetüüp")

#Ü5
try:
    A=int(input("Anna arv: "))
    B=int(input("Anna arv: "))
    sum=A+B
    print("A+B=", sum)
except:
    print("Vale andmetüüp")
