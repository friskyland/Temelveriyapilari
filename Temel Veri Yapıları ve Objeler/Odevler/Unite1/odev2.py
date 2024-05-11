"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre
kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)
"""

boy = float(input("Lütfen Boyunuzu metre olarak giriniz:"))
kilo = int(input("Lütfen kilonuzu giriniz:"))
boycm = boy / 100

beden_kitle = kilo / boy ** 2
print("Beden Kitle İndeksiniz:",beden_kitle)

