# İkinci dereceden ax2 + bx + c = 0 denkleminin diskriminant çözümünü yapınız? Kullanıcıdan a,b ve c değerlerini alarak deltayı hesaplayınız?

# Öğrendiklerim
# pow(number,times)

a = int(input('A değerini giriniz : '))
b = int(input('B değerini giriniz : '))
c = int(input('C değerini giriniz : '))

delta = pow(b, 2) - 4*a*c

print('Delta : ' + str(delta))