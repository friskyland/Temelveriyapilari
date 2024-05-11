"""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın
ve şu kurallara göre ekrana şu yazıları yazdırın.

Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez
"""

boy = int(input("Boyunuz (CM):"))
kilo = int(input("Kilonuz:"))
boym = boy / 100
bki = kilo / boym ** 2

if bki < 18.5:
    print("Beden Kitle İndeksiniz:",bki,"Zayıf")
elif bki > 18.5 and bki < 25:
    print("Beden Kitle İndeksiniz:",bki,"Normal")
elif bki > 25 and bki < 30:
    print("Beden Kitle İndeksiniz:",bki,"Fazla Kilolu")
else:
    print("Beden Kitle İndeksiniz:",bki,"Obez")
