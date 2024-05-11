print("""**************************************
4 İŞLEM HESAP MAKİNESİ PROGRAMI

İşlemler;

(1) Toplama 
(2) Çıkarma
(3) Çarpma
(4) Bölme

**************************************""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

işlem = input("İşlemi Giriniz:")

if işlem == "1":
    print("{} ile {} sayılarının toplamı {}".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} sayılarının farkı {}".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} sayılarının çarpımı {}".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} sayılarının bölümü {}".format(a,b,a/b))
else:
    print("İşlem numarasını hatalı girdiniz!")