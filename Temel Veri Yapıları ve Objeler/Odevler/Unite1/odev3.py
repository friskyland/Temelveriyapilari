"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

"""
kmyakit = float(input("Kilometrede ne kadar yaktığınız yazınız:"))
kmyol = int(input("Kaç kilometre yol yaptığızı yazınız:"))

print(("Tutar: {} TL.".format(kmyakit * kmyol)))