print("""
*******************************
ATM Makinesine Hoşgeldiniz.
*******************************

İşlemler;

(1) Bakiye Sorgulama
(2) Para Yatırma
(3) Para Çekme

Programdan çıkmak için; Q'ya basınız.
*******************************
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if (işlem == "q"):
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Yatırılacak miktarı giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Çekilecek miktarı giriniz:"))

        if (miktar > bakiye):
            print("Bakiyeniz Yeterli Değildir!")
        else:
            bakiye -= miktar
            print("Para çekme işleminiz gerçekleşti.")



    else:
        print("Geçersiz işlem numarası.")
