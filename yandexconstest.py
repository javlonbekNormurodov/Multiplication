# MULTIPLICATION

b = int(input("Nechagacha sonlarning ko'paytmasini ko'rmoqchisiz: "))
a = 1
for j in range(1,b+1):
    for i in range(1,11):
        print(f'{a} * {i} = {a * i}')
    print("\t")
    a += 1

