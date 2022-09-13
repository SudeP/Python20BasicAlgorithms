# Vize notunun %40'ını, Final notunun %60'ını alarak ortalama notu hesaplayan, ortalama 50 den büyükse "Geçti", küçükse "Kaldı" yazan programı yazınız?

# Öğrendiklerim
# yok

vize = int(input('Vize puanınınız : '))
final = int(input('Final puanınınız : '))

print(vize * .4 + final * .6 >= 50 and 'Geçtin' or 'Kaldın')