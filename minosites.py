def elso_feladat():
    print("I/A:")
    muzeum_neve:str = input("\t Múzeum neve:")
    latogato_neve:str = input("\t Látógató neve:")
    ertekeles:int = int(input("\t Értékelés (1-20): "))
    print("I/B:")
    if ertekeles <= 0:
        print("\t Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles > 20:
        print("\t 20 pont feletti értékelés nem elfogadható! ")
    else: 
        print("\t Köszönjük az értékelést!")

