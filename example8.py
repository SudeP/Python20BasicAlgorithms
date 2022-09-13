# n'den m'ye kadar olan sayılardan 7'ye tam bölünenleri bulunuz? n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktır. 

# Öğrendiklerim
# print için virgül ile birden fazla object dönebiliyormusuz :). yeni farkettim....
# list(), filter(), lambda x :

n = int(input('N sayısını giriniz : '))
m = int(input('M sayısını giriniz : '))

integersDividedBySeven = list(filter(lambda number : number % 7 == 0, range(n, m)))

print('7''ye tam bölünen sayılar : ', integersDividedBySeven)