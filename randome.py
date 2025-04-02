opakovat = "ano"
while opakovat == "ano":
   
    
    pole = []
    cislo1 = input("jake cislo chcete pouzit(1-9)")
    cislo2 = input("jake druhe cislo chcete pouzit(1-9)")
    cislo1 = int(cislo1)
    cislo2 = int(cislo2)
    pole.append(cislo1+cislo2)
    pole.append(cislo1-cislo2)
    pole.append(cislo1*cislo2)
    pole.append(cislo1/cislo2)
    import random
    print("vas random vysledek je",random.choice(pole))
    print("vase vsechny vysledky jsou",pole)
    
    opakovat = input("chcete pokracovat? ano/ne")
        
