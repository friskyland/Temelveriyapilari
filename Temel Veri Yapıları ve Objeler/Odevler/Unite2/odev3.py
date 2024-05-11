"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""
vize1 = int(input("Lütfen Vize1 notunuzu giriniz:"))
vize2 = int(input("Lütfen Vize2 notunuzu giriniz:"))
final = int(input("Lütfen Final notunuzu giriniz:"))

total = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if (total >= 90):
    print(total,"AA")
elif (total >= 85):
    print(total,"BA")
elif (total >= 80):
    print(total,"BB")
elif (total >= 75):
    print(total,"CB")
elif (total >= 70):
    print(total,"CC")
elif (total >= 65):
    print(total,"DC")
elif (total >= 60):
    print(total,"DD")
elif (total >= 55):
    print(total,"FD")
else:
    print(total,"FF")

