print("""
**************************
Kullanıcı Girişi Programı
**************************
""")

sys_userid = "onuro"
sys_pw = "123321"
giriş_hakkı = 3

while True:
    userid = input("Kullanıcı Adı:")
    password = input("Parola:")
    if (userid != sys_userid and password == sys_pw):
        print("Hatalı kullanıcı...")
        giriş_hakkı -= 1
    elif (userid == sys_userid and password != sys_pw):
        print("Hatalı Parola...")
        giriş_hakkı -= 1
    elif (userid != sys_userid and password != sys_pw):
        print("Kullanıcı ve Parola hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı...")
        break
    if (giriş_hakkı == 0):
        print("Giriş hakkınız kalmadı...")
        break
