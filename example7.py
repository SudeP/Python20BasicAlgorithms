# 1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz? n sayısı kullanıcıdan alınacaktır

# Öğrendiklerim
# yok iterate with linq

n = int(input('N sayısını giriniz : '))

print('Tek sayaların toplamı : '
    + str(sum(number for number in range(1, n) if number % 2 != 0))
)