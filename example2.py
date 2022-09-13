#Kullanıcıdan iki sayı alarak bunların toplamını ve ortalamasını ekrana yazan programı yazınız?


#Öğrendiklerim
# int(), str(), range(), len(), sum(), format(), ${}

numbers = []

for i in range(2):
    numbers.append(int(input('${i} elemanı giriniz : '.format(i=i))))

print('Girilen sayıların toplamı : ' + str(sum(numbers)))
print('Girilen sayıların ortalaması : ' + str(sum(numbers) / len(numbers)))