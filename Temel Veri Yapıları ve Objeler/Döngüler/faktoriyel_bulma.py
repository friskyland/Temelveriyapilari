print("""
************************************
FAKTORİYEL BULMA PROGRAMI
************************************
Çıkmak için Q'ya basınız...
""")

while True:
    sayi = input("Sayı:")
    if (sayi == "q" or "Q"):
        print("Program Sonlandırılıyor....")
        break

    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *= i
        print("Faktöriyel",faktoriyel)
