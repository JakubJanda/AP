while True:
    end = int(input("Zadejte číslo jehož faktoriál chcete"))
    if end>=0:
        break
    else:
        print("Zadej to normalne k#rva!")


faktorial = 1
for i in range(1,end+1):
    faktorial *= i
    print(faktorial)
    