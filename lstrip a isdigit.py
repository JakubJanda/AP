while True:                #cyklus, který bude probíhat pořád
    Cislo = input("zadejte číslo: ")
    if Cislo.lstrip("-").isdigit():
        max = int(Cislo)
        break
    else: 
       print("Nezadali jste číslo")
while input("Pro ukončení zadejte písmeno K") != "K":
    Cislo = input("Zadejte číslo: ")
    if Cislo.lstrip("-").isdigit():
     Cislo = int(Cislo)
     if max < Cislo:
         max = Cislo
    else:
       print("Nezadali jste číslo.")

print("Největší číslo bylo: " + str(max))
