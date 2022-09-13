# Kullanıcıdan ismini ve soyismini alarak içerisinde kaç adet sesli kaç adet sessiz harf olduğunu bulan programı yazınız

# Öğrendiklerim
# yok

vowels = ['a', 'e', 'i', 'o', 'u', 'ö', 'ü']

vowelsLettersCount = 0
consonantLettersCount = 0

def doCountingLetters(string):
    global vowelsLettersCount, consonantLettersCount
    for letter in list(string):
        if letter.lower() in vowels:
            vowelsLettersCount += 1
        else:
            consonantLettersCount += 1

name = input('İsminiz : ')
surname = input('Soyisminiz : ')

doCountingLetters(name)
doCountingLetters(surname)

print('Sesli harflerin adeti : ', vowelsLettersCount)
print('Sessiz harflerin adeti : ', consonantLettersCount)