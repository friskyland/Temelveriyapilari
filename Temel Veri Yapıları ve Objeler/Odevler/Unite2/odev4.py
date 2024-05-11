"""Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5
"""
###### KODA BAŞLA:
print("""
**********************************************
GEOMETRİK ŞEKİL HESAPLAMA
***********************************************\n
Lütfen İşlem Numarasını Belirtiniz:
(1) Üçgen
(2) Dörtgen
""")
islem = input()


if islem == "1":
    ucgen1 = int(input("Lütfen üçgenin 'a' kenarını belirtiniz:"))
    ucgen2 = int(input("Lütfen üçgenin 'b' kenarını belirtiniz:"))
    ucgen3 = int(input("Lütfen üçgenin 'c' kenarını belirtiniz:"))

    if (abs(ucgen1 + ucgen2) > ucgen3 and abs(ucgen1 + ucgen3) > ucgen2 and abs(ucgen2 + ucgen3) > ucgen1):
        if (ucgen1 == ucgen2 and ucgen1 == ucgen3):
            print("Bu bir Eşkenar Üçgen'dir.")
        elif ((ucgen1 == ucgen2 and ucgen1 != ucgen3) or (ucgen1 == ucgen3 and ucgen1 != ucgen2) or (ucgen2 == ucgen3 and ucgen2 != ucgen1)):
            print("Bu bir İkizkenar Üçgen'dir.")
        else:
            print("Bu bir Çeşitkenar Üçgen'dir.")
    else:
        print("HATA: Bu değerler Üçgen belirtmiyor.")


elif islem == "2":
    dortgen1 = int(input("Lütfen dörtgenin 'a' kenarını belirtiniz:"))
    dortgen2 = int(input("Lütfen dörtgenin 'b' kenarını belirtiniz:"))
    dortgen3 = int(input("Lütfen dörtgenin 'c' kenarını belirtiniz:"))
    dortgen4 = int(input("Lütfen dörtgenin 'd' kenarını belirtiniz:"))

    if (dortgen1 == dortgen2 and dortgen1 == dortgen3 and dortgen1 == dortgen4):
        print("Bu bir Kare'dir.")
    elif dortgen1 == dortgen3 and dortgen2 == dortgen4:
        print("Bu bir Dikdörtgen'dir.")
    else:
        print("Bu bir Dörtgen'dir.")
else:
    print("Hatalı işlem numarası girdiniz!")

