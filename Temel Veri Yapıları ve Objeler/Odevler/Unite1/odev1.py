"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""

Birinci_sayi = int(input("Lütfen Birinci Sayıyı Girin:"))
İkinci_sayi = int(input("Lütfen İkinci Sayıyı Girin:"))
Ucuncu_sayi = int(input("Lütfen Üçüncü Sayıyı Girin:"))

sonuc = [Birinci_sayi,İkinci_sayi,Ucuncu_sayi]
islem_sonuc = Birinci_sayi * İkinci_sayi * Ucuncu_sayi

print("Girilen Birinci Sayı: {}\nGirilen İkinci Sayı: {}\nGirilen Üçüncü Sayı: {}\n".format(sonuc[0],sonuc[1],sonuc[2]))
print("Çarpma İşleminin Sonucu:",islem_sonuc)
