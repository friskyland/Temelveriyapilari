"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

a = int(input("Lütfen 1. Sayıyı Girin:"))
b = int(input("Lütfen 2. Sayıyı Girin:"))
c = int(input("Lütfen 3. Sayıyı Girin:"))

if (a > b and a > c):
    print(a)
elif (b > a and b > c):
    print(b)
else:
    print(c)