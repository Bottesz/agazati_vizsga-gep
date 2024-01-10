import random

szam_lista = []
index = 0
while index < 15:
    vszam = random.randint(-90,500)
    szam_lista.append(vszam)
    index += 1


def masodik_feladat():
    print("II/A,B,C:")   
    index = 0
    while index < len(szam_lista):
        if index == 0:
            print(f"\t{szam_lista[index]}*",end="")
        else:
            print(f"*{szam_lista[index]}",end="")
        index += 1

def oszhatoak_szama():
    index = 0
    megszam = 0
    while index < len(szam_lista):
        if szam_lista[index] % 10 == 0:
            megszam += 1
        index += 1
    return f" 10-zel megszamolhatók {megszam}"

def konzolra_kiir():
    print("\nII/D,E:\n\t",oszhatoak_szama())

def fajlba_ir():
    f = open("kimutatas.txt","w",encoding="utf-8")
    f.write("II/F\n")
    f.write(f"\t{oszhatoak_szama()}")
    f.close()
    