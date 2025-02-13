max = 0
for i in range(10):
    print("zadejte číslo:" + str(i+1))
    x = int(input())
    if x > max:
        max = x
print("Největší zadané číslo bylo" + str(max))
  