# Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız?

# Öğrendiklerim
# [condition] and [true_result] or [false_result]
# [true_result] if [condition] else [false_result]

bigestNumber = 0

for i in range(3):
    tempory = int(input('${i}. sayıyı giriniz : '.format(i=i)))
    bigestNumber = tempory > bigestNumber and tempory or bigestNumber

print('Girdiğiniz sayılardaki en büyük olan sayı : ' + str(bigestNumber))