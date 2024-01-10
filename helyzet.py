import Gep
f = open("gep.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def gepek_szama():
    sorok_szama = 0
    index = 0
    while index < len(sorok):
        sorok_szama += 1
        index += 1
    print(f"III/A,B:\n\t A gepek szama: {index}")

def atlag():
    index = 0
    osszeg = 0
    osztando = 0
    while index <len(sorok):
        Gepek=Gep.Gep(sorok[index])
        if Gepek.id % 2 == 0:
            osszeg += Gepek.id
            osztando += 1
        index += 1 
    eredmeny = osszeg / osztando
    print(f"III/C:\n\t páros teremszamu termek azonosito atlaga:{eredmeny}")

def legkisebb():
    index = 0
    legkisebb = 0
    legkisebb_hely = ""
    while index < len(sorok):
        Gepek=Gep.Gep(sorok[index])
        if Gepek.id < legkisebb:
            legkisebb = Gepek.id
            legkisebb_hely = Gepek.hely
        index += 1










