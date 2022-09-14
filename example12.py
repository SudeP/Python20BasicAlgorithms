# 0 ile 1000 arasındaki Asal sayıları bulan programı yazınız?
# Öğrendiklerim
# yok

primeNumbers = []

for i in range(1, 1000):
    if i == 1 or i == 2:
        primeNumbers.append(i)
        
    if i % 2 == 0:
        pass

    else:
        dividedNumbers = []

        for k in range(1, i):
            
            if i % k == 0:
                dividedNumbers.append(k)

        if len(dividedNumbers) < 3:
            primeNumbers.append(i)


for i in primeNumbers:
    print(i)
