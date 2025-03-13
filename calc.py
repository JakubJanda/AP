while True: 
    clen1 = int(input("zadejte první člen"))
    clen2 = int(input("zadejte druhý člen"))
    
    
    """
    print("1.Součet")
    print("2.Součín")
    print("3.Rozdíl")    
    print("4.Podíl") 
    """
    print("1.Součet \n2.Součet\n3.Rozdíl\n4.Podíl")
    
    operace = int(input("vyberte číslo početní operace, kterou chcete vykonat")) 
    
    match operace:
        case 1:  
            soucet = clen1 + clen2
            print("Soucet je:" + str(soucet))
        case 2:   
            soucin = clen1 * clen2
            print("Soucin je:" + str(soucin))
        case 3:
            rozdil = clen1 - clen2
            print("rozdil je:" + str(rozdil))
        case 4: 
            if clen2 == 0:
                print("nelze delit nulou")
            else:
             podil  = clen1 / clen2
            print("Podil je:" + str(podil))
        case _:
            print("No tak to ne šerife")
            
    if clen2 == 0:
        print("nelze dělit 0")
    else:
        print(podil)
    
    konec = input("přejete si ukončit program? Y/N")
    if konec == "Y" or konec == "y":
        break
    elif konec ==  "N" or konec == "y":
        print("Jdeme na další")
    else:
        print("neplatné zadání, program se zavírá")
        break
    